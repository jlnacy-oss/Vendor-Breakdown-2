# -*- coding: utf-8 -*-
"""
people_wave8.py — Person research wave 8, completed 15 September 2026.

HCLTech, Honeywell and IBM leadership.

PROFESSIONAL, PUBLISHED INFORMATION ONLY. See people_schema.py.
Sources in this wave carried dates of birth, spouses, children, parents'
occupations, caste/ethnicity, home locations and executive compensation. None of
it is here. Where family control is a governance fact material to a commercial
relationship, it is recorded as ownership and board control, not as a family tree.

Arvind Krishna appears twice because IBM watsonx and IBM Consulting are tracked as
separate vendors. The career is the same; the focus and talking points differ.
"""

RESEARCHED_ON = "2026-09-15"

_KRISHNA_CAREER = [
    {"period": "2021\u2013present", "role": "Chairman", "org": "IBM"},
    {"period": "2020\u2013present", "role": "Chief Executive Officer", "org": "IBM"},
    {"period": "2015\u20132020", "role": "Senior Vice President, IBM Cloud &amp; Cognitive Software and IBM Research", "org": "IBM"},
    {"period": "1990\u20132015", "role": "Research and technical leadership, from the Thomas J. Watson Research Center", "org": "IBM"},
]
_KRISHNA_EDU = [
    "PhD, University of Illinois Urbana-Champaign",
    "BTech, Indian Institute of Technology Kanpur",
]

