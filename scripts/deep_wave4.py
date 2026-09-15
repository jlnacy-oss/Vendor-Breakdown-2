# -*- coding: utf-8 -*-
"""
deep_wave4.py — Research wave 4, completed 15 September 2026.

DXC Technology, EY, Google, HCLTech, IBM Consulting.
"""

VENDORS = [
    # =================================================================
    {
        "slug": "dxc",
        "name": "DXC Technology",
        "website": "https://dxc.com",
        "linkedin": "https://www.linkedin.com/company/dxctechnology",
        "group": "SI / Consulting",
        "category": "Managed IT services &amp; application operations",
        "tagline": "A shrinking managed-services incumbent trying to convert legacy estate ownership into "
                   "an AI repositioning",
        "founded": "2017 (merger of CSC and the HPE Enterprise Services business)",
        "hq": "Ashburn, Virginia",
        "employees": "Approximately 131,000 as at the February 2024 CEO announcement; a current figure was "
                     "not confirmed in this pass",
        "ownership": "Public (NYSE: DXC)",
        "revenue": "Approximately $12.6B in FY2026 (year ended 31 March 2026), derived from the four "
                   "reported quarters and consistent with guidance of $12.67\u201312.81B. Revenue declined "
                   "every quarter on an organic basis \u2014 4.3%, 4.2%, 4.3% and 6.6%",
        "revenue_short": "~$12.6B (FY26)",
        "offering": "Managed infrastructure, application services, cloud operations, security, insurance "
                    "software and analytics \u2014 largely running estate that clients have outsourced. "
                    "Now organised into a Core Track (the existing business) and a Fast Track (new "
                    "differentiated offerings), under an Xponential AI framework, with OASIS as its AI-based "
                    "orchestration platform.",
        "digital_twin": "No",
        "genai": "Yes (OASIS, Xponential AI)",
        "buyer": "CIO and infrastructure operations leadership",
        "customers": [],
        "people": [
            {"name": "Raul Fernandez", "title": "President &amp; Chief Executive Officer"},
            {"name": "David Herzog", "title": "Chairman of the Board"},
        ],
        "description": "The smallest and weakest-performing of the large integrators tracked here. Revenue "
                       "has declined organically in every quarter of FY2026 and Q4 EBIT turned negative at "
                       "-$39M. What it does have is deep ownership of client legacy estate \u2014 including "
                       "the Hogan core banking code \u2014 which it is trying to monetise through AI-fronted "
                       "interfaces rather than replacement.",
        "position_note": "DXC's relevance is specific and narrow: it holds and maintains legacy systems that "
                         "other vendors would propose replacing. The Hogan strategy is the clearest example "
                         "\u2014 rather than reviving or rebuilding the core banking platform, it is being "
                         "extended through lightweight AI APIs, on the argument that owning and maintaining "
                         "the code gives DXC a position no one else can take. For an infrastructure "
                         "portfolio that framing matters wherever a PortCo runs unglamorous but critical "
                         "legacy systems. The caution is financial rather than technical: this is a "
                         "declining business and vendor viability belongs in any diligence.",
        "gip_connection": "No publicly disclosed GIP relationship. The likeliest route in is an inherited "
                          "managed-services contract at a PortCo rather than a new selection. Given the "
                          "revenue trajectory, contract renewal and service continuity are worth reviewing "
                          "wherever DXC is already embedded.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of DXC only.",
        "use_cases": [
            {
                "sector": "Financial services \u2014 legacy modernisation",
                "status": "Announced",
                "deployment": "Extension of the Hogan core banking platform through lightweight, AI "
                              "API-centric interfaces rather than replacement. Fernandez has framed this as "
                              "an extension rather than a revival, arguing that DXC's ownership and "
                              "maintenance of the underlying code is the differentiator.",
                "impact": "Positioned to let banks offer new services at a fraction of the cost and speed of "
                          "rebuild; existing customers were expected to be named in the new fiscal year",
                "source": "https://s27.q4cdn.com/120381974/files/doc_financials/2026/q2/Transcript-DXC-Q2-2026-Earnings-Call.pdf",
            },
            {
                "sector": "AI orchestration",
                "status": "Announced",
                "deployment": "Launch of OASIS, an AI-based orchestration platform, alongside the "
                              "Xponential AI framework and the formal split into Core Track and Fast Track "
                              "operating models.",
                "impact": "Positioned as the vehicle for repositioning DXC for AI-driven enterprise IT",
                "source": "https://investors.dxc.com/investor-news/news-details/2026/DXC-Technology-Reports-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx",
            },
            {
                "sector": "Financial performance",
                "status": "Deployed",
                "deployment": "Margin and cash discipline pursued while the top line declines \u2014 the "
                              "central management priority across FY2026.",
                "impact": "Q3 EBIT of $179M at a 5.6% margin, up 22.6%; free cash flow guidance raised to "
                          "~$650M from ~$600M; but Q4 EBIT fell to -$39M",
                "source": "https://investors.dxc.com/investor-news/news-details/2026/DXC-Technology-Reports-Third-Quarter-Fiscal-Year-2026-Results/default.aspx",
            },
            {
                "sector": "Commercial momentum",
                "status": "Deployed",
                "deployment": "Bookings tracked as the leading indicator of the turnaround, with mixed "
                              "results across the year.",
                "impact": "Q3 book-to-bill of 1.20x with trailing twelve-month at 1.13x in one segment, but "
                          "Q3 bookings themselves declined 6% and Q2 book-to-bill was 0.85",
                "source": "https://investors.dxc.com/investor-news/news-details/2026/DXC-Technology-Reports-Third-Quarter-Fiscal-Year-2026-Results/default.aspx",
            },
        ],
        "customer_sentiment": "The honest read is that the customer base is shrinking. Organic revenue fell "
                              "in every quarter of FY2026 and the decline steepened to 6.6% in Q4. "
                              "Management points to bookings growth and improved client connection; the "
                              "bookings data is inconsistent quarter to quarter, and Fernandez acknowledged "
                              "in Q4 that top-line performance fell short. DXC publishes no attributable "
                              "client outcomes.",
        "sentiment_bull": [
            "Deep ownership of client legacy estate, including source code for platforms like Hogan, which competitors cannot replicate",
            "Free cash flow guidance raised during the year to approximately $650M despite declining revenue",
            "Adjusted EBIT margin guidance of 7.0\u20138.0% held through the year, with Q3 EBIT up 22.6%",
            "A clear and specific strategic framing \u2014 Core Track and Fast Track \u2014 rather than a generic AI narrative",
        ],
        "sentiment_bear": [
            "Organic revenue declined in all four quarters of FY2026, worsening to 6.6% in Q4",
            "Q4 EBIT turned negative at -$39M, a 111% year-over-year swing",
            "Bookings are inconsistent \u2014 Q2 book-to-bill of 0.85, Q3 bookings down 6% \u2014 so the turnaround is not yet visible in forward demand",
            "Current headcount was not disclosed in the results reviewed; the most recent confirmed figure is roughly 131,000 from February 2024",
            "Smallest of the large integrators tracked here, and the only one with a declining top line \u2014 vendor viability is a legitimate diligence question",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 no current headcount disclosure or reliable "
                              "employer-review data was gathered. Given a multi-year revenue decline, treat "
                              "delivery-team stability as something to test directly rather than assume.",
        "glassdoor": None,
        "kpis": [
            ("2017", "Founded"),
            ("~$12.6B", "FY2026 revenue"),
            ("-6.6%", "Q4 organic growth"),
            ("~$650M", "Free cash flow"),
            ("1.13x", "TTM book-to-bill"),
        ],
        "notes": "Full-year revenue is derived from the four reported quarters rather than taken from a "
                 "single disclosure, and headcount could not be confirmed for FY2026. Both are flagged on "
                 "the page rather than presented as company figures.",
    },

    # =================================================================
    {
        "slug": "ey",
        "name": "EY",
        "website": "https://www.ey.com",
        "linkedin": "https://www.linkedin.com/company/ernstandyoung",
        "group": "SI / Consulting",
        "category": "Big Four professional services network",
        "tagline": "Using itself as the first client for AI \u2014 the Client Zero model \u2014 with 30% "
                   "AI revenue growth to show for it",
        "founded": "1989 (merger of Ernst &amp; Whinney and Arthur Young &amp; Co.; oldest component dates to 1849)",
        "hq": "London, United Kingdom (Ernst &amp; Young Global Limited; a network of member firms)",
        "employees": "Approximately 406,209 at FY2025 year-end, up 3.4%. By service line: Assurance 130,898 "
                     "(+2.6%), Consulting 124,238 (+5.4%), Tax 75,314 (+3.0%), practice support 50,723 "
                     "(+3.7%), Strategy and Transactions 25,036 (-1.8%)",
        "ownership": "Private company limited by guarantee; a network of member firms",
        "revenue": "$53.2B combined global revenue for FY2025 (year ended June 2025), up 4.0% in local "
                   "currency, with a FY20\u2013FY25 compound annual growth rate of 8.2%. EMEIA grew fastest "
                   "at 5.5% to $21.1B; the Americas grew 3.3% to $24.7B; Asia-Pacific grew 2.3% to $7.4B",
        "revenue_short": "$53.2B (FY25)",
        "offering": "Assurance, tax, consulting, strategy and transactions (through EY-Parthenon), legal and "
                    "managed services, delivered by member firms. The AI programme runs under the EY All in "
                    "strategy, with AI-powered solutions, industry alliances and AI governance frameworks "
                    "as named service lines.",
        "digital_twin": "No",
        "genai": "Yes (Client Zero model)",
        "buyer": "CEO, CFO, audit committee and transformation sponsors",
        "customers": [],
        "people": [
            {"name": "Janet Truncale", "title": "Global Chair &amp; Chief Executive Officer"},
        ],
        "description": "The third-largest Big Four network by revenue, and the one with the most distinctive "
                       "AI operating model. Truncale, the first woman to lead a Big Four firm, runs a Client "
                       "Zero approach \u2014 EY applies AI to its own processes first, then sells the "
                       "learnings. AI-related revenue grew 30% in FY2025.",
        "position_note": "Client Zero is a genuinely differentiated pitch and the numbers behind it are "
                         "concrete: more than 100 AI applications deployed internally, over 50,000 AI agents "
                         "in development, and more than 15,000 EY people working on AI-led client projects. "
                         "The credible version of that claim is that EY can show a buyer what a deployment "
                         "looked like inside a 400,000-person organisation before asking them to run one. "
                         "The structural caveat is the same as Deloitte's and sharper here: EY is a network "
                         "of member firms, the global figures are aggregated, and audit independence "
                         "restricts what consulting work can follow an audit relationship. EY's central "
                         "structure has also been under cost pressure since Project Everest collapsed in 2023.",
        "gip_connection": "No publicly disclosed GIP relationship. Note that EY US selected CrowdStrike's "
                          "Falcon Next-Gen SIEM as the foundation for its global cybersecurity managed "
                          "services \u2014 relevant if both vendors come up in the same conversation. As "
                          "with Deloitte, check for an existing audit relationship at fund or PortCo level "
                          "before scoping consulting work.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "Internal AI transformation",
                "status": "Deployed",
                "deployment": "The Client Zero model \u2014 EY applies AI to its own processes and platforms "
                              "first, then applies those learnings to client enterprise-wide "
                              "transformations. Truncale's signature strategy.",
                "impact": "More than 100 AI applications deployed and more than 50,000 AI agents in development",
                "source": "https://fortune.com/ranking/most-powerful-women/2026/janet-truncale/",
            },
            {
                "sector": "AI services",
                "status": "Deployed",
                "deployment": "AI-led client work spanning enterprise-wide transformations through to AI "
                              "governance frameworks supporting responsible implementation, delivered "
                              "through the consulting and EY-Parthenon service lines.",
                "impact": "AI-related revenue grew 30% in FY2025; more than 15,000 EY people worked on AI-led "
                          "client projects",
                "source": "https://www.cpapracticeadvisor.com/2025/10/17/ey-posts-4-jump-in-global-revenue-in-2025/171117/",
            },
            {
                "sector": "Network performance",
                "status": "Deployed",
                "deployment": "Second year of the EY All in strategy, built around AI-powered solutions, "
                              "deeper industry alliances and continuous learning.",
                "impact": "$53.2B revenue, up 4.0% in local currency; consulting headcount grew fastest at "
                          "5.4% while strategy and transactions shrank 1.8%",
                "source": "https://www.consulting.us/news/12529/ey-global-posts-4-growth-to-reach-532-billion-in-revenue-in-2025",
            },
            {
                "sector": "Central cost structure",
                "status": "Research finding",
                "deployment": "Following the collapse of the Project Everest consulting spin-off in 2023, "
                              "Truncale cut a layer of management, reduced central headcount and returned "
                              "some responsibilities to national member firms.",
                "impact": "The global assessment on member firms fell below 3.5% of their combined revenue, "
                          "down from above 4% pre-Everest; payments for centrally provided services fell to "
                          "$3.2B from $3.4B",
                "source": "https://www.internationalaccountingbulletin.com/news/ey-reduces-headcount/",
            },
        ],
        "customer_sentiment": "Growth of 4.0% with consulting and tax as the primary drivers suggests "
                              "clients are buying the transformation work rather than only compliance. The "
                              "weak spot is visible in the segment data: strategy and transactions revenue "
                              "was flat and its headcount fell 1.8%, which is where discretionary, "
                              "deal-linked demand shows up first. EY publishes no client-level outcome "
                              "metrics.",
        "sentiment_bull": [
            "Client Zero gives EY a genuinely differentiated proof point \u2014 AI deployed at scale inside a 400,000-person firm before being sold",
            "AI-related revenue grew 30% in FY2025, with over 15,000 people on AI-led client projects",
            "FY20\u2013FY25 compound annual growth of 8.2% \u2014 the strongest medium-term record among the Big Four tracked here",
            "Consulting headcount grew 5.4%, faster than any other service line, indicating where investment is going",
        ],
        "sentiment_bear": [
            "Growth of 4.0% trails Deloitte's 4.8% and both trail Accenture's 7%",
            "Strategy and transactions was flat on revenue with headcount down 1.8% \u2014 the deal-linked business is not recovering",
            "Central structure has been under cost pressure since Project Everest collapsed in 2023; the global assessment has fallen below 3.5% of member firm revenue",
            "As a member-firm network the aggregate figure describes a network, not the entity you contract with",
            "Audit independence restricts consulting work where an EY member firm already audits the client",
        ],
        "employee_sentiment": "Headcount grew 3.4% overall, but the distribution is telling: consulting up "
                              "5.4%, strategy and transactions down 1.8%, and central global headcount "
                              "reduced under a cost-trimming drive. EY US separately announced a $100M "
                              "investment in its employee rewards programme. No independent employer-review "
                              "data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1989", "Founded"),
            ("406,209", "People"),
            ("$53.2B", "FY2025 revenue"),
            ("+30%", "AI revenue growth"),
            ("50,000+", "AI agents in development"),
        ],
    },

    # =================================================================
    {
        "slug": "google",
        "name": "Google",
        "website": "https://cloud.google.com",
        "linkedin": "https://www.linkedin.com/company/google",
        "group": "Frontier AI / LLM",
        "category": "Cloud, frontier models &amp; consumer platforms",
        "tagline": "The only competitor that owns the whole stack \u2014 custom silicon, frontier models, "
                   "developer platform and consumer distribution",
        "founded": "1998",
        "hq": "Mountain View, California (Alphabet Inc.)",
        "employees": "Not broken out separately in the results reviewed in this pass",
        "ownership": "Segment of Alphabet Inc. (NASDAQ: GOOGL, GOOG)",
        "revenue": "Alphabet passed $400B of annual revenue for the first time in FY2025. Q2 2026 revenue "
                   "was $119.8B, up 24%, with operating income of $40.8B, up 30%. Google Cloud reached "
                   "$24.77B in Q2 2026, up 82%, with operating income of $8.81B against $2.83B a year earlier",
        "revenue_short": "$24.8B/qtr (Cloud)",
        "offering": "Google Cloud infrastructure and the Gemini model family, plus the Gemini Enterprise "
                    "Agent Platform (formerly Vertex AI), Workspace Studio for no-code agent building, and "
                    "custom silicon \u2014 Ironwood TPUs, with an eighth generation splitting into "
                    "Broadcom-designed training chips and MediaTek-designed inference chips.",
        "digital_twin": "Via partners",
        "genai": "Yes (Gemini, full stack)",
        "buyer": "CIO, CTO, data and platform leadership",
        "customers": ["KPMG"],
        "people": [
            {"name": "Sundar Pichai", "title": "Chief Executive Officer, Alphabet &amp; Google"},
            {"name": "Thomas Kurian", "title": "Chief Executive Officer, Google Cloud"},
        ],
        "description": "Google Cloud accelerated from 48% growth in Q4 2025 to 63% in Q1 2026 to 82% in Q2, "
                       "with backlog reaching $514B. Gemini processes roughly 22 billion tokens per minute "
                       "through direct API use, and nearly 90% of the Fortune 100 use Gemini Enterprise.",
        "position_note": "Kurian's competitive argument is that rivals hand customers components rather than "
                         "an assembled platform, and the vertical integration behind that claim is real "
                         "\u2014 Google is the only player owning custom silicon, frontier models, developer "
                         "platform and consumer distribution under one roof. For an infrastructure "
                         "portfolio, two commercial mechanics matter more than the architecture: Kurian has "
                         "said most Google Cloud infrastructure contracts run about five years, and that "
                         "customers committing $100 of spend typically end up spending more than $150. Both "
                         "are relevant to how a multi-PortCo commitment should be structured. The "
                         "counterweight is capital intensity \u2014 2026 capex guidance of $195\u2013205B, "
                         "with free cash flow turning negative in Q2 2026.",
        "gip_connection": "No publicly disclosed GIP relationship. Google Cloud is near-certain to be "
                          "present in some PortCos already, so the practical question is consolidated "
                          "commercial terms rather than a first introduction. Note the dual relationship "
                          "risk that applies to all hyperscalers: Google's own data-centre build-out makes "
                          "it a counterparty to digital-infrastructure assets as well as a supplier.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of "
                                "GOOGL/GOOG only.",
        "use_cases": [
            {
                "sector": "Enterprise AI adoption",
                "status": "Deployed",
                "deployment": "Gemini Enterprise, the enterprise agent and assistant platform, adopted "
                              "across large corporates. KPMG reported 90% Gemini Enterprise adoption among "
                              "its own employees.",
                "impact": "Nearly 90% of Fortune 100 companies using Gemini Enterprise; paid monthly active "
                          "users grew 40% quarter over quarter in Q1 2026",
                "source": "https://finance.yahoo.com/technology/ai/articles/google-just-dropped-bombshell-ai-185617741.html",
            },
            {
                "sector": "Cloud &amp; AI infrastructure",
                "status": "Deployed",
                "deployment": "Google Cloud infrastructure and enterprise AI solutions, including TPU system "
                              "sales, with growth accelerating through three consecutive quarters.",
                "impact": "Q4 2025 $17.7B (+48%) \u2192 Q1 2026 $20.0B (+63%) \u2192 Q2 2026 $24.77B (+82%); "
                          "backlog reached $514B, with just over half expected to convert within 24 months",
                "source": "https://futurumgroup.com/insights/alphabet-q2-fy-2026-google-cloud-leads-growth-amid-rising-ai-investment/",
            },
            {
                "sector": "Model usage at scale",
                "status": "Deployed",
                "deployment": "First-party Gemini models consumed through direct API use by customers, "
                              "alongside the Gemini app on the consumer side.",
                "impact": "~22 billion tokens per minute in Q2 2026, up from 16 billion a quarter earlier and "
                          "10 billion in Q4 2025; over 9 million developers building monthly; 330+ Cloud "
                          "customers each processed over a trillion tokens in twelve months",
                "source": "https://www.pymnts.com/earnings/2026/google-cloud-rides-enterprise-ai-demand-to-82percent-growth/",
            },
            {
                "sector": "Autonomous vehicles",
                "status": "Deployed",
                "deployment": "Waymo autonomous ride-hailing, operationally relevant as a transport "
                              "infrastructure data point rather than an enterprise offering.",
                "impact": "Surpassed 500,000 fully autonomous rides per week; a $2.1B employee compensation "
                          "charge for Waymo was recorded in Q4 2025",
                "source": "https://s206.q4cdn.com/479360582/files/doc_financials/2026/q1/2026q1-alphabet-earnings-release.pdf",
            },
        ],
        "customer_sentiment": "Enterprise demand is outrunning capacity, which is why capex guidance keeps "
                              "rising. Roughly 75% of Google Cloud customers were using AI products as of "
                              "Q1 2026, and the expansion pattern Kurian describes \u2014 $100 of commitment "
                              "becoming more than $150 of spend \u2014 indicates land-and-expand is working "
                              "rather than customers capping usage. The historical enterprise complaint "
                              "about Google, that it was a distant third with weaker enterprise support "
                              "than AWS or Azure, is harder to sustain at 82% growth, but it is the "
                              "objection a PortCo CIO will still raise.",
        "sentiment_bull": [
            "Cloud growth accelerated across three consecutive quarters to 82%, with operating income tripling year over year to $8.81B",
            "$514B backlog, with just over half expected to convert within 24 months \u2014 revenue visibility no competitor discloses at this scale",
            "Genuine full-stack vertical integration: custom TPUs, frontier models, agent platform and consumer distribution",
            "Nearly 90% of the Fortune 100 on Gemini Enterprise, and 350 million paid subscriptions across the wider business",
        ],
        "sentiment_bear": [
            "2026 capital expenditure guidance raised to $195\u2013205B, and free cash flow turned negative in Q2 2026",
            "Backlog figures vary noticeably between sources and presentation dates \u2014 use Alphabet's filings, not conference coverage",
            "Enterprise support and account management remain the historical objection against Google relative to AWS and Azure",
            "Consumer and advertising exposure means the enterprise story sits inside a business with quite different risk drivers",
            "Concentration risk cuts both ways: a hyperscaler that is also building data centres is a competitor to some infrastructure assets",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 Google headcount is not broken out separately "
                              "in the results reviewed and no reliable employer-review data was gathered. "
                              "Treat as a gap.",
        "glassdoor": None,
        "kpis": [
            ("1998", "Founded"),
            ("$24.8B", "Cloud rev (Q2 26)"),
            ("+82%", "Cloud growth"),
            ("$514B", "Cloud backlog"),
            ("~90%", "Fortune 100 on Gemini Ent."),
        ],
        "notes": "Cloud backlog and capital expenditure figures moved substantially within 2026 and differ "
                 "between conference presentations and SEC filings. The figures here follow Alphabet's "
                 "reported results; re-run before using any number externally.",
    },

    # =================================================================
    {
        "slug": "hcltech",
        "name": "HCLTech",
        "website": "https://www.hcltech.com",
        "linkedin": "https://www.linkedin.com/company/hcltech",
        "group": "SI / Consulting",
        "category": "IT services with a large engineering practice",
        "tagline": "The India-heritage firm with the strongest engineering and R&amp;D business \u2014 "
                   "growing at nearly 10% while the rest of the company grows at 4%",
        "founded": "1976 (HCL); publicly listed since 1999",
        "hq": "Noida, India",
        "employees": "227,181 at FY2026 close, a net addition of 3,761 including 11,744 freshers; trailing "
                     "twelve-month attrition improved to 12.5% from 13%",
        "ownership": "Public (NSE/BSE: HCLTECH)",
        "revenue": "$14.66B in FY2026 (year ended 31 March 2026), up 6% in USD and 3.9% at constant "
                   "currency; services revenue up 4.8% at constant currency. EBIT margin of 17.2%, or 17.9% "
                   "adjusted for one-time restructuring. FY2027 guidance of just 1\u20134% constant currency",
        "revenue_short": "$14.7B (FY26)",
        "offering": "IT and business services, engineering and R&amp;D services, and HCLSoftware products. "
                    "The AI portfolio runs under AI Force and AI Foundry, with Advanced AI reported as a "
                    "separate revenue line.",
        "digital_twin": "Via engineering services",
        "genai": "Yes (AI Force, AI Foundry)",
        "buyer": "CIO, engineering and product leadership; strong in technology, financial services and telecoms",
        "customers": [],
        "people": [
            {"name": "C Vijayakumar", "title": "Chief Executive Officer &amp; Managing Director"},
            {"name": "Roshni Nadar Malhotra", "title": "Chairperson"},
        ],
        "description": "Delivered 3.9% constant-currency growth in FY2026 in what its CEO called an "
                       "uncertain demand environment, with Advanced AI revenue crossing a $620M annualised "
                       "run rate. The segment that stands out is Engineering and R&amp;D Services, which "
                       "grew 9.8% \u2014 two and a half times the company average.",
        "position_note": "The Engineering and R&amp;D segment is the reason to look at HCLTech rather than "
                         "its India-heritage peers for infrastructure work. It grew 9.8% in a year when the "
                         "company grew 3.9%, which says clients with complex physical and product "
                         "engineering problems are still spending while general IT discretionary demand is "
                         "flat. That is the opposite of the pattern in most of this peer set. The "
                         "counterweight is the FY2027 guidance of 1\u20134% constant currency \u2014 a band "
                         "wide enough that Vijayakumar explicitly attributed it to uncertainty, with the "
                         "bottom end assuming continued softness.",
        "gip_connection": "No publicly disclosed GIP relationship. Engineering and R&amp;D Services is the "
                          "part worth testing against asset-level problems; the mainstream IT services "
                          "business competes on the same ground as TCS, Infosys and Wipro.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "Engineering &amp; R&amp;D",
                "status": "Deployed",
                "deployment": "Engineering and R&amp;D Services for product-centric enterprises, "
                              "semiconductor companies and deep technology clients \u2014 the segment most "
                              "directly linked to physical and product engineering rather than corporate IT.",
                "impact": "9.8% constant-currency growth for FY2026, against 3.9% for the company overall",
                "source": "https://www.cioandleader.com/hcltech-crossed-us-14-6b-in-revenue-while-its-ai-business-hit-us-620m/",
            },
            {
                "sector": "AI services",
                "status": "Deployed",
                "deployment": "AI-led service offerings reported as a distinct Advanced AI revenue line, "
                              "built on the AI Force and AI Foundry platforms.",
                "impact": "Annualised Advanced AI revenue crossed $620M in Q4 FY2026",
                "source": "https://www.hcltech.com/en-us/press-releases/hcltech-fy26-revenue-39-led-increasing-demand-advanced-ai",
            },
            {
                "sector": "Commercial performance",
                "status": "Deployed",
                "deployment": "New deal signings across services and software, with growth concentrated in "
                              "technology and services, financial services and telecoms.",
                "impact": "$9.3B of new deal total contract value in FY2026; Technology and Services grew "
                          "15%, Financial Services 7.5%, Telecoms/Media 5.2%",
                "source": "https://www.tribuneindia.com/news/hcltech-fy26-revenue-up-3-9-led-by-increasing-demand-for-advanced-ai-2-2/",
            },
            {
                "sector": "Delivery efficiency",
                "status": "Deployed",
                "deployment": "Revenue growth delivered with almost no net headcount addition \u2014 a "
                              "deliberate decoupling of growth from hiring, supported by rolling rather than "
                              "fixed annual hiring targets.",
                "impact": "Revenue rose from $13.8B to $14.7B while net headcount grew by fewer than 4,000; "
                          "outsourcing costs rose from 13% to 14.2% of revenue",
                "source": "https://www.cioandleader.com/hcltech-crossed-us-14-6b-in-revenue-while-its-ai-business-hit-us-620m/",
            },
        ],
        "customer_sentiment": "The demand picture splits cleanly by client type. Complex engineering clients "
                              "are leaning in \u2014 Engineering and R&amp;D grew 9.8% \u2014 while general "
                              "discretionary IT spending is soft, with decisions being delayed. "
                              "Geographically the US, the largest market, grew only 2.3% while the Rest of "
                              "World grew 17.8% off a smaller base. HCLTech publishes no attributable client "
                              "outcomes.",
        "sentiment_bull": [
            "Engineering and R&amp;D Services grew 9.8% against 3.9% company growth \u2014 the clearest signal in this peer set that engineering demand is holding up",
            "Advanced AI crossed a $620M annualised run rate and is reported as its own line",
            "Attrition improved to 12.5% from 13%, the lowest in its immediate peer group",
            "EBIT margin of 17.2% (17.9% adjusted) is at the top of the India-heritage peer set",
        ],
        "sentiment_bear": [
            "FY2027 guidance of 1\u20134% constant currency is the weakest forward outlook of any vendor in this wave",
            "The US, its largest geography, grew only 2.3% at constant currency",
            "Outsourcing costs rose from 13% to 14.2% of revenue, which pressures the margin advantage",
            "Growth of 3.9% with net headcount up fewer than 4,000 can read as efficiency or as an inability to convert demand \u2014 the guidance suggests the latter is a live risk",
            "Competes directly with TCS, Infosys, Wipro and Cognizant on price in the mainstream services business",
        ],
        "employee_sentiment": "Attrition fell to 12.5% on a trailing twelve-month basis from 13% a year "
                              "earlier, and 11,744 freshers were hired against roughly 7,800 the previous "
                              "year, so entry-level intake rose even as net addition stayed under 4,000. "
                              "Hiring has moved to a rolling basis rather than fixed annual targets. No "
                              "independent employer-review data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1976", "Founded"),
            ("227,181", "Employees"),
            ("$14.7B", "FY2026 revenue"),
            ("$620M", "Advanced AI run rate"),
            ("17.2%", "EBIT margin"),
        ],
    },

    # =================================================================
    {
        "slug": "ibm-consulting",
        "name": "IBM Consulting",
        "website": "https://www.ibm.com/consulting",
        "linkedin": "https://www.linkedin.com/company/ibm",
        "group": "SI / Consulting",
        "category": "Systems integration &amp; managed operations",
        "tagline": "Rebuilding the consulting model around supervised AI agents rather than billable hours",
        "founded": "Part of IBM, founded 1911; the modern consulting arm dates from the 2002 PwC Consulting acquisition",
        "hq": "Armonk, New York",
        "employees": "Not disclosed separately from IBM, whose total workforce is approximately 280,000",
        "ownership": "Segment of International Business Machines Corporation (NYSE: IBM)",
        "revenue": "Over $21B in 2025, up from approximately $20.7B in 2024 \u2014 roughly a third of IBM's "
                   "total revenue, alongside Software at about $26B and Infrastructure at about $14B",
        "revenue_short": "$21B (2025)",
        "offering": "Strategy, technology and operations consulting, systems integration and managed "
                    "services, closely coupled to IBM's own stack \u2014 watsonx, Red Hat OpenShift, "
                    "automation and the Z mainframe platform. Delivery runs on Consulting Advantage "
                    "internally and Enterprise Advantage for clients.",
        "digital_twin": "Client-specific builds",
        "genai": "Yes (watsonx, agent supervision)",
        "buyer": "CIO and transformation sponsors, typically where IBM technology is already installed",
        "customers": [],
        "people": [
            {"name": "Mohamad Ali", "title": "Senior Vice President, IBM Consulting"},
            {"name": "Arvind Krishna", "title": "Chairman, President &amp; Chief Executive Officer, IBM"},
        ],
        "description": "IBM's services arm, at over $21B of 2025 revenue. It is the clearest example in this "
                       "set of a consultancy restructuring its own delivery model around AI agents: "
                       "Consulting Advantage lets IBM consultants build and manage agent teams, and "
                       "Enterprise Advantage now sells that capability to clients.",
        "position_note": "Ali describes the new consulting model as a live dashboard where humans monitor "
                         "digital workers and vice versa \u2014 which is a materially different proposition "
                         "from selling consultant days, and worth understanding whoever a PortCo ends up "
                         "using. The volume claim behind it is specific: 52,000 investigations completed in "
                         "January alone using this approach. The structural consideration for any buyer is "
                         "that IBM Consulting is tightly coupled to IBM's own stack, so a recommendation "
                         "arriving through this channel will tend toward watsonx, Red Hat and Z. That is "
                         "not disqualifying \u2014 it is often the right answer where that estate already "
                         "exists \u2014 but it is not vendor-neutral advice, and IBM watsonx is tracked "
                         "separately in this app for that reason.",
        "gip_connection": "No publicly disclosed GIP relationship. The most likely entry point is an "
                          "existing IBM technology footprint at a PortCo \u2014 mainframe, Red Hat or "
                          "watsonx \u2014 with consulting following the estate rather than being selected "
                          "independently.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of IBM only.",
        "use_cases": [
            {
                "sector": "Consulting delivery model",
                "status": "Deployed",
                "deployment": "Consulting Advantage, unveiled in 2024, lets IBM consultants build and manage "
                              "teams of AI agents; Enterprise Advantage, released in January 2026, gives "
                              "clients the same platform to build and manage agents at scale. A real-time "
                              "dashboard shows which humans are attached to which digital workers.",
                "impact": "52,000 investigations completed in January 2026 alone using this model",
                "source": "https://finance.yahoo.com/sectors/technology/articles/future-consulting-real-time-dashboard-090101696.html",
            },
            {
                "sector": "Generative AI commercial traction",
                "status": "Deployed",
                "deployment": "IBM's generative AI book of business, measured inception to date as software "
                              "transactional revenue plus new SaaS annual contract value plus consulting "
                              "signings on specific offerings. Consulting is a substantial contributor.",
                "impact": "Passed $12.5B inception to date by Q4 2025, up from $9.5B and $5B at earlier "
                          "milestones",
                "source": "https://newsroom.ibm.com/2026-01-28-IBM-RELEASES-FOURTH-QUARTER-RESULTS",
            },
            {
                "sector": "Enterprise incumbency",
                "status": "Deployed",
                "deployment": "Consulting sold alongside IBM's installed base, with 93% of the Fortune 500 "
                              "using IBM hybrid cloud products \u2014 the distribution advantage the "
                              "consulting arm sells into.",
                "impact": "Consulting revenue rose to over $21B in 2025 from approximately $20.7B in 2024, "
                          "accelerating on demand for AI design, deployment and governance",
                "source": "https://www.sec.gov/Archives/edgar/data/51143/000005114325000010/ibm-ex99_1.htm",
            },
            {
                "sector": "Portfolio expansion",
                "status": "Deployed",
                "deployment": "The $6.4B HashiCorp acquisition, completed in 2025, strengthened the hybrid "
                              "cloud portfolio that consulting implements, alongside Red Hat OpenShift and "
                              "the watsonx stack (watsonx.ai, watsonx.data, watsonx.governance).",
                "impact": "IBM guided to more than 5% constant-currency revenue growth in 2026 and roughly "
                          "$1B of additional free cash flow",
                "source": "https://newsroom.ibm.com/2026-01-28-IBM-RELEASES-FOURTH-QUARTER-RESULTS",
            },
        ],
        "customer_sentiment": "Consulting accelerated in 2025 on demand for help designing, deploying and "
                              "governing AI at scale \u2014 governance being the part clients struggle with "
                              "most and the part IBM has built explicit tooling for in watsonx.governance. "
                              "The candid note comes from IBM itself: Krishna described consulting as "
                              "embracing disruption, an acknowledgement that the traditional model is under "
                              "pressure from the same technology it is selling. No attributable client "
                              "outcomes are published.",
        "sentiment_bull": [
            "The only firm in this set that has rebuilt its own delivery model around supervised AI agents and put volume numbers against it",
            "$12.5B generative AI book of business inception to date, up from $5B roughly a year earlier",
            "93% of the Fortune 500 use IBM hybrid cloud products \u2014 an installed base consulting sells into rather than competing for cold",
            "watsonx.governance addresses AI governance specifically, which is the area most enterprises are least equipped for",
        ],
        "sentiment_bear": [
            "Consulting revenue grew only about 1.5% in 2025 \u2014 from roughly $20.7B to over $21B \u2014 well behind Accenture's 7%",
            "Tightly coupled to IBM's own stack, so advice arriving through this channel is not vendor-neutral",
            "Consulting has been flat in some recent periods; the acceleration is recent and narrow",
            "The generative AI book of business is an inception-to-date cumulative measure combining software, SaaS and signings \u2014 not comparable to an annual revenue figure",
            "Scale is roughly a third of Accenture's in the same market",
        ],
        "employee_sentiment": "Not disclosed separately from IBM. IBM has publicly rebalanced its workforce "
                              "toward AI and hybrid cloud skills while reducing roles in legacy "
                              "infrastructure support, across a total workforce of approximately 280,000. No "
                              "consulting-specific employer-review data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1911", "IBM founded"),
            ("$21B", "2025 revenue"),
            ("$12.5B", "GenAI book of business"),
            ("93%", "Fortune 500 on IBM hybrid cloud"),
            ("52,000", "Jan 2026 agent investigations"),
        ],
        "notes": "IBM watsonx is tracked separately in this app. The generative AI book of business is an "
                 "IBM-wide, inception-to-date measure spanning software, SaaS and consulting signings \u2014 "
                 "do not read it as consulting annual revenue.",
    },
]
