# -*- coding: utf-8 -*-
"""
deep_wave8.py — Research wave 8 (final), completed 15 September 2026.

Syntax, TCS, Tribola Tech, UiPath, Wipro, Workday, xAI.
This wave completes deep research across all 49 tracked vendors.
"""

VENDORS = [
    # =================================================================
    {
        "slug": "syntax",
        "name": "Syntax",
        "website": "https://www.syntax.com",
        "linkedin": "https://www.linkedin.com/company/syntax",
        "group": "SI / Consulting",
        "category": "Managed cloud for mission-critical ERP",
        "tagline": "A specialist that runs SAP and Oracle estates for a living \u2014 and is now shipping "
                   "shop-floor AI",
        "founded": "1972",
        "hq": "Montr\u00e9al, Qu\u00e9bec, Canada",
        "employees": "Approximately 2,000\u20132,200 across six global locations",
        "ownership": "Private; roughly $300M of funding and seven acquisitions per third-party trackers",
        "revenue": "Not disclosed. Third-party estimates vary wildly \u2014 $231.8M, $418.7M, a "
                   "$100\u2013500M band and a $500M\u20131B band all appear across different trackers. "
                   "Treat all of them as unreliable and confirm directly",
        "revenue_short": "Not disclosed",
        "offering": "Managed cloud hosting and application managed services for SAP and Oracle estates "
                    "\u2014 including E-Business Suite, JD Edwards, PeopleSoft, Hyperion and Siebel "
                    "\u2014 across private, public, hybrid and multi-cloud, plus security services, "
                    "consulting and systems integration.",
        "digital_twin": "No",
        "genai": "Yes (AI-first managed services)",
        "buyer": "CIO and ERP application owners at mid-market and large manufacturers",
        "customers": [],
        "people": [
            {"name": "Christian Primeau", "title": "Global Chief Executive Officer"},
        ],
        "description": "A 50-year-old specialist that does one thing: run mission-critical SAP and Oracle "
                       "environments for over 1,000 customers, concentrated in manufacturing, automotive, "
                       "energy and mining. It holds SAP Gold Partner status, Oracle, AWS Advanced, "
                       "Microsoft Gold and IBM Silver partnerships.",
        "position_note": "Syntax is the most asset-adjacent of the smaller vendors in this app, and "
                         "ShiftBook is the reason. Released in May 2026 and purpose-built for SAP Digital "
                         "Manufacturing, it handles shift handovers, connects frontline teams and targets "
                         "shop-floor performance \u2014 which is operational technology territory, not "
                         "corporate IT. Its client base is already concentrated in manufacturing, "
                         "automotive, energy and mining. For a PortCo running SAP on the plant floor, that "
                         "combination is more relevant than a global integrator's generic capability. The "
                         "diligence caution is the same as with any private specialist: no disclosed "
                         "financials, and the third-party revenue estimates in circulation differ by a "
                         "factor of four.",
        "gip_connection": "No publicly disclosed GIP relationship. The plausible fit is at a single "
                          "asset-heavy PortCo running SAP or Oracle, particularly in manufacturing or "
                          "energy, rather than as a portfolio-level supplier.",
        "blackrock_connection": "None identified.",
        "use_cases": [
            {
                "sector": "Manufacturing \u2014 shop floor",
                "status": "Announced",
                "deployment": "ShiftBook, purpose-built for SAP Digital Manufacturing, streamlining shift "
                              "handovers and connecting frontline teams to drive shop-floor performance.",
                "impact": "Takes Syntax into operational technology rather than corporate IT \u2014 the "
                          "layer closest to asset performance",
                "source": "https://www.zoominfo.com/c/syntax-systems-ltd/37339220",
            },
            {
                "sector": "Application managed services",
                "status": "Announced",
                "deployment": "AI-First Application Managed Services for SAP solutions, launched April "
                              "2026, applying agentic AI to the ongoing operation of SAP estates rather "
                              "than to implementation projects.",
                "impact": "Repositions a traditional managed-services business around AI-driven operations",
                "source": "https://www.owler.com/company/syntax1",
            },
            {
                "sector": "Partner credentials",
                "status": "Deployed",
                "deployment": "Two decades of Gold status as a certified SAP Operations Partner, with new "
                              "certifications added in June 2026 for SAP Business AI operations and SAP "
                              "security operations.",
                "impact": "Specific accreditation for operating SAP Business AI \u2014 a narrower and more "
                          "verifiable credential than general AI capability claims",
                "source": "https://www.zoominfo.com/c/syntax-systems-ltd/37339220",
            },
            {
                "sector": "Delivery model",
                "status": "Deployed",
                "deployment": "A Boutique at Scale positioning \u2014 personalised, agile engagements "
                              "delivered with enterprise-scale capability across six global locations, "
                              "with an April 2026 construction-sector win combining industry knowledge with "
                              "agentic AI-driven SAP cloud transformation.",
                "impact": "Over 1,000 customers across manufacturing, automotive, energy, financial "
                          "services, healthcare, mining and media",
                "source": "https://vendordirectory.shrm.org/company/910001/syntax",
            },
        ],
        "customer_sentiment": "Little independent evidence is available. The strongest indirect signal is "
                              "longevity in a demanding niche \u2014 two decades of SAP Operations Partner "
                              "Gold status and over 1,000 customers running mission-critical estates, where "
                              "switching costs are high and poor service surfaces quickly. One third-party "
                              "tracker reports an 87/100 CEO approval rating, which is soft evidence at best.",
        "sentiment_bull": [
            "Deep, verifiable specialisation in running SAP and Oracle estates \u2014 including legacy platforms like JD Edwards and PeopleSoft that larger firms deprioritise",
            "ShiftBook is genuine operational-technology capability aimed at the shop floor, not repackaged corporate IT",
            "Specific SAP Business AI operations and security operations certifications rather than generic AI claims",
            "Client base already concentrated in manufacturing, automotive, energy and mining \u2014 the sectors closest to infrastructure assets",
        ],
        "sentiment_bear": [
            "No disclosed financials, and third-party revenue estimates differ by a factor of four \u2014 from $232M to over $500M",
            "At roughly 2,000 people, surge capacity and geographic coverage are limited",
            "Seven acquisitions and roughly $300M of funding imply a private-equity-style roll-up, which carries integration and ownership-horizon questions",
            "Publishes no attributable customer outcomes or metrics",
            "Tightly coupled to SAP and Oracle \u2014 valuable where those estates exist, irrelevant where they don't",
        ],
        "employee_sentiment": "Not covered in this pass. Headcount is reported at roughly 2,000\u20132,200 "
                              "across six locations, up from about 1,400 in 2021. No reliable "
                              "employer-review data was gathered.",
        "glassdoor": None,
        "kpis": [
            ("1972", "Founded"),
            ("~2,100", "Employees"),
            ("n/d", "Revenue"),
            ("1,000+", "Customers"),
            ("20 yrs", "SAP Gold Operations Partner"),
        ],
        "notes": "Revenue estimates for Syntax vary by more than four times across trackers and none are "
                 "company-disclosed. The page shows the range rather than picking one. Confirm directly in "
                 "any diligence.",
    },

    # =================================================================
    {
        "slug": "tcs",
        "name": "Tata Consultancy Services",
        "website": "https://www.tcs.com",
        "linkedin": "https://www.linkedin.com/company/tata-consultancy-services",
        "group": "SI / Consulting",
        "category": "IT services &amp; AI-led transformation",
        "tagline": "The largest India-heritage integrator, with the biggest disclosed AI revenue line in "
                   "its peer set \u2014 and 23,460 fewer people",
        "founded": "1968",
        "hq": "Mumbai, India (part of the Tata Group)",
        "employees": "Headcount fell by 23,460 during FY2026, including roughly 12,200 confirmed job cuts "
                     "concentrated in middle and senior management, from 607,979 associates at FY2025 close",
        "ownership": "Public (NSE/BSE: TCS); majority-owned by Tata Sons",
        "revenue": "Crossed $30B in annual revenue. Q4 FY2026 revenue of \u20b970,698 crore, up 9.6% year "
                   "over year, with three consecutive quarters of sequential growth and the best margins in "
                   "four years at a 19.8% net margin, up 80 basis points",
        "revenue_short": "$30B+ (FY26)",
        "offering": "Application services, consulting, engineering, cloud and business process services, "
                    "organised around a five-pillar strategy. AI runs through the WisdomNext platform, with "
                    "AI reported as a distinct revenue line, and TCS is building a dedicated AI "
                    "infrastructure business.",
        "digital_twin": "Via engineering services",
        "genai": "Yes (WisdomNext, disclosed AI line)",
        "buyer": "CIO and business leadership at the largest global enterprises",
        "customers": [],
        "people": [
            {"name": "K Krithivasan", "title": "Chief Executive Officer &amp; Managing Director"},
            {"name": "Aarthi Subramanian", "title": "Executive Director, President &amp; Chief Operating Officer"},
        ],
        "description": "The largest Indian IT services firm and, on the evidence here, the one converting "
                       "AI into revenue fastest: annualised AI revenue passed $1.8B in Q3 FY2026, $2.3B in "
                       "Q4 and $2.6B by Q1 FY2027, against a stated ambition to become the world's largest "
                       "AI-led technology services company.",
        "position_note": "TCS has the most concrete AI evidence base of any services firm in this app. "
                         "Krithivasan projects AI could reach 20% of total revenue; 54 of the top 60 global "
                         "clients are already running AI-embedded projects; and management reports 10\u201315% "
                         "productivity improvements on active AI projects. That last number is the useful "
                         "one for a portfolio programme, because it is a delivery metric rather than a "
                         "sales metric. The other side is stark and worth stating plainly: headcount fell "
                         "by 23,460 in the same year, concentrated in middle and senior management. The "
                         "productivity gains and the job losses are the same phenomenon, and any PortCo "
                         "negotiating an AI-led managed services contract should understand that the "
                         "vendor's own economics now assume fewer people per unit of delivery.",
        "gip_connection": "No publicly disclosed GIP relationship. TCS is the most likely incumbent at "
                          "large PortCos with existing offshore application or infrastructure contracts. "
                          "Its stated build of an AI infrastructure business is worth watching as a "
                          "potential digital-infrastructure adjacency.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "AI revenue line",
                "status": "Deployed",
                "deployment": "AI services reported as a distinct annualised revenue line, built on "
                              "investments across the full stack from infrastructure to intelligence.",
                "impact": "Annualised AI revenue passed $1.8B in Q3 FY2026, surpassed $2.3B in Q4, and "
                          "reached $2.6B by Q1 FY2027 \u2014 with Krithivasan projecting AI could reach 20% "
                          "of total revenue",
                "source": "https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q4-fy-2026",
            },
            {
                "sector": "Client adoption",
                "status": "Deployed",
                "deployment": "Generative AI frameworks embedded directly into client core operations "
                              "rather than run as peripheral experiments, altering the commercial structure "
                              "of outsourcing contracts.",
                "impact": "54 of the top 60 global clients executing AI-embedded projects, with 10\u201315% "
                          "productivity improvements reported across active AI deployments",
                "source": "https://streamlinefeed.co.ke/news/tcs-ceo-krithivasan-ai-revenue-26-billion",
            },
            {
                "sector": "Workforce capability",
                "status": "Deployed",
                "deployment": "Large-scale AI training through the WisdomNext platform, launched June 2024, "
                              "covering foundational and advanced AI and machine learning competencies.",
                "impact": "More than 217,000 employees trained in advanced AI competencies, with over half "
                          "a million trained on foundational AI and ML skills",
                "source": "https://hindustanherald.in/tcs-ai-revenue-job-cuts-india-fy26/",
            },
            {
                "sector": "Commercial momentum",
                "status": "Deployed",
                "deployment": "Large deal signings across Enterprise Transformation, Digital Engineering "
                              "and Cloud Modernization, broad-based across major markets and most industries.",
                "impact": "FY2026 total contract value of $40.7B \u2014 among the highest ever recorded "
                          "\u2014 with $12B in Q4 alone, three mega deals in Q4 and five across the year; "
                          "clients contributing over $100M annually rose to 66",
                "source": "https://www.sahi.com/blogs/tcs-q4-fy26-results-analysis",
            },
        ],
        "customer_sentiment": "Client behaviour contradicts the existential narrative that AI would collapse "
                              "IT outsourcing budgets. TCV of $40.7B, clients above $100M rising to 66, and "
                              "54 of the top 60 clients running AI-embedded work all point the same way: "
                              "budgets are being redirected toward AI implementation rather than cut. "
                              "Krithivasan's own framing is more measured \u2014 macro headwinds continue, "
                              "but customer conviction in technology investment is sustained.",
        "sentiment_bull": [
            "The largest disclosed AI revenue line of any services firm tracked here \u2014 $2.6B annualised and growing quarterly",
            "FY2026 TCV of $40.7B, among the highest in company history, with three consecutive quarters of sequential growth",
            "Best margins in four years at a 19.8% net margin, up 80 basis points",
            "54 of the top 60 global clients running AI-embedded projects \u2014 penetration, not pilots",
        ],
        "sentiment_bear": [
            "Headcount fell 23,460 in FY2026, including roughly 12,200 confirmed cuts concentrated in middle and senior management",
            "Growth is respectable rather than strong, and management has acknowledged high single-digit growth was difficult to achieve",
            "The 20% AI revenue projection is a CEO statement of direction, not guidance",
            "Heavy exposure to the same offshore labour-arbitrage model that its own productivity gains are compressing",
            "North America, the largest market, has been broadly flat to slightly negative across recent quarters",
        ],
        "employee_sentiment": "The FY2026 picture is contraction at the experienced end alongside mass "
                              "reskilling: headcount down 23,460, roughly 12,200 confirmed cuts focused on "
                              "middle and senior management, while more than 217,000 people were trained in "
                              "advanced AI and over half a million on foundational AI and ML. Attrition in "
                              "IT services stood at 13.3% at FY2025 close. No independent employer-review "
                              "data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1968", "Founded"),
            ("$30B+", "Annual revenue"),
            ("$2.6B", "AI revenue run rate"),
            ("$40.7B", "FY2026 TCV"),
            ("-23,460", "Headcount change"),
        ],
    },

    # =================================================================
    {
        "slug": "tribola-tech",
        "name": "Tribola Tech",
        "website": "https://www.tribolatech.com",
        "linkedin": "https://www.linkedin.com/company/tribolatech-inc",
        "group": "SI / Consulting",
        "category": "Enterprise AI, Salesforce &amp; data engineering",
        "tagline": "A small US-India delivery firm with three focused practices and almost no public record",
        "founded": "Operating roots from 2009; Infinite Tek Inc. established 2024",
        "hq": "San Ramon, California, with delivery in Bengaluru, Karnataka, India",
        "employees": "Not disclosed",
        "ownership": "Private",
        "revenue": "Not disclosed",
        "revenue_short": "Not disclosed",
        "offering": "Three specialist practices \u2014 Enterprise AI (AI agents, intelligent automation, "
                    "enterprise knowledge, document intelligence and governed production solutions), "
                    "Salesforce (Agentforce, Data Cloud, Service Cloud, Sales Cloud), and Data Engineering "
                    "\u2014 supported by Global Technology Delivery across the United States and India.",
        "digital_twin": "No",
        "genai": "Yes (Enterprise AI practice)",
        "buyer": "Customer operations and data leadership at mid-market enterprises",
        "customers": [],
        "people": [],
        "description": "The smallest vendor tracked in this app by a wide margin, and the least documented. "
                       "It positions around complex customer and operational workflows that do not fit "
                       "inside a single platform, with a stated approach of defining the business problem "
                       "before selecting technology.",
        "position_note": "Tribola's stated method \u2014 start with the workflow, the experience, the "
                         "information required and the outcome that needs to improve, then decide the "
                         "combination of AI, Salesforce, data and engineering \u2014 is the right sequence, "
                         "and it is the sequence most large integrators claim and fewer follow. At this "
                         "size that claim is at least plausible, because a small firm cannot afford to lead "
                         "with a platform it happens to resell. But there is very little here to assess. "
                         "No leadership is named publicly, no financials are disclosed, no headcount is "
                         "published, and no attributable client work appears anywhere in the material "
                         "reviewed. This should be treated as a referral-and-references decision, not a "
                         "research-led one.",
        "gip_connection": "No publicly disclosed GIP relationship. At this scale the only realistic fit is "
                          "a single scoped workstream at one PortCo \u2014 most plausibly Salesforce or "
                          "data engineering work \u2014 and it would need direct reference checking rather "
                          "than desk diligence.",
        "blackrock_connection": "None identified.",
        "use_cases": [
            {
                "sector": "Enterprise AI",
                "status": "Announced",
                "deployment": "AI agents, intelligent automation, enterprise knowledge, document "
                              "intelligence and governed production solutions applied to real enterprise "
                              "work rather than pilots.",
                "impact": "No client outcomes or metrics are published",
                "source": "https://www.tribolatech.com/",
            },
            {
                "sector": "Salesforce",
                "status": "Announced",
                "deployment": "Customer operations transformation using Salesforce, Agentforce, Data Cloud, "
                              "Service Cloud and Sales Cloud with connected AI experiences.",
                "impact": "No client outcomes or metrics are published",
                "source": "https://www.tribolatech.com/",
            },
            {
                "sector": "Data engineering",
                "status": "Announced",
                "deployment": "Building data platforms and pipelines intended to power analytics, "
                              "Salesforce and enterprise AI from a trusted foundation.",
                "impact": "No client outcomes or metrics are published",
                "source": "https://www.tribolatech.com/",
            },
        ],
        "customer_sentiment": "No customer evidence of any kind was found in this pass \u2014 no named "
                              "clients, no case studies, no testimonials, no third-party reviews. That is "
                              "not a negative signal about quality; it simply means there is nothing to "
                              "assess from outside.",
        "sentiment_bull": [
            "Narrow, coherent focus on three practices rather than claiming end-to-end capability",
            "Stated method puts the business problem ahead of the platform, which is the right sequence",
            "Small enough that senior involvement in an engagement is credible",
            "US and India delivery footprint gives cost flexibility on scoped work",
        ],
        "sentiment_bear": [
            "The least-documented vendor in this app \u2014 no financials, no headcount, no named leadership, no client references",
            "Corporate identity is unclear from public material: Tribola Tech, TribolaTech Inc and Infinite Tek Inc all appear, with an infini-tek.com contact address",
            "No published evidence of delivery at enterprise scale",
            "Concentration and key-person risk are unquantifiable without direct diligence",
            "Being a Salesforce-centric shop limits relevance where Salesforce is not the estate",
        ],
        "employee_sentiment": "Not covered \u2014 no headcount disclosure and no employer-review data of any "
                              "kind was found.",
        "glassdoor": None,
        "kpis": [
            ("2009", "Operating roots"),
            ("3", "Specialist practices"),
            ("US + India", "Delivery footprint"),
            ("n/d", "Revenue"),
            ("n/d", "Employees"),
        ],
        "notes": "This is the thinnest page in the app and deliberately so. Tribola Tech publishes almost "
                 "nothing beyond its own website, and the corporate entity naming is inconsistent across "
                 "that material. Any engagement here should rest on references and direct diligence, not "
                 "on this page.",
    },

    # =================================================================
    {
        "slug": "uipath",
        "name": "UiPath",
        "website": "https://www.uipath.com",
        "linkedin": "https://www.linkedin.com/company/uipath",
        "group": "Automation",
        "category": "Agentic automation &amp; orchestration",
        "tagline": "Arguing that agents need deterministic automation underneath them \u2014 the execution "
                   "layer, not the reasoning layer",
        "founded": "2005 (in Romania)",
        "hq": "New York, New York",
        "employees": "Not disclosed in the results reviewed in this pass",
        "ownership": "Public (NYSE: PATH)",
        "revenue": "Q4 FY2026 revenue of $481M, up 14%, with ARR of $1.853B at 31 January 2026, up 11%. "
                   "GAAP operating income of $80M and non-GAAP operating income of $150M. ARR grew steadily "
                   "through the year \u2014 $1.693B, $1.723B, $1.782B, $1.853B",
        "revenue_short": "$1.85B ARR (FY26)",
        "offering": "The UiPath Platform for Agentic Automation and Orchestration, combining deterministic "
                    "robotic process automation with agentic AI and enterprise orchestration, plus built-in "
                    "security and governance. Recent additions include pre-built agentic solutions by "
                    "industry and the acquired WorkFusion agents for financial crime compliance.",
        "digital_twin": "No",
        "genai": "Yes (agentic automation)",
        "buyer": "COO, shared services and process owners; increasingly CIO for orchestration",
        "customers": [],
        "people": [
            {"name": "Daniel Dines", "title": "Founder, Chief Executive Officer &amp; Executive Chairman"},
            {"name": "Raghu Malpani", "title": "Chief Product &amp; Technology Officer"},
        ],
        "description": "$1.853B of ARR growing 11%, with the argument that enterprises scaling AI need "
                       "something that executes reliably rather than something that reasons well. Dines "
                       "frames UiPath as the execution layer enterprises trust for mission-critical "
                       "processes in the agentic era.",
        "position_note": "The distinction UiPath draws is worth taking seriously for infrastructure "
                         "operations: deterministic automation does the same thing every time, agentic AI "
                         "adapts, and mission-critical processes often need the former with the latter "
                         "layered on selectively. Regulated or safety-relevant workflows at a PortCo are "
                         "exactly where that matters \u2014 you do not want a probabilistic system "
                         "executing a compliance step. UiPath's own S/4HANA migration with Deloitte, which "
                         "reached 93% clean core in solution design and 88% overall, is a useful reference "
                         "because it is the vendor eating its own cooking on an ERP migration. The "
                         "commercial reality check is growth: 11% ARR growth is the slowest of any software "
                         "vendor tracked in this app.",
        "gip_connection": "No publicly disclosed GIP relationship. Most relevant to the Corporate Functions "
                          "Efficiency area of the reference model \u2014 back-office and shared-services "
                          "process automation \u2014 and potentially to compliance-heavy workflows where "
                          "deterministic execution is a requirement rather than a preference.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of PATH only.",
        "use_cases": [
            {
                "sector": "Platform positioning",
                "status": "Deployed",
                "deployment": "Deterministic automation, agentic AI and enterprise orchestration brought "
                              "together on a single governed platform, with tools for building and testing "
                              "agents and expanded built-in security and governance introduced at FUSION.",
                "impact": "ARR of $1.853B at FY2026 close, up 11%, with GAAP operating income of $80M and "
                          "non-GAAP operating income of $150M",
                "source": "https://ir.uipath.com/news/detail/431/uipath-reports-fourth-quarter-and-full-year-fiscal-2026-financial-results",
            },
            {
                "sector": "Healthcare",
                "status": "Announced",
                "deployment": "Agentic AI solutions for healthcare providers and payers covering medical "
                              "records summarisation, claim denial prevention and resolution, and prior "
                              "authorisation, using purpose-built, compliant and governed agents.",
                "impact": "Targets revenue cycle management \u2014 a high-volume, compliance-bound process "
                          "where deterministic execution matters",
                "source": "https://natlawreview.com/press-releases/uipath-reports-fourth-quarter-and-full-year-fiscal-2026-financial-results",
            },
            {
                "sector": "ERP modernisation",
                "status": "Deployed",
                "deployment": "UiPath's own migration to SAP S/4HANA, delivered with Deloitte, using "
                              "agentic automation to modernise its internal ERP.",
                "impact": "93% clean core in solution design and 88% clean core across the overall "
                          "implementation",
                "source": "https://ir.uipath.com/news/detail/404/uipath-reports-second-quarter-fiscal-2026-financial-results",
            },
            {
                "sector": "Financial crime compliance",
                "status": "Announced",
                "deployment": "Acquisition of WorkFusion, a pioneer in AI agents for financial crime "
                              "compliance, extending the platform into a regulated, audit-heavy domain.",
                "impact": "Announced alongside a new $500M share repurchase authorisation following "
                          "completion of a $1B programme",
                "source": "https://www.businesswire.com/news/home/20260311599358/en/UiPath-Reports-Fourth-Quarter-and-Full-Year-Fiscal-2026-Financial-Results",
            },
        ],
        "customer_sentiment": "Dines reports that customers consistently say automation and agentic AI are "
                              "stronger together, and that enterprises want a unified platform rather than "
                              "standalone tools. That framing is consistent with the numbers \u2014 steady, "
                              "unspectacular ARR growth from an installed base moving beyond pilots into "
                              "production. Net new ARR of $31M in Q2 FY2026 is the uncomfortable detail: "
                              "expansion is happening, but slowly.",
        "sentiment_bull": [
            "Profitable on both a GAAP and non-GAAP basis, which is rare among AI-positioned software vendors at this scale",
            "The deterministic-plus-agentic argument is genuinely differentiated and matters in regulated or safety-relevant processes",
            "Completed a $1B buyback and authorised a further $500M \u2014 a capital-return posture, not a cash-burn one",
            "Industry-specific agentic solutions (healthcare, financial crime) rather than horizontal claims",
        ],
        "sentiment_bear": [
            "ARR growth of 11% is the slowest of any software vendor tracked in this app, and it was flat at 11\u201312% across all four quarters",
            "Net new ARR of $31M in a single quarter is small against a $1.7B base",
            "RPA is the category most directly threatened by general-purpose agents \u2014 the repositioning is necessary, not opportunistic",
            "Competes with Microsoft, Salesforce, ServiceNow and SAP, all of which bundle automation into platforms customers already own",
            "Headcount is not disclosed in the results reviewed, limiting any read on delivery capacity",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 headcount was not disclosed and no "
                              "employer-review data was gathered. One leadership signal: CTO Raghu Malpani "
                              "took on an expanded role as Chief Product and Technology Officer, "
                              "consolidating product and engineering under a single leader reporting to Dines.",
        "glassdoor": None,
        "kpis": [
            ("2005", "Founded"),
            ("$1.85B", "ARR (FY26)"),
            ("+11%", "ARR growth"),
            ("$481M", "Q4 revenue"),
            ("$150M", "Non-GAAP op income"),
        ],
    },

    # =================================================================
    {
        "slug": "wipro",
        "name": "Wipro",
        "website": "https://www.wipro.com",
        "linkedin": "https://www.linkedin.com/company/wipro",
        "group": "SI / Consulting",
        "category": "IT services &amp; consulting",
        "tagline": "The weakest grower in its peer set, betting a turnaround on services-as-a-software",
        "founded": "1945",
        "hq": "Bengaluru, India",
        "employees": "Not disclosed in the results reviewed in this pass",
        "ownership": "Public (NSE/BSE: WIPRO; NYSE: WIT)",
        "revenue": "\u20b9928,093 million in FY2026 (year ended 31 March 2026) at a 16.3% operating margin, "
                   "with $16.4B of bookings and $7.8B of large-deal wins. Q1 FY2027 IT services revenue was "
                   "$2.61B, up just 0.9% at constant currency and down 1.2% sequentially, with operating "
                   "margin falling 1.2 points to 16%",
        "revenue_short": "~$10B (FY26)",
        "offering": "IT and consulting services across applications, infrastructure, engineering and "
                    "business process operations, with Wipro Intelligence as the AI programme \u2014 "
                    "industry platforms, the Winx and Vega delivery platforms, and an Innovation Network "
                    "with labs in the US, Australia and the Middle East. A new AI Native Business &amp; "
                    "Platforms unit pivots toward a services-as-a-software model.",
        "digital_twin": "Via engineering services",
        "genai": "Yes (Wipro Intelligence)",
        "buyer": "CIO and business leadership; strongest in BFSI",
        "customers": ["Olam Group"],
        "people": [
            {"name": "Srinivas Pallia", "title": "Chief Executive Officer &amp; Managing Director"},
            {"name": "Aparna C. Iyer", "title": "Chief Financial Officer"},
            {"name": "Rishad A. Premji", "title": "Executive Chairman"},
        ],
        "description": "The slowest-growing of the India-heritage integrators tracked here, with Q1 FY2027 "
                       "IT services revenue up just 0.9% at constant currency and declining sequentially. "
                       "Its response is a structural one \u2014 a new AI Native Business and Platforms unit "
                       "pivoting to a services-as-a-software model.",
        "position_note": "The services-as-a-software pivot is the most explicit statement by any integrator "
                         "in this app that the old model is finished. Selling outcomes delivered by "
                         "platforms rather than hours delivered by people changes the commercial "
                         "conversation fundamentally, and for a portfolio owner that is the direction to "
                         "push every services vendor toward. Pallia's observation that AI has become a "
                         "standing board-level mandate at many organisations matches what the reference "
                         "model assumes about executive sponsorship. The problem is that Wipro is "
                         "attempting this from the weakest position in its peer set: Americas 2 revenue "
                         "down 7.3%, margin compressing, and healthcare and energy clients under structural "
                         "pressure. Execution risk here is materially higher than at TCS, Infosys or "
                         "Cognizant.",
        "gip_connection": "No publicly disclosed GIP relationship. Most likely to appear as an incumbent "
                          "at a PortCo with an existing applications or infrastructure contract. The Olam "
                          "Group deal signals an appetite for large strategic agreements, which may make "
                          "Wipro commercially aggressive on portfolio-scale opportunities.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "Business model shift",
                "status": "Announced",
                "deployment": "The AI Native Business &amp; Platforms unit, pivoting Wipro toward a "
                              "services-as-a-software model \u2014 selling platform-delivered outcomes "
                              "rather than staffed effort \u2014 anchored by a strategic deal with the Olam "
                              "Group.",
                "impact": "Described by Pallia as a decisive investment to capture AI-era opportunities at scale",
                "source": "https://www.wipro.com/newsroom/press-releases/2026/wipro-announces-results-for-the-quarter-and-year-ended-march-31-2026/",
            },
            {
                "sector": "AI delivery platforms",
                "status": "Deployed",
                "deployment": "The Wipro Intelligence programme, anchored on industry platforms, the Winx "
                              "and Vega delivery platforms, and an Innovation Network with new labs in the "
                              "US, Australia and the Middle East.",
                "impact": "Two large multi-year deals tied to Wipro Intelligence highlighted in Q3 FY2026; "
                          "AI described by Pallia as a standing board-level mandate at many client organisations",
                "source": "https://finance.yahoo.com/news/wipro-q3-earnings-call-highlights-131157177.html",
            },
            {
                "sector": "Commercial performance",
                "status": "Deployed",
                "deployment": "Large deal bookings tracked as the leading indicator through a difficult "
                              "demand environment, with growth sequentially broad-based across three of "
                              "four markets and four of five sectors in Q3 FY2026.",
                "impact": "FY2026 bookings of $16.4B with $7.8B of large-deal wins; Q3 TCV of $3.3B with "
                          "year-to-date TCV around $13B, up roughly 25%",
                "source": "https://www.stocktitan.net/sec-filings/WIT/6-k-wipro-ltd-current-report-foreign-issuer-983a38732b2e.html",
            },
            {
                "sector": "Cash generation",
                "status": "Deployed",
                "deployment": "Margin held within a narrow band while investing in clients, capabilities "
                              "and people, with disciplined cash conversion.",
                "impact": "FY2026 operating cash flow at 112.6% of net income; over $1.3B of cash returned "
                          "to shareholders during the year",
                "source": "https://www.wipro.com/content/dam/nexus/en/investor/quarterly-results/2025-2026/q4fy26/press-release-q4fy26.pdf",
            },
        ],
        "customer_sentiment": "Pallia describes a macro environment that remains resilient while "
                              "uncertainty shapes decision-making \u2014 spending measured with more rigour "
                              "and longer decision cycles. The sector detail is harsher: the US healthcare "
                              "ecosystem is under sustained structural and demographic pressure, producing "
                              "flat or negative growth for specific clients, and energy is similarly soft. "
                              "Wipro publishes no attributable client outcomes.",
        "sentiment_bull": [
            "The services-as-a-software pivot is the most explicit break with the hours-based model of any integrator tracked here",
            "Operating cash flow at 112.6% of net income with over $1.3B returned to shareholders",
            "FY2026 bookings of $16.4B and year-to-date TCV up roughly 25% in Q3 \u2014 the order book is healthier than the revenue line",
            "APMEA grew 13.5% year over year, showing the model works where demand exists",
        ],
        "sentiment_bear": [
            "Q1 FY2027 IT services revenue grew just 0.9% at constant currency and fell 1.2% sequentially \u2014 the weakest in its peer set",
            "Operating margin fell 1.2 points to 16% on salary increases, large-deal ramp-ups and AI investment",
            "Americas 2 revenue declined 7.3% year over year and 2.5% sequentially",
            "Q2 FY2027 guidance of -1.5% to +0.5% constant currency contemplates further contraction",
            "Healthcare and energy verticals face structural pressure, not cyclical softness",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 headcount was not disclosed in the results "
                              "reviewed and no employer-review data was gathered. Margin commentary "
                              "indicates salary increases were absorbed during the year, which suggests "
                              "retention spending rather than cuts.",
        "glassdoor": None,
        "kpis": [
            ("1945", "Founded"),
            ("~$10B", "FY2026 revenue"),
            ("16.3%", "Operating margin"),
            ("$16.4B", "FY2026 bookings"),
            ("+0.9%", "Q1 FY27 growth"),
        ],
        "notes": "Wipro reports in rupees; dollar conversions vary with the rate used and figures between "
                 "$9.9B and $10.5B appear across sources for FY2026. The rupee figure and margin are the "
                 "reliable ones.",
    },

    # =================================================================
    {
        "slug": "workday",
        "name": "Workday",
        "website": "https://www.workday.com",
        "linkedin": "https://www.linkedin.com/company/workday",
        "group": "Enterprise software",
        "category": "HCM &amp; financial management",
        "tagline": "Sitting on the cleanest HR and finance dataset in enterprise software, and turning it "
                   "into agents",
        "founded": "2005",
        "hq": "Pleasanton, California",
        "employees": "Not disclosed in the results reviewed; $166M of restructuring expense was recorded in "
                     "Q1 FY2026",
        "ownership": "Public (NASDAQ: WDAY)",
        "revenue": "$9.6B total revenue in FY2026 (year ended 31 January 2026), up from $8.4B, with "
                   "subscription revenue rising from $7.7B to $8.8B. Operating cash flow grew from $2.5B to "
                   "$2.9B, and $2.9B of shares were repurchased. Non-GAAP operating margin around 28.5%",
        "revenue_short": "$9.6B (FY26)",
        "offering": "A unified platform for human capital management and financial management, with Workday "
                    "Illuminate as the AI layer and a growing set of Illuminate Agents. Workday Build is a "
                    "new open developer platform letting customers and partners create and share "
                    "AI-powered solutions on Workday.",
        "digital_twin": "No",
        "genai": "Yes (Illuminate)",
        "buyer": "CHRO and CFO",
        "customers": ["Salesforce", "Sunnybrook Health Sciences Centre", "Fuji Electric",
                      "The Magnum Ice Cream Company", "US Physical Therapy"],
        "people": [
            {"name": "Carl Eschenbach", "title": "Chief Executive Officer"},
            {"name": "Zane Rowe", "title": "Chief Financial Officer"},
        ],
        "description": "Subscription revenue grew from $7.7B to $8.8B in FY2026, with subscription backlog "
                       "of $25.96B, up 17%. More than 75% of core customers use Workday Illuminate, and "
                       "over a billion AI actions ran on the platform during the year.",
        "position_note": "Workday's claim is data, not models: Illuminate is trained on what it describes "
                         "as the largest and cleanest finance and HR dataset, with more than 75 million "
                         "users under contract and a trillion transactions processed in a year. For a "
                         "portfolio programme the relevant point is that HR and finance are the two "
                         "functions every PortCo has regardless of sector, which makes Workday one of the "
                         "few genuinely portfolio-wide plays in the Corporate Functions Efficiency area of "
                         "the reference model. The adoption metrics are the most convincing part: over 75% "
                         "of net new deals and 35% of customer expansions included one or more AI products, "
                         "which means AI is affecting what gets bought rather than being bolted on "
                         "afterwards.",
        "gip_connection": "No publicly disclosed GIP relationship. HR and finance are universal across "
                          "PortCos, so this is one of the more plausible candidates for consolidated "
                          "portfolio-level licensing. Note that Salesforce is a long-standing Workday HCM "
                          "customer, and both vendors are tracked here.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of WDAY only.",
        "use_cases": [
            {
                "sector": "AI adoption",
                "status": "Deployed",
                "deployment": "Workday Illuminate embedded across HR and finance workflows, with Illuminate "
                              "Agents introduced to accelerate hiring, improve frontline worker "
                              "experiences, simplify financial processes and improve access to employee "
                              "information.",
                "impact": "More than 75% of core customers using Illuminate AI, with over 1 billion AI "
                          "actions on the platform in a single year; more than 75% of net new deals and 35% "
                          "of customer expansions included one or more AI products",
                "source": "https://diginomica.com/if-you-were-build-enterprise-ai-system-scale-would-it-look-workday-yes-says-ceo-carl-eschenbach",
            },
            {
                "sector": "Data foundation",
                "status": "Deployed",
                "deployment": "Illuminate built on Workday's own transactional dataset rather than "
                              "general-purpose training data \u2014 the finance and HR records of its "
                              "contracted user base.",
                "impact": "More than 75 million users under contract and a trillion transactions processed "
                          "in a single year",
                "source": "https://www.workday.com/content/dam/web/en-us/documents/investor/workday-fiscal-2026-second-quarter-prepared-remarks.pdf",
            },
            {
                "sector": "Platform expansion",
                "status": "Deployed",
                "deployment": "Four acquisitions completed in FY2026 \u2014 Flowise (low-code AI agent "
                              "building), Paradox (candidate experience agent), Sana Labs (enterprise "
                              "knowledge) and Pipedream (integration platform for AI agents) \u2014 plus "
                              "Workday Build, an open developer platform for customers and partners.",
                "impact": "Subscription backlog reached $25.96B, up 17%, including the Paradox contribution",
                "source": "https://www.sec.gov/Archives/edgar/data/0001327811/000110465926055697/tm263922d2_ars.pdf",
            },
            {
                "sector": "Full-suite adoption",
                "status": "Deployed",
                "deployment": "Selling HR and finance together rather than HCM alone, with full-suite "
                              "adoption highest in state, local and education, and healthcare.",
                "impact": "Half of net new global deals in Q3 FY2026 included both HR and finance; roughly "
                          "30% of net new deals were full suite, rising to 50% or more in SLED and healthcare",
                "source": "https://www.fool.com/earnings/call-transcripts/2025/11/25/workday-wday-q3-2026-earnings-call-transcript/",
            },
        ],
        "customer_sentiment": "The adoption data is the strongest evidence of any vendor in this wave: over "
                              "three-quarters of core customers actively using the AI layer, and AI present "
                              "in more than three-quarters of net new deals. Eschenbach frames the "
                              "proposition as helping customers manage their two most critical assets "
                              "\u2014 people and money \u2014 on one platform, and the rising full-suite "
                              "attach rate supports that. Named go-lives include Salesforce, a long-time "
                              "HCM customer.",
        "sentiment_bull": [
            "More than 75% of core customers use Illuminate AI, with over a billion AI actions on the platform in a year",
            "Subscription backlog of $25.96B, up 17%, with subscription revenue up from $7.7B to $8.8B",
            "HR and finance are universal functions, making Workday one of the few genuinely portfolio-wide candidates",
            "Operating cash flow grew from $2.5B to $2.9B alongside $2.9B of share repurchases",
        ],
        "sentiment_bear": [
            "Subscription growth of roughly 14\u201315% is solid but not exceptional against ServiceNow at 24.5%",
            "$166M of restructuring expense in Q1 FY2026 pushed GAAP operating margin down to 1.8% for the quarter",
            "Four acquisitions in one year carries integration risk and makes organic growth harder to read",
            "Competes directly with SAP and Oracle, both of which bundle HCM and financials into wider estates",
            "Headcount is not disclosed in the results reviewed, so the restructuring's scale is unclear",
        ],
        "employee_sentiment": "Not covered in this pass. The one concrete signal is $166M of restructuring "
                              "expense recorded in Q1 FY2026, alongside management commentary about driving "
                              "continued efficiencies throughout the business. No employer-review data was "
                              "gathered.",
        "glassdoor": None,
        "kpis": [
            ("2005", "Founded"),
            ("$9.6B", "FY2026 revenue"),
            ("$8.8B", "Subscription revenue"),
            ("$25.96B", "Subscription backlog"),
            ("75M+", "Users under contract"),
        ],
    },

    # =================================================================
    {
        "slug": "xai",
        "name": "xAI",
        "website": "https://x.ai",
        "linkedin": "https://www.linkedin.com/company/xai",
        "group": "Frontier AI / LLM",
        "category": "Frontier AI lab \u2014 now a SpaceX subsidiary",
        "tagline": "The largest GPU cluster in the world attached to the smallest revenue of any frontier "
                   "lab \u2014 and no longer an independent company",
        "founded": "9 March 2023 (by Elon Musk and eleven co-founders)",
        "hq": "Bay Area, California; Colossus supercomputers in Memphis, Tennessee",
        "employees": "Not disclosed. All eleven original co-founders had departed by March 2026, leaving "
                     "Musk as the only remaining founding figure",
        "ownership": "Wholly-owned subsidiary of SpaceX following an all-stock acquisition completed 2 "
                     "February 2026 that valued xAI at roughly $250B and the combined entity at about "
                     "$1.25 trillion. SpaceX subsequently listed on Nasdaq in June 2026",
        "revenue": "Approximately $500M annualised recurring revenue in early 2026, up from roughly $350M "
                   "of revenue in 2025, against a reported burn close to $1B per month. A full-year 2026 "
                   "target of around $2B has been reported",
        "revenue_short": "~$500M ARR",
        "offering": "The Grok model family, sold through SuperGrok consumer subscriptions via the X app, "
                    "API access and enterprise deals, with Grok Voice available in Tesla vehicles. Compute "
                    "runs on the Colossus I and II clusters in Memphis.",
        "digital_twin": "No",
        "genai": "Yes (Grok)",
        "buyer": "Consumers via X; developers via API; a small but growing enterprise and government channel",
        "customers": [],
        "people": [
            {"name": "Elon Musk", "title": "Founder"},
        ],
        "description": "Raised $20B in January 2026 at a $230B valuation, then merged into SpaceX a month "
                       "later at roughly $250B. Colossus grew from 100,000 GPUs at its October 2024 launch "
                       "to 555,000, with the two Memphis clusters together housing over a million GPUs and "
                       "drawing 2 gigawatts.",
        "position_note": "xAI is the clearest example in this app of infrastructure scale running far ahead "
                         "of commercial traction: roughly $500M of ARR against approximately $42B raised "
                         "and a reported $1B monthly burn, with a GPU estate that makes it one of NVIDIA's "
                         "largest single data-centre customers. For an infrastructure investor the "
                         "interesting artefact is Colossus itself \u2014 the first gigawatt-scale AI "
                         "training cluster, reportedly built in 122 days \u2014 and the fact that in May "
                         "2026 SpaceX leased Colossus 1 to a direct competitor, which is a revealing "
                         "signal about how AI compute is becoming a tradeable asset class rather than a "
                         "proprietary moat. The governance picture is the part that should give any "
                         "enterprise buyer pause, and it is set out below rather than softened.",
        "gip_connection": "No publicly disclosed GIP relationship. Relevance to the portfolio is as a "
                          "compute and power demand driver rather than as a vendor \u2014 Colossus draws 2 "
                          "gigawatts, and its power sourcing has already produced a regulatory finding. One "
                          "secondary source lists BlackRock among xAI's investors; this was not confirmed "
                          "in primary material and should be verified internally before it is relied on.",
        "blackrock_connection": "One third-party tracker lists BlackRock among xAI's investor roster "
                                "alongside Andreessen Horowitz, Sequoia, Fidelity, NVIDIA and sovereign "
                                "funds. This was not confirmed in primary sources in this pass and should "
                                "be treated as unverified.",
        "use_cases": [
            {
                "sector": "AI infrastructure",
                "status": "Deployed",
                "deployment": "The Colossus I and II supercomputers in Memphis \u2014 described as the "
                              "world's first gigawatt-scale AI training cluster and reportedly built in 122 "
                              "days \u2014 scaling from 100,000 H100s at launch toward a stated target of "
                              "one million GPUs.",
                "impact": "555,000 GPUs and roughly $18B of GPU investment, drawing 2 gigawatts; makes xAI "
                          "one of NVIDIA's largest single data-centre customers",
                "source": "https://www.gradually.ai/en/grok-statistics/",
            },
            {
                "sector": "Corporate structure",
                "status": "Deployed",
                "deployment": "All-stock merger into SpaceX completed 2 February 2026, valuing xAI at "
                              "roughly $250B and creating a combined entity worth about $1.25 trillion "
                              "\u2014 reported as the largest private corporate merger by valuation. "
                              "SpaceX listed on Nasdaq in June 2026.",
                "impact": "Grok is now a product line inside a publicly traded rocket company, backstopped "
                          "by SpaceX capital and compute",
                "source": "https://aibusinessweekly.net/p/xai-statistics",
            },
            {
                "sector": "Distribution",
                "status": "Deployed",
                "deployment": "Grok integrated directly into the X platform, with SuperGrok subscriptions "
                              "sold through the app, Grok Voice deployed in Tesla vehicles, and API access "
                              "for developers.",
                "impact": "Reported reach of approximately 600 million monthly active users across X and "
                          "Grok applications, though Grok holds only about 2.8% of global AI chatbot web "
                          "traffic, ranking fifth",
                "source": "https://gulfnews.com/business/markets/elon-musks-xai-raises-20-billion-in-nvidia-backed-funding-round-1.500400546",
            },
            {
                "sector": "Compute as an asset",
                "status": "Announced",
                "deployment": "In May 2026 SpaceX leased the original Colossus 1 data centre to a direct "
                              "competitor, while Grok 5 continued training on Colossus 2 with variants "
                              "reported at up to 10 trillion parameters.",
                "impact": "Treats AI compute capacity as a leasable asset rather than a proprietary "
                          "advantage \u2014 a structurally significant precedent for digital infrastructure",
                "source": "https://aibusinessweekly.net/p/grok-ai-statistics",
            },
        ],
        "customer_sentiment": "Commercial traction is far behind its peers. At roughly $500M of ARR, xAI "
                              "sits against Anthropic's $47B and OpenAI's $25B, and Grok's share of AI "
                              "chatbot web traffic is around 2.8%, fifth behind ChatGPT, Gemini, Claude and "
                              "DeepSeek. Grok 4.5, released July 2026, ranked fourth on the Artificial "
                              "Analysis Intelligence Index and is priced aggressively at $2 and $6 per "
                              "million tokens, so the strategy is clearly price and distribution rather "
                              "than capability leadership.",
        "sentiment_bull": [
            "Colossus is a genuine engineering achievement \u2014 the first gigawatt-scale AI training cluster, reportedly built in 122 days",
            "Backstopped by SpaceX capital and compute after the February 2026 merger, removing near-term funding risk",
            "Distribution through X reaches roughly 600 million monthly active users without separate customer acquisition",
            "Aggressive API pricing at $2 and $6 per million tokens undercuts frontier competitors materially",
        ],
        "sentiment_bear": [
            "Roughly $500M of ARR against approximately $42B raised and a reported $1B monthly burn \u2014 the widest gap between capital and revenue of any vendor tracked here",
            "All eleven original co-founders departed by March 2026, leaving Musk as the sole remaining founding figure",
            "Serious regulatory and legal exposure: a California Attorney General investigation and cease-and-desist over alleged Grok-generated non-consensual explicit imagery and potential child sexual abuse material, with parallel scrutiny in Europe and Asia, national bans in Indonesia and Malaysia, and a class-action lawsuit",
            "The EPA ruled that xAI illegally operated natural-gas generators for its Colossus data centres in Tennessee, adding environmental compliance liability",
            "Grok 5 missed both its Q1 and Q2 2026 target windows, and Grok holds only about 2.8% of chatbot traffic",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 headcount is not disclosed and no "
                              "employer-review data was gathered. The one unambiguous signal is founder "
                              "attrition: all eleven original co-founders had left by March 2026.",
        "glassdoor": None,
        "kpis": [
            ("2023", "Founded"),
            ("~$500M", "ARR"),
            ("~$42B", "Capital raised"),
            ("555,000", "GPUs at Colossus"),
            ("~$250B", "Merger valuation"),
        ],
        "notes": "xAI no longer exists as an independent company; it is a SpaceX subsidiary following the "
                 "February 2026 merger, and reporting now sometimes refers to the combined AI division "
                 "rather than xAI. The governance and regulatory issues listed under 'What to "
                 "pressure-test' are material to any enterprise adoption decision and are stated as "
                 "reported by the sources cited.",
    },
]
