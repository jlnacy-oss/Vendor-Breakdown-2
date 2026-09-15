# -*- coding: utf-8 -*-
"""
people_wave2.py — Person research wave 2, completed 15 September 2026.

AVEVA and Bain & Company leadership.

This wave produced two corrections to the vendor records, both now applied:
  - Peter Herweck was removed as Schneider Electric CEO in November 2024.
  - Orit Gadiesh became Bain's Chair Emeritus in February 2025; Manny Maceda is Chair.

PROFESSIONAL, PUBLISHED INFORMATION ONLY. See people_schema.py.
"""

RESEARCHED_ON = "2026-09-15"

PEOPLE = [
    # ================================================= AVEVA
    {
        "id": "aveva-caspar-herzberg",
        "vendor_slug": "aveva",
        "name": "Caspar Herzberg",
        "title": "Chief Executive Officer",
        "in_role_since": "CEO since March 2023",
        "focus": "Runs AVEVA as a Schneider Electric company, integrating three software portfolios "
                 "\u2014 Schneider Electric Software, AVEVA and OSIsoft \u2014 into one industrial "
                 "software business, and sits on the Schneider Electric Executive Committee.",
        "background": "An unusual profile for an industrial software CEO: his degrees are in Arabic and "
                      "Middle Eastern studies and international politics, not engineering, and he built his "
                      "career on the commercial and geographic side rather than the product side. He began "
                      "at Accenture in London working on digital transformation for the global energy "
                      "sector, then spent over a decade at Cisco leading sales and services and developing "
                      "smart-cities strategies across China, Asia, Japan, Australia, the USA and Europe. He "
                      "ran Schneider Electric's business across more than 80 countries as President, Middle "
                      "East &amp; Africa, joined AVEVA as Chief Revenue Officer in 2021, became COO in 2022 "
                      "and CEO in March 2023. He is also a reserve officer in the German Federal Armed "
                      "Forces, holding the rank of Major.",
        "career": [
            {"period": "2023\u2013present", "role": "Chief Executive Officer", "org": "AVEVA"},
            {"period": "2022\u20132023", "role": "Chief Operating Officer", "org": "AVEVA"},
            {"period": "2021\u20132022", "role": "Chief Revenue Officer", "org": "AVEVA"},
            {"period": "before 2021", "role": "President, Middle East &amp; Africa", "org": "Schneider Electric"},
            {"period": "~10 years", "role": "Sales and services leadership; smart cities strategy", "org": "Cisco"},
            {"period": "early career", "role": "Consultant, energy sector digital transformation", "org": "Accenture (London)"},
        ],
        "education": [
            "MSc, International Politics, School of Oriental and African Studies, University of London",
            "BA, Arabic &amp; Modern Middle Eastern Studies, St Anne's College, University of Oxford",
        ],
        "public_roles": [
            "Member, Schneider Electric Executive Committee",
            "Author, <i>Smart Cities, Digital Nations</i>",
            "Major (Reserve), German Federal Armed Forces",
        ],
        "notable": [
            {"point": "Frames AVEVA's position as serving over 90% of industrial companies across energy, "
                      "water, food, manufacturing, pharmaceuticals and smart cities \u2014 the sectors "
                      "closest to an infrastructure portfolio.",
             "source": "https://www.automationmag.com/aveva-caspar-herzberg-ceo/"},
            {"point": "His stated strategy is integrated data and AI-infused applications delivered as SaaS "
                      "to reduce total cost of ownership \u2014 a cost argument rather than a capability one.",
             "source": "https://www.aveva.com/en/about/news/press-releases/2023/aveva-announces-new-ceo-and-vision-for-connected-industries-of-the-future/"},
        ],
        "talking_points": [
            "Smart cities and public-sector infrastructure are his genuine specialism, not a talking point \u2014 he wrote a book on it.",
            "Commercially grounded rather than technical: he came up through revenue and country management, so expect a business-case conversation.",
            "He sits on Schneider Electric's Executive Committee, so an AVEVA conversation can reach the parent without a separate introduction.",
        ],
        "links": [
            {"label": "AVEVA leadership page", "url": "https://www.aveva.com/en/about/about-aveva/leadership/"},
            {"label": "World Economic Forum profile", "url": "https://www.weforum.org/stories/authors/caspar-herzberg/"},
            {"label": "Appointment announcement", "url": "https://www.aveva.com/en/about/news/press-releases/2023/aveva-announces-new-ceo-and-vision-for-connected-industries-of-the-future/"},
        ],
    },
    {
        "id": "aveva-peter-herweck",
        "vendor_slug": "aveva",
        "name": "Peter Herweck",
        "title": "Chairperson, AVEVA",
        "in_role_since": "Chairperson following his move from AVEVA CEO to Schneider Electric CEO in 2023",
        "focus": "Board-level oversight of AVEVA. No longer an executive at Schneider Electric \u2014 he was "
                 "removed as its CEO in November 2024.",
        "background": "A career industrial-automation executive. He was CEO of Siemens' process industries "
                      "and drives division in 2014 and regional head of Siemens China from 2008 to 2010, "
                      "then moved to Schneider Electric to lead its global Industrial Automation business, "
                      "serving concurrently as Vice Chairman of the AVEVA board. He became AVEVA's CEO in "
                      "May 2021 and led the integration of Schneider Electric Software, AVEVA and OSIsoft "
                      "and the launch of the Data Hub platform. He was promoted to CEO of Schneider "
                      "Electric in May 2023, but the board removed him after eighteen months, in November "
                      "2024, citing divergences in executing the company roadmap; Olivier Blum replaced him.",
        "career": [
            {"period": "2023\u2013present", "role": "Chairperson", "org": "AVEVA"},
            {"period": "May 2023\u2013Nov 2024", "role": "Chief Executive Officer (removed by the board)", "org": "Schneider Electric"},
            {"period": "2021\u20132023", "role": "Chief Executive Officer", "org": "AVEVA"},
            {"period": "before 2021", "role": "EVP, Industrial Automation; Vice Chairman of the AVEVA Board", "org": "Schneider Electric"},
            {"period": "2014", "role": "Chief Executive Officer, Process Industries and Drives", "org": "Siemens"},
            {"period": "2008\u20132010", "role": "Regional head, China", "org": "Siemens"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Removed as Schneider Electric CEO in November 2024 after eighteen months, the board "
                      "citing divergences in executing the company roadmap. Reporting suggested growth came "
                      "from AI and data centres rather than the software integration he led.",
             "source": "https://www.facilitiesdive.com/news/schneider-electric-replaces-ceo-peter-herweck-amid-strategic-execution-issue/732144/"},
            {"point": "Led the integration of three software businesses \u2014 Schneider Electric Software, "
                      "AVEVA and OSIsoft \u2014 and the launch of the Data Hub platform and cloud transition "
                      "during his two years as AVEVA CEO.",
             "source": "https://www.datacenterdynamics.com/en/news/aveva-boss-peter-herweck-announced-as-new-ceo-of-schneider-electric/"},
        ],
        "talking_points": [
            "A board seat, not an executive one \u2014 route commercial discussion through Herzberg, not him.",
            "He knows the AVEVA/OSIsoft integration intimately because he ran it; useful if data-historian architecture is the question.",
            "Treat his Schneider Electric departure as context, not a talking point \u2014 it was public and unflattering.",
        ],
        "links": [
            {"label": "Schneider Electric CEO change (Nov 2024)", "url": "https://www.facilitiesdive.com/news/schneider-electric-replaces-ceo-peter-herweck-amid-strategic-execution-issue/732144/"},
            {"label": "AVEVA to Schneider move (2023)", "url": "https://www.datacenterdynamics.com/en/news/aveva-boss-peter-herweck-announced-as-new-ceo-of-schneider-electric/"},
        ],
        "notes": "The prior vendor record listed him as \"Chairperson (Schneider Electric CEO)\". That was "
                 "stale \u2014 he was removed from the Schneider Electric role in November 2024. His AVEVA "
                 "chairmanship is per AVEVA and Wikipedia; confirm it is current before relying on it.",
    },

    # ================================================= Bain & Company
    {
        "id": "bain-christophe-de-vusser",
        "vendor_slug": "bain",
        "name": "Christophe De Vusser",
        "title": "Worldwide Managing Partner, Chief Executive Officer &amp; Chairman of the Board",
        "in_role_since": "Took office 1 July 2024, having been elected in January 2024",
        "focus": "Runs Bain's global strategy and operations, including Modernize Bain \u2014 the firm's own "
                 "AI transformation programme aimed at client impact and at preserving its culture through "
                 "the shift.",
        "background": "The single most directly relevant person in this contact list to an infrastructure "
                      "private-equity firm. He spent his Bain career in private equity: he led the firm's "
                      "EMEA Private Equity practice and is recognised internally as one of its foremost "
                      "experts in deal advisory and value creation for portfolio companies owned by "
                      "financial investors \u2014 which is to say, exactly the work GIP commissions. He "
                      "joined Bain in 2000 after starting in consumer products at Procter &amp; Gamble, ran "
                      "the Brussels office from 2012 to 2018 and doubled its business, joined the global "
                      "board in 2018, then tripled the EMEA private equity practice. A Belgian citizen, he "
                      "is the first European to lead Bain in its history.",
        "career": [
            {"period": "2024\u2013present", "role": "Worldwide Managing Partner, CEO &amp; Chairman of the Board", "org": "Bain &amp; Company"},
            {"period": "2018\u20132024", "role": "Head of EMEA Private Equity practice; Board of Directors", "org": "Bain &amp; Company"},
            {"period": "2012\u20132018", "role": "Managing Partner, Brussels office", "org": "Bain &amp; Company"},
            {"period": "2000\u20132012", "role": "Consultant to Partner, private equity and consumer products", "org": "Bain &amp; Company"},
            {"period": "early career", "role": "Consumer products", "org": "Procter &amp; Gamble"},
        ],
        "education": [
            "Civil Engineering, University of Ghent",
            "Business Communications, University of Ghent",
        ],
        "public_roles": [
            "Member, Business Roundtable",
            "Member, World Economic Forum International Business Council",
            "Member, WEF Alliance of CEO Climate Leaders",
        ],
        "notable": [
            {"point": "Led Bain's EMEA private equity practice and more than doubled it over five years, "
                      "specialising in commercial due diligence and value creation in portfolio companies "
                      "\u2014 directly the work an infrastructure fund buys.",
             "source": "https://www.bain.com/about/media-center/press-releases/2024/christophe-de-vusser-takes-office-as-bain--companys--worldwide-managing-partner-and-ceo/"},
            {"point": "Owns Modernize Bain, the firm's internal AI transformation \u2014 so he can speak to "
                      "what AI has actually done to a professional services delivery model from the inside.",
             "source": "https://www.bain.com/our-team/christophe-de-vusser/"},
        ],
        "talking_points": [
            "He speaks private equity natively \u2014 value creation planning and commercial diligence are his own practice area, not a firm capability he is relaying.",
            "Modernize Bain gives him a first-person view of AI's effect on a people business; a credible conversation about what actually changed rather than what was announced.",
            "Bain publishes no revenue and no AI figure while BCG and McKinsey both do. Worth asking him directly rather than working around it.",
        ],
        "links": [
            {"label": "Bain profile", "url": "https://www.bain.com/our-team/christophe-de-vusser/"},
            {"label": "Appointment announcement", "url": "https://www.bain.com/about/media-center/press-releases/2024/christophe-de-vusser-takes-office-as-bain--companys--worldwide-managing-partner-and-ceo/"},
            {"label": "Business Roundtable profile", "url": "https://www.businessroundtable.org/members/christophe-de-vusser"},
        ],
    },
    {
        "id": "bain-manny-maceda",
        "vendor_slug": "bain",
        "name": "Manny Maceda",
        "title": "Chair",
        "in_role_since": "Chair since February 2025, succeeding Orit Gadiesh",
        "focus": "Chairs the firm following two terms as its chief executive, and continues to work "
                 "closely with De Vusser on shaping Bain's direction.",
        "background": "Led Bain as Worldwide Managing Partner and CEO from 2018 until 30 June 2024, a "
                      "period of accelerated expansion during which the firm roughly doubled in size and "
                      "built out its digital capabilities substantially. He succeeded Orit Gadiesh as Chair "
                      "in February 2025, taking a role she had held for three decades.",
        "career": [
            {"period": "2025\u2013present", "role": "Chair", "org": "Bain &amp; Company"},
            {"period": "2018\u20132024", "role": "Worldwide Managing Partner &amp; Chief Executive Officer", "org": "Bain &amp; Company"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Oversaw a period in which Bain's reported revenue roughly doubled, from a little "
                      "over $3B in 2018 to around $6B by 2023, alongside a surge in digital capability.",
             "source": "https://www.consultancy.eu/news/9580/bain-company-names-christophe-de-vusser-next-global-ceo"},
            {"point": "Became Chair in February 2025 as Orit Gadiesh moved to Chair Emeritus after three "
                      "decades in the role.",
             "source": "https://www.bain.com/about/media-center/press-releases/20252/bain--company-appoints-manny-maceda-as-chair-as-orit-gadiesh-takes-role-of-chair-emeritus/"},
        ],
        "talking_points": [
            "A recent former CEO now chairing \u2014 influential but not the operating decision-maker; De Vusser is.",
            "He built the digital capability Bain now sells, so he is a credible reference on whether it is real.",
        ],
        "links": [
            {"label": "Chair appointment announcement", "url": "https://www.bain.com/about/media-center/press-releases/20252/bain--company-appoints-manny-maceda-as-chair-as-orit-gadiesh-takes-role-of-chair-emeritus/"},
        ],
    },
    {
        "id": "bain-orit-gadiesh",
        "vendor_slug": "bain",
        "name": "Orit Gadiesh",
        "title": "Chair Emeritus",
        "in_role_since": "Chair Emeritus since February 2025, having been Chair for roughly three decades from 1993",
        "focus": "Emeritus role. Continues to be associated with the firm's culture and values rather than "
                 "its operations.",
        "background": "One of the most consequential figures in modern consulting. She was Bain's first "
                      "woman consultant, the first woman to hold a firm-wide global leadership position "
                      "there, and on becoming Chair in 1993 the first female chairman in the global "
                      "consulting industry. She took the role during the firm's recovery period and is "
                      "credited with relaxing Bain's one-client-per-industry rule, which diversified the "
                      "client base and reduced dependence on a handful of accounts. Over more than four "
                      "decades she worked with hundreds of CEOs and senior executives on strategy and "
                      "large-scale transformation, and shaped the culture and values the firm still runs on.",
        "career": [
            {"period": "2025\u2013present", "role": "Chair Emeritus", "org": "Bain &amp; Company"},
            {"period": "1993\u20132025", "role": "Chair", "org": "Bain &amp; Company"},
            {"period": "from 1977", "role": "Consultant through to firm-wide leadership", "org": "Bain &amp; Company"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Relaxed Bain's one-client-per-industry rule, diversifying the client base and "
                      "reducing over-reliance on a few clients \u2014 a structural change that shaped the "
                      "firm's modern economics.",
             "source": "https://umbrex.com/resources/profiles-of-the-top-consulting-firms/overview-profile-and-history-of-bain/"},
            {"point": "Moved to Chair Emeritus in February 2025 after three decades as Chair.",
             "source": "https://www.bain.com/about/media-center/press-releases/20252/bain--company-appoints-manny-maceda-as-chair-as-orit-gadiesh-takes-role-of-chair-emeritus/"},
        ],
        "talking_points": [
            "Emeritus \u2014 a figure of standing rather than a route to a commercial decision.",
            "If Bain's culture or continuity comes up, she is the reference point the firm itself uses.",
        ],
        "links": [
            {"label": "Chair Emeritus announcement", "url": "https://www.bain.com/about/media-center/press-releases/20252/bain--company-appoints-manny-maceda-as-chair-as-orit-gadiesh-takes-role-of-chair-emeritus/"},
        ],
        "notes": "The prior vendor record listed her simply as \"Chairman\". That was stale \u2014 she became "
                 "Chair Emeritus in February 2025 and Manny Maceda is now Chair.",
    },
]
