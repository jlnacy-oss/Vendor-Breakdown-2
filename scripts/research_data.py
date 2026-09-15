# -*- coding: utf-8 -*-
"""
research_data.py — the REGENERABLE research layer.

Everything in this file comes from public sources and can be thrown away and
rebuilt by a fresh research pass. No GIP-confidential data belongs here; that
lives in gip-tracker.xlsx and is read by the browser at load time.

Two collections:
  TAXONOMY  — the filter categories used on the overview page
  VENDORS   — every tracked vendor. Vendors carrying research_status="full"
              are backed by vendor_data.py (deep research complete).
              research_status="pending" means the shell exists and the deep
              research pass has not run yet.
"""
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from vendor_data import VENDORS as RESEARCHED
from deep_research import DEEP

# --------------------------------------------------------------- taxonomy
TAXONOMY = [
    "LLM / Foundation Model",
    "ERP",
    "CRM",
    "ITSM / Workflow",
    "System Integrator",
    "Consulting / Advisory",
    "Managed Services",
    "Data Platform",
    "Analytics & BI",
    "Cybersecurity",
    "Physical / Industrial AI",
    "Digital Twin",
    "Engineering Software",
    "Cloud & Infrastructure",
    "Automation / RPA",
    "Semiconductors / Compute",
    "Content & Marketing",
]

# Tags for the nine vendors that already have deep-research dashboards.
TAGS_RESEARCHED = {
    "sand-technologies":  ["Physical / Industrial AI", "Digital Twin", "System Integrator"],
    "palantir":           ["Physical / Industrial AI", "Data Platform", "Analytics & BI"],
    "c3ai":               ["Physical / Industrial AI", "Analytics & BI"],
    "cognite":            ["Physical / Industrial AI", "Digital Twin", "Data Platform"],
    "bentley-systems":    ["Engineering Software", "Digital Twin"],
    "aveva":              ["Engineering Software", "Digital Twin", "Physical / Industrial AI"],
    "ibm-watsonx":        ["LLM / Foundation Model", "Data Platform", "Physical / Industrial AI"],
    "honeywell-forge":    ["Physical / Industrial AI", "Digital Twin"],
    "siemens-xcelerator": ["Physical / Industrial AI", "Digital Twin", "Engineering Software"],
}

