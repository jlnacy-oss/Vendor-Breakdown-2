/* gip-panel.js — renders the GIP engagement block and contact cards
   on any vendor white page that contains:
     <div id="gip-panel" data-vendor="Vendor Name"></div>
     <div class="card-grid" id="gip-people"></div>
*/
(function () {
  "use strict";
  var panel = document.getElementById("gip-panel");
  if (!panel) return;
  var vendorName = panel.getAttribute("data-vendor") || "";
  var key = vendorName.toLowerCase();

  function initials(n) {
    var p = n.split(/\s+/).filter(Boolean);
    return (((p[0] || "")[0] || "") + ((p[p.length - 1] || "")[0] || "")).toUpperCase();
  }

  function stat(n, l) {
    return '<div class="gip-stat"><div class="n">' + n + '</div><div class="l">' + l + '</div></div>';
  }

  GIP.ready(function (d) {
    var rows = d.byVendor[key] || [];
    var score = d.scores[key];
    var meta = d.vendors[key] || {};

    if (!rows.length) {
      panel.innerHTML = '<div style="color:var(--ink-3); font-size:13px;">' +
        'No engagement logged for ' + GIP.esc(vendorName) + ' yet. Add a row to the ' +
        '<b>Engagements</b> sheet of gip-tracker.xlsx naming this vendor and it appears here.</div>';
    } else {
      var pcs = {};
      rows.forEach(function (r) { if (r.portco) pcs[r.portco] = 1; });
      var head = '<div class="gip-summary">' +
        (score ? stat(score.total + " <span style='font-size:12px;color:var(--ink-3);'>/100</span>", "Engagement score") : "") +
        stat(rows.length, "Thread" + (rows.length === 1 ? "" : "s")) +
        stat(Object.keys(pcs).length, "PortCo" + (Object.keys(pcs).length === 1 ? "" : "s")) +
        (meta.tier ? stat(GIP.esc(meta.tier), "Relationship tier") : "") +
        (meta.owner ? stat(GIP.esc(meta.owner), "Owner") : "") +
        "</div>";

      var body = '<table class="dtable"><thead><tr>' +
        '<th style="width:14%;">Requested by</th><th style="width:22%;">Connection &amp; reason</th>' +
        '<th style="width:14%;">PortCo</th><th style="width:26%;">Use case</th>' +
        '<th style="width:12%;">Status</th><th style="width:12%;">Next step</th>' +
        "</tr></thead><tbody>" +
        rows.map(function (r) {
          return "<tr>" +
            "<td>" + GIP.esc(r.requestedBy || "—") +
            (r.requesterOrg ? '<br><span style="color:var(--ink-3);font-size:11.5px;">' + GIP.esc(r.requesterOrg) + "</span>" : "") + "</td>" +
            "<td>" + GIP.esc(r.connection || "—") +
            (r.reason ? '<br><span style="color:var(--ink-3);">' + GIP.esc(r.reason) + "</span>" : "") + "</td>" +
            "<td>" + GIP.esc(r.portco || "—") + "</td>" +
            "<td>" + GIP.esc(r.useCase || "—") +
            (r.useArea ? '<br><span class="tag">' + GIP.esc(r.useArea) + "</span>" : "") + "</td>" +
            '<td><span class="pill ' + GIP.statusClass(r.status) + '">' + GIP.esc(r.status || "—") + "</span></td>" +
            "<td>" + GIP.esc(r.nextStep || "—") + "</td></tr>";
        }).join("") + "</tbody></table>";

      panel.innerHTML = head + body;
    }

    var box = document.getElementById("gip-people");
    if (!box) return;
    var seeded = [];
    if (window.APP) {
      var v = APP.vendors.filter(function (x) { return x.name.toLowerCase() === key; })[0];
      if (v) seeded = v.people.map(function (p) {
        return { name: p.name, title: p.title, href: p.href, id: p.id, extra: d.peopleById[p.id] || null };
      });
    }
    (d.peopleByVendor[key] || []).forEach(function (p) {
      if (!p.show) return;
      if (seeded.some(function (s) { return s.name.toLowerCase() === p.name.toLowerCase(); })) return;
      seeded.push({ name: p.name, title: p.title, href: null, extra: p });
    });

    if (!seeded.length) {
      var none = document.getElementById("nopeople");
      if (none) none.style.display = "block";
      return;
    }
    box.innerHTML = seeded.map(function (p) {
      var e = p.extra || {};
      var foot = [];
      if (e.linkedin) foot.push('<a href="' + GIP.esc(e.linkedin) + '" target="_blank" rel="noopener">LinkedIn &#8599;</a>');
      if (e.email) foot.push('<a href="mailto:' + GIP.esc(e.email) + '">' + GIP.esc(e.email) + "</a>");
      if (e.phone) foot.push("<span>" + GIP.esc(e.phone) + "</span>");
      if (p.href) foot.push('<a href="' + p.href + '">Full profile &rarr;</a>');
      if (p.id) foot.push('<a href="contact-' + p.id + '-one-sheet.pdf" download>One-sheet &darr;</a>');
      if (!foot.length) foot.push('<span class="muted">No contact details on file</span>');
      var lines = [];
      if (e.background) lines.push(GIP.esc(e.background));
      if (e.howWeKnow) lines.push("<b>How we know them:</b> " + GIP.esc(e.howWeKnow));
      if (e.notes) lines.push(GIP.esc(e.notes));
      if (!lines.length) lines.push('<span style="color:var(--ink-3);">Background not yet researched.</span>');
      var alt = /chief technology|cto/i.test(p.title || "");
      return '<div class="pcard"><div class="pcard-head">' +
        '<div class="mono' + (alt ? " alt" : "") + '">' + GIP.esc(initials(p.name)) + "</div><div>" +
        '<div class="pcard-name">' + GIP.esc(p.name) + "</div>" +
        '<div class="pcard-role">' + GIP.esc(p.title) + "</div></div></div>" +
        '<div class="pcard-body">' + lines.join("<br>") + "</div>" +
        '<div class="pcard-foot">' + foot.join("") + "</div></div>";
    }).join("");
  });
})();
