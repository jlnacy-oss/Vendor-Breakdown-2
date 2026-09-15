# -*- coding: utf-8 -*-
"""
people_wave13.py — Person research wave 13, completed 15 September 2026.

Perplexity, PwC and Salesforce leadership.

PROFESSIONAL, PUBLISHED INFORMATION ONLY. See people_schema.py.
Sources in this wave carried dates of birth, national origin, family religion,
race, dietary practice and accounts of personal experiences of discrimination.
None of it is here. Where a leadership first is a professional fact about the
firm's history rather than about the person's protected characteristics, it is
recorded as the former.
"""

RESEARCHED_ON = "2026-09-15"

PEOPLE = [
    # ================================================= Perplexity
    {
        "id": "perplexity-aravind-srinivas",
        "vendor_slug": "perplexity",
        "name": "Aravind Srinivas",
        "title": "Co-Founder &amp; Chief Executive Officer",
        "in_role_since": "Co-founded Perplexity in August 2022 and has led it since",
        "focus": "Leads Perplexity's product and strategy, including the citation-first answer engine, the "
                 "Comet agentic browser, and the publisher revenue-share programme.",
        "background": "One of very few people to have done research at all three leading AI labs, which is "
                      "the origin of Perplexity's model-agnostic design. He took a dual degree at IIT "
                      "Madras and a PhD in computer science at UC Berkeley under Pieter Abbeel, publishing "
                      "on contrastive learning, vision transformers, diffusion generative models and "
                      "reinforcement learning. Along the way he interned at OpenAI in 2018 on policy "
                      "gradient algorithms, at DeepMind in 2019 on large-scale contrastive learning, and "
                      "at Google Research in 2020 and 2021 on vision models including Bottleneck "
                      "Transformers and HaloNet. He joined OpenAI as a research scientist in 2021, working "
                      "on language models and diffusion generative models and contributing to DALL-E 2, "
                      "and left in 2022 to co-found Perplexity with Denis Yarats, Andy Konwinski and "
                      "Johnny Ho. He also taught deep unsupervised learning at Berkeley.",
        "career": [
            {"period": "2022\u2013present", "role": "Co-Founder &amp; Chief Executive Officer", "org": "Perplexity"},
            {"period": "2021\u20132022", "role": "Research Scientist \u2014 language models and diffusion generative models", "org": "OpenAI"},
            {"period": "2020\u20132021", "role": "Research intern \u2014 vision models", "org": "Google Research"},
            {"period": "2019", "role": "Research intern \u2014 large-scale contrastive learning", "org": "DeepMind"},
            {"period": "2018", "role": "Research intern \u2014 policy gradient algorithms", "org": "OpenAI"},
        ],
        "education": [
            "PhD Computer Science, University of California, Berkeley (advised by Pieter Abbeel)",
            "BTech and MS, Indian Institute of Technology Madras",
        ],
        "public_roles": ["Taught deep unsupervised learning courses at UC Berkeley"],
        "notable": [
            {"point": "Had simultaneous visibility into OpenAI, DeepMind and Google Brain roadmaps between "
                      "2019 and 2022 \u2014 the rare vantage point behind Perplexity's deliberately "
                      "model-agnostic product strategy, which avoids foundational-model lock-in.",
             "source": "https://perplexityaimagazine.com/perplexity-hub/aravind-srinivas-perplexity-ceo/"},
            {"point": "Advocates a citation-first approach \u2014 verifiable answers rather than links "
                      "\u2014 and launched a Publishers Program sharing revenue with the outlets "
                      "Perplexity cites, while the company faces active scraping litigation.",
             "source": "https://en.wikipedia.org/wiki/Aravind_Srinivas"},
        ],
        "talking_points": [
            "A researcher-founder who buys inference rather than training frontier models \u2014 the model-agnostic argument is his genuine position, not a hedge.",
            "Citation-first matters for any use where output has to be auditable. That is the case worth testing for research-heavy roles at PortCos.",
            "Publisher litigation is unresolved and material to enterprise adoption. He launched the revenue-share programme in response; ask where that now stands.",
        ],
        "links": [
            {"label": "Forbes profile", "url": "https://www.forbes.com/profile/aravind-srinivas/"},
            {"label": "TechCrunch author profile", "url": "https://techcrunch.com/author/aravind-srinivas"},
            {"label": "Career analysis", "url": "https://perplexityaimagazine.com/perplexity-hub/aravind-srinivas-perplexity-ceo/"},
        ],
    },

    # ================================================= PwC
    {
        "id": "pwc-mohamed-kande",
        "vendor_slug": "pwc",
        "name": "Mohamed Kande",
        "title": "Global Chairman",
        "in_role_since": "Selected December 2023; four-year term began 1 July 2024, succeeding Bob Moritz",
        "focus": "Leads the PwC network's integrated Network Leadership Team across more than 364,000 "
                 "people in 151 countries, with AI capability, alliances and managed services as his "
                 "investment priorities.",
        "background": "An electrical engineer turned consultant, and the first consulting partner to lead "
                      "a network that has traditionally been audit-led \u2014 a structural fact about PwC "
                      "worth understanding. He joined PwC in August 2011 from PRTM Management Consultants, "
                      "where he was managing partner for Europe, the Middle East and South Asia, and "
                      "before that worked at Motorola in Chicago and DTI Telecom in Canada. At PwC he led "
                      "advisory for technology, media, telecoms and hospitality, became CEO of the "
                      "combined consulting businesses in the US, Mexico and Japan, and served as Global "
                      "Advisory Leader from 2019 \u2014 where he drove the network's alliance strategy and "
                      "was executive sponsor for its investments in generative AI, managed services and "
                      "business model reinvention. He has over 32 years of professional services "
                      "experience and became a licensed CPA in 2022.",
        "career": [
            {"period": "2024\u2013present", "role": "Global Chairman", "org": "PwC"},
            {"period": "2019\u20132024", "role": "Global Advisory Leader; co-leader, US Consulting Solutions", "org": "PwC"},
            {"period": "earlier", "role": "Chief Executive Officer, combined consulting businesses in the US, Mexico and Japan", "org": "PwC"},
            {"period": "earlier", "role": "US and Global Advisory Leader, technology, media, telecoms and hospitality", "org": "PwC"},
            {"period": "before 2011", "role": "Managing Partner, Europe, Middle East and South Asia", "org": "PRTM Management Consultants"},
            {"period": "earlier", "role": "Engineering and commercial roles", "org": "Motorola (Chicago) and DTI Telecom (Canada)"},
        ],
        "education": [
            "MBA, University of Chicago",
            "MS Electrical Engineering, University of Montreal",
            "Dipl\u00f4me d'ing\u00e9nieur, Electrical Engineering, ESIGELEC, France",
            "Licensed CPA, Washington D.C. (2022)",
        ],
        "public_roles": [],
        "notable": [
            {"point": "The first consulting partner to lead PwC's global network, which has traditionally "
                      "been audit-led \u2014 a structural shift in where the firm's centre of gravity sits.",
             "source": "https://www.consultancy.uk/news/35829/mohamed-kande-in-line-to-become-pwc-global-chair"},
            {"point": "Was executive sponsor for PwC's generative AI, managed services and business model "
                      "reinvention investments before taking the chair, and drove its alliance strategy "
                      "\u2014 so the $1.5B AI programme is his own.",
             "source": "https://www.pwc.com/gx/en/news-room/press-releases/2023/pwc-selects-mohamed-kande-as-next-global-chair.html"},
        ],
        "talking_points": [
            "An engineer by training in a network of accountants \u2014 he will engage on technology substance further than a typical Big Four chair.",
            "He built PwC's alliance strategy, so which technology partner PwC would deliver on is a question he can answer definitively.",
            "He has said publicly that PwC cannot hire enough AI engineers. Delivery capacity, not capability, is the constraint to probe.",
        ],
        "links": [
            {"label": "PwC appointment announcement", "url": "https://www.pwc.com/gx/en/news-room/press-releases/2023/pwc-selects-mohamed-kande-as-next-global-chair.html"},
            {"label": "Milken Institute profile", "url": "https://milkeninstitute.org/events/global-conference-2026/speakers/mohamed-kande"},
            {"label": "Accounting Today coverage", "url": "https://www.accountingtoday.com/news/pwc-names-mohammed-kande-as-new-global-chair"},
        ],
    },

    # ================================================= Salesforce
    {
        "id": "salesforce-marc-benioff",
        "vendor_slug": "salesforce",
        "name": "Marc Benioff",
        "title": "Chair &amp; Chief Executive Officer",
        "in_role_since": "Co-founded Salesforce in 1999 and has led it since",
        "focus": "Sets Salesforce's strategy, currently the repositioning of the entire company around "
                 "Agentforce and the shift from seat-based licensing toward measuring and pricing work "
                 "delivered.",
        "background": "He founded Salesforce in 1999 after thirteen years at Oracle, where he began his "
                      "career, and built the company on the argument that enterprise software should be "
                      "delivered as a service rather than installed. He has run it for more than a quarter "
                      "of a century through successive platform shifts \u2014 cloud, mobile, social, and "
                      "now agents \u2014 and has grown it by acquisition as much as organically, including "
                      "Tableau, MuleSoft, Slack and, in November 2025, Informatica.",
        "career": [
            {"period": "1999\u2013present", "role": "Co-Founder, Chair &amp; Chief Executive Officer", "org": "Salesforce"},
            {"period": "1986\u20131999", "role": "Sales, marketing and product roles over thirteen years", "org": "Oracle"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Introduced Agentic Work Units as a reported metric \u2014 2.4 billion delivered, "
                      "growing 57% quarter over quarter \u2014 the first serious attempt by a major vendor "
                      "to report AI on output rather than seats.",
             "source": "https://s205.q4cdn.com/626266368/files/doc_financials/2026/q4/CRM-Q4-FY26-Earnings-Press-Release.pdf"},
            {"point": "Says headcount is still growing, concentrated in sales, on the logic that agents can "
                      "qualify leads and provide service but selling still requires people \u2014 a useful "
                      "check on his own automation narrative.",
             "source": "https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Fourth-Quarter-Fiscal-2026-Results/default.aspx"},
        ],
        "talking_points": [
            "Thirteen years at Oracle before founding Salesforce \u2014 he knows exactly how the incumbent he displaced sells.",
            "Agentic Work Units are his framing and his risk. Pushing for outcome-linked commercial terms is pushing on an open door.",
            "Over 60% of agentic bookings come from existing-customer expansion. If a PortCo already runs Salesforce, you are negotiating an upsell, not a selection.",
        ],
        "links": [
            {"label": "Salesforce FY2026 Q4 results", "url": "https://www.salesforce.com/news/press-releases/2026/02/25/fy26-q4-earnings/"},
            {"label": "Investor relations release", "url": "https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Fourth-Quarter-Fiscal-2026-Results/default.aspx"},
        ],
        "notes": "Education and detail of his Oracle roles were not confirmed in this pass and are "
                 "deliberately left thin rather than guessed.",
    },
    {
        "id": "salesforce-robin-washington",
        "vendor_slug": "salesforce",
        "name": "Robin Washington",
        "title": "President &amp; Chief Operating and Financial Officer",
        "in_role_since": "President and COFO; a Salesforce board director since 2013 and Lead Independent Director from 2022 to 2025",
        "focus": "Owns an unusually broad remit \u2014 business strategy and operations, global finance, "
                 "employee success, global strategic customers and partners, marketing, communications, "
                 "and real estate and workplace services \u2014 with profitable growth and operational "
                 "excellence as the mandate.",
        "background": "A finance leader who moved from the board into the executive seat, which is rare "
                      "and consequential. She was Chief Accounting Officer at PeopleSoft, CFO of Hyperion "
                      "Solutions from 2006 to 2007, and then EVP and CFO of Gilead Sciences from 2008 to "
                      "2019 \u2014 more than a decade running finance at a major biopharmaceutical "
                      "company. She joined the Salesforce board in 2013 and served as Lead Independent "
                      "Director from 2022 to 2025, through the activist-investor period and the "
                      "profitable-growth pivot, before taking the combined President and COFO role.",
        "career": [
            {"period": "current", "role": "President &amp; Chief Operating and Financial Officer", "org": "Salesforce"},
            {"period": "2022\u20132025", "role": "Lead Independent Director", "org": "Salesforce"},
            {"period": "2013\u2013present", "role": "Member of the Board of Directors", "org": "Salesforce"},
            {"period": "2008\u20132019", "role": "Executive Vice President &amp; Chief Financial Officer", "org": "Gilead Sciences"},
            {"period": "2006\u20132007", "role": "Chief Financial Officer", "org": "Hyperion Solutions"},
            {"period": "earlier", "role": "Chief Accounting Officer", "org": "PeopleSoft"},
        ],
        "education": ["BBA, University of Michigan Ross School of Business"],
        "public_roles": ["Member of the Board of Directors, Salesforce"],
        "notable": [
            {"point": "Served as Lead Independent Director from 2022 to 2025 \u2014 through the activist "
                      "campaign and the profitable-growth pivot \u2014 before moving into the executive "
                      "seat, so she helped set the discipline she now enforces.",
             "source": "https://michiganross.umich.edu/about/profile/robin-washington"},
            {"point": "Her remit is far wider than finance: operations, employee success, marketing, "
                      "strategic customers and partners, and real estate all report through her.",
             "source": "https://www.salesforce.com/blog/author/robin-washington"},
        ],
        "talking_points": [
            "Finance, operations, and strategic customers and partners all sit with her \u2014 the single most useful counterpart for a portfolio-scale Salesforce agreement.",
            "Eleven years as CFO of Gilead means she has run finance in a regulated, capital-intensive industry, not just software.",
            "She came from the board and owns the profitable-growth mandate. Expect discipline on discounting and rigour on commitments.",
        ],
        "links": [
            {"label": "Salesforce author profile", "url": "https://www.salesforce.com/blog/author/robin-washington"},
            {"label": "Michigan Ross profile", "url": "https://michiganross.umich.edu/about/profile/robin-washington"},
            {"label": "Stanford Directors' College profile", "url": "https://conferences.law.stanford.edu/directorscollege2026/speakers/robin-washington/"},
        ],
    },
]