# --------------------------------------------------------------- pending vendors
# Only facts held with high confidence are recorded here: legal name, primary
# website, LinkedIn company page, and a one-line description of what the company
# does. Revenue, headcount, use cases, sentiment and named executives are left
# empty deliberately — those get filled by the deep-research pass, not guessed.
PENDING = [
    # ---- frontier AI / LLM
    ("openai", "OpenAI", "https://openai.com", "https://www.linkedin.com/company/openai",
     "Frontier AI / LLM", ["LLM / Foundation Model"],
     "Frontier AI lab behind the GPT model family and ChatGPT; sells API access and enterprise assistants."),
    ("anthropic", "Anthropic", "https://www.anthropic.com", "https://www.linkedin.com/company/anthropicresearch",
     "Frontier AI / LLM", ["LLM / Foundation Model"],
     "Frontier AI lab behind the Claude model family; sells API access, Claude for Work, and agentic coding tools."),
    ("google", "Google", "https://cloud.google.com", "https://www.linkedin.com/company/google",
     "Frontier AI / LLM", ["LLM / Foundation Model", "Cloud & Infrastructure", "Analytics & BI"],
     "Gemini model family, Vertex AI, and Google Cloud infrastructure and analytics services."),
    ("microsoft", "Microsoft", "https://www.microsoft.com", "https://www.linkedin.com/company/microsoft",
     "Frontier AI / LLM", ["LLM / Foundation Model", "Cloud & Infrastructure", "ERP",
                           "Analytics & BI", "Cybersecurity"],
     "Azure cloud and AI services, the Copilot assistant family, Dynamics 365 ERP/CRM, Fabric, and security products."),
    ("aws", "Amazon Web Services", "https://aws.amazon.com", "https://www.linkedin.com/company/amazon-web-services",
     "Frontier AI / LLM", ["Cloud & Infrastructure", "LLM / Foundation Model", "Data Platform"],
     "Cloud infrastructure provider; Bedrock model hosting, SageMaker, and the Nova model family."),
    ("nvidia", "NVIDIA", "https://www.nvidia.com", "https://www.linkedin.com/company/nvidia",
     "Frontier AI / LLM", ["Semiconductors / Compute", "Cloud & Infrastructure"],
     "GPU and accelerated-computing supplier underpinning most AI training and inference, plus Omniverse digital-twin software."),
    ("meta", "Meta", "https://ai.meta.com", "https://www.linkedin.com/company/meta",
     "Frontier AI / LLM", ["LLM / Foundation Model"],
     "Publisher of the open-weight Llama model family alongside its consumer social platforms."),
    ("xai", "xAI", "https://x.ai", "https://www.linkedin.com/company/xai",
     "Frontier AI / LLM", ["LLM / Foundation Model"],
     "Frontier AI lab behind the Grok model family, with API and enterprise offerings."),
    ("perplexity", "Perplexity", "https://www.perplexity.ai", "https://www.linkedin.com/company/perplexity-ai",
     "Frontier AI / LLM", ["LLM / Foundation Model"],
     "AI answer engine combining retrieval and generation, with enterprise and API tiers."),

    # ---- enterprise software
    ("sap", "SAP", "https://www.sap.com", "https://www.linkedin.com/company/sap",
     "Enterprise software", ["ERP", "Analytics & BI"],
     "The dominant enterprise ERP suite (S/4HANA), with the Business Technology Platform and Joule AI assistant."),
    ("oracle", "Oracle", "https://www.oracle.com", "https://www.linkedin.com/company/oracle",
     "Enterprise software", ["ERP", "Cloud & Infrastructure", "Data Platform"],
     "Database, Fusion Cloud ERP/HCM applications, and Oracle Cloud Infrastructure."),
    ("salesforce", "Salesforce", "https://www.salesforce.com", "https://www.linkedin.com/company/salesforce",
     "Enterprise software", ["CRM", "Analytics & BI", "Automation / RPA"],
     "The leading CRM platform, plus Data Cloud, Tableau, MuleSoft and the Agentforce agent framework."),
    ("servicenow", "ServiceNow", "https://www.servicenow.com", "https://www.linkedin.com/company/servicenow",
     "Enterprise software", ["ITSM / Workflow", "Automation / RPA"],
     "Enterprise workflow and IT service management platform with an expanding agentic AI layer."),
    ("workday", "Workday", "https://www.workday.com", "https://www.linkedin.com/company/workday",
     "Enterprise software", ["ERP"],
     "Cloud HCM and financial management suite for large enterprises."),
    ("adobe", "Adobe", "https://www.adobe.com", "https://www.linkedin.com/company/adobe",
     "Enterprise software", ["Content & Marketing"],
     "Creative and digital-experience software, including the Firefly generative models."),

    # ---- data platforms
    ("databricks", "Databricks", "https://www.databricks.com", "https://www.linkedin.com/company/databricks",
     "Data platform", ["Data Platform", "Analytics & BI"],
     "Lakehouse data and AI platform built around Apache Spark, Delta Lake, Unity Catalog and MLflow."),
    ("snowflake", "Snowflake", "https://www.snowflake.com", "https://www.linkedin.com/company/snowflake-computing",
     "Data platform", ["Data Platform", "Analytics & BI"],
     "Cloud data warehouse and data-sharing platform with native AI/ML services."),

    # ---- automation & security
    ("uipath", "UiPath", "https://www.uipath.com", "https://www.linkedin.com/company/uipath",
     "Automation", ["Automation / RPA"],
     "Robotic process automation and agentic automation platform for back-office and operational workflows."),
    ("crowdstrike", "CrowdStrike", "https://www.crowdstrike.com", "https://www.linkedin.com/company/crowdstrike",
     "Cybersecurity", ["Cybersecurity"],
     "Cloud-native endpoint protection and threat intelligence via the Falcon platform."),

    # ---- system integrators, consultancies & delivery partners
    ("accenture", "Accenture", "https://www.accenture.com", "https://www.linkedin.com/company/accenture",
     "SI / Consulting", ["System Integrator", "Consulting / Advisory", "Managed Services"],
     "Global professional services firm; strategy, technology implementation and managed operations at scale."),
    ("deloitte", "Deloitte", "https://www.deloitte.com", "https://www.linkedin.com/company/deloitte",
     "SI / Consulting", ["Consulting / Advisory", "System Integrator"],
     "Big Four professional services network; audit, consulting, risk and technology implementation."),
    ("pwc", "PwC", "https://www.pwc.com", "https://www.linkedin.com/company/pwc",
     "SI / Consulting", ["Consulting / Advisory", "System Integrator"],
     "Big Four professional services network; assurance, advisory, tax and technology transformation."),
    ("ey", "EY", "https://www.ey.com", "https://www.linkedin.com/company/ernstandyoung",
     "SI / Consulting", ["Consulting / Advisory", "System Integrator"],
     "Big Four professional services network; assurance, consulting, strategy and transactions."),
    ("kpmg", "KPMG", "https://kpmg.com", "https://www.linkedin.com/company/kpmg",
     "SI / Consulting", ["Consulting / Advisory", "System Integrator"],
     "Big Four professional services network; audit, tax and advisory including technology delivery."),
    ("mckinsey", "McKinsey & Company", "https://www.mckinsey.com", "https://www.linkedin.com/company/mckinsey",
     "SI / Consulting", ["Consulting / Advisory"],
     "Global management consultancy; QuantumBlack is its AI and analytics arm."),
    ("bcg", "Boston Consulting Group", "https://www.bcg.com", "https://www.linkedin.com/company/boston-consulting-group",
     "SI / Consulting", ["Consulting / Advisory"],
     "Global management consultancy; BCG X is its technology build and AI arm."),
    ("bain", "Bain & Company", "https://www.bain.com", "https://www.linkedin.com/company/bain-and-company",
     "SI / Consulting", ["Consulting / Advisory"],
     "Global management consultancy with a large private equity advisory practice."),
    ("ibm-consulting", "IBM Consulting", "https://www.ibm.com/consulting", "https://www.linkedin.com/company/ibm",
     "SI / Consulting", ["System Integrator", "Consulting / Advisory", "Managed Services"],
     "IBM's services arm; systems integration and managed operations, often paired with watsonx."),
    ("tcs", "Tata Consultancy Services", "https://www.tcs.com", "https://www.linkedin.com/company/tata-consultancy-services",
     "SI / Consulting", ["System Integrator", "Managed Services"],
     "India-headquartered global IT services and consulting firm, part of the Tata Group."),
    ("infosys", "Infosys", "https://www.infosys.com", "https://www.linkedin.com/company/infosys",
     "SI / Consulting", ["System Integrator", "Managed Services"],
     "India-headquartered global IT services firm; Infosys Topaz is its AI services brand."),
    ("wipro", "Wipro", "https://www.wipro.com", "https://www.linkedin.com/company/wipro",
     "SI / Consulting", ["System Integrator", "Managed Services"],
     "India-headquartered global IT services and consulting firm."),
    ("hcltech", "HCLTech", "https://www.hcltech.com", "https://www.linkedin.com/company/hcltech",
     "SI / Consulting", ["System Integrator", "Managed Services"],
     "India-headquartered global technology services firm with a large engineering services practice."),
    ("cognizant", "Cognizant", "https://www.cognizant.com", "https://www.linkedin.com/company/cognizant",
     "SI / Consulting", ["System Integrator", "Managed Services"],
     "US-headquartered global IT services and consulting firm."),
    ("capgemini", "Capgemini", "https://www.capgemini.com", "https://www.linkedin.com/company/capgemini",
     "SI / Consulting", ["System Integrator", "Consulting / Advisory", "Managed Services"],
     "France-headquartered global consulting and technology services group; strong engineering practice."),
    ("ntt-data", "NTT DATA", "https://www.nttdata.com", "https://www.linkedin.com/company/ntt-data",
     "SI / Consulting", ["System Integrator", "Managed Services"],
     "Japan-headquartered global IT services and systems integration firm."),
    ("dxc", "DXC Technology", "https://dxc.com", "https://www.linkedin.com/company/dxctechnology",
     "SI / Consulting", ["System Integrator", "Managed Services"],
     "US-headquartered IT services firm focused on managed infrastructure and application operations."),
    ("booz-allen", "Booz Allen Hamilton", "https://www.boozallen.com", "https://www.linkedin.com/company/booz-allen-hamilton",
     "SI / Consulting", ["Consulting / Advisory", "System Integrator"],
     "US consulting firm concentrated in government, defense and critical infrastructure work."),
    ("syntax", "Syntax", "https://www.syntax.com", "https://www.linkedin.com/company/syntax",
     "SI / Consulting", ["Managed Services", "ERP"],
     "Managed cloud and application services provider specialising in running SAP and Oracle ERP estates."),
    ("aziro", "Aziro", "https://www.aziro.com/en", "https://www.linkedin.com/company/azirotech",
     "SI / Consulting", ["System Integrator", "Managed Services"],
     "AI-native product engineering firm, rebranded from MSys Technologies in June 2025; infrastructure "
     "engineering, DevSecOps, QA automation and agentic platform work for enterprises and ISVs."),
    ("tribola-tech", "Tribola Tech", "https://www.tribolatech.com", "https://www.linkedin.com/company/tribolatech-inc",
     "SI / Consulting", ["System Integrator", "CRM", "Data Platform"],
     "US and India delivery firm (San Ramon, CA and Bengaluru) focused on Enterprise AI, Salesforce "
     "and data engineering."),
]


