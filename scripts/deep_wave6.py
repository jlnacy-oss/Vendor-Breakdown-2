# -*- coding: utf-8 -*-
"""
deep_wave6.py — Research wave 6, completed 15 September 2026.

NTT DATA, NVIDIA, OpenAI, Oracle, Perplexity.
"""

VENDORS = [
    # =================================================================
    {
        "slug": "ntt-data",
        "name": "NTT DATA",
        "website": "https://www.nttdata.com",
        "linkedin": "https://www.linkedin.com/company/ntt-data",
        "group": "SI / Consulting",
        "category": "IT services, systems integration &amp; data centres",
        "tagline": "A telco-owned integrator that also owns physical infrastructure \u2014 unusual in this "
                   "set, and under-recognised even by its own CEO's account",
        "founded": "1988 (spun off from NTT; the data communications business dates to 1967)",
        "hq": "Toyosu, K\u014dt\u014d, Tokyo, Japan",
        "employees": "197,800 group-wide (2025); the international business led from NTT DATA, Inc. "
                     "accounts for roughly 150,000 of them",
        "ownership": "Subsidiary of NTT, Inc. \u2014 NTT DATA Group Corporation",
        "revenue": "\u00a54.64 trillion (approximately $42.27B) in FY2025, with operating income of "
                   "\u00a5323.9B (~$2.95B) and net income of \u00a5142.5B (~$1.3B). The international "
                   "business, formed by merging NTT Ltd into NTT DATA, is described as a roughly $30B "
                   "operation, of which about $18B sits outside Japan",
        "revenue_short": "~$42.3B (FY25)",
        "offering": "Systems integration, application and infrastructure managed services, and "
                    "consulting \u2014 combined, since the NTT Ltd merger, with data centre and network "
                    "infrastructure. R&amp;D includes photonics-powered data centres that transmit data "
                    "using light rather than electrical signals.",
        "digital_twin": "Not confirmed in this pass",
        "genai": "Yes (services)",
        "buyer": "CIO and infrastructure leadership; historically strongest in Japan, financial services and public sector",
        "customers": [],
        "people": [
            {"name": "Abhijit Dubey", "title": "President &amp; Chief Executive Officer, NTT DATA, Inc."},
        ],
        "description": "Japan's largest IT services company and, after absorbing NTT Ltd, a combined "
                       "business and technology services operation of roughly $30B outside the group's "
                       "domestic base. Unusually for an integrator, it sits inside a telecommunications "
                       "group and carries real physical infrastructure alongside the services business.",
        "position_note": "NTT DATA's distinguishing feature for an infrastructure portfolio is that it is "
                         "not purely a services firm \u2014 through the NTT group it owns data centre and "
                         "network assets, and its research agenda includes photonics-based data centres "
                         "using light rather than electrical signalling for transmission. That puts it on "
                         "both sides of the digital-infrastructure conversation. Dubey's own framing of the "
                         "AI challenge is the useful one: applying AI inside core operations is a materially "
                         "harder problem than applying it to a single function, which is exactly the gap "
                         "between a PortCo productivity pilot and asset optimisation. The candid "
                         "counterpoint, also his, is that the firm's biggest commercial problem is "
                         "recognition \u2014 buyers do not think of NTT DATA when drawing up a shortlist.",
        "gip_connection": "No publicly disclosed GIP relationship. Worth noting the dual position: NTT group "
                          "data centre assets make it a potential counterparty in digital infrastructure as "
                          "well as a services supplier. Clarify which relationship is in play before "
                          "engaging.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "Digital infrastructure R&amp;D",
                "status": "Announced",
                "deployment": "Photonics-powered data centres, using light rather than electrical signals "
                              "to transmit data \u2014 part of the NTT group's broader optical networking "
                              "research agenda.",
                "impact": "Positions NTT DATA as an infrastructure operator and researcher, not only an integrator",
                "source": "https://finance.yahoo.com/news/ntt-data-ceo-one-week-095211711.html",
            },
            {
                "sector": "Corporate structure",
                "status": "Deployed",
                "deployment": "Merger of NTT Ltd into NTT DATA, consolidating international IT services, "
                              "data centre and network operations under a single brand and leadership.",
                "impact": "Created a business and technology services operation of roughly $30B, with about "
                          "$18B generated outside Japan across around 150,000 employees",
                "source": "https://mar.nttdata.com/leadership",
            },
            {
                "sector": "Group scale",
                "status": "Deployed",
                "deployment": "The full NTT DATA Group, combining the Japanese domestic business with "
                              "international operations, reported through NTT, Inc.",
                "impact": "FY2025 revenue of \u00a54.64 trillion (~$42.27B), operating income of "
                          "\u00a5323.9B, and 197,800 employees",
                "source": "https://en.wikipedia.org/wiki/NTT_Data",
            },
        ],
        "customer_sentiment": "The most candid available assessment comes from Dubey himself, who has "
                              "described the firm's central challenge as getting onto the radar of potential "
                              "customers at all \u2014 an unusual admission from a $42B company, and one "
                              "that matches its low profile in Western shortlists relative to Accenture, "
                              "Capgemini or the India-heritage firms. NTT DATA publishes few attributable "
                              "client outcomes in English-language material.",
        "sentiment_bull": [
            "Roughly $42B of group revenue makes it one of the largest integrators in the world, and larger than Capgemini",
            "Owns physical data centre and network infrastructure through the NTT group \u2014 rare among services firms",
            "Photonics data centre research is a genuine technical differentiator rather than a marketing position",
            "Dubey brings McKinsey senior-partner and oilfield-services background, which is closer to infrastructure than a typical services CEO profile",
        ],
        "sentiment_bear": [
            "Brand recognition is the firm's own stated problem \u2014 it is frequently absent from Western vendor shortlists",
            "Operating margin of roughly 7% on group revenue is thin against Accenture or the India-heritage peer set",
            "Complex structure \u2014 group corporation, Japanese domestic entity and international entity \u2014 makes it harder to know which entity you are contracting with",
            "Publicly available financial and operational detail in English is materially thinner than for any comparable peer in this app",
            "The NTT Ltd merger is still being digested; integration risk is live",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 no reliable employer-review data was gathered "
                              "and headcount is reported at group level without recent breakdown. Treat as a gap.",
        "glassdoor": None,
        "kpis": [
            ("1988", "Founded"),
            ("197,800", "Employees"),
            ("~$42.3B", "FY2025 revenue"),
            ("~$30B", "International business"),
            ("~7%", "Operating margin"),
        ],
        "notes": "This page rests on thinner sourcing than others in the app. NTT DATA's English-language "
                 "disclosure is limited, some figures are from secondary compilations rather than filings, "
                 "and leadership detail dates from the 2024 appointment announcements. Verify before relying "
                 "on any figure here.",
    },

    # =================================================================
    {
        "slug": "nvidia",
        "name": "NVIDIA",
        "website": "https://www.nvidia.com",
        "linkedin": "https://www.linkedin.com/company/nvidia",
        "group": "Frontier AI / LLM",
        "category": "Accelerated computing &amp; AI infrastructure",
        "tagline": "The supply constraint on the entire AI economy \u2014 and now reporting physical AI as "
                   "its own revenue line",
        "founded": "1993",
        "hq": "Santa Clara, California",
        "employees": "Not disclosed in the results reviewed in this pass",
        "ownership": "Public (NASDAQ: NVDA)",
        "revenue": "$215.9B in FY2026 (year ended January 2026), up 65%, with Data Center at $193.7B, up "
                   "68%. Q4 FY2026 revenue was a record $62.3B, up 75%. Q1 FY2027 reached $81.6B with Data "
                   "Center up 92% to $75.2B, and guidance of about $91B for Q2 FY2027",
        "revenue_short": "$215.9B (FY26)",
        "offering": "GPU and rack-scale accelerated computing \u2014 the Blackwell and Grace Blackwell "
                    "platforms, with Vera Rubin ramping \u2014 plus NVLink interconnect, BlueField data "
                    "processors, networking, and the CUDA software stack. Automotive and robotics run "
                    "through DRIVE and the Alpamayo open model family.",
        "digital_twin": "Yes (Omniverse)",
        "genai": "Yes (the substrate for most of it)",
        "buyer": "Hyperscalers, frontier labs, sovereign AI programmes and OEMs",
        "customers": ["OpenAI", "Anthropic", "Microsoft", "Oracle", "Google Cloud", "xAI"],
        "people": [
            {"name": "Jensen Huang", "title": "Founder &amp; Chief Executive Officer"},
        ],
        "description": "FY2026 revenue of $215.9B, up 65%, with Data Center at 90% of the total. Huang has "
                       "said cloud GPUs are sold out, that NVIDIA expects at least $1 trillion of cumulative "
                       "Blackwell and Vera Rubin revenue through 2027, and bluntly that supply will fall "
                       "short of demand.",
        "position_note": "Two things here matter to an infrastructure portfolio more than the headline "
                         "numbers. First, NVIDIA reported $6B of physical AI revenue in FY2026 \u2014 "
                         "robotics, autonomous mobility, industrial systems \u2014 which makes it one of the "
                         "few vendors in this app putting a disclosed figure against the category most "
                         "relevant to operating assets. Second, Huang's reframing of the data centre as a "
                         "factory producing tokens rather than storing files is the argument underpinning "
                         "the entire digital-infrastructure investment thesis, and it is worth engaging "
                         "with critically rather than adopting. The practical constraint for any PortCo is "
                         "supply: cloud GPUs are sold out, memory shortages are forcing NVIDIA to "
                         "prioritise data centre over gaming, and access runs through the hyperscalers "
                         "rather than direct.",
        "gip_connection": "No publicly disclosed GIP relationship. NVIDIA is relevant to the portfolio "
                          "mainly as a supply constraint and a demand driver \u2014 its capacity decisions "
                          "set the cost and availability of compute for every AI programme, and its "
                          "partnerships with Google Cloud, Microsoft, Oracle and xAI to build US AI "
                          "infrastructure make it a direct influence on digital-infrastructure asset demand.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of NVDA only.",
        "use_cases": [
            {
                "sector": "Physical AI",
                "status": "Deployed",
                "deployment": "Robotics, autonomous mobility and industrial systems, including L4-ready "
                              "mobility networks through a partnership with Uber and DRIVE-powered "
                              "Mercedes-Benz vehicles, plus the Alpamayo family of open AV models, "
                              "simulation tools and datasets.",
                "impact": "$6B of physical AI revenue reported in FY2026; automotive revenue rose 39% to a "
                          "record $2.3B",
                "source": "https://theenergymag.com/news/market-news/nvidia-reports-215-9-billion-in-fy-2026-revenue-as-data-center-networking-surges-142",
            },
            {
                "sector": "Frontier AI compute",
                "status": "Announced",
                "deployment": "Strategic partnerships to deploy NVIDIA systems at gigawatt scale \u2014 at "
                              "least 10 gigawatts for OpenAI's next-generation infrastructure, and Anthropic "
                              "running on NVIDIA infrastructure for the first time with an initial 1 "
                              "gigawatt of Grace Blackwell and Vera Rubin capacity.",
                "impact": "Alongside partnerships with Google Cloud, Microsoft, Oracle and xAI to build US "
                          "AI infrastructure with hundreds of thousands of GPUs",
                "source": "https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2026",
            },
            {
                "sector": "Platform transition",
                "status": "Announced",
                "deployment": "The Vera Rubin platform, comprising six new chips co-designed for agentic AI "
                              "workloads, with AWS, Google Cloud, Microsoft Azure and Oracle Cloud "
                              "Infrastructure among the first to deploy Vera Rubin instances.",
                "impact": "Targets up to a 10x reduction in inference token cost against Blackwell; "
                          "BlueField-4 powers a new AI-native storage class",
                "source": "https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026",
            },
            {
                "sector": "Supply &amp; demand",
                "status": "Deployed",
                "deployment": "Blackwell and Grace Blackwell rack-scale systems shipping into sustained "
                              "excess demand, with an annual product cadence and networking attach growing "
                              "alongside compute.",
                "impact": "Data Center networking revenue surged 142% in FY2026; Huang projects at least $1 "
                          "trillion cumulative Blackwell and Vera Rubin revenue through 2027 and has said "
                          "supply will be short",
                "source": "https://tech-insider.org/nvidia-earnings-81-billion-quarter-2026/",
            },
        ],
        "customer_sentiment": "Demand exceeds supply by NVIDIA's own account, which removes any normal "
                              "negotiating dynamic \u2014 cloud GPUs are sold out and Grace Blackwell "
                              "rack-scale systems have long been allocated. The friction is showing "
                              "elsewhere: a global memory shortage has pushed NVIDIA to prioritise Blackwell "
                              "and Rubin over GeForce, leaving gaming customers, now under 8% of the "
                              "business, feeling deprioritised. That is a useful signal about where NVIDIA's "
                              "attention goes when capacity is scarce.",
        "sentiment_bull": [
            "FY2026 revenue up 65% to $215.9B with Data Center up 68% \u2014 growth at a scale with no precedent in semiconductors",
            "Non-GAAP gross margins in the low-to-mid 70s despite unprecedented volume",
            "$6B of disclosed physical AI revenue \u2014 the category most relevant to operating infrastructure assets",
            "Vera Rubin targets a 10x reduction in inference token cost, which directly addresses the cost pressure now constraining enterprise AI",
        ],
        "sentiment_bear": [
            "The stock fell after each of the three most recent results despite beating expectations 18 times in 20 quarters \u2014 expectations may have reached unattainable levels",
            "Customer concentration is extreme: a handful of hyperscalers and frontier labs drive the majority of Data Center revenue, and their capex plans are the single point of failure",
            "AMD's Helios rack-scale system is expected to compete directly with Vera Rubin",
            "Memory shortages are constraining supply and forcing internal prioritisation, with gaming customers the visible casualty",
            "Huang's $1 trillion cumulative projection is a management statement of ambition, not guidance",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 headcount was not disclosed in the results "
                              "reviewed and no reliable employer-review data was gathered. The one "
                              "governance data point found: 96% of Huang's target compensation is "
                              "performance-dependent, with FY2026 reported compensation of $36.3M.",
        "glassdoor": None,
        "kpis": [
            ("1993", "Founded"),
            ("$215.9B", "FY2026 revenue"),
            ("$193.7B", "Data Center revenue"),
            ("$6B", "Physical AI revenue"),
            ("+142%", "Networking growth"),
        ],
    },

    # =================================================================
    {
        "slug": "openai",
        "name": "OpenAI",
        "website": "https://openai.com",
        "linkedin": "https://www.linkedin.com/company/openai",
        "group": "Frontier AI / LLM",
        "category": "Frontier AI lab \u2014 consumer and enterprise",
        "tagline": "The most widely deployed AI product in the enterprise, losing money at a scale that "
                   "will be tested by a public listing",
        "founded": "2015 (as a non-profit); recapitalised in October 2025 as OpenAI Group PBC",
        "hq": "San Francisco, California",
        "employees": "Not reliably disclosed",
        "ownership": "Private. $852B post-money valuation from a $122B round in March 2026 led by SoftBank "
                     "and Microsoft. Confidential S-1 filed 8 June 2026; reporting indicates a 2027 listing "
                     "is more likely than 2026",
        "revenue": "Annualised run rate reported at roughly $20B at end-2025, about $25B by February 2026 "
                   "and over $40B by August 2026. Leaked audited figures indicate $13.1B of booked revenue "
                   "in 2025 against an operating loss of $20.9B",
        "revenue_short": "$40B+ (Aug 2026)",
        "offering": "ChatGPT across free, Plus ($20/month) and Pro ($200/month) tiers, enterprise plans, and "
                    "the API and developer platform. An advertising pilot was added during 2026.",
        "digital_twin": "No",
        "genai": "Yes (GPT family)",
        "buyer": "Broad \u2014 consumers, developers and enterprise IT, with enterprise now above 40% of revenue",
        "customers": [],
        "people": [
            {"name": "Sam Altman", "title": "Chief Executive Officer"},
            {"name": "Sarah Friar", "title": "Chief Financial Officer"},
        ],
        "description": "The most broadly adopted AI product in the enterprise \u2014 roughly 92% of the "
                       "Fortune 500 use ChatGPT and business customers passed one million in November 2025 "
                       "\u2014 while carrying losses large enough that the IPO timetable has slipped from a "
                       "2026 listing toward 2027.",
        "position_note": "For a portfolio programme, OpenAI's advantage is penetration: the product is "
                         "already inside most organisations, often through individual and team "
                         "subscriptions before IT gets involved, which makes governance rather than "
                         "procurement the first problem to solve. The strategic risk to watch is what a "
                         "listing does to the product. A public company optimises for margin and for "
                         "revenue-driving enterprise features; reporting suggests API-only customers may "
                         "find themselves in a lower priority tier than large enterprise accounts. Any "
                         "PortCo running production workloads on the API should have a portability plan "
                         "regardless, and the economics of open-weight alternatives strengthen every time a "
                         "closed provider approaches a listing.",
        "gip_connection": "No publicly disclosed GIP relationship. ChatGPT is near-certain to be present "
                          "across PortCos already, frequently through unmanaged individual subscriptions "
                          "\u2014 which makes this a governance and consolidation question rather than a "
                          "vendor selection one. OpenAI's compute commitments also make it a major driver "
                          "of data-centre demand, including through Oracle's backlog.",
        "blackrock_connection": "No publicly disclosed operating relationship. OpenAI is private; the March "
                                "2026 round was led by SoftBank and Microsoft.",
        "use_cases": [
            {
                "sector": "Enterprise penetration",
                "status": "Deployed",
                "deployment": "ChatGPT deployed across consumer, team and enterprise tiers, with the "
                              "developer ecosystem expanding through the API.",
                "impact": "Approximately 92% of the Fortune 500 use ChatGPT; business customers passed one "
                          "million in November 2025; ChatGPT reached 900 million weekly and crossed one "
                          "billion monthly active users in June 2026",
                "source": "https://aibusinessweekly.net/p/openai-statistics",
            },
            {
                "sector": "Revenue mix shift",
                "status": "Deployed",
                "deployment": "A deliberate shift from consumer subscriptions toward enterprise contracts "
                              "and developer API usage, with a new advertising line added during 2026.",
                "impact": "Enterprise now above 40% of revenue and on pace for parity with consumer; the ads "
                          "pilot reached $100M of annualised revenue in under six weeks",
                "source": "https://www.buildmvpfast.com/blog/openai-ipo-filing-valuation-s1-2026",
            },
            {
                "sector": "Capital markets",
                "status": "Announced",
                "deployment": "A $122B funding round at $852B post-money in March 2026 led by SoftBank and "
                              "Microsoft, followed by a confidential S-1 filed 8 June 2026 with Goldman "
                              "Sachs, Morgan Stanley and JPMorgan leading.",
                "impact": "Altman has reportedly treated any valuation below $1 trillion as a non-starter; "
                          "CFO Sarah Friar told staff OpenAI will be a public company in 2027",
                "source": "https://fortrovepartners.com/openai-ipo-timeline-valuation-tracker/",
            },
            {
                "sector": "Cost structure",
                "status": "Research finding",
                "deployment": "Compute and infrastructure commitments scaling ahead of revenue, under a "
                              "renegotiated Microsoft arrangement.",
                "impact": "Leaked audited 2025 figures show $13.1B booked revenue against a $20.9B operating "
                          "loss; projected cash burn revised up to roughly $27B in 2026 and ~$63B in 2027",
                "source": "https://tech-insider.org/openai-ipo-850-billion-valuation-2026/",
            },
        ],
        "customer_sentiment": "Adoption is the strongest of any AI vendor tracked here and it arrived "
                              "bottom-up rather than through procurement, which is both the strength and "
                              "the governance problem. The counter-signal is competitive: Anthropic "
                              "overtook OpenAI on revenue in April 2026 and on private valuation in May, "
                              "and Ramp data shows roughly 79% overlap in paying customers between the two "
                              "\u2014 enterprises are running both rather than standardising.",
        "sentiment_bull": [
            "Roughly 92% of the Fortune 500 use ChatGPT, and over a million business customers \u2014 unmatched penetration",
            "Revenue run rate moved from about $20B at end-2025 to over $40B by August 2026",
            "Enterprise is now above 40% of revenue and closing on parity with consumer, shifting the mix toward contracted spend",
            "The ads pilot reached $100M annualised in under six weeks, evidencing a genuinely new revenue line",
        ],
        "sentiment_bear": [
            "Leaked audited 2025 figures show $13.1B of booked revenue against a $20.9B operating loss \u2014 the run-rate numbers and the audited numbers are very different things",
            "Projected cash burn of roughly $27B in 2026 and ~$63B in 2027",
            "One analyst framing of the valuation is that it prices a monopoly outcome that does not yet exist",
            "A listing will reprioritise enterprise accounts over API-only customers, per reporting \u2014 a real consideration for production workloads",
            "Anthropic passed OpenAI on both revenue and private valuation during 2026",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 headcount is not reliably disclosed and no "
                              "employer-review data was gathered. One governance detail found: Altman "
                              "reportedly holds no equity in the company.",
        "glassdoor": None,
        "kpis": [
            ("2015", "Founded"),
            ("$40B+", "Run rate (Aug 2026)"),
            ("$852B", "Valuation (Mar 2026)"),
            ("~92%", "Fortune 500 using ChatGPT"),
            ("$20.9B", "2025 operating loss"),
        ],
        "notes": "OpenAI's reported figures vary widely by source and date, and the gap between annualised "
                 "run rate and audited booked revenue is large. Treat every number here as reported rather "
                 "than confirmed, and re-run before external use \u2014 particularly around the IPO.",
    },

    # =================================================================
    {
        "slug": "oracle",
        "name": "Oracle",
        "website": "https://www.oracle.com",
        "linkedin": "https://www.linkedin.com/company/oracle",
        "group": "Enterprise software",
        "category": "Database, ERP applications &amp; AI cloud infrastructure",
        "tagline": "Sold roughly a decade of future cloud capacity to the AI labs \u2014 now it has to "
                   "build it, and fund it",
        "founded": "1977",
        "hq": "Austin, Texas",
        "employees": "Approximately 162,000 (FY2026 10-K)",
        "ownership": "Public (NYSE: ORCL); founder Larry Ellison holds roughly 40.6% beneficial ownership",
        "revenue": "$67.4B in FY2026 (year ended 31 May 2026) with GAAP net income of $17.1B and GAAP EPS of "
                   "$5.83. Q4 revenue grew 21% to $19.2B, with OCI up 93% to $5.8B",
        "revenue_short": "$67.4B (FY26)",
        "offering": "Oracle Database, Fusion Cloud ERP and HCM applications, NetSuite, industry software "
                    "including Cerner health records, and Oracle Cloud Infrastructure \u2014 now the growth "
                    "engine and the reason for the capital programme.",
        "digital_twin": "No",
        "genai": "Yes (OCI AI infrastructure)",
        "buyer": "CFO and CIO for applications; AI labs and hyperscale customers for OCI capacity",
        "customers": ["OpenAI", "Meta", "NVIDIA"],
        "people": [
            {"name": "Clay Magouyrk", "title": "Co-Chief Executive Officer"},
            {"name": "Mike Sicilia", "title": "Co-Chief Executive Officer"},
            {"name": "Larry Ellison", "title": "Chairman &amp; Chief Technology Officer"},
            {"name": "Safra Catz", "title": "Executive Vice Chair of the Board"},
        ],
        "description": "Remaining performance obligations reached $638B at FY2026 close, up more than 6.5 "
                       "times from $98B two years earlier \u2014 signed, non-cancellable contracts giving "
                       "Oracle more than a decade of visibility in its infrastructure business, against "
                       "$67.4B of actual annual revenue.",
        "position_note": "The RPO figure is the single most striking number anywhere in this app, and it "
                         "cuts both ways. Oracle has effectively pre-sold roughly ten years of OCI capacity "
                         "to the most capital-rich AI companies in the world, which makes the revenue ramp "
                         "close to contracted if it can build and energise the capacity on schedule. The "
                         "funding gap is the risk: Oracle burned $55.7B of capex against $32B of operating "
                         "cash flow in FY2026, producing negative free cash flow of $23.7B, and guided to "
                         "roughly $70B of net capex in FY2027 alongside about $40B of combined debt and "
                         "equity raising. For an infrastructure investor that is a recognisable "
                         "shape \u2014 a contracted offtake book being funded ahead of construction \u2014 "
                         "and it should be assessed with the same discipline as any greenfield programme.",
        "gip_connection": "No publicly disclosed GIP relationship. Oracle's ERP and database footprint makes "
                          "it likely present at PortCo level for corporate systems. Separately, its data "
                          "centre build-out makes it a significant demand driver in digital infrastructure "
                          "\u2014 relevant to asset-side analysis, not just vendor management.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of ORCL only.",
        "use_cases": [
            {
                "sector": "AI cloud infrastructure",
                "status": "Deployed",
                "deployment": "Oracle Cloud Infrastructure sold to AI labs and hyperscale customers, with "
                              "most of the recent backlog coming from contracts where customers either "
                              "prepaid for GPUs or bought and supplied the hardware themselves.",
                "impact": "OCI revenue up 93% to $5.8B in Q4 FY2026; $67B of AI infrastructure contracts "
                          "signed in the quarter alone",
                "source": "https://erp.today/oracle-q4-2026-earnings-ai-cloud-backlog-funding/",
            },
            {
                "sector": "Contracted backlog",
                "status": "Deployed",
                "deployment": "Remaining performance obligations tracked as the central metric, built "
                              "through successive multi-billion-dollar contracts including the OpenAI and "
                              "Stargate commitment cluster and new commitments from Meta and NVIDIA.",
                "impact": "RPO grew from $138B at FY2025 close to $455B (Q1), $523B (Q2), $553B (Q3) and "
                          "$638B (Q4 FY2026) \u2014 up 363% year over year",
                "source": "https://houseblend.io/articles/pdfs/oracle-fy2026-results-netsuite-impact.pdf",
            },
            {
                "sector": "Capital programme",
                "status": "Announced",
                "deployment": "Capital expenditure to build the capacity behind the backlog, with "
                              "fixed-price contracts where component costs are known and pass-through "
                              "mechanisms where supply-chain or future cost uncertainty is high.",
                "impact": "$55.7B capex in FY2026 against $32B of operating cash flow \u2014 negative free "
                          "cash flow of $23.7B; ~$70B net capex guided for FY2027 with ~$40B of combined "
                          "debt and equity to be raised",
                "source": "https://www.optionstradingreport.com/2026/09/oracle-reports-tomorrow-a-638-billion-backlog-says-the-selloff-is-misreading-the-risk/",
            },
            {
                "sector": "Leadership transition",
                "status": "Deployed",
                "deployment": "Safra Catz moved to Executive Vice Chair in September 2025, with Clay "
                              "Magouyrk (previously President of OCI) and Mike Sicilia (previously President "
                              "of Industries) appointed co-CEOs. Hilary Maxon joined as CFO from Schneider "
                              "Electric.",
                "impact": "Puts the architect of OCI in the CEO seat as infrastructure becomes the growth "
                          "engine; the new CFO's background is in electrification and automation transformation",
                "source": "https://monteinvestments.substack.com/p/oracle-q4-2026-earnings-analysis-rpo-oci-data-center-ai-infrastructure",
            },
        ],
        "customer_sentiment": "Customer behaviour is the strongest evidence available and it is unusually "
                              "concrete: buyers are prepaying for GPUs or supplying hardware themselves to "
                              "secure OCI capacity. That is committed demand, not pipeline. Investor "
                              "sentiment is the opposite \u2014 shares fell about 10% after the Q4 results "
                              "on the capital-raising plan and were down nearly 20% across 2026, with the "
                              "stock near its lowest levels since late 2024 despite the backlog.",
        "sentiment_bull": [
            "$638B of signed, non-cancellable RPO gives more than a decade of infrastructure revenue visibility \u2014 unmatched in enterprise technology",
            "OCI grew 93% in Q4 FY2026, with customers prepaying or supplying their own hardware to secure capacity",
            "The co-CEO who built OCI now runs the company, and the new CFO comes from an electrification and automation background",
            "FY2026 GAAP net income of $17.1B means the core applications and database business still funds substantial profit",
        ],
        "sentiment_bear": [
            "Negative free cash flow of $23.7B in FY2026, with ~$70B of net capex and ~$40B of new debt and equity planned for FY2027",
            "Revenue recognition depends entirely on building and energising capacity on schedule \u2014 an execution risk, not a demand risk",
            "Extreme customer concentration: the backlog is dominated by a handful of AI labs whose own funding is not assured",
            "The stock fell roughly 20% across 2026 and about 10% after Q4 results, so public markets are discounting the backlog heavily",
            "Traditional on-premise revenue declined about 2% and is now a minority of sales \u2014 the legacy base is shrinking as the bet scales",
        ],
        "employee_sentiment": "Not covered in this pass beyond the FY2026 10-K headcount of approximately "
                              "162,000. No reliable employer-review data was gathered. Note the leadership "
                              "churn as context: a CEO transition, a new CFO hired externally, and a "
                              "wholesale strategic repositioning within twelve months.",
        "glassdoor": None,
        "kpis": [
            ("1977", "Founded"),
            ("~162,000", "Employees"),
            ("$67.4B", "FY2026 revenue"),
            ("$638B", "RPO backlog"),
            ("-$23.7B", "Free cash flow"),
        ],
    },

    # =================================================================
    {
        "slug": "perplexity",
        "name": "Perplexity",
        "website": "https://www.perplexity.ai",
        "linkedin": "https://www.linkedin.com/company/perplexity-ai",
        "group": "Frontier AI / LLM",
        "category": "AI answer engine &amp; agentic browser",
        "tagline": "A citation-first answer engine betting that owning the browsing surface matters more "
                   "than owning the model",
        "founded": "2022 (by Aravind Srinivas, Denis Yarats, Johnny Ho and Andy Konwinski)",
        "hq": "San Francisco, California",
        "employees": "Approximately 1,400 (third-party estimate), up from around 300 in 2024",
        "ownership": "Private. Valued at roughly $20B in a ~$200M round in September 2025, after earlier "
                     "2025 rounds at $14B and $18B; some trackers report marks above $21B in early 2026. "
                     "Total funding is reported between $1.2B and $1.72B depending on source. Backers "
                     "include NVIDIA, SoftBank, Jeff Bezos, IVP, Accel, NEA, Databricks and Bessemer",
        "revenue": "Annualised recurring revenue reported above $450M by March 2026, up from roughly $100M "
                   "in early 2025 and about $63M at end-2024; some trackers put it near $500M by "
                   "mid-2026. Over $200M of total recognised revenue in 2025",
        "revenue_short": "~$450\u2013500M ARR",
        "offering": "An answer engine returning synthesised, cited answers rather than links, sold through a "
                    "free tier, Pro at $20/month, Max at $200/month, enterprise plans, an API, and a "
                    "publisher revenue-share programme. Comet, a Chromium-based agentic browser, went free "
                    "worldwide in October 2025. Deep Research provides asynchronous multi-step research.",
        "digital_twin": "No",
        "genai": "Yes (built on third-party models)",
        "buyer": "Individual knowledge workers and research-heavy teams; enterprise plans are a newer line",
        "customers": [],
        "people": [
            {"name": "Aravind Srinivas", "title": "Co-Founder &amp; Chief Executive Officer"},
            {"name": "Denis Yarats", "title": "Co-Founder &amp; Chief Technology Officer"},
        ],
        "description": "Went from a $121M valuation in April 2023 to roughly $20B by September 2025, on "
                       "annualised revenue reported above $450M by March 2026. The strategic bet is Comet "
                       "\u2014 a free agentic browser \u2014 on the thesis that owning the browsing surface "
                       "beats owning the underlying model.",
        "position_note": "Perplexity does not train frontier models; it buys inference from Anthropic, "
                         "OpenAI and open-weight providers and competes on interface, citation discipline "
                         "and distribution. That is a real product advantage for research-shaped work "
                         "\u2014 compare X to Y, what does this paper say \u2014 and a structural "
                         "vulnerability, because its suppliers are also its competitors and its valuation "
                         "is priced where foundation labs trade. For a portfolio programme the honest "
                         "framing is that this is a productivity tool for research-heavy roles, not "
                         "enterprise infrastructure, and it should be evaluated against Gemini Enterprise "
                         "or Microsoft Copilot rather than alongside them.",
        "gip_connection": "No publicly disclosed GIP relationship. Relevance sits in the Individual "
                          "Productivity area of the reference model \u2014 research and analysis workflows "
                          "\u2014 rather than asset optimisation. Note that active publisher litigation "
                          "over content scraping is a live consideration for any enterprise deployment.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "Product distribution",
                "status": "Deployed",
                "deployment": "Comet, a Chromium-based agentic browser with a sidebar assistant integrating "
                              "search, task automation and multi-task management, made free worldwide in "
                              "October 2025 after launching to Max subscribers \u2014 a distribution "
                              "land-grab intended to be monetised later through subscriptions, enterprise "
                              "and publisher economics.",
                "impact": "Described by the company as its highest-stakes bet; extends the product from "
                          "answering questions to completing tasks, including shopping and transactions",
                "source": "https://valueaddvc.com/company/perplexity-ai",
            },
            {
                "sector": "Usage &amp; scale",
                "status": "Deployed",
                "deployment": "The core answer engine, used for research-shaped queries against live web "
                              "sources with citations attached.",
                "impact": "Monthly active users grew from 2 million in 2023 to 30 million by April 2025; "
                          "roughly 780 million monthly queries and about 30 million queries per day, growing "
                          "over 20% month over month",
                "source": "https://www.getpanto.ai/blog/perplexity-ai-statistics",
            },
            {
                "sector": "Revenue growth",
                "status": "Deployed",
                "deployment": "A four-line model: Pro and Max subscriptions, enterprise contracts, sponsored "
                              "answers against free-tier queries, and the Comet Plus publisher "
                              "revenue-share programme. Growth is increasingly usage-based rather than seat-based.",
                "impact": "ARR above $450M by March 2026, from roughly $100M in early 2025; over $200M of "
                          "recognised revenue in 2025",
                "source": "https://perplexityaimagazine.com/perplexity-hub/aravind-srinivas-perplexity-ceo/",
            },
            {
                "sector": "Research agents",
                "status": "Deployed",
                "deployment": "Deep Research, an asynchronous multi-step agent that runs extended research "
                              "tasks and returns sourced output \u2014 the shift from answer engine to "
                              "research platform.",
                "impact": "Positions the product against Google AI Overviews, ChatGPT Search and Microsoft "
                          "Copilot rather than against traditional search",
                "source": "https://perplexityaimagazine.com/perplexity-hub/aravind-srinivas-perplexity-ceo/",
            },
        ],
        "customer_sentiment": "The product has genuine loyalty for research-shaped queries, and roughly 74% "
                              "of desktop visits arriving directly rather than through referral suggests "
                              "habitual use rather than incidental traffic. The cautionary signal is that "
                              "monthly website visits declined from a November 2025 peak to about 138 "
                              "million by May 2026, ranking ninth globally in its category \u2014 so "
                              "engagement is deep but the user base is not obviously compounding against "
                              "much larger competitors.",
        "sentiment_bull": [
            "ARR grew from roughly $100M to above $450M in about a year, driven by agents and usage-based rather than seat-based pricing",
            "Citation-first design is a real differentiator for research work and for any use where output has to be verifiable",
            "Comet going free worldwide is a credible distribution strategy if owning the browsing surface proves to matter",
            "Cap table includes NVIDIA, SoftBank, Bezos, Databricks and Accel \u2014 strategic as well as financial backing",
        ],
        "sentiment_bear": [
            "Buys most frontier inference from Anthropic, OpenAI and open-weight providers \u2014 its suppliers are also its competitors",
            "Valued at roughly 40 to 100 times ARR depending on which figures are used, priced where foundation labs trade despite not training frontier models",
            "Active publisher lawsuits over content scraping are unresolved and material to enterprise adoption",
            "Website visits declined from their November 2025 peak; it has not dented Google's 90%+ search share",
            "Reported figures vary widely across trackers \u2014 valuation between $20B and $23B, funding between $1.2B and $1.72B, ARR between $200M and $500M",
        ],
        "employee_sentiment": "Not covered in this pass. Headcount is a third-party estimate of roughly "
                              "1,400, up from about 300 in 2024 \u2014 a near-fivefold increase in two "
                              "years, which is worth noting as a culture and delivery risk but is not "
                              "sentiment data. Treat as a gap.",
        "glassdoor": None,
        "kpis": [
            ("2022", "Founded"),
            ("~1,400", "Employees (est.)"),
            ("~$450M+", "ARR"),
            ("~$20B", "Valuation"),
            ("780M", "Monthly queries"),
        ],
        "notes": "Perplexity is private and publishes no audited financials. Valuation, funding and ARR "
                 "figures differ materially between trackers and the ranges are shown rather than a single "
                 "number. Verify directly before external use.",
    },
]