PEOPLE = [
    # ================================================= HCLTech
    {
        "id": "hcltech-c-vijayakumar",
        "vendor_slug": "hcltech",
        "name": "C Vijayakumar",
        "title": "Chief Executive Officer &amp; Managing Director",
        "in_role_since": "CEO since October 2016; Managing Director since July 2021",
        "focus": "Runs HCLTech globally, with the Engineering and R&amp;D Services business and the "
                 "Advanced AI revenue line as the growth engines against a weak FY2027 outlook of "
                 "1\u20134% constant currency.",
        "background": "Known internally as CVK, he has spent nearly three decades at HCLTech and started "
                      "on the infrastructure side, which explains where the company's strengths still lie. "
                      "He joined in 1994 as part of the founding startup team of Comnet, a subsidiary later "
                      "merged into HCLTech, and was instrumental in designing and implementing India's "
                      "first fully automated trading network at the National Stock Exchange. He led the "
                      "exponential growth of HCL's Infrastructure Services Business as its President, and "
                      "incubated the products and platforms portfolio that became a billion-dollar "
                      "business. As CEO he has pushed HCLTech toward cloud, IoT, cybersecurity and AI, and "
                      "is described as focused on execution and acquisitive by disposition.",
        "career": [
            {"period": "2021\u2013present", "role": "Chief Executive Officer &amp; Managing Director", "org": "HCLTech"},
            {"period": "2016\u20132021", "role": "Chief Executive Officer", "org": "HCL Technologies"},
            {"period": "earlier", "role": "President, Infrastructure Services Business", "org": "HCL Technologies"},
            {"period": "1994", "role": "Founding startup team", "org": "Comnet (merged into HCLTech)"},
        ],
        "education": [
            "BE Electrical &amp; Electronics Engineering, PSG College of Technology, Coimbatore",
            "Executive Management Programme, Xavier School of Management (XLRI)",
        ],
        "public_roles": ["Chief Executive Officer &amp; Managing Director, HCLSoftware"],
        "notable": [
            {"point": "Built his career on infrastructure services and helped implement India's first fully "
                      "automated trading network at the National Stock Exchange \u2014 genuine large-scale "
                      "operational infrastructure experience rather than application services.",
             "source": "https://indiaspora.org/business-leader/c-vijaykumar/"},
            {"point": "Incubated HCLTech's products and platforms portfolio into a billion-dollar business, "
                      "and now also leads HCLSoftware \u2014 so software and services P&amp;L sit with the "
                      "same person.",
             "source": "https://www.hcltech.com/leadership"},
        ],
        "talking_points": [
            "Infrastructure services is his home ground, not a talking point \u2014 the closest fit of any India-heritage CEO to asset-heavy operations.",
            "Engineering and R&amp;D Services grew 9.8% against 3.9% company growth. He will know that is the strongest card in his hand.",
            "FY2027 guidance of 1\u20134% is the weakest in the peer set; there is commercial motivation to win portfolio-scale work.",
        ],
        "links": [
            {"label": "HCLTech leadership page", "url": "https://www.hcltech.com/leadership"},
            {"label": "Indiaspora profile", "url": "https://indiaspora.org/business-leader/c-vijaykumar/"},
        ],
    },
    {
        "id": "hcltech-roshni-nadar-malhotra",
        "vendor_slug": "hcltech",
        "name": "Roshni Nadar Malhotra",
        "title": "Chairperson (Non-Executive, Non-Independent)",
        "in_role_since": "Chairperson of HCLTech and of HCL Group",
        "focus": "Board leadership of HCLTech and the wider HCL Group, plus chairing its Corporate Social "
                 "Responsibility committee. She is also the company's largest shareholder following a 2025 "
                 "transfer of shares, so ownership and board control sit together.",
        "background": "She leads both HCLTech and HCL Group as Chairperson, and was the first woman to "
                      "chair a listed Indian IT company. Her route in was through HCL Corporation, where "
                      "she became executive director and CEO within a year of joining, before taking the "
                      "HCLTech chairmanship. Alongside the corporate roles she is a Trustee of the Shiv "
                      "Nadar Foundation, which has invested $1.5 billion in institution-building since its "
                      "inception, and Chairperson of VidyaGyan, a leadership academy for meritorious rural "
                      "students from economically underprivileged backgrounds in Uttar Pradesh. She founded "
                      "The Habitats Trust, a conservation organisation.",
        "career": [
            {"period": "current", "role": "Chairperson", "org": "HCLTech"},
            {"period": "current", "role": "Chairperson", "org": "HCL Group"},
            {"period": "earlier", "role": "Executive Director &amp; Chief Executive Officer", "org": "HCL Corporation"},
        ],
        "education": ["BA and MBA, Northwestern University (Kellogg School of Management)"],
        "public_roles": [
            "Trustee, Shiv Nadar Foundation",
            "Founder, The Habitats Trust",
            "Chairperson, VidyaGyan Leadership Academy",
            "Chairperson, HCLTech Corporate Social Responsibility Committee; member, Stakeholders' Relationship and ESG/DEI committees",
            "Dean's Distinguished Service Award and 2023 Schaffner Award, Kellogg School of Management",
            "Lewis Institute Community Changemaker Award, Babson College (2017)",
        ],
        "notable": [
            {"point": "Became HCLTech's largest shareholder in 2025 through a transfer of shares, so board "
                      "control and economic ownership are held by the same person \u2014 a governance fact "
                      "worth understanding before any long-term commitment.",
             "source": "https://en.wikipedia.org/wiki/Roshni_Nadar"},
            {"point": "Chairs both HCLTech and HCL Group while HCLTech carries a market capitalisation "
                      "above $55 billion, and drives the Shiv Nadar Foundation's $1.5 billion "
                      "institution-building programme.",
             "source": "https://www.hcltech.com/leadership"},
        ],
        "talking_points": [
            "Non-executive chairperson with controlling ownership \u2014 she does not run operations, but nothing strategic happens against her.",
            "Her published priorities are education, conservation and ESG; those are the registers she engages in, not delivery detail.",
            "Route commercial discussion through Vijayakumar. Reserve her for genuinely strategic or reputational matters.",
        ],
        "links": [
            {"label": "HCLTech leadership page", "url": "https://www.hcltech.com/leadership"},
            {"label": "HCLTech Annual Report 2025 board", "url": "https://www.hcltech.com/hcl-annual-report-2025/founder-and-board-of-directors"},
        ],
        "notes": "HCLTech is a family-controlled group. That is recorded here as ownership and board "
                 "control because it is material to a commercial relationship; family detail carried by "
                 "the sources is deliberately omitted.",
    },

    # ================================================= Honeywell
    {
        "id": "honeywell-forge-vimal-kapur",
        "vendor_slug": "honeywell-forge",
        "name": "Vimal Kapur",
        "title": "Chairman &amp; Chief Executive Officer",
        "in_role_since": "CEO since June 2023; Chairman since June 2024",
        "focus": "Leads the company as a pure-play automation business, having reshaped the portfolio "
                 "through roughly $14 billion of acquisitions and the separation of Honeywell's other "
                 "segments.",
        "background": "A thirty-seven-year Honeywell insider who came up through process automation, which "
                      "is exactly the ground Honeywell Forge sits on. He began his career in 1986 and "
                      "joined a Honeywell joint venture in India in 1989, becoming Managing Director of "
                      "Honeywell Automation India. He went on to lead Honeywell Process Solutions as "
                      "President, steering it through an oil and gas downturn, then served as President "
                      "and CEO of Performance Materials and Technologies from 2021 to 2022 and as "
                      "President and Chief Operating Officer of Honeywell before taking the CEO role.",
        "career": [
            {"period": "2023\u2013present", "role": "Chief Executive Officer (Chairman from 2024)", "org": "Honeywell"},
            {"period": "2022\u20132023", "role": "President &amp; Chief Operating Officer", "org": "Honeywell"},
            {"period": "2021\u20132022", "role": "President &amp; Chief Executive Officer, Performance Materials and Technologies", "org": "Honeywell"},
            {"period": "earlier", "role": "President, Honeywell Process Solutions", "org": "Honeywell"},
            {"period": "earlier", "role": "Managing Director", "org": "Honeywell Automation India Ltd."},
            {"period": "1989", "role": "Joined via a Honeywell joint venture in India", "org": "Honeywell"},
        ],
        "education": ["Electronics engineering (instrumentation), Thapar Institute of Engineering, Patiala"],
        "public_roles": [
            "Member, The Business Council",
            "Member, Charlotte Executive Leadership Council",
            "Member, U.S.-India CEO Forum",
        ],
        "notable": [
            {"point": "Ran Honeywell Process Solutions through an oil and gas downturn \u2014 direct "
                      "operating experience of industrial customers cutting capital budgets, which is "
                      "unusual and useful context for an infrastructure conversation.",
             "source": "https://www.weforum.org/people/vimal-kapur/"},
            {"point": "Has reshaped the portfolio around roughly $14 billion of acquisitions and positions "
                      "the company as a pure-play automation business \u2014 a significant narrowing of "
                      "what Honeywell is.",
             "source": "https://www.honeywell.com/us/en/company/leadership/vimal-kapur"},
        ],
        "talking_points": [
            "Process automation is his actual career, not a portfolio he inherited \u2014 a plant-floor conversation will land.",
            "He has personally managed through an industrial capex downturn; arguments about payback periods and operational savings will get a realistic hearing.",
            "The pure-play automation repositioning means Forge is now closer to the centre of the company than it was. Worth testing what that means for roadmap commitment.",
        ],
        "links": [
            {"label": "Honeywell leadership profile", "url": "https://www.honeywell.com/us/en/company/leadership/vimal-kapur"},
            {"label": "World Economic Forum profile", "url": "https://www.weforum.org/people/vimal-kapur/"},
        ],
        "notes": "Honeywell's own leadership page now describes the company as \"Honeywell Technologies, a "
                 "global pure-play automation company\", which suggests the corporate separation has "
                 "changed the entity name and scope since the Honeywell Forge vendor page was written. "
                 "That vendor record should be re-run.",
    },

    # ================================================= IBM (watsonx)
    {
        "id": "ibm-watsonx-arvind-krishna",
        "vendor_slug": "ibm-watsonx",
        "name": "Arvind Krishna",
        "title": "Chairman &amp; Chief Executive Officer, IBM",
        "in_role_since": "CEO since April 2020; Chairman since January 2021",
        "focus": "Leads IBM overall, with the hybrid cloud and AI strategy \u2014 watsonx, Red Hat and the "
                 "generative AI book of business \u2014 as the centre of it.",
        "background": "A researcher who rose to run the company, which is rare at IBM's scale and shapes "
                      "how technical a conversation with him can be. He joined IBM in 1990 at the Thomas "
                      "J. Watson Research Center and spent twenty-five years in research and technical "
                      "leadership before being promoted to Senior Vice President in 2015, running IBM "
                      "Cloud &amp; Cognitive Software and IBM Research. He was the principal architect of "
                      "the Red Hat acquisition, the largest in IBM's history, which is the foundation of "
                      "the hybrid cloud strategy he now runs the company on. He holds a doctorate from the "
                      "University of Illinois Urbana-Champaign.",
        "career": _KRISHNA_CAREER,
        "education": _KRISHNA_EDU,
        "public_roles": [],
        "notable": [
            {"point": "Was the principal architect of the Red Hat acquisition, the largest in IBM's "
                      "history, before becoming CEO \u2014 so the hybrid cloud strategy is genuinely his "
                      "own rather than inherited.",
             "source": "https://en.wikipedia.org/wiki/Arvind_Krishna"},
            {"point": "Reports IBM's generative AI book of business past $12.5B inception to date, and "
                      "guided to more than 5% constant-currency revenue growth in 2026 with roughly $1B of "
                      "additional free cash flow.",
             "source": "https://newsroom.ibm.com/2026-01-28-IBM-RELEASES-FOURTH-QUARTER-RESULTS"},
        ],
        "talking_points": [
            "Twenty-five years in IBM Research before management \u2014 he can go deep on architecture, and expects the other side to keep up.",
            "watsonx.governance is the part of the stack most enterprises are least equipped for; that is the strongest opening rather than model capability.",
            "The generative AI book of business is a cumulative inception-to-date figure spanning software, SaaS and consulting signings. Do not treat it as annual revenue in front of him.",
        ],
        "links": [
            {"label": "IBM Q4 2025 results", "url": "https://newsroom.ibm.com/2026-01-28-IBM-RELEASES-FOURTH-QUARTER-RESULTS"},
            {"label": "IBM SEC filing", "url": "https://www.sec.gov/Archives/edgar/data/51143/000005114325000010/ibm-ex99_1.htm"},
        ],
    },

    # ================================================= IBM Consulting
    {
        "id": "ibm-consulting-arvind-krishna",
        "vendor_slug": "ibm-consulting",
        "name": "Arvind Krishna",
        "title": "Chairman &amp; Chief Executive Officer, IBM",
        "in_role_since": "CEO since April 2020; Chairman since January 2021",
        "focus": "Sets IBM's overall direction, including how the Consulting arm is repositioned \u2014 he "
                 "has publicly described consulting as embracing disruption, an acknowledgement that the "
                 "traditional delivery model is under pressure from the technology IBM sells.",
        "background": "A researcher who rose to run the company. He joined IBM in 1990 at the Thomas J. "
                      "Watson Research Center and spent twenty-five years in research and technical "
                      "leadership before becoming Senior Vice President in 2015, running IBM Cloud &amp; "
                      "Cognitive Software and IBM Research. He was the principal architect of the Red Hat "
                      "acquisition, the largest in IBM's history. Consulting under him is deliberately "
                      "coupled to IBM's own stack \u2014 watsonx, Red Hat, automation and Z.",
        "career": _KRISHNA_CAREER,
        "education": _KRISHNA_EDU,
        "public_roles": [],
        "notable": [
            {"point": "Described IBM Consulting as embracing disruption \u2014 an unusually candid "
                      "acknowledgement from a CEO that the services model is being compressed by the "
                      "technology the firm is selling.",
             "source": "https://newsroom.ibm.com/2026-01-28-IBM-RELEASES-FOURTH-QUARTER-RESULTS"},
            {"point": "Consulting revenue grew only about 1.5% in 2025, to over $21B, well behind "
                      "Accenture's 7% \u2014 the context for the agentic delivery model IBM is now "
                      "building around Consulting Advantage and Enterprise Advantage.",
             "source": "https://www.sec.gov/Archives/edgar/data/51143/000005114325000010/ibm-ex99_1.htm"},
        ],
        "talking_points": [
            "Advice arriving through IBM Consulting is not vendor-neutral \u2014 it tends toward watsonx, Red Hat and Z. He would not dispute that; ask directly what the alternatives were.",
            "He has conceded publicly that consulting is being disrupted, which makes a conversation about outcome-based rather than day-rate pricing a live one.",
            "For a PortCo with an existing IBM estate, he is the escalation point that makes consulting and software commitments move together.",
        ],
        "links": [
            {"label": "IBM Q4 2025 results", "url": "https://newsroom.ibm.com/2026-01-28-IBM-RELEASES-FOURTH-QUARTER-RESULTS"},
            {"label": "IBM Consulting", "url": "https://www.ibm.com/consulting"},
        ],
    },
]
