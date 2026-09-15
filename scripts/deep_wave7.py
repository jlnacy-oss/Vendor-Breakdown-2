# -*- coding: utf-8 -*-
"""
deep_wave7.py — Research wave 7, completed 15 September 2026.

PwC, Salesforce, SAP, ServiceNow, Snowflake.
"""

VENDORS = [
    # =================================================================
    {
        "slug": "pwc",
        "name": "PwC",
        "website": "https://www.pwc.com",
        "linkedin": "https://www.linkedin.com/company/pwc",
        "group": "SI / Consulting",
        "category": "Big Four professional services network",
        "tagline": "The slowest-growing Big Four network, cutting headcount while spending $1.5B a year "
                   "on AI capability",
        "founded": "1998 (merger of Price Waterhouse, founded 1849, and Coopers &amp; Lybrand, founded 1854)",
        "hq": "London, United Kingdom (PricewaterhouseCoopers International Limited; a network of member firms)",
        "employees": "364,000 across 137 countries and territories \u2014 down 5,600 over the year to 30 "
                     "June 2025, with the US firm cutting roughly 1,500 roles",
        "ownership": "Private network of member firms",
        "revenue": "$56.9B gross revenue for FY2025 (year ended 30 June 2025), up 2.7% in local currency "
                   "and 2.9% in US dollars from $55.4B. The Americas grew 5.5% to $25.5B and EMEA 2.5% to "
                   "$22.5B, while Asia declined 4.1% to $8.8B",
        "revenue_short": "$56.9B (FY25)",
        "offering": "Assurance, tax and legal, and advisory, with Strategy& as the premium strategy arm. "
                    "New AI-specific services include Assurance for AI \u2014 independent assurance over "
                    "whether AI systems are designed, deployed and operated responsibly.",
        "digital_twin": "No",
        "genai": "Yes (advisory + assurance)",
        "buyer": "CFO, audit committee, risk and transformation leadership",
        "customers": [],
        "people": [
            {"name": "Mohamed Kande", "title": "Global Chairman"},
        ],
        "description": "$56.9B of FY2025 revenue on 2.7% growth \u2014 the slowest of the Big Four \u2014 "
                       "while cutting 5,600 roles and quietly dropping the previous leadership's pledge to "
                       "add 100,000 people by mid-2026. Against that, it invested nearly $1.5B in AI "
                       "capability and upskilled over 315,000 of its own people.",
        "position_note": "The most interesting thing PwC has built for an infrastructure portfolio is not a "
                         "consulting practice but Assurance for AI \u2014 independent assurance over AI "
                         "systems, which is a natural extension of audit into a domain most boards cannot "
                         "yet evaluate. For a fund that has to give portfolio companies confidence their AI "
                         "deployments are defensible, that is a distinct service from the implementation "
                         "work every other firm sells, and it carries the independence question with it: "
                         "assurance means something precisely because the assurer did not build the thing. "
                         "The commercial caveat is capacity \u2014 Kande has said publicly that PwC is "
                         "hiring hundreds of engineers globally and simply cannot find enough qualified "
                         "candidates.",
        "gip_connection": "No publicly disclosed GIP relationship. As with the other Big Four, check for an "
                          "existing audit relationship at fund or PortCo level first \u2014 and note that "
                          "if you want PwC's AI assurance work, that independence constraint cuts the other "
                          "way and may be the point rather than the obstacle.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "AI assurance",
                "status": "Deployed",
                "deployment": "Assurance for AI, launched to provide independent assurance over AI systems "
                              "\u2014 giving businesses confidence that systems are designed, deployed and "
                              "operated responsibly and transparently, complementing rather than replacing "
                              "existing services.",
                "impact": "Extends the audit franchise into AI governance, a service distinct from "
                          "implementation consulting",
                "source": "https://www.accountingtoday.com/news/pwc-global-revenue-grows-to-56-9b",
            },
            {
                "sector": "AI investment",
                "status": "Deployed",
                "deployment": "Nearly $1.5B invested during FY2025 to scale next-generation AI capabilities "
                              "across the network, part of $3.1B of total network investment, alongside 12 "
                              "strategic acquisitions.",
                "impact": "Over 315,000 PwC people upskilled in AI; the firm works with 82% of the Fortune "
                          "Global 500",
                "source": "https://www.cpapracticeadvisor.com/2025/10/28/pwc-reports-global-revenue-of-56-9-billion-in-2025/171838/",
            },
            {
                "sector": "Network performance",
                "status": "Deployed",
                "deployment": "Revenue growth across most of the network, with the strongest performance in "
                              "the US and Brazil and fee growth in Japan, South Korea and India despite a "
                              "regional decline.",
                "impact": "Americas up 5.5% to $25.5B; EMEA up 2.5% to $22.5B; Asia down 4.1% to $8.8B",
                "source": "https://www.consulting.us/news/12580/pwc-grows-global-revenue-by-27-to-569-billion",
            },
            {
                "sector": "Talent constraint",
                "status": "Research finding",
                "deployment": "An active global search for hundreds of AI engineers to support the "
                              "expansion of technology-driven services.",
                "impact": "Kande has stated publicly that PwC cannot find enough qualified candidates \u2014 "
                          "a capacity constraint on delivery, not a demand problem",
                "source": "https://finance.yahoo.com/news/global-chairman-mohamed-kande-says-165750085.html",
            },
        ],
        "customer_sentiment": "PwC works with 82% of the Fortune Global 500, so the relationship base is "
                              "intact. The demand signal is weaker than the peer set: 2.7% growth against "
                              "Deloitte's 4.8%, KPMG's 5.1% and EY's 4.0%, with Asia declining outright. "
                              "PwC describes it as a solid performance in a challenging climate, which is "
                              "fair, but the regional divergence suggests clients are prioritising and PwC "
                              "is not consistently making the cut. No client-level outcomes are published.",
        "sentiment_bull": [
            "Assurance for AI is a genuinely differentiated service that leans on the audit franchise rather than competing head-on with implementation firms",
            "Nearly $1.5B of AI investment in a single year, plus 12 strategic acquisitions",
            "Over 315,000 people upskilled in AI \u2014 the largest disclosed internal upskilling programme in this peer set",
            "Works with 82% of the Fortune Global 500, giving unusually broad cross-sector visibility",
        ],
        "sentiment_bear": [
            "Slowest growth of the Big Four at 2.7% local currency \u2014 roughly half Deloitte's and KPMG's rates",
            "Headcount fell 5,600 and the previous pledge to add 100,000 people by mid-2026 was quietly dropped",
            "Asia revenue declined 4.1%, the only outright regional decline among the Big Four this cycle",
            "Kande has publicly acknowledged PwC cannot hire enough AI engineers, which constrains delivery capacity",
            "Member-firm structure means the aggregate describes a network, not the entity you contract with",
        ],
        "employee_sentiment": "The direction is contraction: headcount down 5,600 to 364,000, roughly 1,500 "
                              "roles cut at the US firm explicitly because attrition was at historic lows, "
                              "and a growth pledge abandoned. Set against that, over 315,000 people were "
                              "upskilled in AI, which is a substantial investment in the remaining "
                              "workforce. No independent employer-review data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1998", "Founded"),
            ("364,000", "People"),
            ("$56.9B", "FY2025 revenue"),
            ("+2.7%", "Growth (local ccy)"),
            ("$1.5B", "AI investment"),
        ],
    },

    # =================================================================
    {
        "slug": "salesforce",
        "name": "Salesforce",
        "website": "https://www.salesforce.com",
        "linkedin": "https://www.linkedin.com/company/salesforce",
        "group": "Enterprise software",
        "category": "CRM, data platform &amp; agentic AI",
        "tagline": "Rebuilt around agents \u2014 and now measuring work delivered rather than seats sold",
        "founded": "1999",
        "hq": "San Francisco, California",
        "employees": "Growing, mostly in sales \u2014 Benioff has said agents can qualify leads and provide "
                     "service but selling still requires people",
        "ownership": "Public (NYSE: CRM)",
        "revenue": "$41.5B in FY2026 (year ended 31 January 2026), up 10% (9% constant currency). Total RPO "
                   "of $72.4B, up 14%; current RPO of $35.1B, up 16%. Operating cash flow of roughly $15B",
        "revenue_short": "$41.5B (FY26)",
        "offering": "The CRM suite \u2014 Sales, Service, Marketing and industry clouds \u2014 plus Data 360 "
                    "(formerly Data Cloud), Tableau, Slack, MuleSoft and Informatica, all under Agentforce "
                    "360 as the agentic layer. Informatica was acquired in November 2025.",
        "digital_twin": "No",
        "genai": "Yes (Agentforce)",
        "buyer": "Chief Revenue Officer, customer service leadership, and increasingly the CIO for the data layer",
        "customers": ["Pfizer", "Marriott", "US Army"],
        "people": [
            {"name": "Marc Benioff", "title": "Chair &amp; Chief Executive Officer"},
            {"name": "Robin Washington", "title": "President, Chief Financial and Operating Officer"},
        ],
        "description": "Agentforce ARR reached $800M in FY2026, up 169%, and passed $1.2B by Q1 FY2027 \u2014 "
                       "up 205%. Combined Agentforce and Data 360 ARR exceeds $2.9B. Salesforce has started "
                       "reporting Agentic Work Units, a measure of tasks completed rather than licences sold.",
        "position_note": "The metric to pay attention to is Agentic Work Units \u2014 2.4 billion delivered "
                         "to date, growing 57% quarter over quarter, defined as moments where AI did work "
                         "rather than just reasoned about it. Whatever you think of the framing, it is the "
                         "first serious attempt by a major vendor to price and report AI on output rather "
                         "than seats, and it is the direction SAP has also signalled. For a portfolio "
                         "programme that matters because seat-based AI budgeting breaks down quickly. The "
                         "second useful signal is that over 60% of Q4 Agentforce and Data 360 bookings came "
                         "from existing customer expansion \u2014 this is landing inside the installed base, "
                         "not winning new logos, which is exactly the pattern to expect at PortCos already "
                         "running Salesforce.",
        "gip_connection": "No publicly disclosed GIP relationship. Salesforce is likely present at PortCos "
                          "with significant customer-facing operations. Note that Informatica \u2014 now a "
                          "Salesforce company \u2014 is data management tooling that may already be deployed "
                          "independently in some portfolio companies.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of CRM only.",
        "use_cases": [
            {
                "sector": "Agentic AI commercial traction",
                "status": "Deployed",
                "deployment": "Agentforce sold across sales, service and platform, with deals closed since "
                              "launch and accounts moving into production.",
                "impact": "Agentforce ARR of $800M at FY2026 close, up 169%, reaching $1.2B and 205% growth "
                          "by Q1 FY2027; over 29,000 deals closed since launch, up 50% quarter over quarter, "
                          "with accounts in production up nearly 50% Q/Q",
                "source": "https://www.salesforce.com/news/press-releases/2026/02/25/fy26-q4-earnings/",
            },
            {
                "sector": "Output-based measurement",
                "status": "Deployed",
                "deployment": "Agentic Work Units introduced to measure tasks actually accomplished by an "
                              "AI agent across Agentforce and Slack, rather than seats or licences.",
                "impact": "2.4 billion AWUs delivered to date, growing 57% quarter over quarter, from nearly "
                          "20 trillion tokens processed \u2014 up 5x year over year",
                "source": "https://s205.q4cdn.com/626266368/files/doc_financials/2026/q4/CRM-Q4-FY26-Earnings-Press-Release.pdf",
            },
            {
                "sector": "Data foundation",
                "status": "Deployed",
                "deployment": "Data 360 as the governed data layer beneath the agents, including Zero Copy "
                              "ingestion that leaves data in place rather than duplicating it.",
                "impact": "112 trillion records ingested in FY2026, up 114%, including 53 trillion via Zero "
                          "Copy, up 310%; 18 terabytes of unstructured data processed",
                "source": "https://www.salesforce.com/news/press-releases/2026/02/25/fy26-q4-earnings/",
            },
            {
                "sector": "Expansion motion",
                "status": "Deployed",
                "deployment": "Agentforce and Data 360 sold primarily into the existing customer base rather "
                              "than as new-logo acquisition, with all top ten Q4 wins including the full "
                              "Agentforce 360 stack.",
                "impact": "More than 60% of Q4 Agentforce and Data 360 bookings came from existing customer "
                          "expansion; industry businesses ended the year at $6.6B ARR, up nearly 20%",
                "source": "https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Fourth-Quarter-Fiscal-2026-Results/default.aspx",
            },
        ],
        "customer_sentiment": "Expansion within the installed base is the strongest evidence \u2014 over 60% "
                              "of agentic bookings came from existing customers, and named references "
                              "include Pfizer, Marriott and the US Army. The market is less convinced: "
                              "despite Agentforce passing $1B of annualised revenue in Q1 FY2027, the "
                              "backlog came in short of expectations and full-year guidance slightly missed, "
                              "feeding a broader investor anxiety that AI erodes seat-based software "
                              "economics faster than vendors can replace the revenue.",
        "sentiment_bull": [
            "Agentforce ARR grew 169% to $800M in FY2026 and 205% to $1.2B by Q1 FY2027 \u2014 genuine, fast monetisation",
            "$72.4B of total RPO, up 14%, with roughly $15B of operating cash flow",
            "Agentic Work Units are the first serious attempt by a major vendor to report AI on output rather than seats",
            "Over 60% of agentic bookings come from existing-customer expansion, which is a far cheaper growth motion than new logos",
        ],
        "sentiment_bear": [
            "Total revenue growth of 10% is modest for a company positioning itself at the centre of an AI transformation",
            "Q1 FY2027 backlog fell short of expectations and full-year guidance slightly missed \u2014 the agentic numbers are not yet moving the aggregate",
            "Agentforce and Data 360's $2.9B combined ARR includes $1.1B from the acquired Informatica business, so organic agentic ARR is smaller than the headline",
            "Headcount is growing mostly in sales, which undercuts the argument that agents replace human effort",
            "Broad investor scepticism about seat-based SaaS in an agentic world is depressing the multiple regardless of execution",
        ],
        "employee_sentiment": "Not covered in this pass. The one disclosed signal is directional rather "
                              "than sentiment-based: headcount is growing, concentrated in sales, on "
                              "Benioff's stated logic that agents can qualify and serve but selling still "
                              "requires people to reach a fragmented market.",
        "glassdoor": None,
        "kpis": [
            ("1999", "Founded"),
            ("$41.5B", "FY2026 revenue"),
            ("$800M", "Agentforce ARR"),
            ("$72.4B", "Total RPO"),
            ("2.4B", "Agentic Work Units"),
        ],
    },

    # =================================================================
    {
        "slug": "sap",
        "name": "SAP",
        "website": "https://www.sap.com",
        "linkedin": "https://www.linkedin.com/company/sap",
        "group": "Enterprise software",
        "category": "Enterprise resource planning &amp; business AI",
        "tagline": "AI is now in two-thirds of cloud orders \u2014 and SAP is rebuilding its roadmap around "
                   "agents rather than features",
        "founded": "1972",
        "hq": "Walldorf, Germany",
        "employees": "Not disclosed in the results reviewed in this pass",
        "ownership": "Public (XETRA: SAP; NYSE: SAP)",
        "revenue": "Q4 2025 revenue of \u20ac9.7B, up 9%, with cloud revenue of \u20ac5.6B, up 26%, and Cloud "
                   "ERP Suite at \u20ac4.9B, up 23%. Total cloud backlog reached a record \u20ac77B, up 30% "
                   "at constant currency. Free cash flow nearly doubled to \u20ac8.24B",
        "revenue_short": "\u20ac9.7B/qtr (Q4 25)",
        "offering": "S/4HANA and the Cloud ERP Suite delivered through RISE with SAP and GROW with SAP, plus "
                    "Business Data Cloud, the Business Technology Platform, and Business AI \u2014 the Joule "
                    "assistant, Joule Work, the Business AI Platform, and the Autonomous Suite agents.",
        "digital_twin": "Via partners",
        "genai": "Yes (Business AI, Joule)",
        "buyer": "CFO, COO and CIO in asset-heavy and process-heavy industries",
        "customers": ["Siemens"],
        "people": [
            {"name": "Christian Klein", "title": "Chief Executive Officer"},
            {"name": "Dominik Asam", "title": "Chief Financial Officer"},
        ],
        "description": "The dominant ERP vendor, with a record \u20ac77B total cloud backlog and Business AI "
                       "included in two-thirds of Q4 2025 cloud order entry. Joule customer numbers grew "
                       "ninefold across 2025, and SAP is now shifting its product roadmap from features "
                       "toward autonomous agents.",
        "position_note": "SAP's structural argument is the one that matters most for asset-heavy "
                         "businesses: general-purpose models cannot reach the business data that sits "
                         "inside an ERP, and Joule can. Klein's own example is a customer win where SAP "
                         "replaced a competitor by combining LLMs with its business data foundation to "
                         "reinvent last-mile delivery logistics \u2014 a capability he argues competitors "
                         "without deep ERP data cannot replicate. Two forward signals worth tracking. SAP "
                         "is moving toward value-based and outcome-based pricing tied to autonomous agents, "
                         "away from traditional ERP licensing logic. And it has deliberately reshuffled its "
                         "development backlog away from customer feature requests toward agents \u2014 which "
                         "means PortCos expecting a steady stream of conventional enhancements may be "
                         "disappointed.",
        "gip_connection": "No publicly disclosed GIP relationship. SAP is the most likely core ERP at "
                          "asset-heavy PortCos, which makes it a Corporate Functions Efficiency play in the "
                          "reference model, and potentially an Asset Optimization one wherever operational "
                          "data already sits inside the SAP estate.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "AI attach rate",
                "status": "Deployed",
                "deployment": "Business AI sold as part of cloud deals rather than as a separate upsell, "
                              "with AI features included in cloud order entry as standard.",
                "impact": "Business AI included in two-thirds of Q4 2025 cloud order entry, a 20% increase "
                          "on the prior quarter; 90% of the 50 largest deals included AI or Business Data Cloud",
                "source": "https://www.asug.com/insights/q4-and-fy-2025-sap-delivers-record-cloud-growth-as-business-ai-fuels-momentum",
            },
            {
                "sector": "Professional services productivity",
                "status": "Deployed",
                "deployment": "Joule for Consultants at Siemens, where the assistant works across the SAP "
                              "application suite with access to business data that general-purpose models "
                              "cannot reach.",
                "impact": "Siemens consultants reinvesting 25% of their weekly time into higher-value work; "
                          "Joule customer numbers grew ninefold across 2025",
                "source": "https://www.cxtoday.com/ai-automation-in-cx/sap-business-ai-q4-2025-earnings/",
            },
            {
                "sector": "Contracted backlog",
                "status": "Deployed",
                "deployment": "Total cloud backlog tracked as the long-lead indicator, built on RISE and "
                              "GROW with SAP adoption across industries and regions.",
                "impact": "Record \u20ac77B total cloud backlog at end-2025, up 30% at constant currency; "
                          "nearly two-thirds of deals above \u20ac1M involved four or more lines of business, "
                          "a 25-percentage-point increase",
                "source": "https://erp.today/sap-q4-2025-earnings-cloud-growth-analysis/",
            },
            {
                "sector": "Agentic roadmap",
                "status": "Announced",
                "deployment": "The Autonomous Enterprise strategy, with the Business AI Platform and Joule "
                              "Work launching in Q3 2026, close to 50 assistants by the end of Q3, and more "
                              "than 400 Autonomous Suite agents by year end, plus three further ERP "
                              "migration assistants with ten underlying agents.",
                "impact": "Development backlog deliberately reshuffled from customer feature requests toward "
                          "agentic AI; Klein has described moving toward value-based and outcome-based "
                          "pricing tied to agents",
                "source": "https://erp.today/sap-ai-pricing-outcome-based-erp-economics/",
            },
        ],
        "customer_sentiment": "Buying behaviour is the strongest evidence and it points to consolidation "
                              "onto the suite: nearly two-thirds of deals above \u20ac1M involved four or "
                              "more lines of business, a 25-point jump, which supports SAP's best-of-suite "
                              "argument over best-of-breed. The risk sits in expectation management \u2014 "
                              "SAP has redirected its roadmap toward agents, and delivery teams that treat "
                              "AI as a later phase risk disappointing customers who bought specifically for "
                              "it.",
        "sentiment_bull": [
            "Record \u20ac77B total cloud backlog, up 30% at constant currency, giving strong multi-year visibility",
            "Business AI attached to two-thirds of Q4 cloud orders \u2014 the highest disclosed AI attach rate of any vendor in this app",
            "Free cash flow nearly doubled to \u20ac8.24B, funding the agentic buildout from operations",
            "Deep ERP data access is a defensible moat that general-purpose model providers cannot replicate",
        ],
        "sentiment_bear": [
            "The share price fell sharply on Q4 earnings day \u2014 in some markets the largest single-day drop since 2020 \u2014 on near-term cloud backlog dynamics",
            "Current cloud backlog growth decelerated through mid-2025, from 29% to 22%, which Klein attributed to tariff-driven uncertainty",
            "Redirecting the development backlog from features to agents risks disappointing customers on conventional roadmap commitments",
            "Outcome-based pricing is easy to announce and hard to operationalise, particularly across a partner-delivered implementation channel",
            "Headcount is not disclosed in the results reviewed, limiting any read on delivery capacity",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 headcount was not disclosed in the results "
                              "reviewed and no employer-review data was gathered. One adjacent signal worth "
                              "noting: SAP has publicly discussed AI replacing parts of its own coding "
                              "work, which customers should read as a statement about where delivery "
                              "economics are heading.",
        "glassdoor": None,
        "kpis": [
            ("1972", "Founded"),
            ("\u20ac9.7B", "Q4 2025 revenue"),
            ("\u20ac77B", "Total cloud backlog"),
            ("2/3", "Cloud orders with AI"),
            ("\u20ac8.24B", "Free cash flow"),
        ],
    },

    # =================================================================
    {
        "slug": "servicenow",
        "name": "ServiceNow",
        "website": "https://www.servicenow.com",
        "linkedin": "https://www.linkedin.com/company/servicenow",
        "group": "Enterprise software",
        "category": "Workflow platform &amp; AI control tower",
        "tagline": "The fastest-growing major enterprise software company \u2014 positioning itself as the "
                   "control layer over everyone else's AI",
        "founded": "2004",
        "hq": "Santa Clara, California",
        "employees": "Growing through acquisition; McDermott has pledged to end 2026 with the same headcount "
                     "as before the Moveworks, Armis and Veza deals, while margins scale",
        "ownership": "Public (NYSE: NOW)",
        "revenue": "Q2 2026 subscription revenue of $3.877B, up 24.5% (23% constant currency). FY2026 "
                   "subscription guidance raised to $15.755\u201315.770B, around 21% constant-currency "
                   "growth, at a 31.5% operating margin and 35% free cash flow margin. Total RPO near $29B",
        "revenue_short": "$15.8B (FY26 guide)",
        "offering": "The Now Platform for IT, employee, customer and creator workflows, extended into CRM "
                    "and CPQ. The AI layer is Now Assist and AI Control Tower, with EmployeeWorks as the "
                    "unified AI front door. Recent acquisitions add conversational AI and enterprise search "
                    "(Moveworks), data cataloguing (data.world) and security (Armis, Veza).",
        "digital_twin": "No",
        "genai": "Yes (Now Assist, AI Control Tower)",
        "buyer": "CIO, IT service management and increasingly CISO and HR leadership",
        "customers": ["ExxonMobil", "Standard Chartered", "Merck &amp; Co.", "State of California",
                      "US Department of the Air Force"],
        "people": [
            {"name": "Bill McDermott", "title": "Chairman &amp; Chief Executive Officer"},
            {"name": "Gina Mastantuono", "title": "President &amp; Chief Financial Officer"},
            {"name": "Amit Zavery", "title": "President, Chief Product Officer &amp; Chief Operating Officer"},
            {"name": "Pat Casey", "title": "Chief Technology Officer &amp; EVP of DevOps"},
        ],
        "description": "Growing subscription revenue at 24.5% at a scale approaching $16B, with AI annual "
                       "contract value passing $1B and accelerating more than 40% quarter over quarter. "
                       "Agentic deployments of ServiceNow AI increased ninefold in nine months, and more "
                       "than 100 billion workflows run on the platform each year.",
        "position_note": "The AI Control Tower positioning is the thing to understand. ServiceNow is not "
                         "trying to be the best model or the best agent \u2014 it is trying to be the "
                         "governance and orchestration layer that sits above everyone else's agents, "
                         "unifying legacy systems, departmental tools, cloud applications and AI agents "
                         "into one pane of glass. For a portfolio with fragmented estates across many "
                         "PortCos, that is a more relevant proposition than another model provider, and it "
                         "maps directly to the Technology / Governance / Security prerequisite in the "
                         "reference model. The Veza and Armis acquisitions extend that into identity and "
                         "asset security \u2014 who and what can access which data, including AI agents "
                         "\u2014 which is the control problem most AI programmes hit second.",
        "gip_connection": "No publicly disclosed GIP relationship. ServiceNow is a plausible portfolio-level "
                          "play precisely because it is estate-agnostic \u2014 it governs what is already "
                          "there rather than requiring replacement. Note Cognizant holds ServiceNow Global "
                          "Elite partner status if implementation capacity comes up.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of NOW only.",
        "use_cases": [
            {
                "sector": "Agentic AI adoption",
                "status": "Deployed",
                "deployment": "Now Assist and AI Control Tower deployed into governed workflows, with "
                              "customers moving from pilots to embedded agents.",
                "impact": "AI annual contract value passed $1B in Q2 2026, accelerating more than 40% "
                          "quarter over quarter; agentic deployments up ninefold in nine months; Now Assist "
                          "customers spending over $1M ACV grew more than 130% year over year",
                "source": "https://finance.biggo.com/news/US_NOW_2026-07-22",
            },
            {
                "sector": "Security &amp; identity",
                "status": "Announced",
                "deployment": "Acquisitions of Armis and Veza to strengthen asset and identity security "
                              "\u2014 managing visibility and access across people, applications, data, "
                              "cloud environments and AI agents as organisations adopt autonomous workflows.",
                "impact": "Cybersecurity is now ServiceNow's fastest-growing line and, per McDermott, "
                          "growing faster than any other top-ten cyber firm",
                "source": "https://www.sec.gov/Archives/edgar/data/1373715/000137371526000005/erq4fy25.htm",
            },
            {
                "sector": "Platform integration",
                "status": "Deployed",
                "deployment": "Moveworks' conversational AI and enterprise search integrated with Employee "
                              "Center Pro in under three weeks and launched as EmployeeWorks, a unified AI "
                              "front door, in February 2026.",
                "impact": "Demonstrates acquisition-to-product velocity; Moveworks closed 15 December 2025 "
                          "and contributed roughly 100 basis points to FY2026 subscription guidance",
                "source": "https://finance.yahoo.com/quote/1NOW.MI/earnings/1NOW.MI-Q1-2026-earnings_call-547931.html",
            },
            {
                "sector": "Enterprise scale",
                "status": "Deployed",
                "deployment": "Large-enterprise deal expansion across technology, CRM and creator "
                              "workflows, with named customers including ExxonMobil, Standard Chartered, "
                              "Merck, the State of California and the US Department of the Air Force.",
                "impact": "630 customers spending over $5M annually, up roughly 22%; 123 deals worth more "
                          "than $1M in net new ACV in Q2 2026; over 100 billion workflows run annually",
                "source": "https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx",
            },
        ],
        "customer_sentiment": "Customer expansion is unusually strong \u2014 630 accounts above $5M a year, "
                              "up 22%, and large deal counts rising sharply. McDermott reports operating to "
                              "a Rule of 56 on the way to 60, which is exceptional at this revenue scale. "
                              "Investor sentiment is disconnected from that: the stock fell as much as 14% "
                              "after Q1 2026 despite beating guidance across almost every metric and raising "
                              "AI forecasts by 50%, which says more about market anxiety over seat-based "
                              "software than about ServiceNow's execution.",
        "sentiment_bull": [
            "Fastest-growing major enterprise software company at this scale \u2014 24.5% subscription growth approaching $16B",
            "AI ACV passed $1B and is accelerating more than 40% quarter over quarter; McDermott expects roughly $1.5B for 2026 against a $1B target",
            "AI Control Tower positioning governs other vendors' agents rather than competing with them \u2014 estate-agnostic and therefore portfolio-friendly",
            "Rule of 56 profile with a 31.5% operating margin and 35% free cash flow margin",
        ],
        "sentiment_bear": [
            "The stock fell as much as 14% after Q1 2026 despite beating on nearly every metric \u2014 the market is discounting SaaS regardless of results",
            "Three acquisitions in quick succession (Moveworks, Armis, Veza) carry integration risk and near-term margin headwinds",
            "Growth includes meaningful inorganic contribution \u2014 roughly 125 basis points from Armis and 100 from Moveworks in FY2026 guidance",
            "Sales headcount rose sharply, which sits awkwardly with an agentic productivity narrative",
            "Q1 2026 included a roughly 75 basis point headwind from delayed large on-premise deals in the Middle East \u2014 geopolitical exposure is real",
        ],
        "employee_sentiment": "The strongest external recognition of any vendor in this app: ServiceNow "
                              "earned a place on Glassdoor's 2026 Best Places to Work list, TIME's "
                              "inaugural America's Growth Leaders 2026 list, and Fortune's World's Best "
                              "Workplaces 2025. McDermott has committed to ending 2026 with the same "
                              "headcount as before the three acquisitions while margins scale, which "
                              "implies consolidation ahead.",
        "glassdoor": None,
        "kpis": [
            ("2004", "Founded"),
            ("$15.8B", "FY2026 subscription"),
            ("+24.5%", "Q2 growth"),
            ("$1B+", "AI annual contract value"),
            ("100B", "Workflows per year"),
        ],
    },

    # =================================================================
    {
        "slug": "snowflake",
        "name": "Snowflake",
        "website": "https://www.snowflake.com",
        "linkedin": "https://www.linkedin.com/company/snowflake-computing",
        "group": "Data platform",
        "category": "AI data cloud",
        "tagline": "Betting that the winner is whoever provides the single source of enterprise truth, not "
                   "whoever has the best model",
        "founded": "2012",
        "hq": "Menlo Park, California",
        "employees": "Not disclosed in the results reviewed in this pass",
        "ownership": "Public (NYSE: SNOW)",
        "revenue": "Q4 FY2026 product revenue of $1.23B, up 30%, with total quarterly revenue of $1.28B. "
                   "Remaining performance obligations of $9.77B, up 42%; net revenue retention of 125%. "
                   "FY2027 product revenue guided to approximately $5.7B, up 27%; Q1 FY2027 product revenue "
                   "reached $1.33B, up 34% \u2014 the strongest sequential dollar growth in company history",
        "revenue_short": "$1.23B/qtr (Q4 FY26)",
        "offering": "The AI Data Cloud \u2014 cross-cloud data warehousing, sharing and governance \u2014 "
                    "with Cortex AI, Cortex Code (a coding agent), and Snowflake Intelligence (an enterprise "
                    "agentic application) on top. Observe adds observability; TensorStax strengthens "
                    "AI-driven data engineering.",
        "digital_twin": "No",
        "genai": "Yes (Cortex, Snowflake Intelligence)",
        "buyer": "Chief Data Officer, data engineering and analytics leadership",
        "customers": [],
        "people": [
            {"name": "Sridhar Ramaswamy", "title": "Chief Executive Officer"},
        ],
        "description": "Product revenue accelerated from 26% growth in Q1 FY2026 to 34% by Q1 FY2027, with "
                       "RPO up 42% to $9.77B and net revenue retention at 125%. Snowflake Intelligence "
                       "reached over 2,500 accounts within three months of launch \u2014 the fastest "
                       "adoption ramp in the company's history.",
        "position_note": "Ramaswamy's thesis is worth quoting in substance because it is the clearest "
                         "articulation of the data-layer argument: no AI model helps if there are four "
                         "sources of enterprise truth, and there are at least three or four credible model "
                         "providers, all of which Snowflake works with. The differentiation is packaging "
                         "governance, auditability and access control into something usable. That maps "
                         "almost exactly to the Data Foundation prerequisite in the reference model, and it "
                         "is the reason Snowflake and Databricks are the two vendors in this app whose "
                         "relevance is about readiness rather than application. One practical detail worth "
                         "raising in any negotiation: Snowflake has built account-level and agent-level "
                         "cost limits, because consumption-based AI spend is hard to control \u2014 that is "
                         "a governance feature a multi-PortCo programme will need.",
        "gip_connection": "No publicly disclosed GIP relationship. Relevance sits in the Data Foundation "
                          "and Workflows prerequisite \u2014 whether a PortCo has a governed single source "
                          "of truth before any AI programme starts. Consumption pricing means cost "
                          "governance should be designed in from the outset rather than retrofitted.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of SNOW only.",
        "use_cases": [
            {
                "sector": "Agentic analytics",
                "status": "Deployed",
                "deployment": "Snowflake Intelligence, an enterprise agentic application that lets business "
                              "users rather than only technical teams interrogate governed data, alongside "
                              "Cortex Code for AI-assisted data engineering.",
                "impact": "Over 2,500 accounts within three months \u2014 the fastest adoption ramp in "
                          "company history, more than doubling quarter over quarter; Cortex Code in use "
                          "across more than 7,100 accounts; over 9,100 accounts using Snowflake AI capabilities",
                "source": "https://futurumgroup.com/insights/snowflake-q4-fy-2026-results-highlight-ai-led-consumption-and-platform-expansion/",
            },
            {
                "sector": "Platform expansion",
                "status": "Announced",
                "deployment": "Acquisition of Observe, taking Snowflake into the IT operations market by "
                              "integrating observability with data and AI workloads, plus TensorStax to "
                              "strengthen AI-driven data engineering inside Cortex Code.",
                "impact": "Observe opens a market Snowflake sizes at over $50B; 430+ new product "
                          "capabilities delivered across FY2026",
                "source": "https://www.snowflake.com/en/news/press-releases/snowflake-reports-financial-results-for-the-fourth-quarter-and-full-year-of-fiscal-2026/",
            },
            {
                "sector": "Infrastructure economics",
                "status": "Announced",
                "deployment": "A five-year, $6B agreement with AWS \u2014 more than doubling prior "
                              "commitments \u2014 covering Graviton chips, reducing bandwidth costs and "
                              "supporting AI workload scaling, alongside deepened partnerships with OpenAI "
                              "and SAP.",
                "impact": "Secures capacity and cost structure for consumption growth without tying "
                          "Snowflake to a single model provider",
                "source": "https://www.sec.gov/Archives/edgar/data/1640147/000164014726000027/fy2027q1earnings.htm",
            },
            {
                "sector": "Customer economics",
                "status": "Deployed",
                "deployment": "Consumption-based pricing across the platform, with account-level and "
                              "agent-level cost limits introduced as AI adoption scales.",
                "impact": "Net revenue retention of 125%; 733 customers with trailing twelve-month product "
                          "revenue above $1M, up 27%; 740 net new customers added, up 40%; over 11,000 "
                          "customers in total",
                "source": "https://www.businesswire.com/news/home/20260225938648/en/Snowflake",
            },
        ],
        "customer_sentiment": "Net revenue retention of 125% and 740 net new customer additions, up 40%, "
                              "point to both expansion and acquisition working at once \u2014 an unusual "
                              "combination. Snowflake Intelligence's ramp to 2,500 accounts in three months "
                              "suggests the agentic layer is being adopted rather than merely purchased. "
                              "The market has been less kind: the stock was down roughly 20% year to date "
                              "in early 2026 before a 36% surge on Q1 FY2027 results, which is a fair "
                              "summary of how volatile sentiment is toward consumption-model software.",
        "sentiment_bull": [
            "Product revenue growth accelerated from 26% to 34% across five quarters, with the strongest sequential dollar growth in company history",
            "RPO up 42% to $9.77B and net revenue retention at 125% \u2014 both expansion and new-logo growth working",
            "Snowflake Intelligence hit 2,500 accounts in three months, the fastest ramp the company has recorded",
            "Genuinely model-agnostic, working with every major provider, with governance and auditability as the product rather than the model",
        ],
        "sentiment_bear": [
            "Consumption pricing makes revenue inherently more volatile than subscription models, in both directions",
            "Competing directly with Databricks, which is growing faster at over 80% and is larger by run rate",
            "Non-GAAP operating margin of only 10.5% in FY2026, expanding to a guided 12.5% \u2014 thin against subscription peers",
            "The $6B AWS commitment is a substantial fixed obligation for a company whose revenue flexes with customer usage",
            "The stock fell roughly 20% year to date in early 2026 before recovering, reflecting real uncertainty about the model",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 headcount was not disclosed in the results "
                              "reviewed and no employer-review data was gathered. Ramaswamy took over in "
                              "early 2024 and FY2026 was his first full fiscal year; the 430+ new "
                              "capabilities delivered suggest a high-velocity engineering culture but that "
                              "is an inference from output, not sentiment data.",
        "glassdoor": None,
        "kpis": [
            ("2012", "Founded"),
            ("$1.23B", "Q4 product revenue"),
            ("+30%", "Growth"),
            ("$9.77B", "RPO"),
            ("125%", "Net revenue retention"),
        ],
    },
]
