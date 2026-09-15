# -*- coding: utf-8 -*-
"""
deep_wave1.py — Research wave 1, completed 15 September 2026.

Each vendor here has been through a real research pass: financials, leadership,
sourced use cases with links, competitive position and three-way sentiment.
Accenture, Adobe, Amazon Web Services.
"""

VENDORS = [
    # =================================================================
    {
        "slug": "accenture",
        "name": "Accenture",
        "website": "https://www.accenture.com",
        "linkedin": "https://www.linkedin.com/company/accenture",
        "group": "SI / Consulting",
        "category": "Global systems integrator &amp; consultancy",
        "tagline": "The largest technology services firm in the world by revenue \u2014 strategy, "
                   "systems integration and managed operations, now organised around AI delivery",
        "founded": "1989 (as Andersen Consulting; renamed Accenture in 2001)",
        "hq": "Dublin, Ireland",
        "employees": "~799,000 (Q3 FY2026)",
        "ownership": "Public (NYSE: ACN)",
        "revenue": "$69.7B in FY2025 (fiscal year ended 31 August 2025), up 7% year over year; "
                   "FY2026 guidance of 2\u20135% local-currency growth",
        "revenue_short": "$69.7B (FY25)",
        "offering": "Strategy &amp; Consulting, Technology, Operations and Song, delivered through "
                    "industry groups and a large offshore delivery network. Its AI delivery runs on "
                    "internal platforms such as GenWizard, and it reports generative and agentic AI "
                    "as a separate revenue line.",
        "digital_twin": "Partner-delivered",
        "genai": "Yes (own P&amp;L line)",
        "buyer": "C-suite of large enterprises \u2014 CEO, COO and CIO",
        "customers": ["Aramco", "EDF Energy (Hinkley Point C)"],
        "people": [
            {"name": "Julie Sweet", "title": "Chair &amp; Chief Executive Officer"},
            {"name": "Karthik Narain", "title": "Group Chief Executive, Technology &amp; Chief Technology Officer"},
            {"name": "John Walsh", "title": "Chief Operating Officer"},
        ],
        "description": "The scale player in technology services: ~799,000 people, $69.7B of FY2025 revenue, "
                       "and $80.6B of new bookings. It has partnered with 195 of its top 200 clients for ten "
                       "years or more, which makes it the default incumbent inside most large enterprises "
                       "rather than a challenger.",
        "position_note": "Accenture and Deloitte are now effectively tied at the top \u2014 Deloitte reported "
                         "$70.5B for the year ended 31 May 2025 against Accenture's $69.67B for the year ended "
                         "31 August 2025, though the fiscal years do not line up. Accenture's differentiator is "
                         "not strategy advice but delivery capacity at scale, and it is the one firm in this set "
                         "that discloses AI as a reported revenue line. For a PE owner the relevant question is "
                         "whether you are buying scarce expertise or rented capacity \u2014 Accenture is "
                         "unambiguously the latter, and priced accordingly.",
        "gip_connection": "No publicly disclosed GIP relationship. Accenture works across every infrastructure "
                          "sector GIP invests in, so any engagement is most likely to arrive through a PortCo's "
                          "existing master services agreement rather than at fund level. Validate internally "
                          "before assuming a clean slate.",
        "blackrock_connection": "No publicly disclosed operating relationship. BlackRock funds hold ACN as a "
                                "standard index position \u2014 a capital-markets fact, not evidence of a "
                                "commercial relationship.",
        "use_cases": [
            {
                "sector": "Energy \u2014 upstream",
                "status": "Deployed",
                "deployment": "Aramco enterprise AI programme: 442 AI use cases identified across operations, "
                              "with more than 200 solutions deployed and 100+ in development as of late 2025, "
                              "spanning reservoir modelling, well placement, drilling optimisation, production "
                              "tuning and predictive maintenance.",
                "impact": "$1.8B in AI-driven realised value recorded in 2024",
                "source": "https://www.accenture.com/us-en/insights/energy/scaling-ai-upstream-energy",
            },
            {
                "sector": "Nuclear \u2014 capital projects",
                "status": "Deployed",
                "deployment": "Hinkley Point C, the UK nuclear project majority owned and operated by EDF "
                              "Energy, combining a nuclear-secure cloud, digital twins and AI-driven analytics "
                              "so that each construction phase informs the next.",
                "impact": "Reduced errors and regulatory friction; accelerated timelines",
                "source": "https://www.accenture.com/us-en/blogs/utilities/how-utilities-accelerate-energy-transition",
            },
            {
                "sector": "Utilities \u2014 benchmark",
                "status": "Research finding",
                "deployment": "Powered for Change 2025 argues for a multigenerational approach to "
                              "infrastructure delivery \u2014 repeatable, standardised designs rather than "
                              "bespoke projects \u2014 with AI used to carry lessons between projects.",
                "impact": "Up to 40% higher success rate on major projects where an integrated digital core "
                          "exists; 30\u201350% cost reduction claimed across successive projects",
                "source": "https://www.accenture.com/content/dam/accenture/final/accenture-com/document-4/Accenture-Powered-For-Change-2025-Report.pdf",
            },
            {
                "sector": "Firm-wide AI business",
                "status": "Deployed",
                "deployment": "Advanced AI reported as its own revenue line since 2023. Cumulative advanced AI "
                              "bookings reached roughly $11.5B across about 11,000 projects, with $4.8B of "
                              "cumulative revenue, and a stated target of 80,000 AI and data professionals by "
                              "the end of FY2026.",
                "impact": "$2.7B FY25 AI revenue (tripled YoY); $5.9B FY25 AI bookings (nearly doubled)",
                "source": "https://www.accenture.com/us-en/about/company/integrated-reporting-financial",
            },
        ],
        "customer_sentiment": "Client retention is the strongest signal in the file \u2014 195 of the top 200 "
                              "clients have been with the firm for a decade or more, and FY2025 produced a "
                              "record 129 quarterly bookings above $100M. The recurring criticism is the one "
                              "that follows every large SI: pyramid staffing means the people who win the work "
                              "are not always the people who deliver it, and buyers who don't write delivery "
                              "seniority into the contract tend to be disappointed.",
        "sentiment_bull": [
            "Only firm in this peer set reporting AI as a disclosed revenue line \u2014 $2.7B in FY25, tripled year over year",
            "$80.6B of FY2025 new bookings with a book-to-bill above 1, and management claiming market-share gains at more than 5x the market",
            "Ecosystem breadth: a top-tier partner to every major cloud and enterprise software vendor, which matters when the client's stack is already fragmented",
            "Delivery capacity is genuinely hard to replicate \u2014 799,000 people is a structural moat against boutique competitors",
        ],
        "sentiment_bear": [
            "Growth has slowed materially: FY2026 guidance of 2\u20135% local currency against 7% delivered in FY2025",
            "A six-month business optimisation programme took a $615M charge in Q4 FY2025, including $344M of severance \u2014 roughly 22,000 roles were cut for staff deemed non-reskillable",
            "Federal business (AFS) is a drag on FY2026 growth, worth about 1.5 points",
            "The AI revenue line is impressive in absolute terms but is still under 4% of total revenue \u2014 the core business is still classic systems integration",
            "Attrition at 14\u201315% annualised makes continuity of named delivery staff a real contracting risk",
        ],
        "employee_sentiment": "Accenture's own January 2026 Pulse of Change survey found worker confidence in "
                              "AI job security had fallen to 48%, down 11 points from summer 2025, and that only "
                              "40% of employees felt ready for AI-augmented work. Voluntary attrition rose to 14% "
                              "in FY2025 with Q4 annualised at 15%. Headcount nonetheless recovered from 779,000 "
                              "to about 799,000 by Q3 FY2026, which points to aggressive hiring in AI and cloud "
                              "roles alongside the cuts elsewhere \u2014 a workforce being replaced rather than shrunk.",
        "glassdoor": None,
        "kpis": [
            ("1989", "Founded"),
            ("799K", "Employees (Q3 FY26)"),
            ("$69.7B", "FY2025 revenue"),
            ("$2.7B", "FY2025 AI revenue"),
            ("$5.9B", "FY2025 AI bookings"),
        ],
    },

    # =================================================================
    {
        "slug": "adobe",
        "name": "Adobe",
        "website": "https://www.adobe.com",
        "linkedin": "https://www.linkedin.com/company/adobe",
        "group": "Enterprise software",
        "category": "Creative, document &amp; marketing software",
        "tagline": "The creative and document software standard, defending its position by embedding "
                   "commercially-safe generative AI across every product",
        "founded": "1982",
        "hq": "San Jose, California",
        "employees": "~31,360 (FY2025 year-end)",
        "ownership": "Public (NASDAQ: ADBE)",
        "revenue": "$23.77B in FY2025, up 11%; total ending ARR of $25.20B (+11.5%). FY2026 guidance of "
                   "$25.9\u201326.1B",
        "revenue_short": "$23.8B (FY25)",
        "offering": "Creative Cloud, Document Cloud and Experience Cloud, with the Firefly generative model "
                    "family embedded across them. Enterprise AI is sold through Firefly Services, Firefly "
                    "Foundry (brand-specific custom models trained on a customer's own IP) and GenStudio. "
                    "Acrobat Studio, released August 2025, folds AI agents into document workflows.",
        "digital_twin": "No",
        "genai": "Yes (Firefly)",
        "buyer": "CMO and creative operations; document workflow owners in enterprise",
        "customers": [],
        "people": [
            {"name": "Shantanu Narayen", "title": "Chair &amp; Chief Executive Officer (transitioning \u2014 see note)"},
        ],
        "description": "The incumbent in creative software, now in the awkward position of being both an AI "
                       "winner and an AI disruption target. AI-influenced ARR passed $5B in FY2025 \u2014 over a "
                       "third of the total base \u2014 while the market prices the stock at a decade-low forward "
                       "multiple on the view that generative tools will erode the moat.",
        "position_note": "Adobe's defensible claim is provenance, not capability: its models are trained on "
                         "content it owns or has licensed, which makes output commercially safe in a way that "
                         "matters to regulated buyers and to anyone indemnifying downstream use. It has also "
                         "stopped insisting Firefly be the only option \u2014 the Generative Media Tool in "
                         "Premiere lets users pick Google Veo, Kling, Runway or Luma instead. That is a "
                         "confident move if the platform is the moat and a concession if the model was.",
        "gip_connection": "No publicly disclosed GIP relationship. Adobe's relevance to an infrastructure "
                          "portfolio is corporate-function rather than asset-level \u2014 marketing, documents "
                          "and contract workflows \u2014 which places it in the Individual Productivity and "
                          "Corporate Functions Efficiency areas of the reference model, not Asset Optimization.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings only.",
        "use_cases": [
            {
                "sector": "Enterprise AI monetisation",
                "status": "Deployed",
                "deployment": "AI-first ARR \u2014 revenue from products that exist only because of generative "
                              "AI, as distinct from AI-influenced ARR across the wider base.",
                "impact": "Crossed $500M in Q2 FY2026, tripled year over year",
                "source": "https://www.marketscale.com/industries/software-and-technology/adobes-firefly-driven-ai-first-arr-has-tripled-signaling-a-shift-from-disruption-target-to-monetization-platform",
            },
            {
                "sector": "Enterprise AI monetisation",
                "status": "Deployed",
                "deployment": "AI-influenced ARR across Creative Cloud, Document Cloud and Experience Cloud, "
                              "monetised through generative credits and higher-tier subscriptions.",
                "impact": "Surpassed $5B at FY2025 close \u2014 more than one third of total ARR",
                "source": "https://sqmagazine.co.uk/adobe-creative-cloud-statistics/",
            },
            {
                "sector": "Media \u2014 custom models",
                "status": "Deployed",
                "deployment": "Firefly Foundry trains brand-specific models on a customer's own content, "
                              "guidelines and IP across image, video, audio and 3D, then runs them as a managed "
                              "service. A media customer added it on top of an existing creative relationship.",
                "impact": "~$7M incremental services sale layered on roughly $10M of existing creative ARR; "
                          "models trained in two to three months",
                "source": "https://futurumgroup.com/insights/adobe-q4-fy-2025-record-revenue-ai-adoption-arr-targets/",
            },
            {
                "sector": "Product adoption",
                "status": "Deployed",
                "deployment": "Firefly generation volume since the March 2023 launch, disclosed at Adobe MAX 2025.",
                "impact": "Over 24 billion assets generated; Photoshop monthly active users up ~10% after Firefly rollout",
                "source": "https://sqmagazine.co.uk/adobe-statistics/",
            },
        ],
        "customer_sentiment": "Enterprise traction is the clearer half of the story: record bookings on deals "
                              "above $1M in Q4 FY2025 and over 25% year-over-year growth in that cohort. The "
                              "friction point with customers is pricing mechanics rather than capability \u2014 "
                              "the generative-credit model makes spend hard to forecast, and Creative Cloud Pro "
                              "at $69.99/month keeps the total cost of a creative seat under permanent review.",
        "sentiment_bull": [
            "AI-influenced ARR above $5B and AI-first ARR past $500M and tripling \u2014 monetisation is real, not a roadmap",
            "Licensed and owned training data makes output commercially safe, which is a genuine differentiator for regulated and brand-sensitive buyers",
            "FY2025 free cash flow above $10B funds buybacks and R&amp;D without dilution",
            "Opening Premiere to third-party models (Veo, Kling, Runway, Luma) suggests confidence that distribution, not the model, is the moat",
        ],
        "sentiment_bear": [
            "The market is pricing disruption: a forward P/E around 12\u201314x is a ten-year low for this business",
            "CEO succession is unresolved \u2014 Shantanu Narayen announced on 12 March 2026 that he will transition once a successor is appointed, and shares fell 7% on the news",
            "AI-first ARR, while growing fast, is roughly 2% of total ARR \u2014 the base business still carries the company",
            "Generative competitors attack the entry tier hardest, where switching costs are lowest",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 no reliable employer-review data was gathered. "
                              "Headcount was approximately 31,360 at FY2025 year-end. Treat as a gap rather than "
                              "a positive signal.",
        "glassdoor": None,
        "kpis": [
            ("1982", "Founded"),
            ("31.4K", "Employees"),
            ("$23.8B", "FY2025 revenue"),
            ("$25.2B", "Ending ARR"),
            ("$5B+", "AI-influenced ARR"),
        ],
        "notes": "Chief Technology Officer was not confirmed in this research pass and has deliberately been "
                 "left off the contact list rather than guessed. CEO succession is live \u2014 re-run this "
                 "vendor's pass once a successor is named.",
    },

    # =================================================================
    {
        "slug": "aws",
        "name": "Amazon Web Services",
        "website": "https://aws.amazon.com",
        "linkedin": "https://www.linkedin.com/company/amazon-web-services",
        "group": "Frontier AI / LLM",
        "category": "Cloud infrastructure &amp; AI platform",
        "tagline": "The largest cloud provider, converting a decade of custom-silicon investment into an "
                   "AI cost advantage",
        "founded": "2006",
        "hq": "Seattle, Washington (Amazon.com, Inc.)",
        "employees": "Not disclosed separately from Amazon",
        "revenue": "$37.59B in Q1 2026 \u2014 roughly a $150B annualised run rate \u2014 up from $29.27B a year "
                   "earlier, the fastest growth in 15 quarters. AI revenue was cited at a $15B+ run rate in "
                   "Q1 2026 and at $25B by August 2026",
        "revenue_short": "~$150B (annualised)",
        "ownership": "Segment of Amazon.com, Inc. (NASDAQ: AMZN)",
        "offering": "Cloud infrastructure across 120 availability zones in 38 regions with 200+ services. The "
                    "AI stack is Bedrock (managed multi-model inference), SageMaker (training), the Nova model "
                    "family, and custom silicon \u2014 Trainium for AI, Graviton for CPU, Nitro for "
                    "virtualisation.",
        "digital_twin": "Via partners (IoT TwinMaker)",
        "genai": "Yes (Bedrock, Nova)",
        "buyer": "CIO, CTO and platform engineering leadership",
        "customers": ["Anthropic", "OpenAI", "Meta"],
        "people": [
            {"name": "Matt Garman", "title": "Chief Executive Officer, AWS"},
            {"name": "Andy Jassy", "title": "President &amp; Chief Executive Officer, Amazon (AWS founder)"},
        ],
        "description": "Holds about 28% of global cloud infrastructure against Azure's 21% and Google Cloud's "
                       "14%. The structural story is vertical integration: custom chips built over a decade now "
                       "carry the majority of Bedrock inference, which converts directly into margin and price "
                       "advantage as workloads shift from training to inference.",
        "position_note": "AWS is the default substrate rather than a differentiated AI vendor \u2014 for an "
                         "infrastructure portfolio the decision is rarely whether to use it but how much "
                         "concentration risk to accept. The genuinely distinctive asset is Trainium: it powers "
                         "more than 50% of Bedrock token usage, saves customers 20\u201330% on inference against "
                         "market alternatives, and underpins a chip portfolio past a $20B annual run rate. "
                         "The offsetting fact is that capacity is booked out to 2028, which weakens the buyer's "
                         "negotiating position rather than strengthening it.",
        "gip_connection": "No publicly disclosed fund-level relationship. AWS is near-certain to already be "
                          "present inside multiple PortCos, so the practical question is consolidated commercial "
                          "terms across the portfolio rather than a first introduction. AWS's own data-centre "
                          "build-out also makes it a counterparty to digital-infrastructure assets, not only a "
                          "supplier \u2014 worth mapping before any portfolio-level negotiation.",
        "blackrock_connection": "No publicly disclosed operating relationship; standard index holdings of AMZN only.",
        "use_cases": [
            {
                "sector": "AI platform",
                "status": "Deployed",
                "deployment": "Amazon Bedrock, the managed multi-model inference service hosting Anthropic, "
                              "Meta, Mistral, OpenAI and Amazon's own Nova models.",
                "impact": "Processed more tokens in Q1 2026 than in all prior years combined; customer spend up "
                          "170% quarter over quarter",
                "source": "https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-aws-ai-q1-2026-earnings",
            },
            {
                "sector": "Custom silicon",
                "status": "Deployed",
                "deployment": "Trainium accelerators for training and inference, sold as capacity rather than "
                              "chips, alongside continued NVIDIA GPU availability.",
                "impact": "Powers over 50% of Bedrock token usage; 20\u201330% inference cost saving; Trainium2 "
                          "~30% better price-performance than comparable GPUs, Trainium3 a further 30\u201340%",
                "source": "https://newsletter.semianalysis.com/p/anthropic-growth-and-bedrock-mix",
            },
            {
                "sector": "Digital infrastructure",
                "status": "Announced",
                "deployment": "Data-centre build-out: $15B committed to Northern Indiana facilities delivering "
                              "2.4 GW (December 2025) and a $7B, 14-year framework agreement with Telangana, "
                              "India to expand the Hyderabad footprint.",
                "impact": "2026 capital expenditure guided to $200B, later raised to $220B",
                "source": "https://sqmagazine.co.uk/aws-statistics/",
            },
            {
                "sector": "Frontier AI compute",
                "status": "Announced",
                "deployment": "Expanded Anthropic collaboration (March 2026) covering up to 5 gigawatts of "
                              "current and future Trainium capacity for frontier model training.",
                "impact": "Contributes to $364B contracted backlog, up 40% year over year; Trainium revenue "
                          "commitments alone exceed $225B",
                "source": "https://axis-intelligence.com/aws-statistics/",
            },
        ],
        "customer_sentiment": "Demand is outrunning supply, which is the clearest possible demand signal and "
                              "the worst possible negotiating environment. Garman has said Trainium is largely "
                              "sold out through the end of next year, that AWS is securing five-year customer "
                              "commitments, and that capacity is booked through 2028. Buyers report the expected "
                              "trade-off \u2014 unmatched breadth and availability against egress economics and "
                              "the gravitational pull of a single provider.",
        "sentiment_bull": [
            "Re-accelerating: Q1 2026 revenue up from $29.27B to $37.59B, the steepest growth in 15 quarters",
            "Vertical integration is showing up in the P&amp;L \u2014 custom silicon past a $20B run rate, with management claiming several hundred basis points of margin advantage on inference versus third-party chips",
            "$364B contracted backlog, up 40% year over year, de-risks the capex programme",
            "Operating income of $14.16B in Q1 2026, up about 23% and ahead of consensus by roughly $1.3B",
        ],
        "sentiment_bear": [
            "$200\u2013220B of 2026 capital expenditure front-loads spend ahead of monetisation and compresses free cash flow",
            "Capacity sold out through 2028 removes buyer leverage and slows onboarding for new workloads",
            "Concentration risk cuts both ways \u2014 much of the AI revenue growth traces to a small number of frontier-lab counterparties",
            "Management's $600B-by-2036 revenue projection is a useful signal of ambition, not a forecast to plan against",
        ],
        "employee_sentiment": "Not covered in this pass \u2014 AWS does not report headcount separately from "
                              "Amazon, and employer-review data for Amazon as a whole is dominated by the "
                              "fulfilment workforce and would not fairly represent AWS. Treat as a gap.",
        "glassdoor": None,
        "kpis": [
            ("2006", "Founded"),
            ("~28%", "Global cloud share"),
            ("$37.6B", "Q1 2026 revenue"),
            ("$25B", "AI revenue run rate"),
            ("$364B", "Contracted backlog"),
        ],
    },
]
