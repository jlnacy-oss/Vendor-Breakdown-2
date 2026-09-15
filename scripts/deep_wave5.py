# -*- coding: utf-8 -*-
"""
deep_wave5.py — Research wave 5, completed 15 September 2026.

Infosys, KPMG, McKinsey & Company, Meta, Microsoft.
"""

VENDORS = [
    # =================================================================
    {
        "slug": "infosys",
        "name": "Infosys",
        "website": "https://www.infosys.com",
        "linkedin": "https://www.linkedin.com/company/infosys",
        "group": "SI / Consulting",
        "category": "IT services &amp; enterprise AI",
        "tagline": "Crossed $20B with an AI strategy that names physical AI as one of six target areas "
                   "\u2014 unusual in this peer set",
        "founded": "1981",
        "hq": "Bengaluru, India",
        "employees": "Over 325,000 at FY2026 close, with more than 20,000 college graduates hired during "
                     "the year; headcount fell 8,440 in Q4 alone and attrition rose to 12.6%",
        "ownership": "Public (NSE/BSE: INFY; NYSE: INFY)",
        "revenue": "$20.2B in FY2026 (year ended 31 March 2026), up 3.1% at constant currency, with Q4 at "
                   "4.1%. Adjusted operating margin of 21%. FY2027 guidance of just 1.5\u20133.5% constant "
                   "currency",
        "revenue_short": "$20.2B (FY26)",
        "offering": "Application services, consulting, engineering and operations. The AI portfolio is "
                    "Infosys Topaz, with Topaz Fabric as the platform layer and Cobalt for cloud. The "
                    "stated AI strategy covers six areas: AI strategy engineering, data, process, legacy "
                    "modernisation, physical AI, and trust.",
        "digital_twin": "Via engineering services",
        "genai": "Yes (Topaz, Topaz Fabric)",
        "buyer": "CIO and business unit leadership; strong in financial services, communications and manufacturing",
        "customers": [],
        "people": [
            {"name": "Salil Parekh", "title": "Chief Executive Officer &amp; Managing Director (term ends March 2027)"},
        ],
        "description": "Crossed $20B of revenue in FY2026 on 3.1% constant-currency growth, with $14.9B of "
                       "large deal wins \u2014 28% higher than the prior year. AI revenue moved from 5.5% of "
                       "total in Q3 FY2026 to 8.2% by mid-2026, the fastest ramp disclosed by any "
                       "India-heritage firm tracked here.",
        "position_note": "Two things distinguish Infosys for an infrastructure portfolio. First, physical AI "
                         "is explicitly one of the six areas in its published AI strategy \u2014 no other "
                         "firm in this peer set names it as a target market rather than a talking point. "
                         "Second, Topaz Fabric is architected so clients can use different foundation models "
                         "while keeping sensitive data inside their own environments, which Parekh calls a "
                         "major differentiator and which matters for regulated operational data. The "
                         "counterweight is the forward outlook: FY2027 guidance of 1.5\u20133.5% constant "
                         "currency is weak, headcount fell 8,440 in a single quarter, and a CEO transition "
                         "is under way.",
        "gip_connection": "No publicly disclosed GIP relationship. The physical AI strand of the strategy is "
                          "the part worth testing directly against asset-level problems; the mainstream "
                          "services business competes on the same ground as TCS, Wipro, HCLTech and "
                          "Cognizant. Note the Anthropic partnership if model choice comes up.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "Enterprise AI",
                "status": "Deployed",
                "deployment": "Infosys Topaz deployed across the large majority of the firm's biggest client "
                              "relationships, with AI programmes moving from proof-of-concept to full-scale "
                              "implementation. Topaz Fabric lets clients run different foundation models "
                              "while keeping sensitive data in their own environments.",
                "impact": "AI revenue rose from 5.5% of total in Q3 FY2026 to 8.2% by mid-2026, with "
                          "double-digit quarter-on-quarter growth",
                "source": "https://m.investing.com/news/transcripts/earnings-call-transcript-infosys-cuts-fy2026-outlook-as-shares-fall-51-premarket-93CH-4808754?ampMode=1",
            },
            {
                "sector": "AI strategy",
                "status": "Deployed",
                "deployment": "An AI services strategy organised around six addressable areas \u2014 AI "
                              "strategy engineering, data, process, legacy modernisation, physical AI and "
                              "trust \u2014 set out at an AI Investor Day, with the AI First value framework "
                              "and Topaz Fabric as the delivery vehicles.",
                "impact": "Named as the basis for claimed market share gains in large transformation opportunities",
                "source": "https://www.stocktitan.net/sec-filings/INFY/6-k-infosys-ltd-current-report-foreign-issuer-ef7670a5a8b6.html",
            },
            {
                "sector": "Commercial performance",
                "status": "Deployed",
                "deployment": "Large deal signings tracked as the forward indicator, with strength in "
                              "financial services, communications and manufacturing, and in Europe "
                              "geographically.",
                "impact": "$14.9B of large deal wins in FY2026, 28% above the prior year, including $3.2B in "
                          "Q4; over $4B returned to shareholders through dividends and buybacks",
                "source": "https://www.businessapac.com/news/infosys-annual-results-2026/",
            },
            {
                "sector": "Ecosystem partnerships",
                "status": "Deployed",
                "deployment": "Agentic AI tooling deployed at scale through partnerships with model and "
                              "hardware providers including Anthropic, Intel and Cognition.",
                "impact": "Positions Infosys as model-agnostic rather than tied to a single provider",
                "source": "https://www.businessapac.com/news/infosys-annual-results-2026/",
            },
        ],
        "customer_sentiment": "Deal data points up \u2014 $14.9B of large wins, 28% above the prior year, "
                              "with strength in financial services, communications and manufacturing. "
                              "Parekh's framing is that clients increasingly treat Infosys as a strategic AI "
                              "partner rather than a delivery vendor, and the AI revenue ramp from 5.5% to "
                              "8.2% supports that more than most such claims. The tension is that this "
                              "coexists with weak forward guidance, which suggests the AI work is not yet "
                              "big enough to offset softness in the base business.",
        "sentiment_bull": [
            "AI revenue rose from 5.5% to 8.2% of total in roughly two quarters \u2014 the fastest disclosed ramp in its peer group",
            "Physical AI named explicitly as one of six strategy areas, which no direct competitor in this set does",
            "Topaz Fabric's model-agnostic architecture keeps client data in the client's own environment",
            "$14.9B of large deal wins, up 28%, with a 21% adjusted operating margin",
        ],
        "sentiment_bear": [
            "FY2027 guidance of 1.5\u20133.5% constant currency is among the weakest in this peer set",
            "Headcount fell 8,440 in Q4 FY2026 and attrition rose to 12.6%",
            "A CEO transition is under way, with Parekh describing a handoff in which the successor focuses on execution",
            "Growth of 3.1% trails Accenture, Cognizant and TCS-scale peers in the same demand environment",
            "CEO pay disclosed at 742 times median employee remuneration including exercised stock, or 289 times excluding it",
        ],
        "employee_sentiment": "The FY2026 picture is of a workforce contracting at the top of the pyramid "
                              "while entry-level intake continues: more than 20,000 college graduates hired "
                              "across the year, but an 8,440 net reduction in Q4 alone and attrition ticking "
                              "up to 12.6%. No independent employer-review data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1981", "Founded"),
            ("325,000+", "Employees"),
            ("$20.2B", "FY2026 revenue"),
            ("8.2%", "Revenue from AI"),
            ("$14.9B", "Large deal wins"),
        ],
        "notes": "Succession is now resolved: the Infosys board has named Ashiss Kumar Dash to succeed "
                 "Salil Parekh as CEO in April 2027. Anything multi-year should involve the incoming "
                 "leadership as well.",
    },

    # =================================================================
    {
        "slug": "kpmg",
        "name": "KPMG",
        "website": "https://kpmg.com",
        "linkedin": "https://www.linkedin.com/company/kpmg",
        "group": "SI / Consulting",
        "category": "Big Four professional services network",
        "tagline": "The smallest of the Big Four, growing steadily on tax and audit while advisory lags",
        "founded": "1987 (merger of Peat Marwick International and Klynveld Main Goerdeler)",
        "hq": "KPMG International Limited; a network of member firms, with global announcements issued from London",
        "employees": "276,030 at FY2025 close, up 1.8% from 275,288 \u2014 with specialist hiring "
                     "concentrated in AI and tax and legal services",
        "ownership": "Private network of member firms",
        "revenue": "$39.8B aggregated across KPMG firms for FY2025 (year ended 30 September 2025) on a "
                   "continued operations basis, up 5.1% in local currency and 5.4% in US dollars. Tax and "
                   "Legal grew 7.5%, Audit 6.0% and Advisory 2.9%",
        "revenue_short": "$39.8B (FY25)",
        "offering": "Audit, tax and legal, and advisory services through member firms. Investment runs under "
                    "the Collective Strategy, a three-year $4.2B plan announced in 2023 covering technology, "
                    "talent and sustainability.",
        "digital_twin": "No",
        "genai": "Advisory &amp; internal deployment",
        "buyer": "CFO, audit committee and risk leadership",
        "customers": [],
        "people": [
            {"name": "Bill Thomas", "title": "Global Chairman &amp; Chief Executive Officer, KPMG International"},
        ],
        "description": "The smallest Big Four network at $39.8B, growing 5.1% in local currency \u2014 "
                       "faster than Deloitte's 4.8% and EY's 4.0%, but from a materially smaller base. "
                       "Growth is concentrated in tax, legal and audit; advisory, where AI work sits, grew "
                       "only 2.9%.",
        "position_note": "The service-line split is the most useful thing on this page. Tax and Legal grew "
                         "7.5% and Audit 6.0%, while Advisory \u2014 the consulting arm that would deliver "
                         "AI work \u2014 grew 2.9%. That is the opposite shape to Accenture or BCG and it "
                         "means the headline growth rate overstates KPMG's momentum in the areas relevant "
                         "to a portfolio AI programme. What KPMG does have is an unusually visible position "
                         "as an AI buyer rather than only a seller: it is a named enterprise customer of "
                         "Anthropic's Claude Code and has reported roughly 90% Gemini Enterprise adoption "
                         "among its own employees. A firm running multiple frontier vendors internally at "
                         "276,000-person scale has learned things worth asking about.",
        "gip_connection": "No publicly disclosed GIP relationship. As with the other Big Four, check for an "
                          "existing audit relationship at fund or PortCo level before scoping consulting "
                          "work \u2014 independence rules constrain what can follow.",
        "blackrock_connection": "No publicly disclosed operating relationship.",
        "use_cases": [
            {
                "sector": "Network performance",
                "status": "Deployed",
                "deployment": "Growth delivered across all regions and all functions in FY2025, following "
                              "the multi-billion-dollar Collective Strategy investment programme launched in "
                              "2023.",
                "impact": "Tax and Legal up 7.5%, Audit up 6.0%, Advisory up 2.9%; Americas up 5.6%, Asia "
                          "Pacific up 4.7%, EMA up 4.7%",
                "source": "https://kpmg.com/xx/en/media/press-releases/2025/12/kpmg-delivers-rise-in-global-revenue.html",
            },
            {
                "sector": "Internal AI adoption",
                "status": "Deployed",
                "deployment": "KPMG runs frontier AI tooling internally at scale across a 276,000-person "
                              "network \u2014 a named enterprise user of Anthropic's Claude Code, and "
                              "reporting roughly 90% Gemini Enterprise adoption among its employees.",
                "impact": "Makes KPMG one of the largest multi-vendor enterprise AI deployments in the "
                          "professional services sector",
                "source": "https://sqmagazine.co.uk/google-cloud-platform-statistics/",
            },
            {
                "sector": "Talent investment",
                "status": "Deployed",
                "deployment": "Specialist hiring focused on AI and tax and legal services, with technology "
                              "learning pathways built across member firms to support upskilling and career "
                              "mobility.",
                "impact": "Global headcount grew 1.8% to 276,030, with the growth concentrated in specialist roles",
                "source": "https://kpmg.com/pk/en/about/performance.html",
            },
            {
                "sector": "Market research",
                "status": "Research finding",
                "deployment": "The KPMG 2025 Global CEO Outlook, surveying large-company chief executives on "
                              "investment intent.",
                "impact": "92% of leaders planned to increase headcount; 69% were allocating up to a fifth "
                          "of budget to AI; 89% anticipated moderate to significant M&amp;A impact over three years",
                "source": "https://kpmg.com/xx/en/our-insights/value-creation/global-ceo-outlook-survey.html",
            },
        ],
        "customer_sentiment": "Growth across all regions and functions is the aggregate signal, and 5.1% is "
                              "respectable against Big Four peers. The composition is the caveat: demand is "
                              "strongest in the compliance-driven lines that clients cannot defer, and "
                              "weakest in advisory, which is discretionary. KPMG publishes no client-level "
                              "outcome metrics.",
        "sentiment_bull": [
            "5.1% local-currency growth outpaced both Deloitte (4.8%) and EY (4.0%) in the same period",
            "Growth across every region and every function, in what the firm describes as challenging market conditions",
            "A $4.2B three-year investment programme in technology, talent and sustainability, now delivering",
            "Running multiple frontier AI vendors internally at scale gives it practical deployment experience, not just methodology",
        ],
        "sentiment_bear": [
            "Advisory grew only 2.9% \u2014 the service line that would deliver AI transformation work is the slowest-growing",
            "Smallest of the Big Four at $39.8B, against Deloitte's $70.5B and EY's $53.2B",
            "Headcount grew just 1.8%, and reporting on the regional breakdown indicates the Americas and Asia Pacific headcount actually shrank",
            "Revenue is reported on a continued operations basis, so the figure is not directly comparable to prior-year totals without adjustment",
            "Member-firm structure means the aggregate describes a network rather than a contracting entity",
        ],
        "employee_sentiment": "Headcount grew 1.8% overall with hiring targeted at AI and tax and legal "
                              "specialists, and the firm points to technology learning pathways and external "
                              "employer recognition. Reporting on the regional breakdown indicates headcount "
                              "fell in the Americas and Asia Pacific even as the global total rose, so the "
                              "net figure conceals contraction in two of three regions. No independent "
                              "employer-review data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1987", "Founded"),
            ("276,030", "People"),
            ("$39.8B", "FY2025 revenue"),
            ("+2.9%", "Advisory growth"),
            ("$4.2B", "Investment programme"),
        ],
    },

    # =================================================================
    {
        "slug": "mckinsey",
        "name": "McKinsey & Company",
        "website": "https://www.mckinsey.com",
        "linkedin": "https://www.linkedin.com/company/mckinsey",
        "group": "SI / Consulting",
        "category": "Strategy consultancy",
        "tagline": "Rebuilding the consulting pyramid around AI agents in its centenary year \u2014 while "
                   "cutting more than 10% of its people",
        "founded": "1926 (by James O. McKinsey); the firm turned 100 in 2026",
        "hq": "New York, New York",
        "employees": "Roughly 40,000 people, down from about 45,000 at the end of 2023 \u2014 a reduction of "
                     "more than 10% in about eighteen months. Sternfels describes a total workforce of "
                     "around 60,000 when roughly 20,000\u201325,000 AI agents are counted alongside humans",
        "ownership": "Private partnership",
        "revenue": "Approximately $16B for 2023 \u2014 disclosed once, in McKinsey's own announcement of "
                   "Bob Sternfels' re-election, and not repeated since. No figure has been published for "
                   "2024 or 2025. MBB combined 2025 revenue is estimated at roughly $36\u201340B across "
                   "about 97,000 consultants, and reporting indicates McKinsey's growth flatlined "
                   "following a period of rapid hiring",
        "revenue_short": "~$16B (2023)",
        "offering": "Strategy, operations, organisation and technology consulting, with QuantumBlack as the "
                    "AI and advanced analytics arm and Lilli as the proprietary internal AI tool.",
        "digital_twin": "No",
        "genai": "Yes (QuantumBlack, Lilli)",
        "buyer": "CEO, board and senior executive sponsors",
        "customers": [],
        "people": [
            {"name": "Bob Sternfels", "title": "Global Managing Partner"},
            {"name": "Alex Singla", "title": "Senior Partner, Co-Lead of QuantumBlack"},
        ],
        "description": "The most prestigious strategy firm, and the one making the most aggressive claims "
                       "about restructuring itself around AI. QuantumBlack, a 1,700-person unit, now drives "
                       "initiatives accounting for roughly 40% of the firm's work \u2014 while headcount has "
                       "fallen more than 10% and about 10% of non-client-facing staff are being cut over "
                       "18 to 24 months.",
        "position_note": "McKinsey is doing publicly what most of this peer set is doing quietly: shrinking "
                         "the support base, holding or growing the client-facing pyramid, and filling the "
                         "gap with agents. Sternfels' stated goal is every employee paired with one or more "
                         "agents, and he has said he expects agent count to match human headcount. Whether "
                         "that is transformation or repackaging is not yet answerable from outside \u2014 "
                         "the supporting numbers are self-reported, the agent count varies between 20,000 "
                         "and 25,000 across the same reporting cycle, and there is no revenue disclosure to "
                         "test any of it against. For a portfolio owner the useful read is directional: the "
                         "pricing model is shifting toward outcomes, and the firm is explicit that "
                         "traditional leverage economics no longer hold.",
        "gip_connection": "No publicly disclosed GIP relationship. McKinsey works extensively with private "
                          "equity and infrastructure owners, so an existing relationship at deal or fund "
                          "level is plausible and would not be public. Check internally before assuming a "
                          "clean slate.",
        "blackrock_connection": "None publicly disclosed.",
        "use_cases": [
            {
                "sector": "Firm operating model",
                "status": "Deployed",
                "deployment": "AI agents deployed alongside consultants across delivery, with the stated "
                              "goal of pairing every employee with one or more agents. Sternfels has said "
                              "the firm used only a few thousand agents eighteen months earlier.",
                "impact": "A workforce described as roughly 60,000 \u2014 about 40,000 humans plus 20,000 to "
                          "25,000 agents; a claimed 1.5 million hours saved in search and synthesis work "
                          "over a year",
                "source": "https://themoneytimes.media/2026/01/13/mckinsey-ceo-bob-sternfels-says-the-firm-now-has-60-000-employees-25-000-of-them-are-ai-agents/",
            },
            {
                "sector": "AI delivery",
                "status": "Deployed",
                "deployment": "QuantumBlack, the AI and advanced analytics unit, with a 1,700-person team "
                              "driving the firm's AI initiatives, supported by proprietary tooling including "
                              "Lilli and dedicated AI implementation teams.",
                "impact": "AI initiatives now account for approximately 40% of McKinsey's work",
                "source": "https://theaiworld.org/news/bob-sternfels-mckinsey-adds-25000-ai-agents",
            },
            {
                "sector": "Workforce restructuring",
                "status": "Announced",
                "deployment": "A reduction of roughly 10% of staff across non-client-facing departments over "
                              "18 to 24 months, announced around the October 2025 centenary events, while "
                              "continuing to hire client-facing consultants.",
                "impact": "Headcount already down from about 45,000 at end-2023 to roughly 40,000 by May "
                          "2025, following flatlined revenue growth after a rapid hiring period",
                "source": "https://consulting5.substack.com/p/mckinsey-at-100-headcount-agents",
            },
            {
                "sector": "Talent model",
                "status": "Research finding",
                "deployment": "A redefinition of the consultant profile toward builder-style capability "
                              "\u2014 candidates who move between traditional consulting and an engineering "
                              "mindset and collaborate with AI systems as part of delivery.",
                "impact": "Mirrors BCG's forward-deployed consultants building AI tools directly on client "
                          "projects; pricing is increasingly tied to outcomes",
                "source": "https://theaiworld.org/news/bob-sternfels-mckinsey-adds-25000-ai-agents",
            },
        ],
        "customer_sentiment": "Not assessable from public sources. McKinsey's client work is confidential "
                              "and it publishes essentially no attributable case studies or outcome metrics. "
                              "The one indirect signal is that revenue growth reportedly flatlined after a "
                              "rapid hiring period, which prompted the restructuring \u2014 that points to "
                              "demand softening rather than accelerating, whatever the AI narrative says.",
        "sentiment_bull": [
            "QuantumBlack is a genuine 1,700-person delivery capability, not a rebadged strategy practice",
            "AI initiatives reportedly account for around 40% of the firm's work \u2014 among the highest proportions claimed in this set",
            "The most explicit shift toward outcome-linked pricing of any strategy firm tracked here",
            "Unmatched access at CEO and board level, which matters when an AI programme needs executive sponsorship rather than technical buy-in",
        ],
        "sentiment_bear": [
            "No revenue disclosure at all \u2014 nothing in the AI narrative can be tested against financial performance",
            "Headcount fell more than 10% in eighteen months, and a further ~10% cut to non-client-facing staff is under way",
            "Revenue growth reportedly flatlined before the restructuring, which is the context the AI story sits inside",
            "Agent counts are self-reported and inconsistent \u2014 20,000 and 25,000 both appear in the same reporting cycle",
            "The firm's own framing concedes that legacy growth and leverage economics no longer work",
        ],
        "employee_sentiment": "The verifiable picture is contraction: roughly 45,000 people at the end of "
                              "2023 down to around 40,000 by May 2025, with a further 10% reduction in "
                              "non-client-facing departments running over 18 to 24 months, announced at the "
                              "centenary gathering. Client-facing hiring is continuing. A chatbot has been "
                              "deployed to run graduate recruitment. No independent employer-review data was "
                              "gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1926", "Founded"),
            ("~40,000", "People"),
            ("~25,000", "AI agents"),
            ("~40%", "Work that is AI"),
            ("~$16B", "Revenue (2023)"),
        ],
        "notes": "McKinsey discloses no revenue, and the AI figures on this page are the firm's own "
                 "statements in podcasts and conference appearances rather than audited disclosure. The "
                 "agent count varies between tellings. Weight accordingly.",
    },

    # =================================================================
    {
        "slug": "meta",
        "name": "Meta",
        "website": "https://ai.meta.com",
        "linkedin": "https://www.linkedin.com/company/meta",
        "group": "Frontier AI / LLM",
        "category": "Consumer platforms &amp; open-weight AI models",
        "tagline": "Spending roughly twice its 2025 capex on AI infrastructure it consumes itself \u2014 and "
                   "now moving some of it off balance sheet with BlackRock",
        "founded": "2004",
        "hq": "Menlo Park, California",
        "employees": "Cutting roughly 10% of the workforce \u2014 about 8,000 roles effective 20 May 2026 "
                     "\u2014 with a further 6,000 open positions left unfilled; the largest restructuring "
                     "since the 2022\u201323 efficiency programme that cut about 21,000 roles",
        "ownership": "Public (NASDAQ: META)",
        "revenue": "$56.31B in Q1 2026, up 33% year over year \u2014 the fastest growth since 2021 \u2014 "
                   "with income from operations of $22.87B. Family daily active people reached 3.56 billion",
        "revenue_short": "$56.3B (Q1 26)",
        "offering": "Facebook, Instagram, WhatsApp and Reality Labs on the consumer side; the Llama "
                    "open-weight model family and, from 2026, Meta Superintelligence Labs, whose first "
                    "proprietary model is Muse Spark. Custom MTIA silicon is being built to reduce "
                    "dependence on NVIDIA.",
        "digital_twin": "No",
        "genai": "Yes (Llama, Muse Spark)",
        "buyer": "Primarily advertisers; open-weight models are consumed directly by developers rather than sold",
        "customers": [],
        "people": [
            {"name": "Mark Zuckerberg", "title": "Founder, Chairman &amp; Chief Executive Officer"},
            {"name": "Alexandr Wang", "title": "Chief AI Officer; lead of Meta Superintelligence Labs"},
        ],
        "description": "The only hyperscale AI spender whose infrastructure is almost entirely "
                       "self-consumed \u2014 there is no Azure or AWS equivalent selling capacity to third "
                       "parties. 2026 capital expenditure guidance has been raised three times to "
                       "$135\u2013145B, roughly double the $72.22B actually spent in 2025, while the company "
                       "cuts 10% of its workforce.",
        "position_note": "Meta's relevance to an infrastructure portfolio is not as a vendor \u2014 it sells "
                         "advertising, and Llama is given away. It matters as a counterparty and a demand "
                         "driver. The most directly relevant fact in this research pass: in the week before "
                         "Q2 2026 earnings, Meta and BlackRock announced a $14B El Paso data centre joint "
                         "venture with BlackRock funds holding 80%, which lets Meta de-consolidate "
                         "significant capex from its balance sheet. That is a BlackRock infrastructure "
                         "transaction with an AI hyperscaler, and it is the template other operators will "
                         "now be asked about. For digital-infrastructure assets, Meta's capex trajectory is "
                         "a demand signal; for the fund, the El Paso structure is a precedent worth "
                         "understanding internally.",
        "gip_connection": "No publicly disclosed direct GIP relationship. However, the $14B El Paso data "
                          "centre joint venture with BlackRock funds at 80% ownership is the closest "
                          "adjacency of any vendor in this app \u2014 confirm internally how that structure "
                          "sits relative to GIP's own digital infrastructure mandate before treating Meta "
                          "as a straightforward third party.",
        "blackrock_connection": "Direct and material: a $14B El Paso data centre joint venture announced in "
                                "2026, with BlackRock funds owning 80%. This lets Meta move significant "
                                "capital expenditure off its own balance sheet while BlackRock takes the "
                                "infrastructure position.",
        "use_cases": [
            {
                "sector": "Digital infrastructure",
                "status": "Announced",
                "deployment": "A $14B El Paso data centre joint venture with BlackRock funds owning 80%, "
                              "announced the day before Q2 2026 earnings, structured so Meta can "
                              "de-consolidate capital expenditure from its balance sheet.",
                "impact": "Part of a programme including $107B of new contractual commitments announced in "
                          "Q1 2026 alone",
                "source": "https://aibusinessweekly.net/p/meta-ai-statistics",
            },
            {
                "sector": "AI infrastructure spend",
                "status": "Deployed",
                "deployment": "Capital expenditure directed at AI data centres, GPUs and power, including "
                              "what Meta describes as the largest AI training cluster in the world \u2014 a "
                              "2 gigawatt facility \u2014 plus data centres under construction in Europe and "
                              "Asia. Physical construction accounts for roughly 40% of total capex.",
                "impact": "2026 guidance raised three times to $135\u2013145B against $72.22B actually spent "
                          "in 2025; total 2026 expenses guided to $162\u2013169B",
                "source": "https://valueaddvc.com/blog/meta-145b-ai-capex-2026-why-zuckerberg-raised-guidance-twice",
            },
            {
                "sector": "Frontier models",
                "status": "Deployed",
                "deployment": "Meta Superintelligence Labs, launched in 2026 with the acquisition of the "
                              "Scale AI team led by Alexandr Wang, released Muse Spark in April 2026 \u2014 "
                              "its first proprietary foundation model, alongside the open-weight Llama family.",
                "impact": "Meta AI reached roughly 1.2 billion monthly active users by Q1 2026, up from 1 "
                          "billion in May 2025; Llama passed 1 billion cumulative downloads",
                "source": "https://www.cnbc.com/2026/04/29/meta-q1-earnings-report-2026.html",
            },
            {
                "sector": "Core business performance",
                "status": "Deployed",
                "deployment": "AI applied to advertising targeting and ranking across Facebook, Instagram "
                              "and WhatsApp \u2014 the mechanism by which the capex is meant to pay back.",
                "impact": "Q1 2026 revenue up 33% to $56.31B, the fastest growth since 2021; ad impressions "
                          "up 19% and average price per ad up 12%",
                "source": "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx",
            },
        ],
        "customer_sentiment": "Meta has no enterprise customer base in the sense the other vendors here do "
                              "\u2014 its customers are advertisers and its models are given away. The "
                              "relevant sentiment is investor sentiment, and it is sceptical: shares fell "
                              "about 7% after Q1 2026 despite beating on revenue and earnings. When "
                              "Zuckerberg described measuring return on the buildout as a technical "
                              "question, several investors read it as an admission that Meta does not yet "
                              "have a clean payback model.",
        "sentiment_bull": [
            "Q1 2026 revenue up 33% to $56.31B, the fastest growth since 2021, with ad impressions up 19% and pricing up 12%",
            "3.56 billion daily active people across the app family \u2014 a distribution base no AI competitor can match",
            "The BlackRock El Paso joint venture shows a workable route to funding capacity without carrying all of it on balance sheet",
            "Open-weight Llama models give enterprises a genuinely free alternative where data residency rules out API providers",
        ],
        "sentiment_bear": [
            "Almost all capex is self-consumed \u2014 unlike Microsoft and Amazon, Meta has no third-party cloud revenue to offset the buildout",
            "Capex guidance raised three times to $135\u2013145B, roughly double 2025, while GPU-heavy assets depreciate over a 4\u20136 year life",
            "Meta extended its depreciation assumption to 5.5 years in 2025, worth nearly $2.9B of reported profit \u2014 an accounting tailwind, not an operating one",
            "Cutting 10% of the workforce while doubling capex is a difficult story to tell internally and externally at the same time",
            "Reality Labs has lost more than $50B cumulatively since 2021 and continues to absorb billions annually",
        ],
        "employee_sentiment": "Meta is cutting about 8,000 roles effective 20 May 2026 \u2014 roughly 10% of "
                              "the workforce \u2014 and leaving a further 6,000 open positions unfilled, the "
                              "largest restructuring since the 2022\u201323 programme that eliminated about "
                              "21,000 roles. Earlier 2026 rounds hit Reality Labs and parts of Facebook, "
                              "global operations and sales. The stated rationale is freeing resources for "
                              "the AI buildout. No independent employer-review data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("2004", "Founded"),
            ("$56.3B", "Q1 2026 revenue"),
            ("+33%", "Revenue growth"),
            ("$135\u2013145B", "2026 capex"),
            ("3.56B", "Daily active people"),
        ],
        "notes": "Capex guidance moved three times during 2026 ($115\u2013135B, then $125\u2013145B, then "
                 "$135\u2013145B). Figures here reflect the latest reviewed; re-run before using externally.",
    },

    # =================================================================
    {
        "slug": "microsoft",
        "name": "Microsoft",
        "website": "https://www.microsoft.com",
        "linkedin": "https://www.linkedin.com/company/microsoft",
        "group": "Frontier AI / LLM",
        "category": "Cloud, enterprise software &amp; AI platform",
        "tagline": "Azure past $100B and accelerating, Copilot seats doubling in two quarters \u2014 funded "
                   "by a capex programme that cut free cash flow by nearly a quarter",
        "founded": "1975",
        "hq": "Redmond, Washington",
        "employees": "Not broken out in the results reviewed; roughly $900M of one-time voluntary retirement "
                     "costs were recorded in Q4 FY2026",
        "ownership": "Public (NASDAQ: MSFT)",
        "revenue": "$331.8B in FY2026 (year ended 30 June 2026), up 18% (16% constant currency), with "
                   "operating income of $155.2B, up 21%, at a record 46.8% operating margin. Microsoft Cloud "
                   "reached $214B for the year, up 27%",
        "revenue_short": "$331.8B (FY26)",
        "offering": "Azure cloud and AI infrastructure, Microsoft 365 and the Copilot family, Dynamics 365 "
                    "for ERP and CRM, GitHub, Fabric for data, and the security portfolio. Nadella has "
                    "stated Microsoft holds royalty-free frontier model IP rights through 2032.",
        "digital_twin": "Via Azure Digital Twins",
        "genai": "Yes (Copilot, Azure AI)",
        "buyer": "CIO, CTO, CISO and business application owners \u2014 typically already under an enterprise agreement",
        "customers": [],
        "people": [
            {"name": "Satya Nadella", "title": "Chairman &amp; Chief Executive Officer"},
            {"name": "Amy Hood", "title": "Executive Vice President &amp; Chief Financial Officer"},
        ],
        "description": "Azure crossed $100B of annual revenue for the first time in FY2026 and accelerated "
                       "to 43% growth in Q4 rather than plateauing. Microsoft 365 Copilot passed 30 million "
                       "paid seats, doubling in two quarters, against a commercial base of roughly 464 "
                       "million seats \u2014 so penetration is still only about 6.5%.",
        "position_note": "Microsoft is the default enterprise AI route for most organisations because the "
                         "commercial relationship already exists \u2014 Copilot lands inside an enterprise "
                         "agreement rather than requiring a new vendor selection. That is genuinely "
                         "important for a portfolio programme: it is the lowest-friction path to individual "
                         "productivity across PortCos, which is one of the three opportunity areas in the "
                         "reference model. Two numbers deserve attention in any negotiation. Copilot "
                         "penetration at roughly 6.5% of eligible seats means Microsoft has enormous "
                         "incentive to discount for volume commitments. And commercial remaining "
                         "performance obligations of $678B, up 84% \u2014 still up 25% excluding OpenAI "
                         "\u2014 mean the demand is broad rather than concentrated in one counterparty.",
        "gip_connection": "No publicly disclosed GIP relationship. Microsoft is near-certain to be present "
                          "across multiple PortCos already through enterprise agreements, so the practical "
                          "question is consolidated licensing terms rather than a first introduction. As "
                          "with the other hyperscalers, its data-centre build-out makes it a counterparty "
                          "to digital infrastructure assets as well as a supplier.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of MSFT only.",
        "use_cases": [
            {
                "sector": "Cloud &amp; AI infrastructure",
                "status": "Deployed",
                "deployment": "Azure and other cloud services, carrying enterprise AI workloads alongside "
                              "core infrastructure, with workloads on infrastructure built two to three "
                              "years ago now generating progressively higher margins.",
                "impact": "Azure surpassed $100B in annual revenue for the first time, growing 41% for the "
                          "year and accelerating to 43% in Q4; Intelligent Cloud full-year operating income "
                          "of $57.0B, up from $44.6B",
                "source": "https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast",
            },
            {
                "sector": "Individual productivity",
                "status": "Deployed",
                "deployment": "Microsoft 365 Copilot embedded across Word, Excel, Teams and Outlook, sold as "
                              "an add-on to existing commercial subscriptions, with a shift toward seats "
                              "plus consumption pricing now under way across GitHub and customer service.",
                "impact": "Passed 30 million paid seats in Q4 FY2026, up from roughly 20 million two "
                          "quarters earlier \u2014 10 million net adds in a single quarter, the fastest since "
                          "the November 2023 launch, at only ~6.5% penetration of ~464 million commercial seats",
                "source": "https://news.alphastreet.com/microsoft-msft-azure-ai-growth-rate-and-enterprise-copilot-monetization/",
            },
            {
                "sector": "Revenue visibility",
                "status": "Deployed",
                "deployment": "Commercial remaining performance obligations \u2014 contracted revenue not "
                              "yet recognised \u2014 tracked as the forward indicator for the capex "
                              "programme.",
                "impact": "$678B at FY2026 close, up 84% year over year with weighted average duration of "
                          "roughly 2.3 years; excluding OpenAI, RPO still grew 25% and commercial bookings "
                          "grew 18%",
                "source": "https://licenseq.com/microsoft-fy26-q4-results-explained/",
            },
            {
                "sector": "Capital programme",
                "status": "Deployed",
                "deployment": "Record capital expenditure directed at AI infrastructure, roughly two thirds "
                              "of it on short-lived assets \u2014 GPUs and CPUs.",
                "impact": "$41B of capex in Q4 FY2026; calendar 2026 capex expectation of approximately "
                          "$175B, revised down from ~$190B purely on a lease reclassification rather than "
                          "any change to investment plans",
                "source": "https://licenseq.com/microsoft-fy26-q4-results-explained/",
            },
        ],
        "customer_sentiment": "The Copilot seat data is the clearest read available and it is strong \u2014 "
                              "doubling in two quarters is the fastest growth since launch. The honest "
                              "counterpoint is that penetration remains around 6.5%, so more than nine in "
                              "ten eligible users have not converted, and Google used exactly that gap as "
                              "its competitive attack line at Cloud Next 2026. Backlog growing 25% even "
                              "excluding OpenAI addresses the concentration-risk objection more "
                              "convincingly than any management commentary.",
        "sentiment_bull": [
            "Azure crossed $100B annually and accelerated to 43% in Q4 \u2014 acceleration, not plateau, against a strong comparable",
            "Record 46.8% operating margin with operating income up 21% to $155.2B while capex nearly doubled",
            "$678B commercial RPO, up 84%; excluding OpenAI it still grew 25%, which dismantles the single-counterparty argument",
            "Copilot at 30 million paid seats with roughly 6.5% penetration \u2014 the upsell runway inside the existing base is enormous",
        ],
        "sentiment_bear": [
            "Free cash flow fell 23% while capex hit a record, with two thirds of that spend on assets Microsoft classifies as short-lived",
            "GAAP profit growth of 31% versus roughly 22% adjusted \u2014 the gap is a $3.2B Anthropic investment gain, not operating performance",
            "From FY2027 Microsoft extends the useful life of data centres and office buildings from 15 to 25 years, which flatters future earnings",
            "Cloud gross margin slipped to 65% from 66% in Q3 as AI workloads mix in",
            "Copilot penetration of about 6.5% can be read as runway or as nine in ten eligible users declining to pay",
        ],
        "employee_sentiment": "Not disclosed in the results reviewed. The one concrete signal is roughly "
                              "$900M of one-time voluntary retirement costs recorded in Q4 FY2026, which "
                              "indicates a meaningful workforce reshaping alongside record profitability. No "
                              "independent employer-review data was gathered in this pass.",
        "glassdoor": None,
        "kpis": [
            ("1975", "Founded"),
            ("$331.8B", "FY2026 revenue"),
            ("$100B+", "Azure annual revenue"),
            ("30M", "Copilot paid seats"),
            ("$678B", "Commercial RPO"),
        ],
    },
]
