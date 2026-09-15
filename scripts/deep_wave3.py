# -*- coding: utf-8 -*-
"""
deep_wave3.py — Research wave 3, completed 15 September 2026.

Capgemini, Cognizant, CrowdStrike, Databricks, Deloitte.
"""

VENDORS = [
    # =================================================================
    {
        "slug": "capgemini",
        "name": "Capgemini",
        "website": "https://www.capgemini.com",
        "linkedin": "https://www.linkedin.com/company/capgemini",
        "group": "SI / Consulting",
        "category": "Consulting, technology &amp; engineering services",
        "tagline": "European systems integrator with a genuine engineering arm, betting heavily on "
                   "offshore scale and an AI-driven operating model",
        "founded": "1 October 1967 (founded by Serge Kampf)",
        "hq": "Paris, France",
        "employees": "423,400 at end-2025, up 24% year over year; offshore is now 66% of the total at 279,200",
        "ownership": "Public (Euronext Paris: CAP; CAC 40 constituent)",
        "revenue": "\u20ac22.465B in 2025, up 1.7% reported and 3.4% at constant currency, ahead of guidance; "
                   "Q4 accelerated sharply to 10.6% constant currency. Operating margin held at 13.3%; net "
                   "profit attributable to shareholders fell 4.2% to \u20ac1.6B",
        "revenue_short": "\u20ac22.5B (2025)",
        "offering": "Strategy, technology and engineering services plus digital business process operations. "
                    "Distinct brands sit underneath: Capgemini Engineering (industrial and product "
                    "engineering), Sogeti, frog, Cambridge Consultants and Synapse Product Development. WNS, "
                    "acquired in 2025, added intelligent operations at scale.",
        "digital_twin": "Via Capgemini Engineering",
        "genai": "Yes (&gt;10% of Q4 bookings)",
        "buyer": "CIO, COO and engineering leadership at large enterprises",
        "customers": [],
        "people": [
            {"name": "Aiman Ezzat", "title": "Chief Executive Officer"},
            {"name": "Nive Bhagat", "title": "Chief Financial Officer"},
            {"name": "Paul Hermelin", "title": "Chairman of the Board"},
        ],
        "description": "The largest European-headquartered integrator, and the one in this set with the most "
                       "credible physical-engineering capability through Capgemini Engineering. 2025 was a "
                       "year of aggressive reshaping: \u20ac3.8B deployed on acquisitions, headcount up 24%, "
                       "and a \u20ac700M restructuring programme announced to reorganise the workforce around AI.",
        "position_note": "Capgemini is the integrator whose structure most closely matches infrastructure "
                         "work \u2014 Capgemini Engineering does product and industrial engineering, not just "
                         "IT, which is a different proposition from the India-heritage firms and from the "
                         "Big Four. The 2025 numbers need reading carefully though: reported growth was "
                         "1.7% and the 10.6% Q4 acceleration came substantially from newly acquired units "
                         "(WNS, Cloud4C) rather than the existing business. Net debt more than doubled to "
                         "\u20ac5.3B funding those deals. This is a firm buying its way into intelligent "
                         "operations while restructuring the base \u2014 capable, but mid-transition.",
        "gip_connection": "No publicly disclosed GIP relationship. Capgemini Engineering is the part worth "
                          "testing for infrastructure assets \u2014 it addresses physical product and systems "
                          "engineering rather than corporate IT, which maps to the Asset Optimization area of "
                          "the reference model rather than Corporate Functions.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard institutional holdings only.",
        "use_cases": [
            {
                "sector": "Firm-wide AI",
                "status": "Deployed",
                "deployment": "AI integrated across the service portfolio and into delivery itself, with the "
                              "partner ecosystem used to shorten time to value. Ezzat has framed the strategy "
                              "as pivoting the group to be the catalyst for enterprise-wide AI adoption.",
                "impact": "Generative and agentic AI accounted for over 10% of Group bookings in Q4 2025",
                "source": "https://www.capgemini.com/news/press-releases/full-year-2025-results/",
            },
            {
                "sector": "Intelligent operations",
                "status": "Deployed",
                "deployment": "Acquisition of WNS (approximately $3.3B) to build digital business process "
                              "services, alongside Cloud4C. Ezzat stated demand was rising before the "
                              "acquisition, which is what prompted it.",
                "impact": "\u20ac3.8B deployed on acquisitions in 2025; Q4 constant-currency growth of 10.6% "
                          "with a significant contribution from the acquired units",
                "source": "https://finance.biggo.com/news/cpTbVZwB5f-9gHaOGXgS",
            },
            {
                "sector": "Workforce restructuring",
                "status": "Announced",
                "deployment": "A \u20ac700M restructuring plan to adapt the workforce to AI-driven delivery, "
                              "running alongside a 24% headcount increase driven by the WNS integration.",
                "impact": "Offshore workforce grew 42% to 279,200 \u2014 now 66% of the total",
                "source": "https://finance.biggo.com/news/cpTbVZwB5f-9gHaOGXgS",
            },
            {
                "sector": "Regional performance",
                "status": "Deployed",
                "deployment": "Growth is concentrated geographically: North America (29% of revenue) grew "
                              "7.3% at a 16.9% margin and UK &amp; Ireland (13%) grew 10.5% at 18.0%, while "
                              "France (19%) declined 4.1% and the rest of Europe (30%) was broadly flat.",
                "impact": "Asia-Pacific and Latin America grew fastest at 13.8%, from a 9% revenue base",
                "source": "https://businesssuccesselites.com/finance/capgemini-fy2025-results-ai-growth-2026/",
            },
        ],
        "customer_sentiment": "The demand signal management points to is a greater number of large "
                              "transformational deals, with cloud, data &amp; AI and digital business process "
                              "services driving it. Capgemini publishes few attributable client outcomes, so "
                              "there is limited independent evidence to weigh; the regional split is the "
                              "clearer read, and it says North American and UK clients are buying while the "
                              "French home market is contracting.",
        "sentiment_bull": [
            "Capgemini Engineering gives it genuine physical and industrial engineering capability, which most integrators in this set lack",
            "Generative and agentic AI already above 10% of Q4 bookings",
            "Exceeded its own revenue guidance in a difficult macro environment, and held operating margin at 13.3%",
            "North America is now the growth engine at 29% of revenue and a 16.9% margin",
        ],
        "sentiment_bear": [
            "Reported growth was only 1.7%; the headline Q4 acceleration leaned substantially on acquisitions rather than the existing base",
            "Net debt more than doubled to \u20ac5.3B after \u20ac3.8B of acquisition spend",
            "Net profit fell 4.2% despite revenue growth",
            "A \u20ac700M restructuring programme concurrent with a 24% headcount rise signals a workforce being rebuilt, not simply expanded",
            "France, still 19% of revenue, declined 4.1% at a 10.9% margin \u2014 the weakest major region",
        ],
        "employee_sentiment": "The structural signals are mixed and worth weighing over any sentiment score: "
                              "headcount rose 24%, almost entirely through the WNS integration, while a "
                              "\u20ac700M restructuring programme reshapes the existing workforce around AI "
                              "delivery. Offshore is now two thirds of the firm. No independent "
                              "employer-review data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1967", "Founded"),
            ("423,400", "Employees"),
            ("\u20ac22.5B", "2025 revenue"),
            ("13.3%", "Operating margin"),
            ("&gt;10%", "Q4 bookings from AI"),
        ],
    },

    # =================================================================
    {
        "slug": "cognizant",
        "name": "Cognizant",
        "website": "https://www.cognizant.com",
        "linkedin": "https://www.linkedin.com/company/cognizant",
        "group": "SI / Consulting",
        "category": "IT services &amp; digital operations",
        "tagline": "Back in growth after a difficult stretch, with an explicit AI builder strategy and a "
                   "new engineering arm from the Belcan acquisition",
        "founded": "1994",
        "hq": "Teaneck, New Jersey",
        "employees": "351,600 at 31 December 2025, up 14,800 year over year; voluntary attrition in tech "
                     "services improved to 13.9% from 15.9%",
        "ownership": "Public (Nasdaq: CTSH)",
        "revenue": "$21.108B in 2025, up 7.0% reported and 6.4% at constant currency, from $19.736B in 2024. "
                   "Full-year operating margin of 16.1%, up 140 basis points. 2026 guidance of 4.0\u20136.5% "
                   "constant-currency growth",
        "revenue_short": "$21.1B (2025)",
        "offering": "Application services, digital engineering, cloud and infrastructure, and business "
                    "process services. The Belcan acquisition added engineering, research and development "
                    "capability aimed at a $190B market; Thirdera made it one of ServiceNow's largest "
                    "partners with Global Elite status.",
        "digital_twin": "Via Belcan engineering",
        "genai": "Yes (AI builder strategy)",
        "buyer": "CIO and business unit leadership; heavy in financial services, health sciences and products &amp; resources",
        "customers": [],
        "people": [
            {"name": "Ravi Kumar S", "title": "Chief Executive Officer"},
            {"name": "Jatin Dalal", "title": "Chief Financial Officer"},
        ],
        "description": "Returned to what it calls the industry's winner's circle two years ahead of the "
                       "target set at its Investor Day, on 7% revenue growth and 140 basis points of margin "
                       "expansion. 28 large deals were signed in 2025 with total contract value up nearly "
                       "50% year over year.",
        "position_note": "Cognizant's turnaround is real but it competes on the same ground as TCS, Infosys "
                         "and Wipro, and its scale sits below Accenture and Capgemini. The two things that "
                         "differentiate it for an infrastructure portfolio are Belcan, which brings genuine "
                         "engineering R&amp;D rather than IT services, and its ServiceNow position \u2014 "
                         "Global Elite partner status matters if a PortCo's workflow layer is ServiceNow. "
                         "Book-to-bill of roughly 1.3x on $28.4B of trailing bookings is the healthiest "
                         "forward signal in its peer group.",
        "gip_connection": "No publicly disclosed GIP relationship. Most plausible route in is a PortCo's "
                          "existing application or infrastructure managed-services contract; Belcan is the "
                          "part worth testing for asset-level engineering work.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of CTSH only.",
        "use_cases": [
            {
                "sector": "Commercial performance",
                "status": "Deployed",
                "deployment": "The AI builder strategy put into motion across 2025, with investment in "
                              "talent, partnership ecosystem and AI platforms to help clients scale AI "
                              "across the enterprise.",
                "impact": "28 large deals signed in 2025 with large-deal TCV up nearly 50% year over year; "
                          "Q4 included twelve deals above $100M, two of them above $500M",
                "source": "https://news.cognizant.com/2026-02-04-Cognizant-Reports-Fourth-Quarter-and-Full-Year-2025-Results",
            },
            {
                "sector": "Bookings &amp; pipeline",
                "status": "Deployed",
                "deployment": "Trailing twelve-month bookings tracked as the forward indicator of the "
                              "turnaround, with Q4 bookings accelerating.",
                "impact": "$28.4B trailing bookings, up 5%, at a book-to-bill of approximately 1.3x; Q4 "
                          "bookings up 9% year over year",
                "source": "https://investors.cognizant.com/news-and-events/news/news-details/2026/Cognizant-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx",
            },
            {
                "sector": "Engineering R&amp;D",
                "status": "Deployed",
                "deployment": "Acquisition of Belcan, which significantly strengthened capability in the "
                              "engineering, research and development market, alongside Thirdera, which took "
                              "Cognizant to ServiceNow Global Elite partner status in early 2025.",
                "impact": "Addresses a market Cognizant sizes at $190B",
                "source": "https://www.sec.gov/Archives/edgar/data/1058290/000135994825000472/ctsh_courtesy-pdf.pdf",
            },
            {
                "sector": "Margin &amp; capital return",
                "status": "Deployed",
                "deployment": "Margin expansion delivered alongside growth, with capital returned through "
                              "buybacks and dividends.",
                "impact": "Operating margin 16.1%, up 140bps; 11% adjusted EPS growth; $2B returned to "
                          "shareholders in 2025, including 17.4 million shares repurchased for $1.3B",
                "source": "https://www.prnewswire.com/news-releases/cognizant-reports-fourth-quarter-and-full-year-2025-results-302678354.html",
            },
        ],
        "customer_sentiment": "Deal metrics are the strongest available proxy and they point the right way: "
                              "large-deal total contract value up nearly 50%, two mega deals above $500M in "
                              "Q4, and book-to-bill at roughly 1.3x. Cognizant publishes almost no "
                              "attributable client outcomes, so the read rests on commercial signals rather "
                              "than evidenced delivery.",
        "sentiment_bull": [
            "Growth restored to 7% with 140 basis points of margin expansion \u2014 both moving the right way at once",
            "Book-to-bill of approximately 1.3x on $28.4B of trailing bookings is a healthy forward indicator",
            "Belcan brings engineering R&amp;D capability rather than more IT services headcount",
            "Attrition improved to 13.9% from 15.9%, which matters for delivery continuity",
        ],
        "sentiment_bear": [
            "2026 guidance of 4.0\u20136.5% constant currency implies deceleration from 2025's 6.4%",
            "Scale sits well below Accenture and Capgemini in a market where scale drives ecosystem access",
            "Highly exposed to the same offshore labour-arbitrage model that AI delivery is compressing",
            "Publishes essentially no attributable client outcomes, so capability claims rest on the firm's own framing",
            "Margin guidance for 2026 of 15.9\u201316.1% implies only 10\u201330 basis points of further expansion",
        ],
        "employee_sentiment": "Headcount grew by 14,800 to 351,600 and voluntary attrition in tech services "
                              "fell to 13.9% from 15.9% a year earlier \u2014 both point to a stabilising "
                              "workforce after a turbulent period. Disclosed pay ratios are steep: the CEO's "
                              "realised compensation was 76 times the median US employee and 237 times the "
                              "global median, reflecting the India-weighted workforce.",
        "glassdoor": None,
        "kpis": [
            ("1994", "Founded"),
            ("351,600", "Employees"),
            ("$21.1B", "2025 revenue"),
            ("$28.4B", "Trailing bookings"),
            ("1.3x", "Book-to-bill"),
        ],
    },

    # =================================================================
    {
        "slug": "crowdstrike",
        "name": "CrowdStrike",
        "website": "https://www.crowdstrike.com",
        "linkedin": "https://www.linkedin.com/company/crowdstrike",
        "group": "Cybersecurity",
        "category": "Cloud-native cybersecurity platform",
        "tagline": "The first pure-play cybersecurity software company past $5B of ARR, consolidating "
                   "security spend onto a single agentic platform",
        "founded": "2011",
        "hq": "Austin, Texas",
        "employees": "Not disclosed in the results reviewed in this pass",
        "ownership": "Public (Nasdaq: CRWD)",
        "revenue": "Ending ARR of $5.25B at FY2026 close (31 January 2026), up 24%, on a record $1.01B of "
                   "net new ARR \u2014 its first year above $1B. Q4 FY2026 revenue of $1.31B, up 23%, with "
                   "non-GAAP operating margin of roughly 25%, up 370 basis points",
        "revenue_short": "$5.25B ARR (FY26)",
        "offering": "The Falcon platform, sold as modules across endpoint, identity, cloud, exposure "
                    "management and next-generation SIEM, with Charlotte AI providing agentic detection and "
                    "response. Falcon Flex is the consumption-style licensing model driving consolidation "
                    "onto the platform.",
        "digital_twin": "No",
        "genai": "Yes (Charlotte AI, agentic SOC)",
        "buyer": "CISO and security operations leadership",
        "customers": ["EY US", "BT"],
        "people": [
            {"name": "George Kurtz", "title": "Founder &amp; Chief Executive Officer"},
            {"name": "Burt Podbere", "title": "Chief Financial Officer"},
        ],
        "description": "Reached $5.25B of ending ARR in FY2026 \u2014 the fastest and only pure-play "
                       "cybersecurity software company to do so \u2014 while expanding non-GAAP operating "
                       "margin by 370 basis points. Kurtz frames the market as consolidating onto Falcon as "
                       "the operating system of cybersecurity for the agentic AI era.",
        "position_note": "The platform consolidation thesis is doing the work here. Falcon Flex lets "
                         "customers commit spend and draw down across modules, and the module adoption "
                         "numbers show it landing \u2014 49% of customers on six or more modules, 24% on "
                         "eight or more. For a portfolio owner that is the relevant mechanic: it is a "
                         "vehicle for consolidating fragmented security spend across assets rather than a "
                         "point product. The counterweight is dependence: consolidating onto one vendor's "
                         "agent across critical infrastructure concentrates operational risk, and the 2024 "
                         "outage is the reason that sentence carries weight rather than being theoretical.",
        "gip_connection": "No publicly disclosed GIP relationship. Security tooling is one of the more "
                          "plausible areas for genuine portfolio-level leverage \u2014 consolidated "
                          "commercial terms across PortCos \u2014 and sits squarely in the Technology / "
                          "Governance / Security prerequisite of the reference model. Note that CrowdStrike "
                          "already sells through service providers, so PortCos may hold it indirectly.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of CRWD only.",
        "use_cases": [
            {
                "sector": "Platform consolidation",
                "status": "Deployed",
                "deployment": "Falcon Flex, a flexible subscription model that lets customers commit spend "
                              "and deploy across modules, positioned explicitly as the mechanism for "
                              "consolidating fragmented security tooling.",
                "impact": "$1.69B of ending ARR from Falcon Flex accounts at FY2026 close, up over 120% year "
                          "over year; module adoption at 49% (six or more), 34% (seven or more) and 24% "
                          "(eight or more)",
                "source": "https://www.businesswire.com/news/home/20260303140639/en/CrowdStrike-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Financial-Results",
            },
            {
                "sector": "Agentic security operations",
                "status": "Deployed",
                "deployment": "Charlotte AI Agentic Response and Agentic Workflows for the security "
                              "operations centre, extended through Charlotte AI AgentWorks built with NVIDIA "
                              "Nemotron models, NeMo Data Designer and NIM microservices, plus Falcon AI "
                              "Detection and Response and Charlotte Agentic SOAR.",
                "impact": "Positions always-on, continuously learning AI agents at the edge for security operations",
                "source": "https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-reports-third-quarter-fiscal-year-2026-financial",
            },
            {
                "sector": "Managed services",
                "status": "Deployed",
                "deployment": "EY US selected Falcon Next-Gen SIEM as the foundational platform powering its "
                              "global cybersecurity managed services; BT launched a business antivirus "
                              "detect-and-respond service powered by Falcon Go.",
                "impact": "Extends reach through service-provider channels rather than direct sales alone",
                "source": "https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-reports-third-quarter-fiscal-year-2026-financial",
            },
            {
                "sector": "Securing AI itself",
                "status": "Deployed",
                "deployment": "AI Model Scanning and detection of Shadow AI to cover cloud risk, plus "
                              "collaboration with AWS, Intel, Meta, NVIDIA and Salesforce on securing "
                              "enterprise AI, and runtime controls for agentic systems and browser-based workflows.",
                "impact": "Positions AI adoption itself as a demand driver, not only a delivery technology",
                "source": "https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-reports-first-quarter-fiscal-year-2026-financial/",
            },
        ],
        "customer_sentiment": "Retention is the number that matters in this category and it is strong \u2014 "
                              "97% gross retention with consistently strong net retention, which means "
                              "customers are staying and spending more. Module adoption rates rising across "
                              "every tier says the consolidation pitch is being accepted rather than "
                              "tolerated. The unavoidable context is the July 2024 update outage, which "
                              "grounded flights and halted hospitals; the FY2026 numbers indicate commercial "
                              "recovery, but procurement memories in critical infrastructure are long and "
                              "any PortCo conversation should expect it to come up.",
        "sentiment_bull": [
            "First pure-play cybersecurity software company to reach $5B of ending ARR, with a record $1.01B of net new ARR",
            "370 basis points of non-GAAP operating margin expansion to roughly 25% \u2014 growth and profitability improving together",
            "97% gross retention with module adoption climbing across every tier",
            "Falcon Flex ARR up over 120% to $1.69B, evidencing genuine consolidation rather than seat growth",
        ],
        "sentiment_bear": [
            "Q4 FY2026 revenue of $1.31B came in below the Wall Street consensus of roughly $1.4B despite 23% growth",
            "The July 2024 outage remains the reference point for single-vendor concentration risk in critical infrastructure",
            "Management's $10B ARR ambition implies sustained high growth against increasingly large comparatives",
            "Platform consolidation cuts both ways \u2014 deep dependence on one agent across operational technology is a board-level risk, not just a procurement one",
            "Competitive pressure from Microsoft bundling security into existing enterprise agreements",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 headcount was not disclosed in the results "
                              "reviewed and no reliable employer-review data was gathered. Treat as a gap.",
        "glassdoor": None,
        "kpis": [
            ("2011", "Founded"),
            ("$5.25B", "Ending ARR (FY26)"),
            ("$1.01B", "Net new ARR"),
            ("97%", "Gross retention"),
            ("~25%", "Non-GAAP op margin"),
        ],
    },

    # =================================================================
    {
        "slug": "databricks",
        "name": "Databricks",
        "website": "https://www.databricks.com",
        "linkedin": "https://www.linkedin.com/company/databricks",
        "group": "Data platform",
        "category": "Lakehouse data &amp; AI platform",
        "tagline": "The data platform that turned into an agent platform \u2014 $7B run rate, growing over "
                   "80%, and cash-flow positive while still private",
        "founded": "2013 (by seven UC Berkeley researchers, the original creators of Apache Spark)",
        "hq": "San Francisco, California",
        "employees": "~12,300 (third-party estimate; not company-disclosed)",
        "ownership": "Private. $190B post-money valuation after a $5B strategic round closed 13 August 2026, "
                     "led by Coatue with Blackstone, MGX, T. Rowe Price accounts and Sixth Street Growth "
                     "\u2014 up from $134B eight months earlier. No S-1 filed",
        "revenue": "$7B annualised run rate as of Q2 2026, growing more than 80% year over year, and "
                   "cash-flow positive. In February 2026 the run rate was $5.4B, up 65%, with more than "
                   "$1.4B of that from AI",
        "revenue_short": "$7B (run rate)",
        "offering": "The lakehouse platform combining data warehousing, engineering and ML, with Unity "
                    "Catalog for governance. The newer agent layer is Lakebase (a database built for AI "
                    "agents), Genie (a business-analysis agent), Agentbricks (embedding intelligence into "
                    "software) and Unity AI Gateway (controlling model use and cost).",
        "digital_twin": "No",
        "genai": "Yes (agent infrastructure)",
        "buyer": "Chief Data Officer, data engineering and platform leadership",
        "customers": [],
        "people": [
            {"name": "Ali Ghodsi", "title": "Co-Founder &amp; Chief Executive Officer"},
            {"name": "Matei Zaharia", "title": "Co-Founder &amp; Chief Technology Officer"},
        ],
        "description": "Grew from a $5.4B run rate in February 2026 to $7B by Q2, at over 80% growth, and "
                       "raised $5B at a $190B valuation in August 2026 despite being cash-flow positive. The "
                       "core data warehouse alone is $1.5B of run rate still growing at 100%.",
        "position_note": "Databricks' pitch to an infrastructure portfolio is neutrality and governance: it "
                         "positions itself as model-agnostic, letting customers run OpenAI, Anthropic, Google "
                         "or open-source models on their own data without that data leaving their secure "
                         "cloud environment. For assets with sensitive operational data and multiple "
                         "regulators, that architecture matters more than benchmark performance. Unity AI "
                         "Gateway is the piece worth understanding \u2014 it exists to control model usage "
                         "and cost, which is precisely the governance problem a multi-PortCo AI programme "
                         "runs into. The offsetting fact is that Databricks itself carries multibillion-dollar "
                         "commitments to all three hyperscalers, so its own cost base is exposed to the same "
                         "token economics it sells tooling to manage.",
        "gip_connection": "No publicly disclosed GIP relationship. Worth noting that Blackstone participated "
                          "in the August 2026 round \u2014 a peer infrastructure and private-markets investor "
                          "taking a position in the vendor, which is context for any commercial discussion.",
        "blackrock_connection": "No publicly disclosed operating relationship. Databricks is private; the "
                                "August 2026 round was led by Coatue with Blackstone, MGX, T. Rowe Price "
                                "accounts and Sixth Street participating.",
        "use_cases": [
            {
                "sector": "Core data platform",
                "status": "Deployed",
                "deployment": "The lakehouse data warehouse, the original product and still the largest "
                              "single line, used for analytics and as the governed foundation under AI workloads.",
                "impact": "$1.5B annualised run rate, still growing at approximately 100% year over year",
                "source": "https://techcrunch.com/2026/08/13/databricks-wanted-to-raise-1b-investors-wanted-15b-it-settled-on-5b-at-a-190b-valuation/",
            },
            {
                "sector": "Agent infrastructure",
                "status": "Deployed",
                "deployment": "Lakebase, a database purpose-built for AI agents, launched June 2025; Genie, "
                              "an agent performing business analysis on demand; and Agentbricks for embedding "
                              "intelligence into software.",
                "impact": "Lakebase surpassed a $100M revenue run rate within roughly a year of launch",
                "source": "https://www.cnbc.com/2026/08/13/databricks-funding-round-190-billion-valuation.html",
            },
            {
                "sector": "AI cost governance",
                "status": "Deployed",
                "deployment": "Unity AI Gateway, which controls which models are used and at what cost "
                              "\u2014 built for the token-cost pressure now affecting enterprise AI budgets. "
                              "Ghodsi reports customers increasingly adopting open-source and Chinese models "
                              "alongside frontier proprietary ones.",
                "impact": "Positioned as a direct response to rising AI token costs; a named use of the $5B raise",
                "source": "https://www.cnbc.com/2026/08/13/databricks-funding-round-190-billion-valuation.html",
            },
            {
                "sector": "Model partnerships",
                "status": "Deployed",
                "deployment": "Partnerships across all three hyperscalers (AWS, Google, Microsoft) plus "
                              "frontier labs \u2014 a $100M partnership with OpenAI and a five-year "
                              "partnership with Anthropic \u2014 supporting the model-agnostic positioning.",
                "impact": "Customers can run multiple model providers against governed data in place",
                "source": "https://tsginvest.com/databricks/",
            },
        ],
        "customer_sentiment": "Ghodsi's own summary of the demand environment is that demand is crazy and "
                              "that the world is focused on agents. The more telling detail is behavioural: "
                              "customers who a year or two ago insisted on frontier proprietary models are "
                              "now adopting open-source and Chinese models as token costs bite, which is "
                              "exactly the shift Databricks' gateway and open tooling are built to serve. "
                              "Databricks publishes few attributable customer metrics, so this rests largely "
                              "on management commentary.",
        "sentiment_bull": [
            "$7B run rate growing over 80% year over year, and cash-flow positive \u2014 an unusual combination at this scale",
            "The core data warehouse is $1.5B and still growing at ~100%, so the growth is not solely AI narrative",
            "Genuinely model-agnostic architecture keeps customer data inside the customer's own cloud environment",
            "Raised $5B at $190B in August 2026, a 42% valuation step-up in eight months, without needing the capital for operations",
        ],
        "sentiment_bear": [
            "Multibillion-dollar cloud commitments to all three hyperscalers create a fixed cost base regardless of demand",
            "Roughly $20B raised over 20 months for a business that describes itself as cash-flow positive \u2014 the board's stated motivation was concern about a possible AI slump",
            "No S-1 filed and Ghodsi has said 2026 is a terrible year to go public; a listing is unlikely before Anthropic or OpenAI",
            "Headcount and customer-count figures in circulation are third-party estimates, not disclosures",
            "Competing simultaneously with Snowflake, Oracle and the hyperscalers it depends on for infrastructure",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 Databricks does not disclose headcount and no "
                              "reliable employer-review data was gathered. The ~12,300 figure in circulation "
                              "is a third-party estimate. Treat as a gap.",
        "glassdoor": None,
        "kpis": [
            ("2013", "Founded"),
            ("$7B", "Run rate (Q2 2026)"),
            ("&gt;80%", "YoY growth"),
            ("$190B", "Valuation (Aug 2026)"),
            ("$1.5B", "Lakehouse run rate"),
        ],
        "notes": "Figures here move quickly and several widely-quoted ones \u2014 headcount, customer count "
                 "\u2014 are third-party estimates rather than company disclosures. Re-run this vendor before "
                 "using any number externally.",
    },

    # =================================================================
    {
        "slug": "deloitte",
        "name": "Deloitte",
        "website": "https://www.deloitte.com",
        "linkedin": "https://www.linkedin.com/company/deloitte",
        "group": "SI / Consulting",
        "category": "Big Four professional services network",
        "tagline": "The largest professional services firm in the world, and the first to cross $70B, "
                   "building agentic AI products rather than only advising on them",
        "founded": "1845",
        "hq": "London, United Kingdom (Deloitte Touche Tohmatsu Limited; a network of member firms)",
        "employees": "Over 470,000 professionals and partners, up from 460,000",
        "ownership": "Private network of member firms",
        "revenue": "$70.5B aggregate global revenue for FY2025 (year ended 31 May 2025), up 4.8% in local "
                   "currency and 4.9% in US dollars \u2014 the first professional services firm to cross "
                   "$70B. Growth was fastest in the Americas at 7.1% and Asia-Pacific at 4.9%",
        "revenue_short": "$70.5B (FY25)",
        "offering": "Audit and assurance, consulting, tax, legal, risk and financial advisory, and managed "
                    "services, delivered by member firms. The AI product line is Zora AI, built with NVIDIA "
                    "to create agentic digital co-workers, supported by a Global Agentic Network, "
                    "Silicon2Service, and the Trustworthy AI governance framework.",
        "digital_twin": "Client-specific builds",
        "genai": "Yes (Zora AI, agentic)",
        "buyer": "CEO, CFO, audit committee and transformation sponsors",
        "customers": ["International Olympic Committee"],
        "people": [
            {"name": "Joe Ucuzoglu", "title": "Global Chief Executive Officer"},
        ],
        "description": "The largest firm in this set by revenue and headcount, and the first professional "
                       "services firm ever to pass $70B. It has committed $3B through FY2030 to generative "
                       "and agentic AI, and is unusual among the Big Four in building a product business "
                       "(Zora AI) rather than only a services practice.",
        "position_note": "Deloitte's distinguishing move is the same one BCG made, at a different scale: "
                         "building rather than only advising. Zora AI is a product business, and the IOC "
                         "relationship is the most directly relevant proof point for infrastructure \u2014 "
                         "from Milano Cortina 2026 onwards Deloitte is Games Technology Integration Partner, "
                         "responsible for an integrated technology infrastructure and games platform across "
                         "the Olympic and Paralympic Games. That is large-scale, time-bound, "
                         "multi-stakeholder infrastructure technology integration, which is closer to a "
                         "PortCo's problem than most consulting case studies. The caveat is structural: "
                         "Deloitte is a network of member firms, so capability and quality vary by "
                         "geography, and the entity you contract with is not the entity that published the "
                         "global number.",
        "gip_connection": "No publicly disclosed GIP relationship. As the largest audit and advisory network, "
                          "an existing relationship at PortCo or fund level \u2014 audit, tax or transaction "
                          "services \u2014 is likely and would carry independence constraints on what "
                          "consulting work can then be done. Check that before scoping anything.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "Sport &amp; venue infrastructure",
                "status": "Deployed",
                "deployment": "Games Technology Integration Partner for the Olympic Games, Paralympic Games "
                              "and Youth Olympic Games from Milano Cortina 2026 onwards, advancing the IOC's "
                              "vision of an integrated technology infrastructure and games platform. "
                              "Deloitte also helped craft the Olympic AI Agenda.",
                "impact": "Expansion of the Worldwide Olympic Partnership announced during Paris 2024",
                "source": "https://www.deloitte.com/global/en/about/press-room/global-revenue-announcement.html",
            },
            {
                "sector": "AI products",
                "status": "Deployed",
                "deployment": "Zora AI, Deloitte's first AI product business, built with NVIDIA to create "
                              "agentic digital co-workers, alongside a Global Agentic Network connecting "
                              "Deloitte solutions with partners and clients, and Silicon2Service for running "
                              "AI safely in government and business.",
                "impact": "$3B committed through FY2030 to expand generative and agentic AI capability",
                "source": "https://thefinancestory.com/deloitte-hits-70-5bn-global-revenue-big-bet-on-autonomous-ai-co-workers",
            },
            {
                "sector": "Scale",
                "status": "Deployed",
                "deployment": "Aggregate global revenue across audit, consulting, tax, legal and managed "
                              "services, delivered through member firms in over 150 countries.",
                "impact": "$70.5B in FY2025 \u2014 first professional services firm to cross $70B \u2014 with "
                          "headcount rising to over 470,000",
                "source": "https://www.consulting.us/news/12469/deloitte-breaches-70-billion-in-annual-revenue",
            },
            {
                "sector": "Governance",
                "status": "Deployed",
                "deployment": "The Trustworthy AI framework, used to guide ethical AI deployment across "
                              "client engagements and Deloitte's own delivery.",
                "impact": "Provides a published governance reference that can be adapted rather than built from scratch",
                "source": "https://thefinancestory.com/deloitte-hits-70-5bn-global-revenue-big-bet-on-autonomous-ai-co-workers",
            },
        ],
        "customer_sentiment": "Scale and growth are the available evidence: 4.8% local-currency growth to "
                              "$70.5B, with the Americas up 7.1%. The geography tells a more nuanced story "
                              "\u2014 Deloitte UK recorded its first revenue decline in fifteen years, and "
                              "headcount grew overall despite job cuts at member firms including the US "
                              "federal government practice. As a private network Deloitte publishes no "
                              "client-level outcome metrics, so there is little to weigh beyond the "
                              "aggregate.",
        "sentiment_bull": [
            "Largest professional services firm in the world by revenue and headcount \u2014 first to cross $70B",
            "Building a product business (Zora AI, with NVIDIA) rather than only selling advisory hours",
            "$3B committed to generative and agentic AI through FY2030 \u2014 a genuine multi-year commitment, not a campaign",
            "The IOC Games technology integration mandate is directly relevant, large-scale infrastructure technology work",
        ],
        "sentiment_bear": [
            "Growth of 4.8% trails Accenture's 7% and Cognizant's 7% \u2014 scale is not translating into pace",
            "Deloitte UK posted its first revenue decline in fifteen years, and the US federal practice cut jobs",
            "The member-firm structure means the global figure describes a network, not a contracting entity; quality and capability vary by geography",
            "Audit independence rules can restrict consulting work where a Deloitte member firm already audits the client \u2014 a real constraint at PortCo level",
            "Discloses aggregate revenue only, with no segment, margin or AI revenue breakout to test the narrative against",
        ],
        "employee_sentiment": "Headcount rose to over 470,000 from 460,000, but that net figure conceals job "
                              "cuts at member firms around the world, including at Deloitte US's federal "
                              "government practice. No independent employer-review data was gathered in this "
                              "pass.",
        "glassdoor": None,
        "kpis": [
            ("1845", "Founded"),
            ("470,000+", "Professionals"),
            ("$70.5B", "FY2025 revenue"),
            ("4.8%", "Growth (local ccy)"),
            ("$3B", "AI commitment to 2030"),
        ],
    },
]
