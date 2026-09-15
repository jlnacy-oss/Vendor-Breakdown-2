# -*- coding: utf-8 -*-
"""
people_wave10.py — Person research wave 10, completed 15 September 2026.

IBM watsonx, Meta and Microsoft leadership.

PROFESSIONAL, PUBLISHED INFORMATION ONLY. See people_schema.py.
Sources carried net worth, dates of birth, spouses, parents' occupations and
private residences. None of it is here.

This wave corrected one vendor record: Alexandr Wang's title is Chief AI Officer,
Meta's first, not simply lead of Meta Superintelligence Labs.
"""

RESEARCHED_ON = "2026-09-15"

PEOPLE = [
    # ================================================= IBM watsonx
    {
        "id": "ibm-watsonx-rob-thomas",
        "vendor_slug": "ibm-watsonx",
        "name": "Rob Thomas",
        "title": "Senior Vice President, Software &amp; Chief Commercial Officer",
        "in_role_since": "SVP of Software and Chief Commercial Officer since 2023",
        "focus": "Runs IBM's software business \u2014 product management, design, development and business "
                 "development \u2014 and carries global responsibility for IBM revenue and profit, "
                 "including worldwide sales, strategic partnerships and the ecosystem.",
        "background": "The single most important commercial counterpart at IBM after Krishna, and a "
                      "twenty-plus-year insider who built the business watsonx now sits on. He has held "
                      "roles across IBM Consulting, IBM Microelectronics and IBM Software, including two "
                      "years based in Tokyo. He joined the software business in 2007 focused on data and "
                      "analytics, and led IBM's transition from databases to broader analytical "
                      "capabilities, its investment in open source, and eventually its move into "
                      "artificial intelligence. He was SVP of Cloud and Data Platform, then SVP of IBM "
                      "Global Markets \u2014 responsible for revenue, profit, business development and "
                      "client success worldwide \u2014 before taking on Software and the Chief Commercial "
                      "Officer role. He has overseen numerous IBM acquisitions, which his own account puts "
                      "at over $20 billion of transaction value, and co-authored <i>Big Data Revolution</i>.",
        "career": [
            {"period": "2023\u2013present", "role": "Senior Vice President, Software &amp; Chief Commercial Officer", "org": "IBM"},
            {"period": "before 2023", "role": "Senior Vice President, IBM Global Markets", "org": "IBM"},
            {"period": "earlier", "role": "Senior Vice President, Cloud and Data Platform", "org": "IBM Software"},
            {"period": "2007\u2013", "role": "Data and analytics \u2014 product engineering and business development", "org": "IBM Software"},
            {"period": "earlier", "role": "Roles across IBM Consulting and IBM Microelectronics, including two years in Tokyo", "org": "IBM"},
        ],
        "education": ["Vanderbilt University"],
        "public_roles": ["Co-author, <i>Big Data Revolution</i>"],
        "notable": [
            {"point": "Has overseen IBM acquisitions representing over $20 billion of transaction value, "
                      "and led the company's transition from databases through analytics and open source "
                      "into AI \u2014 the lineage that produced watsonx.",
             "source": "https://www.robdthomas.com/about"},
            {"point": "Holds both the software P&amp;L and global commercial responsibility for IBM revenue "
                      "and profit, so product roadmap and commercial terms sit in one seat.",
             "source": "https://www.ibm.com/investor/governance/senior-leadership"},
        ],
        "talking_points": [
            "Product and commerce in one person \u2014 he can commit on both capability and price without escalating.",
            "He built the data and analytics business that watsonx descends from, so the data-foundation argument is his own history rather than a pitch.",
            "He writes publicly about agents acting rather than advising, and about data lagging behind agent decisions. That is a good opening if data readiness is your concern.",
        ],
        "links": [
            {"label": "IBM senior leadership", "url": "https://www.ibm.com/investor/governance/senior-leadership"},
            {"label": "Personal professional site", "url": "https://www.robdthomas.com/about"},
        ],
    },

    # ================================================= Meta
    {
        "id": "meta-mark-zuckerberg",
        "vendor_slug": "meta",
        "name": "Mark Zuckerberg",
        "title": "Founder, Chairman &amp; Chief Executive Officer",
        "in_role_since": "Founded the company in 2004 and has led it since; renamed Meta in 2021",
        "focus": "Sets Meta's direction and personally drives the AI programme \u2014 2026 capital "
                 "expenditure guidance of $135\u2013145B, the Meta Superintelligence Labs structure, and "
                 "the shift from open-weight Llama toward proprietary frontier models.",
        "background": "He founded Facebook in 2004 and has run it for more than two decades, through "
                      "successive platform bets \u2014 mobile, then the metaverse pivot that renamed the "
                      "company in 2021 and absorbed tens of billions into Reality Labs, and now "
                      "superintelligence. Reporting describes him personally recruiting AI researchers, "
                      "meeting candidates at his own homes to assemble a team of around fifty, and "
                      "maintaining close control over AI initiatives \u2014 which some employees are "
                      "reported to feel limits experimentation. In March 2026 he restructured engineering "
                      "teams and AI research divisions again.",
        "career": [
            {"period": "2021\u2013present", "role": "Founder, Chairman &amp; Chief Executive Officer", "org": "Meta Platforms, Inc."},
            {"period": "2004\u20132021", "role": "Founder, Chairman &amp; Chief Executive Officer", "org": "Facebook, Inc. (renamed Meta in 2021)"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "The $14B El Paso data centre joint venture with BlackRock funds at 80% ownership "
                      "was struck under him, and lets Meta de-consolidate significant capital expenditure "
                      "\u2014 the most directly GIP-adjacent transaction of any vendor tracked here.",
             "source": "https://aibusinessweekly.net/p/meta-ai-statistics"},
            {"point": "Raised 2026 capex guidance three times to $135\u2013145B while cutting roughly 10% "
                      "of the workforce, and described measuring return on the buildout as a technical "
                      "question \u2014 which investors read as an absent payback model.",
             "source": "https://valueaddvc.com/blog/meta-145b-ai-capex-2026-why-zuckerberg-raised-guidance-twice"},
        ],
        "talking_points": [
            "Meta is not a vendor to you \u2014 it sells advertising and gives Llama away. It matters as a counterparty and a demand driver.",
            "The BlackRock El Paso structure is the precedent other operators will now be asked about. Understand it internally before any conversation.",
            "He has pivoted the company twice in five years. Treat strategic commitments as contingent on the current bet holding.",
        ],
        "links": [
            {"label": "Meta Q1 2026 results", "url": "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/default.aspx"},
            {"label": "Capex analysis", "url": "https://valueaddvc.com/blog/meta-145b-ai-capex-2026-why-zuckerberg-raised-guidance-twice"},
        ],
    },
    {
        "id": "meta-alexandr-wang",
        "vendor_slug": "meta",
        "name": "Alexandr Wang",
        "title": "Chief AI Officer",
        "in_role_since": "Joined Meta in June 2025 as its first-ever Chief AI Officer, leading Meta Superintelligence Labs",
        "focus": "Shapes Meta's AI vision and drives its strategic initiatives from concept to execution, "
                 "leading Meta Superintelligence Labs alongside Meta's other AI product and research teams.",
        "background": "A founder rather than a corporate executive, and he arrived through one of the "
                      "largest acqui-hires in the industry's history. He founded Scale AI in 2016 as a "
                      "19-year-old MIT student, building it in a Silicon Valley pool house through Y "
                      "Combinator with co-founder Lucy Guo. Scale became the data and infrastructure layer "
                      "behind most leading models across the industry and reached a valuation of nearly "
                      "$29 billion. In June 2025 Meta invested $14.3 billion for a 49% stake in Scale and "
                      "brought Wang in to lead the newly created Meta Superintelligence Labs; he remained "
                      "on Scale's board. His team delivered Muse Spark in April 2026, Meta's first "
                      "proprietary foundation model and a departure from its strict open-weight approach. "
                      "He has called it an appetiser for larger models to come.",
        "career": [
            {"period": "2025\u2013present", "role": "Chief AI Officer; lead of Meta Superintelligence Labs", "org": "Meta"},
            {"period": "2016\u20132025", "role": "Founder &amp; Chief Executive Officer", "org": "Scale AI"},
        ],
        "education": ["Massachusetts Institute of Technology (left to found Scale AI)"],
        "public_roles": ["Board of Directors, Scale AI"],
        "notable": [
            {"point": "Built Scale AI into the data infrastructure layer behind most leading models in the "
                      "industry, at a valuation near $29 billion, before Meta invested $14.3 billion for a "
                      "49% stake to bring him in.",
             "source": "https://www.meta.com/about/leadership/alexandr-wang/"},
            {"point": "In March 2026 Zuckerberg restructured engineering and AI research divisions, "
                      "changing Wang's responsibilities. Meta has not indicated he is leaving; the stated "
                      "intent is to strengthen AI development.",
             "source": "https://www.wionews.com/technology/meta-ai-chief-alexandr-wang-s-role-evolves-as-mark-zuckerberg-restructures-ai-leadership-1773040904464"},
        ],
        "talking_points": [
            "His actual expertise is data infrastructure for training models \u2014 closer to the Data Foundation problem than to applications.",
            "Meta's model strategy shifted under him from strictly open-weight to proprietary. If a PortCo's case rests on open weights, test how durable that is.",
            "His remit was restructured in March 2026. Confirm who owns what before relying on any commitment.",
        ],
        "links": [
            {"label": "Meta leadership page", "url": "https://www.meta.com/about/leadership/alexandr-wang/"},
            {"label": "Muse Spark and the year in review", "url": "https://www.cnbc.com/2026/06/14/meta-hired-alexandr-wang-to-build-ai-its-zuckerbergs-job-to-sell-it.html"},
        ],
        "notes": "The vendor record described him as \"Lead, Meta Superintelligence Labs\". His actual "
                 "title is Chief AI Officer, Meta's first; the vendor page has been corrected.",
    },

    # ================================================= Microsoft
    {
        "id": "microsoft-satya-nadella",
        "vendor_slug": "microsoft",
        "name": "Satya Nadella",
        "title": "Chairman &amp; Chief Executive Officer",
        "in_role_since": "CEO since February 2014; Chairman since 2021",
        "focus": "Leads Microsoft through the AI platform shift \u2014 Azure past $100B and accelerating, "
                 "Copilot at 30 million paid seats, and a capital programme of roughly $175B for calendar "
                 "2026.",
        "background": "A long-serving insider who came up through the enterprise businesses, which is why "
                      "the cloud pivot worked. He ran the Server and Tools business before becoming CEO, "
                      "and is widely credited with shifting Microsoft's culture from what he describes as "
                      "know-it-all to learn-it-all. The strategic pattern he is known for is funding new "
                      "businesses long before they become growth businesses \u2014 most visibly throttling "
                      "back the Windows franchise to pay for the cloud investment that now underpins the "
                      "company. He has stated that Microsoft holds royalty-free frontier model IP rights "
                      "through 2032.",
        "career": [
            {"period": "2014\u2013present", "role": "Chief Executive Officer (Chairman from 2021)", "org": "Microsoft"},
            {"period": "before 2014", "role": "Executive Vice President, Cloud and Enterprise; led Server and Tools", "org": "Microsoft"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Describes capital allocation as giving oxygen to new businesses long before they "
                      "become growth businesses \u2014 the logic behind throttling Windows to fund cloud, "
                      "and now behind the AI capex programme.",
             "source": "https://fortune.com/ranking/businessperson-of-the-year/2019/satya-nadella"},
            {"point": "Oversaw FY2026 revenue of $331.8B at a record 46.8% operating margin, with "
                      "commercial remaining performance obligations of $678B \u2014 still up 25% excluding "
                      "OpenAI.",
             "source": "https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast"},
        ],
        "talking_points": [
            "Enterprise-bred, not consumer \u2014 a conversation about deployment across a fragmented portfolio is his natural territory.",
            "Copilot penetration is roughly 6.5% of eligible seats. He knows the upsell runway is the story; volume commitments are where the leverage is.",
            "Escalation point above the account team, not a working counterpart. Reserve for portfolio-scale licensing.",
        ],
        "links": [
            {"label": "Microsoft FY2026 Q4 results", "url": "https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast"},
            {"label": "Fortune profile", "url": "https://fortune.com/ranking/businessperson-of-the-year/2019/satya-nadella"},
        ],
    },
    {
        "id": "microsoft-amy-hood",
        "vendor_slug": "microsoft",
        "name": "Amy Hood",
        "title": "Executive Vice President &amp; Chief Financial Officer",
        "in_role_since": "CFO since 2013 \u2014 the first woman to hold the role at Microsoft",
        "focus": "Leads Microsoft's worldwide finance organisation \u2014 business operations, "
                 "acquisitions, treasury, tax, global real estate, accounting and reporting, internal audit "
                 "and investor relations \u2014 and steers the company's AI spending.",
        "background": "An investment banker turned operator, and Nadella's principal strategic partner for "
                      "more than a decade. She joined Microsoft in 2002 from Goldman Sachs, where she "
                      "worked in investment banking and capital markets, and held roles in investor "
                      "relations, as chief of staff in the Server and Tools business, and running strategy "
                      "and business development in the Business division \u2014 where she helped lead the "
                      "transition to Office 365 and worked on the Skype acquisition. After the COO role "
                      "was vacated she also took on worldwide licensing and pricing. She has been "
                      "materially involved in LinkedIn, GitHub and Activision Blizzard, and Nadella "
                      "publicly credits her with an outsize strategic role in capital allocation. She is "
                      "reported to challenge projects when colleagues, including the CEO, get carried "
                      "away.",
        "career": [
            {"period": "2013\u2013present", "role": "Executive Vice President &amp; Chief Financial Officer", "org": "Microsoft"},
            {"period": "before 2013", "role": "CFO of the Business division; strategy and business development", "org": "Microsoft"},
            {"period": "earlier", "role": "Chief of staff, Server and Tools Business; investor relations", "org": "Microsoft"},
            {"period": "before 2002", "role": "Investment banking and capital markets", "org": "Goldman Sachs"},
        ],
        "education": [
            "MBA, Harvard University",
            "BA Economics, Duke University",
        ],
        "public_roles": ["Board of Directors, 3M (since 2017)"],
        "notable": [
            {"point": "Took on responsibility for worldwide licensing and pricing after the COO role was "
                      "vacated \u2014 which makes her the person who owns how Microsoft prices to large "
                      "customers, not just how it reports.",
             "source": "https://fortune.com/ranking/most-powerful-women/2016/amy-hood"},
            {"point": "Nadella credits her with an outsize strategic role in capital allocation \u2014 "
                      "including the decision to throttle Windows to fund the cloud \u2014 and she is "
                      "described as willing to challenge projects even when the CEO is enthusiastic.",
             "source": "https://fortune.com/ranking/businessperson-of-the-year/2019/satya-nadella"},
        ],
        "talking_points": [
            "Licensing and pricing sit with her. For a portfolio-wide Microsoft agreement she is the substantive counterpart, not the account team.",
            "Ex-Goldman investment banker \u2014 expect a rigorous, numbers-led negotiation and prepare accordingly.",
            "Free cash flow fell 23% in FY2026 while capex hit a record. She owns that tension and will have a considered answer.",
        ],
        "links": [
            {"label": "Fortune Most Powerful Women profile", "url": "https://dc.fortune.com/ranking/most-powerful-women/2024/amy-hood/"},
            {"label": "Microsoft FY2026 Q4 results", "url": "https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast"},
        ],
    },
]
