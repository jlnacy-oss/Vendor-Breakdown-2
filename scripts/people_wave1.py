# -*- coding: utf-8 -*-
"""
people_wave1.py — Person research wave 1, completed 15 September 2026.

Accenture, Adobe, Amazon Web Services and Anthropic leadership.

PROFESSIONAL, PUBLISHED INFORMATION ONLY. See people_schema.py for the rule and
the guard that enforces it. Personal contact details live only in the People sheet
of gip-tracker.xlsx, entered by the user.
"""

PEOPLE = [
    # ================================================= Accenture
    {
        "id": "accenture-julie-sweet",
        "vendor_slug": "accenture",
        "name": "Julie Sweet",
        "title": "Chair &amp; Chief Executive Officer",
        "in_role_since": "CEO since September 2019; Chair since September 2021",
        "focus": "Sets Accenture's strategy and operations across roughly 799,000 people, and has "
                 "driven the firm's reinvention around AI delivery \u2014 including the creation of "
                 "Reinvention Services as an AI-focused integrated division.",
        "background": "A lawyer by training rather than a technologist, which is unusual for the role and "
                      "shapes how she engages: she came up through governance and commercial risk, not "
                      "delivery. She spent ten years as a partner at Cravath, Swaine &amp; Moore working on "
                      "M&amp;A and corporate law for Fortune 500 clients before joining Accenture in 2010 as "
                      "General Counsel. She ran Accenture's largest geography, North America, for four "
                      "years before taking the global CEO role.",
        "career": [
            {"period": "2019\u2013present", "role": "Chief Executive Officer (Chair from 2021)", "org": "Accenture"},
            {"period": "2015\u20132019", "role": "Chief Executive Officer, North America", "org": "Accenture"},
            {"period": "2010\u20132015", "role": "General Counsel, Chief Compliance Officer &amp; Corporate Secretary", "org": "Accenture"},
            {"period": "2000\u20132010", "role": "Partner, M&amp;A and corporate law", "org": "Cravath, Swaine &amp; Moore LLP"},
        ],
        "education": ["J.D., Columbia Law School", "B.A., Claremont McKenna College"],
        "public_roles": [
            "Board of Trustees, World Economic Forum",
            "Board of Trustees, Center for Strategic &amp; International Studies",
            "Board of Trustees, Marriott Foundation for People with Disabilities",
            "Board Co-Chair, New York Jobs CEO Council",
            "Board Co-Chair, Welcome.US",
        ],
        "notable": [
            {"point": "Created Accenture's Reinvention Services, an AI-focused integrated division, and "
                      "positioned AI as a separately reported revenue line \u2014 $2.7B in FY2025, tripled "
                      "year over year.",
             "source": "https://www.accenture.com/us-en/about/company/integrated-reporting-financial"},
            {"point": "Publicly acknowledged that the adverse business environment which began in FY2024 "
                      "persisted through FY2025, while still delivering 7% growth \u2014 a candid framing "
                      "worth matching in conversation rather than contradicting.",
             "source": "https://www.outlookbusiness.com/corporate/accentures-fy25-revenue-up-7-yoy-ai-deal-bookings-double-to-59-billion"},
        ],
        "talking_points": [
            "Her framing is reinvention and value delivered, not technology for its own sake \u2014 lead with the business outcome.",
            "The legal and governance background means AI risk, compliance and contracting are native territory, not a deflection.",
            "FY2026 growth guidance of 2\u20135% is materially below FY2025's 7%; she will expect you to know that.",
        ],
        "links": [
            {"label": "World Economic Forum profile", "url": "https://www.weforum.org/stories/authors/julie-sweet/"},
            {"label": "Accenture FY2025 results", "url": "https://www.accenture.com/us-en/about/company/integrated-reporting-financial"},
        ],
    },
    {
        "id": "accenture-karthik-narain",
        "vendor_slug": "accenture",
        "name": "Karthik Narain",
        "title": "Group Chief Executive, Technology &amp; Chief Technology Officer",
        "in_role_since": "Group Chief Executive, Technology since 2023; added CTO from 1 September 2024",
        "focus": "Leads Accenture's Technology business \u2014 Cloud First, Data &amp; AI, enterprise and "
                 "industry platforms, Security, and the ecosystem and advanced technology centres \u2014 "
                 "and owns the firm's technology strategy.",
        "background": "Joined Accenture in 2015 and rose through the technology organisation rather than "
                      "arriving from outside. He led Technology for the Communications, Media &amp; "
                      "Technology industry group and Technology in North America, then led Accenture Cloud "
                      "First and Data &amp; AI, nearly tripling the firm's cloud-certified workforce. He "
                      "succeeded Paul Daugherty in the CTO role when Daugherty retired after a 38-year "
                      "career. His own career spans about 25 years across financial services, high tech and "
                      "software platforms.",
        "career": [
            {"period": "2024\u2013present", "role": "Group Chief Executive, Technology &amp; Chief Technology Officer", "org": "Accenture"},
            {"period": "2023\u20132024", "role": "Group Chief Executive, Technology", "org": "Accenture"},
            {"period": "2020\u20132023", "role": "Lead, Accenture Cloud First and Data &amp; AI", "org": "Accenture"},
            {"period": "2015\u20132020", "role": "Technology lead, Communications Media &amp; Technology, and Technology North America", "org": "Accenture"},
        ],
        "education": [],
        "public_roles": ["Member, Accenture Global Management Committee"],
        "notable": [
            {"point": "Nearly tripled Accenture's cloud-certified workforce while leading Cloud First, "
                      "which became one of the firm's top growth drivers.",
             "source": "https://www.businesswire.com/news/home/20230727478836/en"},
            {"point": "Took on the CTO title in September 2024 on top of running the Technology business "
                      "\u2014 an unusual combination that concentrates both strategy and P&amp;L in one seat.",
             "source": "https://www.businesswire.com/news/home/20240611685425/en/accenture-announces-leadership-appointments"},
        ],
        "talking_points": [
            "He owns both the technology strategy and the Technology P&amp;L, so he can commit on both capability and commercials in one conversation.",
            "Cloud and data foundations are his home ground \u2014 a good route into the Data Foundation prerequisite rather than a use-case discussion.",
            "Ecosystem partnerships sit under him, which matters if you want Accenture to deliver on a specific vendor's stack.",
        ],
        "links": [
            {"label": "Appointment announcement (2024)", "url": "https://www.businesswire.com/news/home/20240611685425/en/accenture-announces-leadership-appointments"},
            {"label": "Earlier appointment (2023)", "url": "https://newsroom.accenture.com/news/2023/accenture-announces-leadership-appointments-fy2024"},
        ],
    },
    {
        "id": "accenture-john-walsh",
        "vendor_slug": "accenture",
        "name": "John Walsh",
        "title": "Chief Operating Officer",
        "in_role_since": "COO since 1 September 2023",
        "focus": "Runs Accenture's global business operations and infrastructure, and executes the "
                 "enterprise reinvention strategy internally.",
        "background": "A career Accenture operator with more than thirty years at the firm. He built a "
                      "technology-enabled global sales organisation as Chief Strategic Accounts &amp; Global "
                      "Sales Officer before becoming COO, and previously led the Communications, Media &amp; "
                      "Technology group and the Northern California office.",
        "career": [
            {"period": "2023\u2013present", "role": "Chief Operating Officer", "org": "Accenture"},
            {"period": "before 2023", "role": "Chief Strategic Accounts &amp; Global Sales Officer", "org": "Accenture"},
            {"period": "earlier", "role": "Group Chief Executive, Global Communications, Media &amp; Technology", "org": "Accenture"},
            {"period": "earlier", "role": "Managing Director, Northern California", "org": "Accenture"},
        ],
        "education": ["B.S., Iowa State University", "Executive management programme, IMD (Switzerland)"],
        "public_roles": ["Member, Accenture Global Management Committee"],
        "notable": [
            {"point": "Established Accenture's technology-enabled global sales organisation, credited with "
                      "contributing to record revenue growth.",
             "source": "https://www.businesswire.com/news/home/20230727478836/en"},
        ],
        "talking_points": [
            "The operations seat \u2014 relevant for delivery model, staffing seniority and how an engagement is actually resourced.",
            "Sales organisation is his heritage, so commercial structure and account coverage are within his gift.",
        ],
        "links": [
            {"label": "Appointment announcement (2023)", "url": "https://newsroom.accenture.com/news/2023/accenture-announces-leadership-appointments-fy2024"},
        ],
    },

    # ================================================= Adobe
    {
        "id": "adobe-shantanu-narayen",
        "vendor_slug": "adobe",
        "name": "Shantanu Narayen",
        "title": "Chair &amp; Chief Executive Officer",
        "in_role_since": "CEO since 1 December 2007; announced 12 March 2026 that he will transition once a successor is appointed, remaining Chair",
        "focus": "Leads Adobe through a second platform transition \u2014 from the cloud/subscription model "
                 "he built to generative AI embedded across Creative Cloud, Document Cloud and Experience "
                 "Cloud.",
        "background": "An engineer turned operator who has run Adobe for eighteen years and is credited as "
                      "the architect of its shift to software-as-a-service. He joined Adobe in 1998 as VP "
                      "and General Manager of the engineering technology group, becoming SVP worldwide "
                      "products in 1999, EVP in 2001 and President &amp; COO in January 2005 before taking "
                      "the CEO role. Before Adobe he co-founded Pictra Inc., an early digital photo-sharing "
                      "company, and held roles at Silicon Graphics and Apple. He holds five patents.",
        "career": [
            {"period": "2007\u2013present", "role": "Chief Executive Officer (Chair from 2017)", "org": "Adobe"},
            {"period": "2005\u20132007", "role": "President &amp; Chief Operating Officer", "org": "Adobe"},
            {"period": "1998\u20132005", "role": "VP &amp; GM engineering technology, then SVP/EVP worldwide products", "org": "Adobe"},
            {"period": "before 1998", "role": "Co-founder", "org": "Pictra Inc."},
            {"period": "earlier", "role": "Director, desktop and collaboration products", "org": "Silicon Graphics"},
            {"period": "earlier", "role": "Senior management roles", "org": "Apple Computer"},
        ],
        "education": [],
        "public_roles": ["Advisory Board, Haas School of Business, University of California, Berkeley"],
        "notable": [
            {"point": "Announced on 12 March 2026 that he will step down as CEO once a successor is "
                      "appointed, remaining Chair. Shares fell around 7% on the news. A special committee "
                      "chaired by Lead Independent Director Frank Calderoni is running the search across "
                      "internal and external candidates.",
             "source": "https://www.businesswire.com/news/home/20260312777904/en/Shantanu-Narayen-Announces-Decision-to-Transition-as-Adobes-CEO-Once-Successor-is-Named"},
            {"point": "Under his tenure AI-influenced ARR passed $5B in FY2025 \u2014 more than a third of "
                      "Adobe's total recurring revenue base.",
             "source": "https://sqmagazine.co.uk/adobe-creative-cloud-statistics/"},
        ],
        "talking_points": [
            "He is a transitioning CEO: strategic commitments made now may outlast him, so establish who else owns the relationship.",
            "He led one platform transition successfully (perpetual to subscription) and is being judged on whether he can lead a second.",
            "The defensible Adobe claim is commercially-safe training data, not model capability \u2014 pitch to indemnity and brand risk.",
        ],
        "links": [
            {"label": "CEO transition announcement", "url": "https://www.businesswire.com/news/home/20260312777904/en/Shantanu-Narayen-Announces-Decision-to-Transition-as-Adobes-CEO-Once-Successor-is-Named"},
            {"label": "Adobe Q4 FY25 earnings transcript", "url": "https://www.adobe.com/cc-shared/assets/investor-relations/pdfs/adbe-q4fy25-transcript.pdf"},
        ],
        "notes": "Adobe's Chief Technology Officer could not be confirmed in research and is deliberately "
                 "absent from the contact list rather than guessed.",
    },

    # ================================================= Amazon Web Services
    {
        "id": "aws-matt-garman",
        "vendor_slug": "aws",
        "name": "Matt Garman",
        "title": "Chief Executive Officer, AWS",
        "in_role_since": "CEO of AWS since June 2024",
        "focus": "Runs AWS \u2014 global cloud and AI infrastructure strategy, the Bedrock and SageMaker "
                 "stack, and the custom silicon programme \u2014 and sits on Amazon's senior leadership "
                 "S-Team.",
        "background": "About as deep an AWS insider as exists. He interned at Amazon in 2005 on an unnamed "
                      "internal startup pitched to him by Andy Jassy, joined full time in 2006 when AWS "
                      "launched, and became one of its first product managers, helping launch the initial "
                      "set of services. He ran EC2 and the Compute Services business for over a decade, "
                      "then led Sales, Marketing and Global Services before succeeding Jassy's successor as "
                      "CEO. Before Amazon he held product management roles at early-stage internet startups "
                      "including SideStep and Riffage.",
        "career": [
            {"period": "2024\u2013present", "role": "Chief Executive Officer", "org": "Amazon Web Services"},
            {"period": "before 2024", "role": "Senior Vice President, Sales, Marketing &amp; Global Services", "org": "Amazon Web Services"},
            {"period": "~2010\u20132020s", "role": "Vice President, Amazon EC2 and Compute Services", "org": "Amazon Web Services"},
            {"period": "2006", "role": "One of the first Product Managers at AWS launch", "org": "Amazon Web Services"},
            {"period": "before 2006", "role": "Product management roles", "org": "SideStep and other early-stage internet startups"},
        ],
        "education": [
            "MBA, Kellogg School of Management, Northwestern University",
            "B.S. and M.S., Industrial Engineering, Stanford University",
        ],
        "public_roles": ["Member, Amazon S-Team (senior leadership team)"],
        "notable": [
            {"point": "Has said AWS is securing five-year customer commitments with capacity booked through "
                      "2028, and that Trainium is largely sold out through the end of next year \u2014 "
                      "context that materially weakens a buyer's negotiating position.",
             "source": "https://finance.biggo.com/news/17c3d23c-6ff9-4199-a99e-b759ebc0b844"},
            {"point": "Frames the AI capex programme in return-on-invested-capital terms rather than as a "
                      "bet, arguing the demand data is not speculative \u2014 useful to engage on directly.",
             "source": "https://www.aboutamazon.com/news/aws/aws/aws-matt-garman-enterprise-ai-roi-interview-2026"},
        ],
        "talking_points": [
            "A product person, not a salesperson \u2014 technical depth on compute and inference economics will land better than a commercial pitch.",
            "He argues enterprises see returns from task-accomplishing agents rather than content generation; frame use cases that way.",
            "Capacity constraint is real and he says so openly; secure allocation early rather than assuming availability.",
        ],
        "links": [
            {"label": "AWS speaker bio", "url": "https://aws.amazon.com/resources/analyst-summit-at-re-invent-speakers/"},
            {"label": "Ten things to know (Amazon)", "url": "https://www.aboutamazon.com/news/aws/aws-ceo-matt-garman-things-to-know"},
            {"label": "Enterprise AI ROI interview (2026)", "url": "https://www.aboutamazon.com/news/aws/aws/aws-matt-garman-enterprise-ai-roi-interview-2026"},
        ],
    },
    {
        "id": "aws-andy-jassy",
        "vendor_slug": "aws",
        "name": "Andy Jassy",
        "title": "President &amp; Chief Executive Officer, Amazon",
        "in_role_since": "CEO of Amazon since July 2021",
        "focus": "Leads Amazon overall, and remains the most senior voice on AWS strategy and the capital "
                 "programme behind it \u2014 he sets the capex envelope AWS builds within.",
        "background": "Founded and built AWS from an internal idea into the largest cloud business in the "
                      "world, running it as CEO until succeeding Jeff Bezos as Amazon CEO in 2021. He "
                      "recruited Matt Garman as an intern to the then-unnamed AWS project in 2005, which "
                      "gives the current AWS leadership an unusually continuous lineage.",
        "career": [
            {"period": "2021\u2013present", "role": "President &amp; Chief Executive Officer", "org": "Amazon"},
            {"period": "2016\u20132021", "role": "Chief Executive Officer", "org": "Amazon Web Services"},
            {"period": "2003\u20132016", "role": "Founder and leader of AWS", "org": "Amazon"},
        ],
        "education": [],
        "public_roles": [],
        "notable": [
            {"point": "Projects AWS revenue could reach $600B annually by 2036 \u2014 double his prior "
                      "estimate \u2014 and has committed roughly $200B of 2026 capital expenditure, later "
                      "raised, ahead of demand.",
             "source": "https://finance.yahoo.com/news/amazon-says-10-years-aws-161434099.html"},
            {"point": "Reported that AWS AI revenue passed a $15B run rate in Q1 2026, with Bedrock "
                      "processing more tokens in that quarter than in all prior years combined.",
             "source": "https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-aws-ai-q1-2026-earnings"},
        ],
        "talking_points": [
            "Escalation point above Garman, not a day-to-day counterpart \u2014 reserve for portfolio-scale commitments.",
            "His public numbers set the frame for any AWS conversation; know the current capex and AI run-rate figures.",
        ],
        "links": [
            {"label": "Q1 2026 AWS commentary", "url": "https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-aws-ai-q1-2026-earnings"},
        ],
    },

    # ================================================= Anthropic
    {
        "id": "anthropic-dario-amodei",
        "vendor_slug": "anthropic",
        "name": "Dario Amodei",
        "title": "Co-Founder &amp; Chief Executive Officer",
        "in_role_since": "Co-founded Anthropic in 2021 and has been CEO since",
        "focus": "Sets Anthropic's research direction and is its principal public voice on AI safety, "
                 "scaling and policy.",
        "background": "A researcher who became a CEO. He was VP of Research at OpenAI, where he led "
                      "development of the GPT-2 and GPT-3 language models, and is a co-inventor of "
                      "reinforcement learning from human feedback \u2014 the technique behind most modern "
                      "conversational AI. Before OpenAI he was a senior research scientist at Google Brain, "
                      "and he also spent time at Baidu. He left OpenAI in late 2020 with his sister Daniela "
                      "and several colleagues over differences on safety culture and commercial direction, "
                      "founding Anthropic around Constitutional AI \u2014 training models against an "
                      "explicit written set of principles rather than relying solely on human feedback.",
        "career": [
            {"period": "2021\u2013present", "role": "Co-Founder &amp; Chief Executive Officer", "org": "Anthropic"},
            {"period": "2019\u20132020", "role": "Vice President of Research", "org": "OpenAI"},
            {"period": "2018\u20132019", "role": "Research Director", "org": "OpenAI"},
            {"period": "2016\u20132018", "role": "Team Lead, AI Safety", "org": "OpenAI"},
            {"period": "earlier", "role": "Senior Research Scientist", "org": "Google Brain"},
            {"period": "earlier", "role": "Researcher", "org": "Baidu"},
        ],
        "education": [
            "PhD, biophysics, Princeton University (Hertz Fellow)",
            "Postdoctoral scholar, Stanford University School of Medicine",
            "Undergraduate study in physics, Stanford University",
        ],
        "public_roles": ["Named to TIME's 100 Most Influential People in AI (2023)"],
        "notable": [
            {"point": "Co-invented reinforcement learning from human feedback and pioneered empirical AI "
                      "scaling laws \u2014 the work underpinning the industry's compute-scaling thesis.",
             "source": "https://www.weforum.org/people/dario-amodei/"},
            {"point": "Has publicly predicted that models could exceed human capability on most "
                      "economically valuable tasks by 2026 or 2027 \u2014 a position worth testing rather "
                      "than accepting, since it shapes how Anthropic prices and roadmaps.",
             "source": "https://publication.aimagazine.com/ai-magazine-top-100-leaders-2026/0796921001767963467/p87"},
        ],
        "talking_points": [
            "Research-led, not commercially-led \u2014 safety and interpretability arguments carry more weight with him than procurement terms.",
            "Constitutional AI and the Responsible Scaling Policy are the frameworks he will reach for; understanding them is table stakes.",
            "With an IPO filed, his public statements now carry securities weight \u2014 expect more caution than in earlier interviews.",
        ],
        "links": [
            {"label": "World Economic Forum profile", "url": "https://www.weforum.org/people/dario-amodei/"},
            {"label": "AI Magazine Top 100 Leaders 2026", "url": "https://publication.aimagazine.com/ai-magazine-top-100-leaders-2026/0796921001767963467/p87"},
        ],
    },
    {
        "id": "anthropic-daniela-amodei",
        "vendor_slug": "anthropic",
        "name": "Daniela Amodei",
        "title": "Co-Founder &amp; President",
        "in_role_since": "Co-founded Anthropic in January 2021 and has been President since",
        "focus": "Runs the business \u2014 operations, people, finance, commercial strategy, enterprise "
                 "partnerships and policy engagement. The counterpart for anything commercial; her brother "
                 "owns research.",
        "background": "An operator rather than a researcher, which is why the division of labour at "
                      "Anthropic is unusually clean. She built her career in operations, recruiting, risk "
                      "management and people programmes \u2014 first at Stripe from 2013 to 2018 as a risk "
                      "manager and lead technical recruiter, then at OpenAI from 2018, where she was an "
                      "engineering manager over natural language processing and music generation teams, VP "
                      "of People, and finally VP of Safety and Policy. She left with her brother and "
                      "colleagues in late 2020 to co-found Anthropic and sits on its board.",
        "career": [
            {"period": "2021\u2013present", "role": "Co-Founder &amp; President", "org": "Anthropic"},
            {"period": "2020", "role": "Vice President of Safety &amp; Policy", "org": "OpenAI"},
            {"period": "2018\u20132020", "role": "Engineering Manager, and VP of People", "org": "OpenAI"},
            {"period": "2013\u20132018", "role": "Risk Manager and Lead Technical Recruiter", "org": "Stripe"},
        ],
        "education": ["BA, University of California, Santa Cruz"],
        "public_roles": [
            "Member, Anthropic Board of Directors",
            "Named to TIME's 100 Most Influential People in AI (2023)",
        ],
        "notable": [
            {"point": "Oversaw fundraising across multiple rounds, including the February 2026 Series G at "
                      "a $380B valuation and the May 2026 Series H at $965B.",
             "source": "https://www.longtermwiki.com/wiki/daniela-amodei"},
            {"point": "Leads enterprise partnerships and policy engagement, and has publicly explained "
                      "Constitutional AI methodology to both policymakers and enterprise customers.",
             "source": "https://www.longtermwiki.com/wiki/daniela-amodei"},
        ],
        "talking_points": [
            "The right counterpart for a commercial or partnership conversation \u2014 Dario is the research voice, she is the business one.",
            "Her background is operations and people, so questions about delivery, support model and scaling will get substantive answers.",
            "She owns policy engagement, which matters if regulatory posture is part of your PortCo diligence.",
        ],
        "links": [
            {"label": "Anthropic newsroom", "url": "https://www.anthropic.com/news/krishna-rao-joins-anthropic"},
        ],
    },
    {
        "id": "anthropic-krishna-rao",
        "vendor_slug": "anthropic",
        "name": "Krishna Rao",
        "title": "Chief Financial Officer",
        "in_role_since": "Anthropic's first CFO, appointed May 2024",
        "focus": "Owns financial strategy and operations through a period of extreme growth and capital "
                 "intensity, and is professionalising the finance function ahead of a public listing.",
        "background": "A finance leader with roughly twenty years across investing, consulting and "
                      "operating roles. He began at Bain &amp; Company as a strategy consultant and moved to "
                      "Blackstone as a private equity investor \u2014 so a private-markets counterpart will "
                      "find shared language. At Airbnb he led corporate and operations FP&amp;A and then "
                      "global corporate and business development, helping raise over $10 billion in equity "
                      "and debt including the IPO, and steering the company through the pandemic. He was "
                      "then CFO of Cedar, a healthcare payments platform, and CFO of Fanatics Commerce "
                      "before joining Anthropic as its first CFO.",
        "career": [
            {"period": "2024\u2013present", "role": "Chief Financial Officer", "org": "Anthropic"},
            {"period": "2023\u20132024", "role": "Chief Financial Officer, Fanatics Commerce", "org": "Fanatics"},
            {"period": "2021\u20132023", "role": "Chief Financial Officer", "org": "Cedar"},
            {"period": "2018\u20132021", "role": "Global Head of Corporate &amp; Business Development", "org": "Airbnb"},
            {"period": "earlier", "role": "Director, Corporate and Operations FP&amp;A", "org": "Airbnb"},
            {"period": "earlier", "role": "Private equity investor", "org": "Blackstone"},
            {"period": "earlier", "role": "Strategy consultant", "org": "Bain &amp; Company"},
        ],
        "education": ["J.D., Yale Law School", "A.B. summa cum laude in Economics, Harvard College"],
        "public_roles": ["Fellow, Tidemark (since 2021)"],
        "notable": [
            {"point": "Framed the February 2026 $30B Series G around enterprise demand, noting that "
                      "customers from startups to the largest enterprises describe Claude as increasingly "
                      "critical to how their businesses work.",
             "source": "https://www.anthropic.com/news/krishna-rao-joins-anthropic"},
            {"point": "Took Airbnb through its IPO and pandemic-era financing \u2014 directly relevant "
                      "experience as Anthropic approaches its own listing.",
             "source": "https://goldhouse.org/people/krishna-rao/"},
        ],
        "talking_points": [
            "Ex-Blackstone and ex-Bain \u2014 the one person at Anthropic who will speak private-markets language natively.",
            "Owns budget and procurement discipline as the company professionalises pre-IPO; the right counterpart for commercial terms at scale.",
            "IPO experience means he will be increasingly careful about what can be said publicly; expect more structure, fewer off-the-cuff commitments.",
        ],
        "links": [
            {"label": "Anthropic appointment announcement", "url": "https://www.anthropic.com/news/krishna-rao-joins-anthropic"},
            {"label": "Gold House profile", "url": "https://goldhouse.org/people/krishna-rao/"},
        ],
    },
]
