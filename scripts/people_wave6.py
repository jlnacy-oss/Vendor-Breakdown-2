# -*- coding: utf-8 -*-
"""
people_wave6.py — Person research wave 6, completed 15 September 2026.

CrowdStrike, Databricks and Deloitte leadership.

PROFESSIONAL, PUBLISHED INFORMATION ONLY. See people_schema.py.
Sources in this wave carried net worth, ages, physical descriptions, immigration
history and family details. None of it is here.
"""

RESEARCHED_ON = "2026-09-15"

PEOPLE = [
    # ================================================= CrowdStrike
    {
        "id": "crowdstrike-george-kurtz",
        "vendor_slug": "crowdstrike",
        "name": "George Kurtz",
        "title": "Founder, President &amp; Chief Executive Officer",
        "in_role_since": "Co-founded CrowdStrike in 2011 and has led it since",
        "focus": "Sets CrowdStrike's strategy, currently around consolidating fragmented security spend "
                 "onto Falcon and positioning it as the operating system of cybersecurity for the agentic "
                 "AI era.",
        "background": "A security practitioner who has built this company twice over. He began in "
                      "accounting and security consulting, holding senior security roles at "
                      "PricewaterhouseCoopers and Ernst &amp; Young, then founded Foundstone in October "
                      "1999 \u2014 recruiting the other six founders himself \u2014 and built it into a "
                      "worldwide security products and services firm with one of the industry's leading "
                      "incident response practices. McAfee acquired it in October 2004 and he stayed, "
                      "rising to Worldwide Chief Technology Officer, General Manager and SVP of Enterprise "
                      "at what was then a multi-billion-dollar security business. That seat convinced him "
                      "the signature-based, on-premise model was broken. He left McAfee in November 2011 "
                      "for Warburg Pincus as entrepreneur-in-residence, designing the company before "
                      "raising outside money, and co-founded CrowdStrike in February 2012 with Dmitri "
                      "Alperovitch and Gregg Marston, Foundstone's former CFO. Warburg Pincus seeded it "
                      "with $25M. He took the company public in 2019. He is credited with helping create "
                      "the field of vulnerability management and authored <i>Hacking Exposed: Network "
                      "Security Secrets &amp; Solutions</i>.",
        "career": [
            {"period": "2012\u2013present", "role": "Co-Founder, President &amp; Chief Executive Officer", "org": "CrowdStrike"},
            {"period": "2011\u20132012", "role": "Entrepreneur-in-Residence", "org": "Warburg Pincus"},
            {"period": "2004\u20132011", "role": "Worldwide Chief Technology Officer, General Manager, SVP Enterprise", "org": "McAfee"},
            {"period": "1999\u20132004", "role": "Founder &amp; Chief Executive Officer", "org": "Foundstone (acquired by McAfee, 2004)"},
            {"period": "earlier", "role": "Senior security positions", "org": "Ernst &amp; Young and PricewaterhouseCoopers"},
        ],
        "education": ["BS Accounting, Seton Hall University"],
        "public_roles": [
            "Author, <i>Hacking Exposed: Network Security Secrets &amp; Solutions</i>",
            "Named a cybersecurity innovator by TIME (2015)",
        ],
        "notable": [
            {"point": "Credited with helping create the field of vulnerability management and with leading "
                      "the industry shift toward cloud-based security architectures \u2014 the thesis "
                      "CrowdStrike was built on.",
             "source": "https://en.wikipedia.org/wiki/George_Kurtz"},
            {"point": "Founded, scaled and sold one security company before building a second to over $5B "
                      "of annual recurring revenue \u2014 and remains the public face of the company "
                      "through both its growth and the July 2024 outage.",
             "source": "https://www.crowdstrike.com/en-us/about-us/executive-team/george-kurtz/"},
        ],
        "talking_points": [
            "A genuine practitioner, not a career executive \u2014 a technical conversation about detection architecture will land, a procurement pitch less so.",
            "He spent seven years inside McAfee watching a legacy model fail; he is unusually alert to incumbency and complacency arguments.",
            "The July 2024 outage is unavoidable context in any critical-infrastructure conversation. He has addressed it publicly; expect him to, and be specific about what assurance you need.",
        ],
        "links": [
            {"label": "CrowdStrike executive profile", "url": "https://www.crowdstrike.com/en-us/about-us/executive-team/george-kurtz/"},
            {"label": "CrowdStrike board profile", "url": "https://www.crowdstrike.com/en-us/about-us/board-of-directors/george-kurtz/"},
        ],
    },
    {
        "id": "crowdstrike-burt-podbere",
        "vendor_slug": "crowdstrike",
        "name": "Burt Podbere",
        "title": "Chief Financial Officer",
        "in_role_since": "CFO through CrowdStrike's private financing rounds and its 2019 IPO",
        "focus": "Long-term financial management and the strategic direction of CrowdStrike's worldwide "
                 "expansion \u2014 currently the shift from seat-based licensing to Falcon Flex "
                 "consumption commitments.",
        "background": "A serial venture-backed CFO who has taken this company through the whole arc from "
                      "private financing to public markets. He guided CrowdStrike through more than $1B in "
                      "equity financing and its high-profile 2019 IPO. Before CrowdStrike he held CFO "
                      "positions at OpenDNS, Net Optics and Epocrates, with extensive international finance "
                      "experience.",
        "career": [
            {"period": "before 2019\u2013present", "role": "Chief Financial Officer", "org": "CrowdStrike"},
            {"period": "earlier", "role": "Chief Financial Officer", "org": "OpenDNS"},
            {"period": "earlier", "role": "Chief Financial Officer", "org": "Net Optics"},
            {"period": "earlier", "role": "Senior finance leadership", "org": "Epocrates"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Guided CrowdStrike through over $1B of equity financing and its 2019 IPO, and now "
                      "reports the Falcon Flex metrics \u2014 $1.69B of ending ARR, up over 120% \u2014 "
                      "that evidence the consolidation thesis.",
             "source": "https://www.crowdstrike.com/en-gb/about-us/executive-team/burt-podbere/"},
            {"point": "Oversaw 370 basis points of non-GAAP operating margin expansion to roughly 25% in "
                      "FY2026, alongside a record $1.01B of net new ARR.",
             "source": "https://www.businesswire.com/news/home/20260303140639/en/CrowdStrike-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Financial-Results"},
        ],
        "talking_points": [
            "Falcon Flex is a consumption commitment structure, and he owns how it is priced \u2014 the right counterpart for a portfolio-wide commitment.",
            "Three prior CFO roles at venture-backed security and health-tech companies; he negotiates for a living and expects the same.",
            "With margin expanding and net new ARR at a record, the company is not under pressure to discount. Structure and term will move further than price.",
        ],
        "links": [
            {"label": "CrowdStrike executive profile", "url": "https://www.crowdstrike.com/en-gb/about-us/executive-team/burt-podbere/"},
            {"label": "FY2026 results", "url": "https://www.businesswire.com/news/home/20260303140639/en/CrowdStrike-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Financial-Results"},
        ],
        "notes": "Education and the exact start date of his CrowdStrike tenure were not confirmed in this "
                 "pass and are deliberately left blank rather than guessed.",
    },

    # ================================================= Databricks
    {
        "id": "databricks-ali-ghodsi",
        "vendor_slug": "databricks",
        "name": "Ali Ghodsi",
        "title": "Co-Founder &amp; Chief Executive Officer",
        "in_role_since": "CEO since January 2016; co-founded Databricks in 2013",
        "focus": "Runs Databricks' growth and international expansion, and is the public voice of the "
                 "data-intelligence thesis \u2014 one governed source of enterprise truth with AI embedded "
                 "throughout.",
        "background": "An academic computer scientist who turned out to be an exceptional operator. He "
                      "holds a PhD in distributed computing from KTH Royal Institute of Technology in "
                      "Sweden and an MBA, and came to UC Berkeley as a visiting scholar, joining the AMPLab "
                      "group. He was one of the creators of Apache Spark, and ideas from his research on "
                      "resource management, scheduling and data caching went into Apache Mesos and Apache "
                      "Hadoop. He was one of the seven Berkeley researchers who incorporated Databricks in "
                      "2013, serving as VP of Engineering and Product Management \u2014 the operational "
                      "leader building the actual product and go-to-market \u2014 before taking over as "
                      "CEO in January 2016 from Ion Stoica. He remains an adjunct professor at UC Berkeley "
                      "and sits on the board of its RiseLab.",
        "career": [
            {"period": "2016\u2013present", "role": "Chief Executive Officer", "org": "Databricks"},
            {"period": "2013\u20132016", "role": "Co-Founder &amp; VP of Engineering and Product Management", "org": "Databricks"},
            {"period": "2009\u20132013", "role": "Visiting scholar, AMPLab; co-creator of Apache Spark", "org": "UC Berkeley"},
            {"period": "ongoing", "role": "Adjunct Professor; board member, RiseLab", "org": "UC Berkeley"},
        ],
        "education": [
            "PhD Distributed Computing, KTH Royal Institute of Technology, Sweden (2006)",
            "MBA, Mid-Sweden University (2003)",
        ],
        "public_roles": [
            "Adjunct Professor, University of California, Berkeley",
            "Board member, UC Berkeley RiseLab",
        ],
        "notable": [
            {"point": "Co-created Apache Spark, and his research on resource management, scheduling and "
                      "data caching was applied in Apache Mesos and Apache Hadoop \u2014 he built parts of "
                      "the infrastructure the industry runs on.",
             "source": "https://www.databricks.com/dataaisummit/speaker/ali-ghodsi"},
            {"point": "Has said customers who a year or two ago insisted on frontier proprietary models are "
                      "now adopting open-source and Chinese models as token costs bite \u2014 the shift "
                      "Unity AI Gateway was built to serve.",
             "source": "https://www.cnbc.com/2026/08/13/databricks-funding-round-190-billion-valuation.html"},
        ],
        "talking_points": [
            "A researcher-CEO: the governance and cost-control argument will get a more substantive hearing than a capability pitch.",
            "He is explicit that model choice is commoditising and the data layer is where the durable advantage sits \u2014 useful framing for a portfolio Data Foundation conversation.",
            "Databricks raised roughly $20B in 20 months while cash-flow positive. Ask why; his board's answer was concern about an AI slump.",
        ],
        "links": [
            {"label": "Databricks speaker profile", "url": "https://www.databricks.com/dataaisummit/speaker/ali-ghodsi"},
            {"label": "Databricks founders page", "url": "https://www.databricks.com/company/founders"},
            {"label": "August 2026 funding round", "url": "https://www.cnbc.com/2026/08/13/databricks-funding-round-190-billion-valuation.html"},
        ],
    },
    {
        "id": "databricks-matei-zaharia",
        "vendor_slug": "databricks",
        "name": "Matei Zaharia",
        "title": "Co-Founder &amp; Chief Technology Officer",
        "in_role_since": "Co-founded Databricks in 2013 and served as its first CTO",
        "focus": "Owns the technology and research roadmap \u2014 Apache Spark, Delta Lake, MLflow, DBRX "
                 "and the current work on combining large language models with external data sources.",
        "background": "He created Apache Spark as his PhD project at UC Berkeley's AMPLab in 2009, work "
                      "that won the 2014 ACM Doctoral Dissertation Award and a US Presidential Early Career "
                      "Award for Scientists and Engineers. He has since led or contributed to most of the "
                      "open-source projects the modern data stack rests on \u2014 MLflow, Delta Lake and "
                      "DBRX among them. He is an Associate Professor of Computer Science at UC Berkeley, "
                      "having returned there after years at Stanford, and holds the CTO role at Databricks "
                      "alongside it. His current research is on combining LLMs with external data sources "
                      "such as search systems, and improving their efficiency and output quality.",
        "career": [
            {"period": "2013\u2013present", "role": "Co-Founder &amp; Chief Technology Officer", "org": "Databricks"},
            {"period": "ongoing", "role": "Associate Professor of Computer Science", "org": "UC Berkeley"},
            {"period": "earlier", "role": "Assistant Professor of Computer Science", "org": "Stanford University"},
            {"period": "2009\u20132013", "role": "PhD researcher, AMPLab; created Apache Spark", "org": "UC Berkeley"},
        ],
        "education": ["PhD Computer Science, UC Berkeley (2014 ACM Doctoral Dissertation Award)"],
        "public_roles": [
            "Associate Professor of Computer Science, UC Berkeley",
            "US Presidential Early Career Award for Scientists and Engineers (PECASE)",
        ],
        "notable": [
            {"point": "Created Apache Spark, which set a world record for data sorting speed in 2014 and "
                      "became the foundation of the modern data platform industry.",
             "source": "https://www.databricks.com/jp/blog/author/matei-zaharia"},
            {"point": "His current research is specifically on grounding large language models in external "
                      "data sources and improving efficiency and result quality \u2014 the technical problem "
                      "behind every enterprise RAG deployment.",
             "source": "https://www.databricks.com/jp/blog/author/matei-zaharia"},
        ],
        "talking_points": [
            "The most technically credentialed person in this contact list; an architecture conversation will be substantive and worth preparing for.",
            "Still an active academic, so he engages with the limits of the technology as readily as its capabilities \u2014 useful for a realistic view of what agents can do on operational data.",
            "His research agenda is effectively Databricks' three-year roadmap. What he is publishing is what the product will do.",
        ],
        "links": [
            {"label": "Databricks author profile", "url": "https://www.databricks.com/jp/blog/author/matei-zaharia"},
            {"label": "Databricks founders page", "url": "https://www.databricks.com/company/founders"},
        ],
    },

    # ================================================= Deloitte
    {
        "id": "deloitte-joe-ucuzoglu",
        "vendor_slug": "deloitte",
        "name": "Joe Ucuzoglu",
        "title": "Global Chief Executive Officer",
        "in_role_since": "Appointed December 2022, taking the role in January 2023",
        "focus": "Leads the largest professional services organisation in the world \u2014 over 470,000 "
                 "professionals and more than $70B of revenue \u2014 across audit and assurance, tax and "
                 "legal, consulting, risk advisory and financial advisory.",
        "background": "A career Deloitte partner who came up through audit rather than consulting, which "
                      "shapes how he thinks about risk and governance. He joined the firm in 1997 and led "
                      "the US Audit &amp; Assurance practice, served as US National Managing Partner for "
                      "Government, Regulatory and Professional Matters, and was CEO of Deloitte US from "
                      "2019 to 2022 before taking the global role. He speaks regularly at US business "
                      "schools including Duke Fuqua, Yale SOM, Virginia Darden, USC Marshall and Notre Dame "
                      "Mendoza.",
        "career": [
            {"period": "2023\u2013present", "role": "Global Chief Executive Officer", "org": "Deloitte"},
            {"period": "2019\u20132022", "role": "Chief Executive Officer", "org": "Deloitte US"},
            {"period": "earlier", "role": "Chief Executive Officer, Audit &amp; Assurance", "org": "Deloitte US"},
            {"period": "earlier", "role": "National Managing Partner, Government, Regulatory and Professional Matters", "org": "Deloitte US"},
            {"period": "from 1997", "role": "Joined the firm; audit and assurance", "org": "Deloitte"},
        ],
        "education": ["BS Accounting, University of Southern California"],
        "public_roles": [
            "Member, Business Roundtable",
            "Member, Council on Foreign Relations",
            "Member, World Economic Forum International Business Council",
            "Board, Yale School of Management Program on Stakeholder Innovation and Management",
            "Board of Trustees, University of Southern California",
            "Chair, Board of Councilors, USC Marshall School of Business",
            "Board of Directors, US Chamber of Commerce (former)",
            "Executive Committee, Partnership for New York City",
        ],
        "notable": [
            {"point": "Under his leadership Deloitte published research in 2023 sizing green hydrogen as a "
                      "potential $1.4 trillion global market by 2050, which he framed as an opportunity to "
                      "accelerate decarbonisation in the hardest-to-abate sectors \u2014 directly adjacent "
                      "to energy-transition infrastructure.",
             "source": "https://wikipedia.com/wiki/Joe_Ucuzoglu"},
            {"point": "Committed $3B through FY2030 to generative and agentic AI, and built Zora AI with "
                      "NVIDIA \u2014 making Deloitte unusual among the Big Four in running a product "
                      "business rather than only an advisory practice.",
             "source": "https://www.deloitte.com/global/en/about/press-room/global-revenue-announcement.html"},
        ],
        "talking_points": [
            "Audit background, not consulting \u2014 governance, controls and independence are native ground, and he will raise them before you do.",
            "Deloitte's green hydrogen work under him is a genuine energy-transition credential, not a marketing position.",
            "If a Deloitte member firm audits a PortCo, independence rules constrain what consulting can follow. He knows those rules better than anyone in this list; ask him directly rather than working around it.",
        ],
        "links": [
            {"label": "Deloitte leadership profile", "url": "https://www.deloitte.com/na/en/about/people/people-stories/joe-ucuzoglu.html"},
            {"label": "World Economic Forum profile", "url": "https://cn.weforum.org/agenda/authors/joe-ucuzoglu"},
            {"label": "Deloitte FY2025 global revenue", "url": "https://www.deloitte.com/global/en/about/press-room/global-revenue-announcement.html"},
        ],
    },
]
