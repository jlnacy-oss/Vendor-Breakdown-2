/* ============================================================
   gip-loader.js — reads gip-tracker.xlsx in the browser.

   Nothing is uploaded. The workbook is parsed locally by the
   bundled SheetJS build (xlsx.full.min.js) and held in memory
   for the life of the page.

   Two load paths:
     1. fetch('gip-tracker.xlsx')  — works when the folder is
        served (python3 -m http.server, or any internal host).
     2. file picker — fallback for opening index.html directly
        from disk, where fetch() is blocked by the browser.

   Usage:  GIP.ready(function(data){ ... });
   ============================================================ */
(function () {
  "use strict";

  var FILE = "gip-tracker.xlsx";
  var STATUS_DEPTH = {
    "requested": 0.10,
    "intro made": 0.25,
    "discovery": 0.45,
    "pilot scoping": 0.60,
    "pilot active": 0.80,
    "deployed / in production": 1.00,
    "paused": 0.50,
    "no fit": 0.15,
    "dormant": 0.20
  };
  var STATUS_CLASS = {
    "deployed / in production": "s-live",
    "pilot active": "s-live",
    "pilot scoping": "s-active",
    "discovery": "s-active",
    "intro made": "s-early",
    "requested": "s-early",
    "paused": "s-cold",
    "no fit": "s-cold",
    "dormant": "s-cold"
  };

  var callbacks = [];
  var state = { loaded: false, source: null, error: null, data: emptyData() };

  function emptyData() {
    return {
      engagements: [], people: [], vendors: {}, portcos: [],
      scores: {}, byVendor: {}, peopleByVendor: {}, peopleById: {}
    };
  }

  function txt(v) {
    if (v === null || v === undefined) return "";
    if (v instanceof Date) return v.toISOString().slice(0, 10);
    return String(v).trim();
  }

  function asDate(v) {
    if (!v) return null;
    if (v instanceof Date) return isNaN(v.getTime()) ? null : v;
    var d = new Date(v);
    return isNaN(d.getTime()) ? null : d;
  }

  function isExample(row) {
    return Object.keys(row).some(function (k) {
      return /^EXAMPLE\b/i.test(txt(row[k]));
    });
  }

  function sheetRows(wb, name) {
    var ws = wb.Sheets[name];
    if (!ws) return [];
    return XLSX.utils.sheet_to_json(ws, { defval: "", raw: false, dateNF: "yyyy-mm-dd" })
      .filter(function (r) {
        return Object.keys(r).some(function (k) { return txt(r[k]) !== ""; });
      })
      .filter(function (r) { return !isExample(r); });
  }

  /* ---------------------------------------------- scoring
     Out of 100:
       breadth   30  distinct PortCos introduced (caps at 5)
       depth     30  furthest status reached on any thread
       momentum  20  how recently anything moved
       substance 20  share of threads with a real use case written down
  */
  function scoreVendor(rows) {
    if (!rows.length) return null;

    var portcos = {};
    rows.forEach(function (r) { if (r.portco) portcos[r.portco.toLowerCase()] = 1; });
    var nPortco = Object.keys(portcos).length;
    var breadth = Math.min(nPortco, 5) / 5;

    var depth = 0;
    rows.forEach(function (r) {
      var d = STATUS_DEPTH[r.status.toLowerCase()];
      if (d !== undefined && d > depth) depth = d;
    });

    var latest = null;
    rows.forEach(function (r) {
      [r.lastTouch, r.dateIntroduced].forEach(function (d) {
        if (d && (!latest || d > latest)) latest = d;
      });
    });
    var momentum = 0, days = null;
    if (latest) {
      days = Math.floor((Date.now() - latest.getTime()) / 86400000);
      momentum = days <= 30 ? 1 : days <= 90 ? 0.7 : days <= 180 ? 0.4 : days <= 365 ? 0.2 : 0;
    }

    var withUse = rows.filter(function (r) { return r.useCase.length > 3; }).length;
    var substance = rows.length ? withUse / rows.length : 0;

    return {
      total: Math.round(breadth * 30 + depth * 30 + momentum * 20 + substance * 20),
      parts: [
        { label: "Breadth", pct: breadth, note: nPortco + " PortCo" + (nPortco === 1 ? "" : "s") },
        { label: "Depth", pct: depth, note: furthest(rows) || "—" },
        { label: "Momentum", pct: momentum, note: days === null ? "no dates" : days + "d since last touch" },
        { label: "Substance", pct: substance, note: withUse + " of " + rows.length + " with a use case" }
      ],
      threads: rows.length,
      portcos: nPortco,
      lastTouch: latest,
      overridden: false
    };
  }

  function furthest(rows) {
    var best = null, bestD = -1;
    rows.forEach(function (r) {
      var d = STATUS_DEPTH[r.status.toLowerCase()];
      if (d !== undefined && d > bestD) { bestD = d; best = r.status; }
    });
    return best;
  }

  function parse(wb) {
    var d = emptyData();

    d.engagements = sheetRows(wb, "Engagements").map(function (r) {
      return {
        id: txt(r["Engagement ID"]),
        vendor: txt(r["Vendor"]),
        requestedBy: txt(r["Requested By"]),
        requesterOrg: txt(r["Requester Org"]),
        connection: txt(r["Connection / Relationship Path"]),
        reason: txt(r["Reason for Intro"]),
        portco: txt(r["PortCo Introduced"]),
        useCase: txt(r["Use Case"]),
        useArea: txt(r["Use Case Area"]),
        status: txt(r["Status"]),
        owner: txt(r["GIP Owner"]),
        dateIntroduced: asDate(r["Date Introduced"]),
        lastTouch: asDate(r["Last Touch"]),
        nextStep: txt(r["Next Step"]),
        nextStepDue: asDate(r["Next Step Due"]),
        notes: txt(r["Notes"]),
        contractEnd: asDate(r["Contract End"]),
        valueBand: txt(r["Annual Value Band"]),
        noticePeriod: txt(r["Notice Period"])
      };
    }).filter(function (r) { return r.vendor; });

    d.people = sheetRows(wb, "People").map(function (r) {
      return {
        id: txt(r["Person ID"]),
        vendor: txt(r["Vendor"]),
        name: txt(r["Full Name"]),
        title: txt(r["Title"]),
        roleType: txt(r["Role Type"]),
        linkedin: txt(r["LinkedIn URL"]),
        email: txt(r["Work Email"]),
        phone: txt(r["Phone"]),
        location: txt(r["Location"]),
        since: txt(r["In Role Since"]),
        background: txt(r["Prior Background"]),
        owner: txt(r["GIP Relationship Owner"]),
        howWeKnow: txt(r["How We Know Them"]),
        lastContact: txt(r["Last Contact"]),
        notes: txt(r["Notes / Facts"]),
        show: txt(r["Show on Card"]).toLowerCase() !== "no",
        // captured in person by the user, never researched
        mobile: txt(r["Mobile"]),
        preferred: txt(r["Preferred Contact"]),
        assistant: txt(r["Assistant / EA"]),
        whereMet: txt(r["Where We Met"]),
        meetingFacts: txt(r["Facts From Meetings"]),
        nextTouch: txt(r["Next Touch"]),
        nextTouchDue: txt(r["Next Touch Due"])
      };
    }).filter(function (r) { return r.name; });

    sheetRows(wb, "Vendors").forEach(function (r) {
      var name = txt(r["Vendor Name"]);
      if (!name) return;
      d.vendors[name.toLowerCase()] = {
        name: name,
        slug: txt(r["Slug"]),
        owner: txt(r["GIP Relationship Owner"]),
        tier: txt(r["Relationship Tier"]),
        msa: txt(r["NDA / MSA in Place"]),
        override: txt(r["Score Override (0-100)"]),
        overrideReason: txt(r["Override Reason"]),
        notes: txt(r["GIP Notes"])
      };
    });

    d.portcos = sheetRows(wb, "PortCos").map(function (r) {
      return {
        name: txt(r["PortCo Name"]), sector: txt(r["Sector"]), region: txt(r["Region"]),
        lead: txt(r["BI / IT Lead"]), fund: txt(r["Fund"]), notes: txt(r["Notes"])
      };
    }).filter(function (r) { return r.name; });

    d.engagements.forEach(function (e) {
      var k = e.vendor.toLowerCase();
      (d.byVendor[k] = d.byVendor[k] || []).push(e);
    });
    d.people.forEach(function (p) {
      var k = p.vendor.toLowerCase();
      (d.peopleByVendor[k] = d.peopleByVendor[k] || []).push(p);
      if (p.id) d.peopleById[p.id] = p;
    });

    Object.keys(d.byVendor).forEach(function (k) {
      var s = scoreVendor(d.byVendor[k]);
      if (!s) return;
      var v = d.vendors[k];
      if (v && v.override !== "" && !isNaN(parseFloat(v.override))) {
        s.total = Math.round(parseFloat(v.override));
        s.overridden = true;
        s.overrideReason = v.overrideReason;
      }
      d.scores[k] = s;
    });

    return d;
  }

  function finish(data, source, error) {
    state.loaded = true;
    state.source = source;
    state.error = error || null;
    state.data = data || emptyData();
    callbacks.forEach(function (fn) {
      try { fn(state.data, state); } catch (e) { console.error(e); }
    });
    callbacks = [];
    renderBar();
  }

  function readBook(buf, source) {
    try {
      // SheetJS's "array" type means Uint8Array. Handed a raw ArrayBuffer it
      // returns a workbook with a single bogus sheet instead of throwing, so
      // coerce before reading — fetch().arrayBuffer() gives an ArrayBuffer.
      var bytes = buf instanceof Uint8Array ? buf : new Uint8Array(buf);
      var wb = XLSX.read(bytes, { type: "array", cellDates: true });
      if (!wb.SheetNames || wb.SheetNames.indexOf("Engagements") < 0) {
        throw new Error("that workbook has no 'Engagements' sheet — is it gip-tracker.xlsx?");
      }
      finish(parse(wb), source);
    } catch (e) {
      console.error(e);
      finish(null, "error", "The file opened but could not be read: " + e.message);
    }
  }

  function tryFetch() {
    if (location.protocol === "file:") { finish(null, "needs-picker"); return; }
    fetch(FILE, { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.arrayBuffer();
      })
      .then(function (buf) { readBook(buf, "auto"); })
      .catch(function () { finish(null, "needs-picker"); });
  }

  function pick() {
    var inp = document.createElement("input");
    inp.type = "file";
    inp.accept = ".xlsx,.xlsm";
    inp.onchange = function () {
      var f = inp.files && inp.files[0];
      if (!f) return;
      var fr = new FileReader();
      fr.onload = function () {
        state.loaded = false;
        callbacks = pendingAgain.slice();
        readBook(new Uint8Array(fr.result), "picked:" + f.name);
      };
      fr.readAsArrayBuffer(f);
    };
    inp.click();
  }

  /* re-run every registered renderer when a new file is picked */
  var pendingAgain = [];

  function renderBar() {
    var bar = document.getElementById("gip-loadbar");
    if (!bar) return;
    var d = state.data;
    var n = d.engagements.length, np = d.people.length;

    if (state.error) {
      bar.className = "loadbar warn";
      bar.innerHTML = '<div class="grow"><b>Could not read the tracker.</b> ' + esc(state.error) + "</div>" +
        '<button class="btn secondary" id="gip-pick">Choose a different file</button>';
    } else if (state.source === "needs-picker") {
      bar.className = "loadbar";
      bar.innerHTML = '<div class="grow"><b>No GIP data loaded.</b> Your browser blocks reading files ' +
        'from disk when a page is opened directly. Pick <code>gip-tracker.xlsx</code> to load it, or serve ' +
        'the folder (<code>python3 -m http.server</code>) and it loads by itself.</div>' +
        '<button class="btn" id="gip-pick">Load tracker &uarr;</button>';
    } else {
      bar.className = "loadbar ok";
      bar.innerHTML = '<div class="grow"><b>Tracker loaded.</b> ' + n + " engagement row" + (n === 1 ? "" : "s") +
        ", " + np + " contact" + (np === 1 ? "" : "s") + ", " + d.portcos.length + " PortCo" +
        (d.portcos.length === 1 ? "" : "s") + ". Everything below is read from your workbook.</div>" +
        '<button class="btn secondary" id="gip-pick">Reload / choose file</button>';
    }
    var b = document.getElementById("gip-pick");
    if (b) b.onclick = pick;
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  window.GIP = {
    ready: function (fn) {
      pendingAgain.push(fn);
      if (state.loaded) fn(state.data, state); else callbacks.push(fn);
    },
    state: state,
    statusClass: function (s) { return STATUS_CLASS[String(s).toLowerCase()] || "s-early"; },
    esc: esc,
    fmtDate: function (d) {
      if (!d) return "—";
      return d.toISOString().slice(0, 10);
    },
    pick: pick
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", tryFetch);
  } else {
    tryFetch();
  }
})();
