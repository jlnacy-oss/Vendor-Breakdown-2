# -*- coding: utf-8 -*-
"""
people_wave12.py — Person research wave 12, completed 15 September 2026.

Oracle and Palantir leadership.

PROFESSIONAL, PUBLISHED INFORMATION ONLY. See people_schema.py.
Sources carried net worth, ages, family relationships, personal lifestyle and
self-described political beliefs. None of it is here. Political affiliation in
particular is a protected attribute and is excluded regardless of the person
having stated it publicly.
"""

RESEARCHED_ON = "2026-09-15"

PEOPLE = [
    # ================================================= Oracle
    {
        "id": "oracle-clay-magouyrk",
        "vendor_slug": "oracle",
        "name": "Clay Magouyrk",
        "title": "Co-Chief Executive Officer",
        "in_role_since": "Co-CEO since 22 September 2025; previously President, Oracle Cloud Infrastructure",
        "focus": "Runs Oracle alongside Mike Sicilia, owning the cloud infrastructure side \u2014 the "
                 "business carrying the $638B backlog and the $70B capital programme behind it.",
        "background": "He built the thing he now runs the company on, and he came from the competitor. He "
                      "joined Oracle in 2014 from Amazon Web Services as a founding member of Oracle's "
                      "cloud engineering team, and oversaw the design, implementation and commercial "
                      "success of OCI Gen2 \u2014 the platform that powers both hyperscale public cloud "
                      "data centres and gigawatt-scale AI training facilities. He was President of Oracle "
                      "Cloud Infrastructure for close to a dozen years before the promotion. Ellison's "
                      "stated reason for elevating him was his experience leading Oracle's large, "
                      "fast-growing cloud infrastructure business.",
        "career": [
            {"period": "2025\u2013present", "role": "Co-Chief Executive Officer", "org": "Oracle"},
            {"period": "2014\u20132025", "role": "Founding member of cloud engineering, then President, Oracle Cloud Infrastructure", "org": "Oracle"},
            {"period": "before 2014", "role": "Engineering", "org": "Amazon Web Services"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Built OCI Gen2 from the founding engineering team onward \u2014 the platform behind "
                      "Oracle's $638B remaining performance obligation and its position as a training and "
                      "inference destination.",
             "source": "https://investor.oracle.com/investor-news/news-details/2025/Oracle-Corporation-Announces-Promotion-of-Clay-Magouyrk-and-Mike-Sicilia-to-CEOs-Safra-Catz-Appointed-Executive-Vice-Chair-of-the-Board-of-Directors/default.aspx"},
            {"point": "Came to Oracle from AWS in 2014, so he has built cloud infrastructure at both the "
                      "market leader and its most aggressive challenger.",
             "source": "https://www.ciodive.com/news/oracle-co-ceo-appointments-cloud-ai-larry-ellison/760773/"},
        ],
        "talking_points": [
            "An infrastructure engineer running a company whose growth depends on building capacity on schedule \u2014 a delivery-risk conversation will be substantive.",
            "He knows AWS from the inside. Comparisons to AWS terms will not surprise him and may work in your favour.",
            "Oracle's backlog converts only if capacity is energised. Ask about power procurement and build timelines, not just contract terms.",
        ],
        "links": [
            {"label": "Co-CEO announcement", "url": "https://investor.oracle.com/investor-news/news-details/2025/Oracle-Corporation-Announces-Promotion-of-Clay-Magouyrk-and-Mike-Sicilia-to-CEOs-Safra-Catz-Appointed-Executive-Vice-Chair-of-the-Board-of-Directors/default.aspx"},
            {"label": "Coverage of the transition", "url": "https://www.ciodive.com/news/oracle-co-ceo-appointments-cloud-ai-larry-ellison/760773/"},
        ],
        "notes": "Education and pre-AWS career were not confirmed in this pass and are deliberately left "
                 "blank rather than guessed.",
    },
    {
        "id": "oracle-mike-sicilia",
        "vendor_slug": "oracle",
        "name": "Mike Sicilia",
        "title": "Co-Chief Executive Officer",
        "in_role_since": "Co-CEO since 22 September 2025; previously President, Oracle Industries",
        "focus": "Runs Oracle alongside Clay Magouyrk, owning applications and industry verticals \u2014 "
                 "the business that includes construction and engineering, healthcare and other "
                 "asset-heavy sectors.",
        "background": "The most infrastructure-adjacent executive in Oracle's leadership, and he arrived "
                      "through an acquisition that matters to your world: he joined Oracle in 2008 when it "
                      "bought **Primavera Systems**, the project and portfolio management software used "
                      "across construction, engineering and capital projects, where he had been CTO. He "
                      "was appointed to lead the Oracle business unit that emerged from that deal and went "
                      "on to oversee several subsequent acquisitions, becoming President of Oracle "
                      "Industries. His engineering teams pioneered intent-based application generation to "
                      "replace traditional coding, and he led the rebuild of Oracle's industry "
                      "applications \u2014 including Oracle Health, following the $28.3B Cerner "
                      "acquisition \u2014 using current AI technology.",
        "career": [
            {"period": "2025\u2013present", "role": "Co-Chief Executive Officer", "org": "Oracle"},
            {"period": "2025", "role": "President, Oracle Industries", "org": "Oracle"},
            {"period": "2008\u20132025", "role": "Led the Primavera business unit, then broader industry applications", "org": "Oracle"},
            {"period": "before 2008", "role": "Chief Technology Officer", "org": "Primavera Systems (acquired by Oracle, 2008)"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Came from Primavera Systems, the project and portfolio management platform used "
                      "across construction, engineering and capital projects \u2014 the Oracle executive "
                      "whose own product background sits closest to infrastructure delivery.",
             "source": "https://siliconangle.com/2025/09/22/oracle-appoints-clay-magouyrk-mike-sicilia-co-ceos-amid-ai-growth/"},
            {"point": "Ellison credited him specifically with modernising Oracle's industry applications, "
                      "including Oracle Health, by rebuilding them with current AI technology rather than "
                      "layering AI on top.",
             "source": "https://siliconangle.com/2025/09/22/oracle-appoints-clay-magouyrk-mike-sicilia-co-ceos-amid-ai-growth/"},
        ],
        "talking_points": [
            "Primavera is his own product heritage. If a PortCo runs capital projects, this is the most productive Oracle conversation available.",
            "He rebuilt industry applications rather than retrofitting AI. Worth asking what that means for migration cost on an existing estate.",
            "Co-CEO structures create ambiguity about who commits to what. Establish early whether Magouyrk or Sicilia owns your relationship.",
        ],
        "links": [
            {"label": "Co-CEO announcement", "url": "https://www.oracle.com/news/announcement/oracle-corporation-announces-promotion-of-clay-magouyrk-and-mike-scilia-2025-09-22/"},
            {"label": "Transition coverage", "url": "https://siliconangle.com/2025/09/22/oracle-appoints-clay-magouyrk-mike-sicilia-co-ceos-amid-ai-growth/"},
        ],
        "notes": "Education was not confirmed in this pass and is deliberately left blank rather than guessed.",
    },
    {
        "id": "oracle-larry-ellison",
        "vendor_slug": "oracle",
        "name": "Larry Ellison",
        "title": "Chairman of the Board &amp; Chief Technology Officer",
        "in_role_since": "Co-founded Oracle in 1977; CEO for more than three decades until 2014; Chairman and CTO since",
        "focus": "Sets Oracle's technical direction and remains the decisive voice on strategy, including "
                 "the AI infrastructure bet and the capital programme behind it.",
        "background": "He co-founded Oracle in 1977 and ran it as CEO for more than thirty years before "
                      "stepping back from day-to-day management in 2014, taking the Chairman and Chief "
                      "Technology Officer roles rather than retiring. He describes a 26-year working "
                      "partnership with Safra Catz that continues in her vice-chair role. He remains the "
                      "person whose judgement determines Oracle's direction: he selected both co-CEOs and "
                      "publicly explained the reasoning for each.",
        "career": [
            {"period": "2014\u2013present", "role": "Chairman of the Board &amp; Chief Technology Officer", "org": "Oracle"},
            {"period": "1977\u20132014", "role": "Co-Founder &amp; Chief Executive Officer", "org": "Oracle"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Argues that the money spent on training must translate into products that are sold "
                      "\u2014 all inferencing \u2014 and that the inference market will eventually "
                      "overshadow training. That thesis is what Oracle's capital programme is built on.",
             "source": "https://www.ciodive.com/news/oracle-co-ceo-appointments-cloud-ai-larry-ellison/760773/"},
            {"point": "Holds roughly 40.6% beneficial ownership of Oracle, so board control and economic "
                      "ownership sit together \u2014 a governance fact material to any long-term commitment.",
             "source": "https://investor.oracle.com/investor-news/news-details/2025/Oracle-Corporation-Announces-Promotion-of-Clay-Magouyrk-and-Mike-Sicilia-to-CEOs-Safra-Catz-Appointed-Executive-Vice-Chair-of-the-Board-of-Directors/default.aspx"},
        ],
        "talking_points": [
            "Nominally CTO, effectively the decision-maker. Nothing strategic at Oracle happens against him.",
            "His inference-over-training thesis is the reason Oracle is taking this much balance-sheet risk. Engage with it directly rather than around it.",
            "Reserve for genuinely strategic conversations; the co-CEOs run the business.",
        ],
        "links": [
            {"label": "Leadership announcement", "url": "https://www.oracle.com/news/announcement/oracle-corporation-announces-promotion-of-clay-magouyrk-and-mike-scilia-2025-09-22/"},
            {"label": "Strategy commentary", "url": "https://www.ciodive.com/news/oracle-co-ceo-appointments-cloud-ai-larry-ellison/760773/"},
        ],
    },
    {
        "id": "oracle-safra-catz",
        "vendor_slug": "oracle",
        "name": "Safra Catz",
        "title": "Executive Vice Chair of the Board",
        "in_role_since": "Executive Vice Chair since September 2025; CEO from 2014 to 2025",
        "focus": "Board-level stewardship alongside Ellison, continuing a partnership he describes as "
                 "spanning 26 years.",
        "background": "She joined Oracle in 1999 after thirteen years in investment banking at Donaldson, "
                      "Lufkin &amp; Jenrette, became its finance chief in 2005, and was named co-CEO in "
                      "2014 alongside Mark Hurd when Ellison stepped back \u2014 continuing as sole CEO "
                      "after Hurd's death in 2019. Across eleven years at the helm she turned Oracle from "
                      "a database provider into a hyperscale cloud business, competing directly with "
                      "Microsoft and Alphabet for data-centre share, and was central to its acquisition "
                      "programme. She is trained in both finance and law.",
        "career": [
            {"period": "2025\u2013present", "role": "Executive Vice Chair of the Board", "org": "Oracle"},
            {"period": "2019\u20132025", "role": "Chief Executive Officer", "org": "Oracle"},
            {"period": "2014\u20132019", "role": "Co-Chief Executive Officer (with Mark Hurd)", "org": "Oracle"},
            {"period": "2005\u20132014", "role": "Chief Financial Officer", "org": "Oracle"},
            {"period": "1986\u20131999", "role": "Investment banking", "org": "Donaldson, Lufkin &amp; Jenrette"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Led Oracle's transformation from database provider to hyperscale cloud business "
                      "across eleven years as CEO, and was central to its acquisition programme including "
                      "the $28.3B Cerner deal.",
             "source": "https://finance.yahoo.com/news/oracle-appoints-insiders-clay-magouyrk-121559145.html"},
            {"point": "Thirteen years in investment banking before Oracle, then nine as its CFO \u2014 she "
                      "understands the financing structure behind the current capital programme better "
                      "than anyone on the board except Ellison.",
             "source": "https://www.cnbc.com/2025/09/22/oracle-names-co-ceos.html"},
        ],
        "talking_points": [
            "Ex-banker and ex-CFO now on the board \u2014 the right escalation if the commercial structure needs board-level comfort.",
            "She built the cloud business commercially; the co-CEOs inherited it. Institutional memory on how the big contracts were actually struck sits with her.",
            "No longer executive. Route operating decisions through Magouyrk and Sicilia.",
        ],
        "links": [
            {"label": "Leadership transition announcement", "url": "https://investor.oracle.com/investor-news/news-details/2025/Oracle-Corporation-Announces-Promotion-of-Clay-Magouyrk-and-Mike-Sicilia-to-CEOs-Safra-Catz-Appointed-Executive-Vice-Chair-of-the-Board-of-Directors/default.aspx"},
            {"label": "Transition coverage", "url": "https://www.cnbc.com/2025/09/22/oracle-names-co-ceos.html"},
        ],
    },

    # ================================================= Palantir
    {
        "id": "palantir-alex-karp",
        "vendor_slug": "palantir",
        "name": "Alexander Karp",
        "title": "Co-Founder &amp; Chief Executive Officer",
        "in_role_since": "Co-founded Palantir in 2003\u20132004; CEO since 2005; board member since 2003",
        "focus": "Leads Palantir's strategy and is its principal public voice, having personally driven "
                 "the AIP Bootcamp go-to-market motion that pulled US commercial revenue up sharply.",
        "background": "A philosopher and lawyer by training rather than a technologist, which is unusual "
                      "for a software CEO and shapes how he argues. He holds a BA from Haverford College, "
                      "a JD from Stanford University, and a PhD from Goethe University in Frankfurt, where "
                      "his work was in social theory. Before Palantir he worked in investing and money "
                      "management, founding the London-based Caedmon Group. He co-founded Palantir with "
                      "Peter Thiel, Stephen Cohen and Joe Lonsdale, and it was seeded in part by In-Q-Tel, "
                      "the CIA's venture arm \u2014 the origin of its government-first strategy. He is "
                      "known for plainspoken investor letters and a mission-first company culture.",
        "career": [
            {"period": "2005\u2013present", "role": "Chief Executive Officer", "org": "Palantir Technologies"},
            {"period": "2003\u2013present", "role": "Co-Founder and Director", "org": "Palantir Technologies"},
            {"period": "before 2003", "role": "Founder; investing and money management", "org": "Caedmon Group (London)"},
        ],
        "education": [
            "PhD, Goethe University Frankfurt",
            "JD, Stanford University",
            "BA, Haverford College",
        ],
        "public_roles": ["Member, Palantir Board of Directors"],
        "notable": [
            {"point": "Personally drove the AIP Bootcamp go-to-market motion \u2014 short, hands-on "
                      "deployments rather than long sales cycles \u2014 which is credited with the surge "
                      "in US commercial revenue.",
             "source": "https://komo.ai/directory/palantir-leadership"},
            {"point": "Palantir is controlled by its founding group through a three-class share structure, "
                      "with Peter Thiel as Chairman retaining outsized voting power \u2014 so the founders "
                      "decide direction regardless of institutional shareholders.",
             "source": "https://komo.ai/directory/palantir-leadership"},
        ],
        "talking_points": [
            "Trained in philosophy and law, not engineering \u2014 he argues from first principles about institutions and will engage on why before how.",
            "The AIP Bootcamp motion is the fastest way to test Palantir on a real PortCo problem without a long procurement cycle.",
            "Founder voting control means commercial flexibility exists if he wants it to. Escalation is unusually meaningful here.",
        ],
        "links": [
            {"label": "Palantir investor management page", "url": "https://investors.palantir.com/management.html"},
            {"label": "SEC registration statement (biographies)", "url": "https://www.sec.gov/Archives/edgar/data/1321655/000119312520258493/d904406d424b4.htm"},
        ],
        "notes": "Sources conflict on his early career \u2014 one widely-circulated profile places him at "
                 "US law firms, which does not match Palantir's own SEC filings or other accounts. The "
                 "Caedmon Group account is used here. One source also reports Palantir relocated its "
                 "headquarters to the Miami area in February 2026; the vendor page should be re-checked.",
    },
    {
        "id": "palantir-stephen-cohen",
        "vendor_slug": "palantir",
        "name": "Stephen Cohen",
        "title": "Co-Founder, President &amp; Secretary",
        "in_role_since": "Co-founded Palantir in 2003; President and Secretary, and a director since 2005",
        "focus": "Oversees product strategy and corporate execution, and sits in the founding group that "
                 "retains voting control of the company.",
        "background": "A Stanford computer science graduate who has been at Palantir since its founding "
                      "and has held various positions across the company in that time. He is one of the "
                      "three figures \u2014 with Karp and Thiel \u2014 who have run Palantir since 2003 "
                      "and retain control through its multi-class share structure. Palantir's C-suite "
                      "averages more than fifteen years of tenure, which is an unusual degree of "
                      "continuity for a company of this size, and he is part of the reason why.",
        "career": [
            {"period": "2005\u2013present", "role": "President, Secretary and Director", "org": "Palantir Technologies"},
            {"period": "2003\u2013present", "role": "Co-Founder", "org": "Palantir Technologies"},
        ],
        "education": ["BS Computer Science, Stanford University"],
        "public_roles": ["Member, Palantir Board of Directors"],
        "notable": [
            {"point": "Part of the founding triumvirate \u2014 with Karp and Thiel \u2014 that has run "
                      "Palantir since 2003 and retains voting control through a three-class share "
                      "structure.",
             "source": "https://komo.ai/directory/palantir-leadership"},
            {"point": "Has been with the company continuously since founding, in a C-suite averaging 15+ "
                      "years of tenure \u2014 unusual continuity for a company at this valuation.",
             "source": "https://investors.palantir.com/management.html"},
        ],
        "talking_points": [
            "Product strategy sits with him \u2014 the right counterpart for roadmap questions rather than commercial ones.",
            "An engineer among founders who are a philosopher and an investor; the most technically grounded of the three.",
            "Continuity is Palantir's genuine differentiator against vendors with revolving leadership. Worth testing what that buys you in practice.",
        ],
        "links": [
            {"label": "Palantir investor management page", "url": "https://investors.palantir.com/management.html"},
            {"label": "SEC registration statement", "url": "https://www.sec.gov/Archives/edgar/data/1321655/000119312520258493/d904406d424b4.htm"},
        ],
    },
    {
        "id": "palantir-shyam-sankar",
        "vendor_slug": "palantir",
        "name": "Shyam Sankar",
        "title": "Chief Technology Officer &amp; Executive Vice President",
        "in_role_since": "At Palantir since 2006; previously Chief Operating Officer, now CTO and EVP",
        "focus": "Owns Palantir's technology direction \u2014 the ontology-driven data model underneath "
                 "Foundry and AIP, and the Forward Deployed Engineer delivery model.",
        "background": "The architect of the two things that actually distinguish Palantir: the "
                      "ontology-driven data model, which maps an organisation's real-world entities and "
                      "relationships rather than its tables, and the Forward Deployed Engineer model, "
                      "where engineers embed directly in the customer's operations rather than delivering "
                      "from a distance. He has been at Palantir since 2006 and previously served as Chief "
                      "Operating Officer before moving to CTO. He holds a BS in Electrical and Computer "
                      "Engineering from Cornell and an MS in Management Science and Engineering from "
                      "Stanford.",
        "career": [
            {"period": "current", "role": "Chief Technology Officer &amp; Executive Vice President", "org": "Palantir Technologies"},
            {"period": "2006\u2013", "role": "Various positions, including Chief Operating Officer and EVP", "org": "Palantir Technologies"},
        ],
        "education": [
            "MS Management Science and Engineering, Stanford University",
            "BS Electrical and Computer Engineering, Cornell University",
        ],
        "public_roles": [],
        "notable": [
            {"point": "Architect of Palantir's ontology-driven data model and the Forward Deployed "
                      "Engineer delivery model \u2014 the two design decisions that most distinguish "
                      "Palantir from a conventional data platform.",
             "source": "https://komo.ai/directory/palantir-leadership"},
            {"point": "Twenty years at the company, spanning COO and CTO \u2014 he has seen both the "
                      "commercial and technical consequences of how Palantir deploys.",
             "source": "https://investors.palantir.com/management.html"},
        ],
        "talking_points": [
            "The ontology model is the real technical argument for Palantir. He is the person who can explain what it costs to build and maintain on a PortCo's data.",
            "Forward Deployed Engineers are expensive and effective. Ask him directly what the steady-state staffing looks like after go-live.",
            "Having been COO as well as CTO, he will not dodge the commercial implications of a technical answer.",
        ],
        "links": [
            {"label": "Palantir investor management page", "url": "https://investors.palantir.com/management.html"},
            {"label": "SEC registration statement", "url": "https://www.sec.gov/Archives/edgar/data/1321655/000119312520258493/d904406d424b4.htm"},
        ],
    },
]