def _from_researched(v, tags=None, group=None, has_pdf=True):
    """Wrap a fully-researched record (vendor_data.py or deep_research.py)."""
    return {
        "slug": v["slug"],
        "name": v["name"],
        "website": v["website"],
        "linkedin": v.get("linkedin", ""),
        "group": group or v.get("group", "Physical / Industrial AI"),
        "category": v["category"],
        "tags": tags if tags is not None else TAGS_RESEARCHED.get(v["slug"], []),
        "description": v["description"],
        "revenue_short": v.get("revenue_short", "—"),
        "hq": v.get("hq", ""),
        "ownership": v.get("ownership", ""),
        "people": v.get("people", []),
        "research_status": "full",
        "has_pdf": has_pdf,
    }


def _from_pending(rec):
    slug, name, website, linkedin, group, tags, desc = rec
    return {
        "slug": slug,
        "name": name,
        "website": website,
        "linkedin": linkedin,
        "group": group,
        "category": " · ".join(tags),
        "tags": tags,
        "description": desc,
        "revenue_short": "Not yet researched",
        "hq": "",
        "ownership": "",
        "people": [],
        "research_status": "pending",
        "has_pdf": False,
    }


# Vendors promoted out of PENDING by a completed deep-research pass keep the tags
# and grouping defined above, so the filters don't shift when research lands.
_DEEP_SLUGS = {d["slug"] for d in DEEP}
_PENDING_META = {p[0]: {"tags": p[5], "group": p[4]} for p in PENDING}

VENDORS = (
    [_from_researched(v) for v in RESEARCHED]
    + [_from_researched(d,
                        tags=_PENDING_META.get(d["slug"], {}).get("tags", []),
                        group=_PENDING_META.get(d["slug"], {}).get("group"),
                        has_pdf=False)
       for d in DEEP]
    + [_from_pending(p) for p in PENDING if p[0] not in _DEEP_SLUGS]
)
VENDORS.sort(key=lambda v: v["name"].lower())

BY_SLUG = {v["slug"]: v for v in VENDORS}


def dash_href(slug):
    return f"{slug}-dashboard.html"


def pdf_href(slug):
    return "Sand-Technologies-One-Sheet.pdf" if slug == "sand-technologies" else f"{slug}-one-sheet.pdf"


def person_id(slug, name):
    import re
    return slug + "-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def person_href(slug, name):
    return f"person-{person_id(slug, name)}.html"


if __name__ == "__main__":
    full = sum(1 for v in VENDORS if v["research_status"] == "full")
    print(f"{len(VENDORS)} vendors — {full} researched, {len(VENDORS) - full} pending")
    print(f"{len(TAXONOMY)} taxonomy tags")
