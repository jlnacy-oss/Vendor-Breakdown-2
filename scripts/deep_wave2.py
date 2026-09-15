# -*- coding: utf-8 -*-
"""
deep_wave2.py — Research wave 2, completed 15 September 2026.

Anthropic, Aziro, Bain & Company, Booz Allen Hamilton, Boston Consulting Group.
"""

VENDORS = [
    # =================================================================
    {
        "slug": "anthropic",
        "name": "Anthropic",
        "website": "https://www.anthropic.com",
        "linkedin": "https://www.linkedin.com/company/anthropicresearch",
        "group": "Frontier AI / LLM",
        "category": "Frontier AI lab \u2014 enterprise-first",
        "tagline": "The fastest revenue ramp recorded in enterprise software, built on enterprise and "
                   "developer demand rather than consumer scale",
        "founded": "2021",
        "hq": "San Francisco, California (public benefit corporation)",
        "employees": "Not publicly disclosed",
        "ownership": "Private; confidential S-1 filed 1 June 2026 targeting an October 2026 Nasdaq listing",
        "revenue": "$47B annualised run rate confirmed in the May 2026 Series H announcement, up from "
                   "roughly $1B in December 2024, $5B in August 2025 and $30B in April 2026. A third-party "
                   "estimate (Sacra) puts July 2026 at $65B \u2014 treat that as an estimate, not a disclosure",
        "revenue_short": "$47B (May 2026)",
        "offering": "The Claude model family, sold through a direct API, Claude for Work, and the three "
                    "major clouds. Product line as of mid-2026: Claude, Claude Code (agentic coding), "
                    "Claude Cowork (desktop task automation for non-developers), Claude Design and Claude "
                    "Science. Primary infrastructure partner is AWS, with availability on Google Cloud "
                    "Vertex AI and Microsoft Azure.",
        "digital_twin": "No",
        "genai": "Yes (frontier models)",
        "buyer": "CIO, CTO and engineering leadership; increasingly line-of-business functions",
        "customers": ["Netflix", "Spotify", "KPMG", "L'Or\u00e9al", "Salesforce"],
        "people": [
            {"name": "Dario Amodei", "title": "Co-Founder &amp; Chief Executive Officer"},
            {"name": "Daniela Amodei", "title": "Co-Founder &amp; President"},
            {"name": "Krishna Rao", "title": "Chief Financial Officer"},
        ],
        "description": "Went from about $1B to $47B of annualised revenue in seventeen months, overtaking "
                       "OpenAI on revenue in April 2026 and on valuation in May. Roughly 80% of revenue comes "
                       "from business and API customers rather than consumers, which is the deliberate "
                       "strategic choice behind the ramp.",
        "position_note": "The enterprise-first thesis is the whole story here. Where competitors built "
                         "consumer scale first, Anthropic priced and packaged for businesses, and the "
                         "customer concentration reflects it \u2014 over 1,000 accounts spending more than "
                         "$1M a year, eight of the Fortune 10, and a documented lead in coding workloads. "
                         "The offsetting structural point is accounting: Anthropic books cloud-reseller "
                         "revenue gross, counting total end-customer spend as revenue and partner payouts "
                         "as expense, which inflates the headline against peers reporting net. Any "
                         "comparison to OpenAI's number needs that adjustment before it means anything.",
        "gip_connection": "No publicly disclosed GIP relationship. Relevance to the portfolio is via the "
                          "Individual Productivity and Corporate Functions Efficiency areas of the reference "
                          "model, and increasingly Asset Optimization where agentic workflows touch "
                          "operational data. Note the indirect exposure: Anthropic's compute agreements are "
                          "a material driver of data-centre and power demand, which touches digital "
                          "infrastructure assets on the investment side as well as the vendor side.",
        "blackrock_connection": "No publicly disclosed operating relationship. Anthropic is private; any "
                                "BlackRock exposure would be through private-markets vehicles rather than "
                                "index holdings, and is not publicly documented.",
        "use_cases": [
            {
                "sector": "Enterprise adoption",
                "status": "Deployed",
                "deployment": "Direct and API enterprise deployment across more than 300,000 business "
                              "customers, with usage expanding from single entry points (API access or "
                              "coding) into multiple organisational functions.",
                "impact": "Customers spending over $100K/yr up 7x year over year; 1,000+ accounts above "
                          "$1M/yr, doubled from 500+ in under two months; eight of the Fortune 10",
                "source": "https://axios.com/2026/02/12/anthropic-raises-30b-at-380b-valuation",
            },
            {
                "sector": "Software engineering",
                "status": "Deployed",
                "deployment": "Claude Code, the agentic coding product, generally available since May 2025 "
                              "and used well beyond coding \u2014 financial analysis, sales operations, "
                              "cybersecurity and research. Named enterprise users include Netflix, Spotify, "
                              "KPMG, L'Or\u00e9al and Salesforce.",
                "impact": "$500M run rate Sept 2025 \u2192 $1B Nov 2025 \u2192 $2.5B Feb 2026; enterprise is "
                          "over half of Claude Code revenue; reported 54% share of coding-specific LLM spend",
                "source": "https://sacra.com/c/anthropic/",
            },
            {
                "sector": "Compute &amp; infrastructure",
                "status": "Announced",
                "deployment": "Expanded AWS agreement (March 2026) for up to 5 gigawatts of current and "
                              "future Trainium capacity to train frontier models; Reuters reported in April "
                              "2026 that Google planned to invest up to $40B.",
                "impact": "Over 100,000 business customers running Claude on Amazon Bedrock as of April 2026",
                "source": "https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-aws-ai-q1-2026-earnings",
            },
            {
                "sector": "Capital markets",
                "status": "Announced",
                "deployment": "$30B Series G closed 12 February 2026 at a $380B post-money valuation, "
                              "followed by a $65B Series H on 28 May 2026 at $965B \u2014 surpassing OpenAI "
                              "to become the most valuable private AI company. Confidential S-1 filed 1 June 2026.",
                "impact": "Approximately $125\u2013132B raised in total across 18 rounds (source estimates vary)",
                "source": "https://axis-intelligence.com/anthropic-statistics/",
            },
        ],
        "customer_sentiment": "The clearest signal is expansion rather than acquisition: accounts that start "
                              "on one use case broaden into others, which is what drives the $1M+ cohort "
                              "doubling in under two months. Ramp card data also shows roughly 79% overlap "
                              "between Anthropic and OpenAI paying customers \u2014 enterprises are running "
                              "both rather than choosing, so wins here are rarely displacement wins and "
                              "budget is being split, not transferred.",
        "sentiment_bull": [
            "Revenue ramp has no precedent in enterprise software: ~$1B to $47B in seventeen months",
            "Enterprise mix of roughly 80% means revenue is contracted and expanding rather than consumer-churning",
            "Documented lead in coding workloads, the single largest paid LLM category",
            "Distribution across all three major clouds \u2014 AWS, Google Cloud and Azure \u2014 which no competitor has matched",
        ],
        "sentiment_bear": [
            "Gross revenue recognition on cloud-reseller channels inflates the headline relative to net-reporting peers \u2014 adjust before comparing",
            "Third-party run-rate figures ($65B for July 2026) circulate widely and are estimates, not disclosures; several widely-cited numbers trace back to modelling rather than the company",
            "Extreme capital intensity \u2014 roughly $125B+ raised \u2014 with compute commitments that must be serviced regardless of demand",
            "Revenue concentration in a fast-moving category where switching costs at the API layer are genuinely low",
            "A pending IPO on 2028-revenue underwriting assumptions puts execution risk on a public timetable",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 Anthropic does not disclose headcount and no "
                              "reliable employer-review data was gathered. Treat as a gap.",
        "glassdoor": None,
        "kpis": [
            ("2021", "Founded"),
            ("$47B", "Run rate (May 2026)"),
            ("$965B", "Valuation (Series H)"),
            ("300K+", "Business customers"),
            ("1,000+", "Accounts over $1M/yr"),
        ],
        "notes": "Chief Technology Officer was not confirmed in this pass and is deliberately omitted rather "
                 "than guessed. Figures move fast here \u2014 re-run this vendor before using any number in a "
                 "board paper, particularly around the IPO.",
    },

    # =================================================================
    {
        "slug": "aziro",
        "name": "Aziro",
        "website": "https://www.aziro.com/en",
        "linkedin": "https://www.linkedin.com/company/azirotech",
        "group": "SI / Consulting",
        "category": "Product engineering &amp; managed services",
        "tagline": "Mid-sized product engineering firm, rebranded from MSys Technologies in 2025 around an "
                   "AI-native positioning",
        "founded": "2007 (as MSys Technologies, Chennai); rebranded to Aziro, announced May\u2013June 2025",
        "hq": "Alpharetta, Georgia, USA; delivery centres in India, with presence in Australia, Malaysia and Vietnam",
        "employees": "~1,200",
        "ownership": "Private; founder-led",
        "revenue": "Approximately $292.5M per a third-party company directory. This figure is not "
                   "company-disclosed and implies revenue per head far above comparable firms of this size "
                   "\u2014 treat it as unverified and confirm directly in any diligence",
        "revenue_short": "~$292M (unverified)",
        "offering": "Infrastructure engineering, digital engineering, AI/ML engineering, DevSecOps and AIOps, "
                    "QA automation, hybrid and multi-cloud, and observability. Productised assets include "
                    "Aziron (an enterprise agent execution platform), CAWi.ai, a RAG application framework, "
                    "an AIOps accelerator and CodeLedger.",
        "digital_twin": "No",
        "genai": "Yes (services + Aziron platform)",
        "buyer": "Engineering and platform leadership at enterprises and ISVs",
        "customers": ["Nutanix"],
        "people": [
            {"name": "Sanjay Sehgal", "title": "Founder, Chairman &amp; Chief Executive Officer"},
        ],
        "description": "A niche engineering partner rather than a scale integrator \u2014 roughly 1,200 people "
                       "against Accenture's 799,000. Its stated focus is product engineering for enterprises, "
                       "high-growth ISVs and AI-first companies, with storage, infrastructure and QA as the "
                       "historical strengths carried over from the MSys years.",
        "position_note": "Aziro competes on depth in a narrow band \u2014 infrastructure and storage "
                         "engineering, QA automation, DevSecOps \u2014 not on breadth. For a portfolio "
                         "programme that makes it a specialist supplier for defined engineering work rather "
                         "than a transformation partner. The diligence caution is straightforward: nearly "
                         "all published case studies are anonymised and vendor-reported, the revenue figure "
                         "in circulation is a directory estimate rather than a disclosure, and the AI-native "
                         "positioning is roughly a year old, so the track record behind it is short.",
        "gip_connection": "No publicly disclosed GIP relationship. At this size, an engagement would most "
                          "plausibly arise at a single PortCo for a scoped engineering workstream rather "
                          "than as a portfolio-level supplier.",
        "blackrock_connection": "None identified.",
        "use_cases": [
            {
                "sector": "Networking \u2014 QA",
                "status": "Deployed (vendor-reported)",
                "deployment": "Local LLM-powered QA agents auto-generating, optimising and executing test "
                              "scripts across a networking company's software stack, with no internet "
                              "connectivity or cloud dependency.",
                "impact": "80% reduction in manual testing; 100% private on-premise inference",
                "source": "https://www.aziro.com/en",
            },
            {
                "sector": "Financial services",
                "status": "Deployed (vendor-reported)",
                "deployment": "Intelligent payment orchestration with cognitive workflows and embedded "
                              "anomaly detection across the financial lifecycle.",
                "impact": "60% improvement in processing speed; 100% accuracy in audit reconciliation",
                "source": "https://www.aziro.com/en",
            },
            {
                "sector": "Insurance",
                "status": "Deployed (vendor-reported)",
                "deployment": "Cloud-agnostic AI-native claims management platform with predictive triage, "
                              "automated case routing and built-in observability.",
                "impact": "40% reduction in infrastructure cost; 99.9% uptime with intelligent failover",
                "source": "https://www.aziro.com/en",
            },
            {
                "sector": "Data storage",
                "status": "Deployed (vendor-reported)",
                "deployment": "AI-powered observability layer predicting bottlenecks and dynamically "
                              "allocating resources using ML-based usage trends.",
                "impact": "30% gain in storage efficiency",
                "source": "https://www.aziro.com/en",
            },
        ],
        "customer_sentiment": "The only attributed customer voice found in this pass is a Nutanix management "
                              "testimonial praising responsiveness on CVE remediation. Every other case study "
                              "is anonymised by industry. That is normal for a firm this size but it means "
                              "there is little independent evidence to weigh \u2014 reference calls would "
                              "carry more weight here than published material.",
        "sentiment_bull": [
            "Deep specialisation in infrastructure, storage and QA engineering \u2014 areas the large integrators staff thinly",
            "Founder-led and small enough that senior attention on an engagement is credible rather than contractual",
            "ISO 27001 certified and Great Place To Work certified",
            "Productised assets (Aziron, CodeLedger, AIOps accelerator) rather than pure staff augmentation",
        ],
        "sentiment_bear": [
            "Revenue figure in circulation is a third-party directory estimate and looks high against a ~1,200 headcount \u2014 verify directly",
            "Almost all case-study impact figures are vendor-reported and anonymised, with no independent validation available",
            "The AI-native brand is about a year old; the underlying business is a 2007-vintage engineering services firm",
            "At this scale, key-person and concentration risk are real, and surge capacity is limited",
        ],
        "employee_sentiment": "Great Place To Work certified, per the company's own announcements. No "
                              "independent employer-review data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("2007", "Founded"),
            ("~1,200", "Employees"),
            ("~$292M", "Revenue (unverified)"),
            ("2025", "Rebranded from MSys"),
            ("5", "Countries"),
        ],
    },

    # =================================================================
    {
        "slug": "bain",
        "name": "Bain & Company",
        "website": "https://www.bain.com",
        "linkedin": "https://www.linkedin.com/company/bain-and-company",
        "group": "SI / Consulting",
        "category": "Strategy consultancy",
        "tagline": "The MBB firm closest to private equity \u2014 and the one that discloses least about itself",
        "founded": "1973",
        "hq": "Boston, Massachusetts",
        "employees": "17,519 at the end of 2025 per Bain's own externally assured GRI sustainability report. "
                     "Figures of 19,000 and 22,000 circulate widely and come from firm announcements and "
                     "Wikipedia respectively",
        "ownership": "Private partnership",
        "revenue": "Not currently disclosed. The last self-reported figure was $16B in the 2023 ESG report. "
                   "The $14B (2025) figure on Wikipedia cites a Forbes profile that actually says $7.5B \u2014 "
                   "that discrepancy has been copied into several comparison articles",
        "revenue_short": "Not disclosed",
        "offering": "Strategy, performance improvement and organisational consulting, with an unusually large "
                    "private equity practice covering commercial due diligence, value creation planning and "
                    "portfolio operations.",
        "digital_twin": "No",
        "genai": "Advisory",
        "buyer": "CEO, board and private equity deal teams",
        "customers": [],
        "people": [
            {"name": "Christophe De Vusser", "title": "Worldwide Managing Partner, CEO &amp; Chairman of the Board"},
            {"name": "Manny Maceda", "title": "Chair"},
            {"name": "Orit Gadiesh", "title": "Chair Emeritus"},
        ],
        "description": "One of the three strategy firms, and the one with the deepest private equity "
                       "franchise \u2014 which makes it the most likely of the MBB set to already be inside "
                       "GIP's diligence workflows. It is also the least transparent: it stopped publishing "
                       "revenue and uses at least two inconsistent headcount methodologies.",
        "position_note": "Bain's PE practice is the relevant asset for an infrastructure fund \u2014 "
                         "commercial due diligence and post-close value creation are its home ground, and it "
                         "is likely already engaged somewhere in the deal pipeline. On AI specifically the "
                         "public record is thin next to BCG, which disclosed 25% of revenue from AI work, and "
                         "McKinsey, reported at around 40% from AI and technology advisory. Bain has "
                         "published no comparable figure. That is an absence of disclosure, not evidence of "
                         "absence of capability \u2014 but it does mean the capability has to be assessed "
                         "through references rather than published numbers.",
        "gip_connection": "No publicly disclosed GIP relationship. Given Bain's private equity franchise, "
                          "check internally before assuming a clean slate \u2014 an existing commercial "
                          "diligence relationship at deal level is plausible and would not be public.",
        "blackrock_connection": "None publicly disclosed.",
        "use_cases": [
            {
                "sector": "Firm disclosure",
                "status": "Research finding",
                "deployment": "Bain stopped publishing revenue after the 2023 ESG report ($16B, 45,100 "
                              "colleagues, 68 countries, 4,100 clients). Its externally assured GRI index "
                              "gives a different and more conservative headcount series: 18,385 (2022), "
                              "18,254 (2023), 17,266 (2024), 17,519 (2025).",
                "impact": "A 5% headcount decline in 2024 was attributed by Bain to a hiring freeze and "
                          "increased turnover",
                "source": "https://strategyu.co/mckinsey-bcg-bain-comparison/",
            },
            {
                "sector": "Peer benchmark",
                "status": "Research finding",
                "deployment": "MBB combined 2025 revenue is estimated at roughly $36\u201340B across about "
                              "97,000 consultants, with revenue per consultant two to three times that of "
                              "Big Four broad consulting.",
                "impact": "Positions Bain as the smallest of the three by headcount",
                "source": "https://www.roadtooffer.com/blog/top-consulting-firms",
            },
        ],
        "customer_sentiment": "Not assessed in this pass. Bain's client work is almost entirely "
                              "confidential and it publishes few attributable case studies, so there is no "
                              "public evidence base to summarise.",
        "sentiment_bull": [
            "The deepest private equity practice of the three strategy firms \u2014 directly relevant to how GIP works",
            "Smallest of MBB by headcount, which usually means more senior time per engagement",
            "Revenue per consultant across MBB runs two to three times Big Four broad consulting, consistent with a premium positioning",
        ],
        "sentiment_bear": [
            "Discloses less than any peer in this set: no current revenue figure, and two inconsistent headcount methodologies",
            "Widely-cited figures are unreliable \u2014 the $14B on Wikipedia traces to a source that says $7.5B",
            "Headcount fell 5% in 2024 on a hiring freeze and elevated turnover, and 2025 barely recovered",
            "No published AI revenue figure while both BCG and McKinsey have put numbers on the table",
        ],
        "employee_sentiment": "Not covered in this pass. The only firm-sourced signal is the 2024 hiring "
                              "freeze and elevated turnover disclosed in its own sustainability reporting.",
        "glassdoor": None,
        "kpis": [
            ("1973", "Founded"),
            ("17,519", "Employees (2025, GRI)"),
            ("n/d", "Revenue"),
            ("64", "Office locations"),
            ("$16B", "Last disclosed (2023)"),
        ],
        "notes": "This is the thinnest white page in the set, and deliberately so. Bain's public disclosure "
                 "is materially weaker than every peer here. Rather than fill the gaps with third-party "
                 "estimates that do not survive checking, the page records what is verifiable and flags the "
                 "rest as unknown.",
    },

    # =================================================================
    {
        "slug": "booz-allen",
        "name": "Booz Allen Hamilton",
        "website": "https://www.boozallen.com",
        "linkedin": "https://www.linkedin.com/company/booz-allen-hamilton",
        "group": "SI / Consulting",
        "category": "Government &amp; critical-infrastructure technology",
        "tagline": "The dominant US national-security technology firm, pivoting into commercial critical "
                   "infrastructure after its hardest year as a public company",
        "founded": "1914",
        "hq": "McLean, Virginia",
        "employees": "31,500 as of 31 March 2026, down 12% year over year",
        "ownership": "Public (NYSE: BAH)",
        "revenue": "$11.2B in FY2026 (year ended 31 March 2026), down 6.4%; adjusted EBITDA $1.23B; record "
                   "backlog of $38B with a trailing twelve-month book-to-bill of 1.1x",
        "revenue_short": "$11.2B (FY26)",
        "offering": "Mission technology for US federal agencies \u2014 AI, cyber, defence technology and "
                    "digital transformation \u2014 delivered increasingly as products and outcome-based "
                    "contracts rather than staffed services. Expanding into commercial critical "
                    "infrastructure through the Defy Security acquisition.",
        "digital_twin": "Partner-delivered",
        "genai": "Yes (agentic cyber and mission systems)",
        "buyer": "Federal agency mission owners; increasingly commercial critical-infrastructure CISOs",
        "customers": [],
        "people": [
            {"name": "Horacio Rozanski", "title": "Chairman, President &amp; Chief Executive Officer"},
        ],
        "description": "The largest pure-play US government technology firm, with deeper operational "
                       "experience in critical national infrastructure than any commercial consultancy. "
                       "FY2026 was, in its CEO's words, the most challenging year it has faced as a public "
                       "company \u2014 revenue down 6.4%, headcount down 12% \u2014 while backlog hit a record $38B.",
        "position_note": "Of every firm in this set, Booz Allen has the most directly transferable "
                         "experience in operating and defending critical infrastructure, because that is "
                         "what federal mission work is. The strategic shift underway makes it more relevant "
                         "to an infrastructure portfolio, not less: the Defy Security acquisition is "
                         "explicitly aimed at scaling cyber product sales into commercial critical "
                         "infrastructure, and it has built partnerships with NVIDIA, AWS, OpenAI and venture "
                         "firms to pull commercial technology into that work. The caveat is cultural as much "
                         "as commercial \u2014 a federal contracting operating model does not always "
                         "translate cleanly to a PE-owned asset's pace or cost expectations.",
        "gip_connection": "No publicly disclosed GIP relationship. Its stated push into commercial critical "
                          "infrastructure cyber makes it a plausible inbound approach rather than an outbound "
                          "search \u2014 and its work sits closest to the Technology / Governance / Security "
                          "prerequisite in the reference model.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of BAH only.",
        "use_cases": [
            {
                "sector": "Critical infrastructure \u2014 cyber",
                "status": "Announced",
                "deployment": "Acquisition of Defy Security to scale cyber product sales and expand reach "
                              "into the commercial critical-infrastructure market, alongside a shift toward "
                              "agentic AI \u2014 automated agents embedded in cyber and defence offerings to "
                              "counter faster-moving offensive cyber threats.",
                "impact": "90% increase in Other Transaction Authority proposal submissions, a leading "
                          "indicator of the shift to non-linear, product-led growth",
                "source": "https://finance.yahoo.com/markets/stocks/articles/booz-allen-hamilton-holding-corporation-123000634.html",
            },
            {
                "sector": "AI partnerships",
                "status": "Announced",
                "deployment": "Partnership with OpenAI to advance AI across national security and critical "
                              "infrastructure missions, adding to an existing network of technology "
                              "partnerships with NVIDIA, AWS and venture capital firms.",
                "impact": "Positions commercial frontier models inside accredited federal mission environments",
                "source": "https://www.businesswire.com/news/home/20260522055202/en/Booz-Allen-Hamilton-Announces-Fourth-Quarter-and-Full-Year-Fiscal-2026-Results",
            },
            {
                "sector": "Federal AI adoption",
                "status": "Research finding",
                "deployment": "A Booz Allen survey published in its Velocity series found a widening gap "
                              "between deployment of agentic AI systems in federal agencies and trust in them.",
                "impact": "Frames the firm's accreditation and assurance work as the commercial opportunity",
                "source": "https://www.businesswire.com/news/home/20260522055202/en/Booz-Allen-Hamilton-Announces-Fourth-Quarter-and-Full-Year-Fiscal-2026-Results",
            },
            {
                "sector": "Business model",
                "status": "Deployed",
                "deployment": "Deliberate decoupling of headcount from revenue \u2014 monetising "
                              "intellectual property and shifting mix toward fixed-price and outcome-based "
                              "contracts, supported by a cost reduction programme.",
                "impact": "~$150M of annual cost reduction, with margin benefit expected in FY2027",
                "source": "https://seekingalpha.com/news/4542196-booz-allen-narrows-revenue-guidance-to-11_3b-11_4b-while-advancing-outcome-based-contracts",
            },
        ],
        "customer_sentiment": "Demand signal and revenue have diverged, which is unusual and worth "
                              "understanding before drawing conclusions. Backlog hit a record $38B with a "
                              "1.1x book-to-bill while revenue fell 6.4% \u2014 the gap is procurement and "
                              "funding timing, including roughly $50M of revenue and $20M of profit lost to "
                              "the government shutdown, not customers leaving. National security demand is "
                              "robust; the civil business is where the damage sits, though management now "
                              "reports an improving pipeline.",
        "sentiment_bull": [
            "Record $38B backlog and 1.1x book-to-bill despite a 6.4% revenue decline \u2014 demand is intact",
            "Net income rose to $205M in Q4 FY2026 even as revenue fell, on cost discipline and contract execution",
            "Unmatched operational experience in critical national infrastructure, now being pointed at commercial buyers",
            "Partnership network (NVIDIA, AWS, OpenAI) gives access to frontier technology inside accredited environments",
        ],
        "sentiment_bear": [
            "FY2026 revenue fell 6.4% to $11.2B and Q4 fell 6.4% \u2014 described by the CEO as the most challenging year as a public company",
            "Headcount down 12% year over year, which constrains near-term delivery capacity",
            "Revenue remains overwhelmingly dependent on US federal budgets and procurement timing \u2014 a single shutdown moved $110M around",
            "CFO transition during the downturn (Matt Calderone departed 1 February 2026) adds execution noise",
            "The commercial critical-infrastructure pivot is early; Defy Security is a small acquisition against an $11B base",
        ],
        "employee_sentiment": "The verifiable signal is structural rather than sentiment-based: headcount "
                              "fell 12% in FY2026 through a delayering and cost reduction programme, and "
                              "management has stated explicitly that it intends to break the historical link "
                              "between headcount growth and revenue growth. No independent employer-review "
                              "data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1914", "Founded"),
            ("31,500", "Employees"),
            ("$11.2B", "FY2026 revenue"),
            ("$38B", "Backlog (record)"),
            ("1.1x", "Book-to-bill"),
        ],
    },

    # =================================================================
    {
        "slug": "bcg",
        "name": "Boston Consulting Group",
        "website": "https://www.bcg.com",
        "linkedin": "https://www.linkedin.com/company/boston-consulting-group",
        "group": "SI / Consulting",
        "category": "Strategy consultancy with an in-house build arm",
        "tagline": "The MBB firm that has put a number on its AI business \u2014 and built an engineering "
                   "arm to deliver it",
        "founded": "1963 (by Bruce Henderson)",
        "hq": "Boston, Massachusetts",
        "employees": "33,500 at the end of 2025, up from about 33,000",
        "ownership": "Private partnership",
        "revenue": "$14.4B in 2025, up 7% from $13.5B in 2024 \u2014 a 22nd consecutive year of growth, though "
                   "a slower pace than the 10% recorded the prior year",
        "revenue_short": "$14.4B (2025)",
        "offering": "Strategy and transformation consulting, paired with BCG X \u2014 an in-house build arm "
                    "that develops bespoke AI solutions and deploys industry platforms such as Auto AI, "
                    "Retail AI and Deep Customer Engagement AI directly into client systems. The BCG X AI "
                    "Science Institute launched in 2025.",
        "digital_twin": "Client-specific builds",
        "genai": "Yes (BCG X)",
        "buyer": "CEO, board and transformation sponsors",
        "customers": ["IBM", "Reckitt", "Foxconn"],
        "people": [
            {"name": "Christoph Schweizer", "title": "Chief Executive Officer"},
            {"name": "Rich Lesser", "title": "Global Chair (CEO 2013\u20132021)"},
        ],
        "description": "$14.4B of 2025 revenue across 33,500 people, with AI and technology services now "
                       "over 40% of the total and AI-specific work at 25% \u2014 roughly $3.6B. It is the "
                       "first of the strategy firms to publish that figure, which makes it the benchmark "
                       "the others get measured against.",
        "position_note": "BCG's distinguishing move is structural, not rhetorical: BCG X means it builds and "
                         "deploys into client systems rather than handing over a recommendation, which puts "
                         "it in genuine overlap with systems integrators on delivery while retaining "
                         "strategy-firm pricing. Its stated 10-20-70 allocation \u2014 10% algorithms, 20% "
                         "technology and data, 70% people and process \u2014 is a useful framing for anyone "
                         "planning portfolio AI adoption, and matches the reference model's emphasis on "
                         "adoption and change over model selection. For an infrastructure portfolio the "
                         "caution is sector fit: its published AI platforms are automotive, retail and "
                         "customer engagement, not asset-heavy infrastructure.",
        "gip_connection": "No publicly disclosed GIP relationship. BCG's published AI platform portfolio "
                          "skews to consumer-facing sectors, so relevance to energy, transport, digital and "
                          "water assets would need to be tested rather than assumed.",
        "blackrock_connection": "None publicly disclosed.",
        "use_cases": [
            {
                "sector": "Applied AI \u2014 enterprise",
                "status": "Deployed",
                "deployment": "BCG X builds bespoke AI solutions and embeds industry-specific platforms "
                              "(Auto AI, Retail AI, Deep Customer Engagement AI) directly into client "
                              "systems, with named applied-AI clients including IBM, Reckitt and Foxconn.",
                "impact": "AI-related work reached 25% of 2025 revenue \u2014 roughly $3.6B \u2014 with AI "
                          "services growing 25% year over year",
                "source": "https://www.bcg.com/press/23april2026-bcg-revenue-22nd-consecutive-year-growth",
            },
            {
                "sector": "Delivery methodology",
                "status": "Deployed",
                "deployment": "The 10-20-70 approach allocates 10% of effort to algorithms, 20% to "
                              "technology and data, and 70% to people and process \u2014 an explicit "
                              "position that AI programmes fail on adoption rather than modelling.",
                "impact": "Adopted as the firm's standard framing across AI engagements",
                "source": "https://www.cityam.com/ai-focused-services-make-up-40-per-cent-of-bcgs-2025-revenue/",
            },
            {
                "sector": "Internal AI adoption",
                "status": "Deployed",
                "deployment": "Firm-wide AI upskilling with employees using AI tools daily, and a technical "
                              "bench expanded through hiring of AI engineers, data scientists and IT architects.",
                "impact": "Nearly 4,000 BCG employees actively developing and scaling AI workflows through "
                          "advanced coding and automation; headcount grew by 500 to 33,500",
                "source": "https://www.prnewswire.com/news-releases/bcg-reports-14-4-billion-in-revenue-marking-22nd-consecutive-year-of-growth-302751073.html",
            },
            {
                "sector": "Research capability",
                "status": "Announced",
                "deployment": "BCG X AI Science Institute, launched in 2025 to advance frontier applications "
                              "across industries at the intersection of science, technology and business.",
                "impact": "Extends the build arm from delivery into applied research",
                "source": "https://www.bcg.com/press/23april2026-bcg-revenue-22nd-consecutive-year-growth",
            },
        ],
        "customer_sentiment": "Twenty-two consecutive years of growth and expansion across all regions is "
                              "the strongest available proxy, since BCG publishes few attributable client "
                              "outcomes. Named applied-AI clients \u2014 IBM, Reckitt, Foxconn \u2014 are "
                              "disclosed without associated metrics, so the impact claims rest on the firm's "
                              "own framing rather than independent measurement.",
        "sentiment_bull": [
            "First strategy firm to publish an AI revenue figure \u2014 25% of $14.4B, about $3.6B \u2014 which sets the benchmark for the category",
            "BCG X provides genuine build-and-deploy capability rather than recommendation-only consulting",
            "22nd consecutive year of growth with expansion across all regions",
            "Roughly 4,000 employees actively building AI workflows, and LinkedIn's AI Talent Maturity Index places its workforce among the leaders",
        ],
        "sentiment_bear": [
            "Growth slowed to 7% in 2025 from 10% in 2024, while AI revenue grew 25% \u2014 implying the non-AI business is close to flat",
            "Headcount grew only 500 in a year in which AI revenue grew 25%, which raises a question about delivery capacity or leverage",
            "Published AI platforms are automotive, retail and customer engagement \u2014 no infrastructure-sector platform is disclosed",
            "Client impact claims are firm-reported without independent measurement",
            "As a private partnership it discloses selectively; the AI figure is published, the underlying margin is not",
        ],
        "employee_sentiment": "The firm reports daily AI tool use across staff and heavy investment in AI "
                              "upskilling, with hiring concentrated in technical roles. No independent "
                              "employer-review data was gathered in this pass, so this reflects the firm's "
                              "own account.",
        "glassdoor": None,
        "kpis": [
            ("1963", "Founded"),
            ("33,500", "Employees"),
            ("$14.4B", "2025 revenue"),
            ("25%", "Revenue from AI"),
            ("40%+", "AI &amp; tech services"),
        ],
    },
]
