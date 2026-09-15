# -*- coding: utf-8 -*-
"""
people_wave14.py — Person research wave 14, completed 15 September 2026.

Sand Technologies and SAP leadership.

PROFESSIONAL, PUBLISHED INFORMATION ONLY. See people_schema.py.
Sources carried dates of birth, birthplaces, nationality and family detail.
None of it is here.
"""

RESEARCHED_ON = "2026-09-15"

PEOPLE = [
    # ================================================= Sand Technologies
    {
        "id": "sand-technologies-fred-swaniker",
        "vendor_slug": "sand-technologies",
        "name": "Fred Swaniker",
        "title": "Founder &amp; Chief Executive Officer",
        "in_role_since": "Founded Sand Technologies and has led it since",
        "focus": "Leads Sand Technologies, which he positions as the physical AI backbone for essential "
                 "industries \u2014 converting real-world operations in utilities, telecoms, healthcare "
                 "and smart cities into data-driven decisions.",
        "background": "A serial institution-builder rather than a conventional technology founder, and the "
                      "talent pipeline behind Sand is his own creation. He began his career at McKinsey "
                      "&amp; Company and took an MBA at Stanford, where he was named an Arjay Miller "
                      "Scholar. He has launched eight organisations across education, technology, talent "
                      "and AI, most notably the African Leadership Group \u2014 which includes the "
                      "pre-university African Leadership Academy, the African Leadership University with "
                      "campuses in Mauritius and Rwanda, and ALX, one of the fastest-growing tech talent "
                      "accelerators, currently training over 700,000 data and AI professionals. The stated "
                      "ambition is three million entrepreneurial African leaders by 2035. Sand Technologies "
                      "is headquartered in the US with engineers across Silicon Valley, France, the UK, "
                      "Romania and emerging markets.",
        "career": [
            {"period": "current", "role": "Founder &amp; Chief Executive Officer", "org": "Sand Technologies"},
            {"period": "current", "role": "Founder", "org": "African Leadership Group (ALX, African Leadership University, African Leadership Academy)"},
            {"period": "2014", "role": "Founder", "org": "African Leadership University"},
            {"period": "2004", "role": "Founder", "org": "African Leadership Academy"},
            {"period": "early career", "role": "Consultant", "org": "McKinsey &amp; Company"},
        ],
        "education": [
            "MBA, Stanford Graduate School of Business (Arjay Miller Scholar)",
            "Bachelor's degree, Macalester College",
        ],
        "public_roles": [
            "Board member, The Rhodes Trust",
            "International Advisory Board, University of Waterloo",
            "Young Global Leader, World Economic Forum",
            "TED Fellow; Aspen Institute Fellow",
            "TIME 100 Most Influential People in the World (2019); TIME100 Impact Award (2023)",
            "Named among the top 15 emerging social entrepreneurs worldwide by Echoing Green",
        ],
        "notable": [
            {"point": "Sand's stated work spans modernising critical utilities in London, optimising rural "
                      "health systems in the US and Africa, electric mobility with Formula E, and "
                      "large-scale telecom infrastructure \u2014 the closest sector match to an "
                      "infrastructure portfolio of any vendor in this app.",
             "source": "https://gabi.unglobalcompact.org/person/fred-swaniker"},
            {"point": "ALX is training over 700,000 data and AI professionals, which gives Sand an unusual "
                      "and self-owned talent pipeline rather than competing for the same engineers as "
                      "every other integrator.",
             "source": "https://gabi.unglobalcompact.org/person/fred-swaniker"},
        ],
        "talking_points": [
            "The talent pipeline is the real structural differentiator \u2014 ALX feeds Sand directly. Test what that means for delivery cost and continuity on a long engagement.",
            "He frames Sand as physical AI for essential industries; that is a narrower and more testable claim than most vendors make. Ask for the utilities references specifically.",
            "McKinsey and Stanford GSB background means the commercial conversation will be structured, not evangelical, despite the mission framing.",
        ],
        "links": [
            {"label": "Sand Technologies leadership team", "url": "https://www.sandtech.com/leadership-team/"},
            {"label": "UN Global Compact profile", "url": "https://gabi.unglobalcompact.org/person/fred-swaniker"},
            {"label": "McKinsey interview", "url": "https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-strategy-and-corporate-finance-blog/the-exchange-fred-swaniker-on-empowering-africas-future-leaders"},
        ],
    },
    {
        "id": "sand-technologies-danai-mavunga",
        "vendor_slug": "sand-technologies",
        "name": "Danai Mavunga",
        "title": "Chief Operating Officer",
        "in_role_since": "Chief Operating Officer at Sand Technologies",
        "focus": "Runs operations, coupling people and strategy to drive business performance across "
                 "Sand's global delivery footprint.",
        "background": "More than a decade building systems and developing high-performing teams in "
                      "high-growth organisations, with an unusual combination of global health and "
                      "education experience before technology. She has worked with the World Health "
                      "Organization and African Leadership University, and now Sand Technologies \u2014 so "
                      "her background is in scaling delivery organisations across difficult operating "
                      "environments rather than in software.",
        "career": [
            {"period": "current", "role": "Chief Operating Officer", "org": "Sand Technologies"},
            {"period": "earlier", "role": "Operations and organisational leadership", "org": "African Leadership University"},
            {"period": "earlier", "role": "Operations and systems roles", "org": "World Health Organization"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Her experience spans the World Health Organization and African Leadership "
                      "University \u2014 scaling operations in constrained environments, which is closer "
                      "to a PortCo's reality than a Silicon Valley operating background.",
             "source": "https://www.sandtech.com/leadership-team/"},
            {"point": "Her stated focus is coupling people and strategy \u2014 the delivery-capability "
                      "question that determines whether an AI programme survives past pilot.",
             "source": "https://www.sandtech.com/leadership-team/"},
        ],
        "talking_points": [
            "The right counterpart for delivery model, team composition and how an engagement is actually staffed.",
            "Operations in global health means she has run programmes where failure has consequences; a realistic conversation about risk is available here.",
            "Sand is small relative to the integrators. Ask her directly about surge capacity and named-team continuity.",
        ],
        "links": [
            {"label": "Sand Technologies leadership team", "url": "https://www.sandtech.com/leadership-team/"},
        ],
        "notes": "Education and pre-WHO career were not confirmed in this pass and are deliberately left "
                 "blank rather than guessed.",
    },
    {
        "id": "sand-technologies-david-bratt",
        "vendor_slug": "sand-technologies",
        "name": "David Bratt",
        "title": "Chief Financial Officer",
        "in_role_since": "Chief Financial Officer at Sand Technologies",
        "focus": "Drives financial strategy and the funding structure enabling Sand to scale in the AI "
                 "industry.",
        "background": "A private-equity and M&amp;A finance operator \u2014 which makes him the most "
                      "natural counterpart at Sand for a private-markets investor. He brings nearly twenty "
                      "years of experience across M&amp;A, private equity and operational finance, helping "
                      "high-growth organisations expand globally. Most recently he helped scale Exiger, a "
                      "supply chain AI and SaaS business, into a multi-billion-dollar enterprise, where he "
                      "played a leading role in acquisitions, financial strategy and operational scaling.",
        "career": [
            {"period": "current", "role": "Chief Financial Officer", "org": "Sand Technologies"},
            {"period": "earlier", "role": "Finance leadership \u2014 acquisitions, financial strategy, operational scaling", "org": "Exiger (supply chain AI/SaaS)"},
            {"period": "earlier", "role": "M&amp;A, private equity and operational finance roles", "org": "High-growth technology organisations"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Helped scale Exiger, a supply chain AI and SaaS company, into a multi-billion-dollar "
                      "enterprise through acquisitions and operational scaling.",
             "source": "https://www.sandtech.com/leadership-team/"},
            {"point": "Nearly twenty years across M&amp;A, private equity and operational finance \u2014 the "
                      "person at Sand who will understand a PE owner's constraints without translation.",
             "source": "https://www.sandtech.com/leadership-team/"},
        ],
        "talking_points": [
            "Ex-private equity \u2014 speak to him in PE terms about value creation and he will engage on that basis.",
            "Sand is private and does not publish financials. He is the person who can answer vendor-viability questions directly.",
            "Exiger experience means he has scaled an AI/SaaS business commercially, not just financed one.",
        ],
        "links": [
            {"label": "Sand Technologies leadership team", "url": "https://www.sandtech.com/leadership-team/"},
        ],
        "notes": "Education and named prior employers before Exiger were not confirmed in this pass and "
                 "are deliberately left blank rather than guessed.",
    },

    # ================================================= SAP
    {
        "id": "sap-christian-klein",
        "vendor_slug": "sap",
        "name": "Christian Klein",
        "title": "Chief Executive Officer",
        "in_role_since": "Co-CEO from 11 October 2019 with Jennifer Morgan; sole CEO since 20 April 2020",
        "focus": "Holds overall responsibility for SAP's strategic direction, management and performance "
                 "\u2014 currently the Autonomous Enterprise strategy, the shift of the roadmap toward "
                 "agents, and the move to value-based pricing.",
        "background": "A career-long SAP insider who joined as a student in 1999 and rose through finance "
                      "and operations rather than sales or product. He was Chief Financial Officer of SAP "
                      "SuccessFactors, then SAP's Chief Controlling Officer, then Chief Operating Officer "
                      "of SAP from 2016 to 2021. He joined the Executive Board in 2018 as head of the "
                      "Intelligent Enterprise Group, combining global responsibility for the development "
                      "and delivery of SAP's core applications with a cross-board mandate for global "
                      "business operations \u2014 an unusually broad brief that prepared him for the CEO "
                      "role. He studied International Business Administration at the University of "
                      "Cooperative Education in Mannheim.",
        "career": [
            {"period": "2020\u2013present", "role": "Chief Executive Officer", "org": "SAP SE"},
            {"period": "2019\u20132020", "role": "Co-Chief Executive Officer (with Jennifer Morgan)", "org": "SAP SE"},
            {"period": "2018\u20132019", "role": "Executive Board member, head of the Intelligent Enterprise Group", "org": "SAP SE"},
            {"period": "2016\u20132021", "role": "Chief Operating Officer", "org": "SAP SE"},
            {"period": "earlier", "role": "Chief Controlling Officer", "org": "SAP SE"},
            {"period": "earlier", "role": "Chief Financial Officer", "org": "SAP SuccessFactors"},
            {"period": "1999", "role": "Joined SAP as a student", "org": "SAP SE"},
        ],
        "education": ["International Business Administration, University of Cooperative Education, Mannheim"],
        "public_roles": [],
        "notable": [
            {"point": "Has said 2026 will be the year AI delivers enterprise-scale return on investment, "
                      "and has redirected SAP's development backlog away from customer feature requests "
                      "toward agentic AI to make that happen.",
             "source": "https://erp.today/sap-ai-pricing-outcome-based-erp-economics/"},
            {"point": "Is moving SAP toward value-based and outcome-based pricing tied to autonomous "
                      "agents \u2014 a fundamental departure from ERP licensing logic, and the direction "
                      "worth pushing every vendor toward.",
             "source": "https://erp.today/sap-ai-pricing-outcome-based-erp-economics/"},
        ],
        "talking_points": [
            "Finance and operations background, not sales \u2014 he engages on business case and delivery economics before capability.",
            "He is explicitly open to outcome-based pricing. For a portfolio ERP conversation that is an open door, not a fight.",
            "The roadmap has been redirected toward agents. If a PortCo expects conventional feature delivery, set that expectation now.",
        ],
        "links": [
            {"label": "SAP leadership profile", "url": "https://www.generationunlimited.org/christian-klein"},
            {"label": "Q4 2025 results and strategy", "url": "https://www.capgemini.com/news/press-releases/full-year-2025-results/"},
            {"label": "Pricing strategy analysis", "url": "https://erp.today/sap-ai-pricing-outcome-based-erp-economics/"},
        ],
    },
    {
        "id": "sap-dominik-asam",
        "vendor_slug": "sap",
        "name": "Dominik Asam",
        "title": "Chief Financial Officer &amp; Member of the Executive Board",
        "in_role_since": "CFO since 7 March 2023, succeeding Luka Mucic",
        "focus": "Owns SAP's finances through the cloud transition and the agentic pivot \u2014 a record "
                 "\u20ac77B cloud backlog, free cash flow that nearly doubled to \u20ac8.24B, and the move "
                 "toward outcome-based pricing.",
        "background": "An engineer turned industrial CFO, hired specifically for the combination of global "
                      "finance and technology experience. He is a mechanical engineering graduate of the "
                      "Technical University of Munich and \u00c9cole Centrale Paris, with an MBA from "
                      "INSEAD. He held senior roles at Goldman Sachs and Siemens, then was CFO of Infineon "
                      "Technologies from 2011, and CFO and Executive Committee member of Airbus from April "
                      "2019 \u2014 where he steered the company through the COVID-19 pandemic while "
                      "driving business transformation. He also sits on the Supervisory Board of "
                      "Bertelsmann.",
        "career": [
            {"period": "2023\u2013present", "role": "Chief Financial Officer &amp; Executive Board member", "org": "SAP SE"},
            {"period": "2019\u20132023", "role": "Chief Financial Officer &amp; Executive Committee member", "org": "Airbus"},
            {"period": "2011\u20132019", "role": "Chief Financial Officer", "org": "Infineon Technologies AG"},
            {"period": "earlier", "role": "Senior finance roles", "org": "Siemens"},
            {"period": "earlier", "role": "Investment banking", "org": "Goldman Sachs"},
        ],
        "education": [
            "MBA, INSEAD",
            "Mechanical Engineering, Technical University of Munich and \u00c9cole Centrale Paris",
        ],
        "public_roles": ["Supervisory Board, Bertelsmann"],
        "notable": [
            {"point": "Was CFO of Airbus through the COVID-19 pandemic and of Infineon for eight years "
                      "before that \u2014 industrial, capital-intensive finance rather than software "
                      "finance, which is rare for an enterprise software CFO.",
             "source": "https://news.sap.com/?p=199110"},
            {"point": "Publicly compares SAP's cloud growth against ServiceNow and Microsoft Dynamics and "
                      "claims SAP is outgrowing the market by roughly ten percentage points \u2014 he "
                      "argues on comparative numbers, so come prepared with your own.",
             "source": "https://erp.today/sap-q4-2025-earnings-cloud-growth-analysis/"},
        ],
        "talking_points": [
            "Airbus and Infineon before SAP \u2014 he understands capital-intensive industrial businesses, which most software CFOs do not.",
            "A mechanical engineer with an INSEAD MBA and Goldman background: technically literate and commercially hard. Both halves of the conversation will be tested.",
            "Outcome-based pricing has to work in his numbers before it reaches a contract. He is the person who decides whether it can.",
        ],
        "links": [
            {"label": "SAP appointment announcement", "url": "https://news.sap.com/?p=199110"},
            {"label": "Q4 2025 earnings analysis", "url": "https://erp.today/sap-q4-2025-earnings-cloud-growth-analysis/"},
        ],
    },
]
