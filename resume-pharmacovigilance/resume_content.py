"""Single source of truth for Aparna Mishra's pharmacovigilance resume.

build_resume.py renders this content into .docx, .pdf and .txt.
Anything wrapped in [square brackets] is a placeholder that must be filled in
with a real value before the resume is sent out (see README.md).
"""

NAME = "APARNA MISHRA"

HEADLINE = (
    "Pharmacovigilance & Drug Safety | ICSR Case Processing | MedDRA Coding | "
    "Adverse Event Reporting"
)

CONTACT = [
    "[City, State], India | Open to relocation | Available for rotational shifts",
    "+91-7355334597 | diaparna03@gmail.com | linkedin.com/in/aparnamishraa176",
]

SUMMARY = (
    "M.Pharm (Pharmacology) postgraduate and certified Clinical Research and Pharmacovigilance "
    "professional targeting Drug Safety Associate / Pharmacovigilance Associate roles. Trained in "
    "end-to-end ICSR case processing - case intake, duplicate check, triage, data entry, MedDRA and "
    "WHO-DD coding, causality and seriousness assessment, medical narrative writing and quality "
    "review - with working knowledge of ICH E2A/E2B(R3)/E2C(R2)/E2D, EU GVP Modules VI and VII, 21 CFR "
    "expedited reporting, and India NDCT Rules 2019 / PvPI timelines (7-day fatal, 15-day serious, "
    "90-day non-serious). Hands-on with VigiFlow and VigiAccess; foundational training in Oracle Argus "
    "Safety, ArisGlobal ARISg and Veeva Vault Safety. Currently in a GMP-regulated role at "
    "Dr. Reddy's Laboratories, bringing documentation accuracy, data-integrity discipline and "
    "SOP compliance transferable to drug safety operations."
)

SKILLS = [
    (
        "Pharmacovigilance Operations",
        "ICSR case processing (end-to-end); case intake and receipt; duplicate search; triage; "
        "case creation and data entry; seriousness, expectedness and listedness assessment; "
        "causality assessment (WHO-UMC, Naranjo algorithm); medical narrative writing; follow-up "
        "requests; quality check (QC) and peer review; case closure and archival",
    ),
    (
        "Case Types & Formats",
        "Spontaneous, solicited, clinical trial, literature and post-marketing cases; AE, ADR, SAE, "
        "SUSAR, AESI, special situations (pregnancy, overdose, off-label use, medication error); "
        "CIOMS I, MedWatch 3500A, E2B(R3) XML, PvPI ADR reporting form, line listings",
    ),
    (
        "Coding & Dictionaries",
        "MedDRA hierarchy (SOC, HLGT, HLT, PT, LLT); MedDRA Term Selection: Points to Consider "
        "(MTS:PTC); WHO Drug Dictionary (WHO-DD) drug coding; medical terminology; "
        "anatomy and physiology",
    ),
    (
        "Safety Databases & Systems",
        "VigiFlow (hands-on, academic instance); VigiBase / VigiAccess; Oracle Argus Safety "
        "(foundational training); ArisGlobal ARISg (foundational); Veeva Vault Safety "
        "(foundational); EudraVigilance and SUGAM portal awareness",
    ),
    (
        "Regulations & Guidelines",
        "ICH E2A, E2B(R3), E2C(R2)/PBRER, E2D, E2E, E2F; EU GVP Module VI, Module VII, Module IX "
        "and Module XV; "
        "21 CFR 314.80 and 312.32 (awareness); Drugs and Cosmetics Act 1940; New Drugs and Clinical "
        "Trials (NDCT) Rules 2019; Schedule Y; PvPI / IPC / CDSCO; AMC and ADR monitoring; "
        "ICH-GCP; GVP and GMP compliance",
    ),
    (
        "Aggregate Reporting & Signal Management",
        "PSUR / PBRER and DSUR structure and content; literature screening (PubMed, Embase); "
        "signal detection and evaluation concepts; Risk Management Plan (RMP); Pharmacovigilance "
        "System Master File (PSMF) awareness; benefit-risk assessment fundamentals",
    ),
    (
        "Quality, Documentation & Compliance",
        "SOP preparation, adherence and review; Good Documentation Practice (GDP); ALCOA+ data "
        "integrity; regulatory reporting timelines and compliance metrics; deviation and CAPA "
        "awareness; audit and "
        "inspection readiness; data privacy and confidentiality",
    ),
    (
        "Technical & Professional",
        "LC-MS and HPLC analysis; analytical method development and validation; GraphPad Prism "
        "(ANOVA, post-hoc, regression); MS Excel (trackers, pivot tables, VLOOKUP), Word, PowerPoint, "
        "Outlook; attention to detail; scientific and regulatory writing; cross-functional "
        "collaboration; delivery against strict reporting deadlines; rotational shift readiness",
    ),
]

EXPERIENCE = [
    {
        "title": "Research & Development Apprentice - Analytical Research & Development (AR&D)",
        "org": "Dr. Reddy's Laboratories Ltd.",
        "location": "[City], India",
        "dates": "Jun 2026 - Present",
        "bullets": [
            "Perform routine and stability-related analytical testing of drug substances and drug "
            "products using LC-MS and HPLC for identification, quantification and impurity profiling "
            "in a GMP-regulated laboratory.",
            "Support method development and validation (specificity, linearity, accuracy, precision, "
            "calibration, system suitability), preparing protocols and reports aligned to ICH "
            "quality guidelines.",
            "Record all raw data, observations and results to Good Documentation Practice and ALCOA+ "
            "data-integrity expectations, producing audit-ready and inspection-ready documentation.",
            "Work strictly to approved SOPs and escalate atypical, out-of-trend or discrepant "
            "results per defined escalation paths - the same evidence-based, source-verified "
            "assessment discipline used in adverse event evaluation and case follow-up.",
            "Coordinate daily with QC, QA and cross-functional teams on sample tracking, "
            "documentation queries and turnaround timelines, consistently meeting committed "
            "deadlines in a deadline-driven regulated environment.",
        ],
    },
]

PV_TRAINING = {
    "heading": "PHARMACOVIGILANCE TRAINING & CASE-PROCESSING EXPOSURE",
    "note": (
        "Certification-based practicum and academic training (not industry case-processing "
        "experience) covering the complete ICSR lifecycle."
    ),
    "entries": [
        {
            "title": "Clinical Research & Pharmacovigilance Certification - Practicum",
            "org": "[Training Institute Name]",
            "location": "",
            "dates": "Oct 2025",
            "bullets": [
                "Trained on the end-to-end ICSR lifecycle - case receipt and intake from spontaneous, "
                "solicited, clinical trial and literature sources, duplicate search, triage for "
                "seriousness, case creation and data entry, coding, medical narrative writing, "
                "quality check and expedited submission - processing [N]+ simulated ICSRs against "
                "the four case validity criteria and mandatory E2B(R3) data elements.",
                "Coded adverse events, indications, medical history and investigations in the MedDRA "
                "hierarchy (SOC, HLGT, HLT, PT, LLT) applying MedDRA Term Selection: Points to "
                "Consider, and coded suspect and concomitant products using WHO Drug Dictionary.",
                "Assessed causality using WHO-UMC categories and the Naranjo algorithm; documented "
                "seriousness criteria (death, life-threatening, hospitalisation or prolongation, "
                "disability, congenital anomaly, other medically significant) and expectedness "
                "against reference safety information.",
                "Drafted structured medical narratives and CIOMS I / MedWatch 3500A style case "
                "documents covering patient history, event chronology, treatment, outcome and "
                "reporter causality, and raised follow-up queries for missing safety information.",
                "Entered and managed adverse event reports in VigiFlow and queried VigiAccess / "
                "VigiBase for product-event pairs; reviewed line listings to understand "
                "signal detection and disproportionality concepts.",
                "Mapped India reporting obligations under NDCT Rules 2019 and PvPI guidance (7-day "
                "fatal or life-threatening, 15-day serious, 90-day non-serious) against EU GVP "
                "Module VI and US 21 CFR expedited reporting timelines.",
                "Screened biomedical literature in PubMed and Embase for valid ICSR criteria and "
                "studied the structure and content of aggregate safety reports - PSUR / PBRER per "
                "ICH E2C(R2), DSUR per ICH E2F - plus Risk Management Plan and PSMF components.",
            ],
        },
        {
            "title": "Medical Scribing & Medical Coding + Applied Pharmacotherapeutics "
            "Certifications",
            "org": "[Training Institute Name]",
            "location": "",
            "dates": "Aug 2025 - Nov 2025",
            "bullets": [
                "Built accuracy in interpreting clinical documentation, medical abbreviations, "
                "laboratory data and diagnosis-to-code mapping, and strengthened drug-class, "
                "interaction and ADR-profile knowledge used to judge event plausibility, "
                "expectedness and medical significance during case assessment.",
            ],
        },
    ],
}

EDUCATION = [
    {
        "degree": "M.Pharm - Pharmacology",
        "institute": "Lovely Professional University, Punjab",
        "dates": "Aug 2024 - May 2026",
        "detail": "Completed. CGPA: [X.XX/10]. Coursework: pharmacovigilance and drug safety, "
        "clinical research, toxicology, biostatistics, regulatory affairs.",
    },
    {
        "degree": "B.Pharm",
        "institute": "Bundelkhand University, Jhansi, Uttar Pradesh",
        "dates": "Aug 2019 - May 2023",
        "detail": "Percentage/CGPA: [X.XX].",
    },
]

PROJECTS = [
    {
        "title": "Validation of a Novel Apparatus for Parkinsonism Motor Dysfunction Assessment",
        "org": "M.Pharm Dissertation, Lovely Professional University",
        "dates": "Jul 2025 - May 2026",
        "bullets": [
            "Designed and validated a novel apparatus for reproducible motor dysfunction assessment in "
            "MPTP / 6-OHDA induced Parkinsonian rodent models under CPCSEA-compliant protocols.",
            "Documented mobility score, coordination index and latency time observations in "
            "standardised source records with over 90% reproducibility across 4 treatment groups "
            "and zero ethical protocol deviations - a documentation discipline equivalent to "
            "structured adverse event capture and case narrative preparation.",
            "Analysed data using ANOVA, post-hoc tests and regression in GraphPad Prism, reporting "
            "statistically significant outcomes (p < 0.05) accepted by the dissertation committee.",
        ],
    },
    {
        "title": "Tablet Formulation and Evaluation Study",
        "org": "Academic Project, Bundelkhand University",
        "dates": "2022 - 2023",
        "bullets": [
            "Applied wet granulation and direct compression, varying excipient ratios to resolve "
            "inconsistent dissolution profiles and batch non-uniformity; conducted pre- and "
            "post-compression testing (hardness, friability, dissolution, weight variation) to "
            "meet IP/USP acceptance criteria.",
            "Produced a complete stability evaluation report with full traceable documentation, "
            "demonstrating regulated-industry reporting skills.",
        ],
    },
]

PUBLICATIONS = [
    "Co-author - \"Hippo YAP/TAZ Signalling in Gastric Cancer Progression\", Medical Oncology, "
    "Springer Nature (Q1-indexed): literature synthesis, evidence appraisal and scientific writing.",
    "Book chapter - \"Toxicokinetics & Toxicodynamics\", LPU Publication House: ADME principles, "
    "toxic dose-response relationships.",
]

CERTIFICATIONS = [
    "Clinical Research & Pharmacovigilance Certification - [Training Institute Name], Oct 2025",
    "Medical Scribing & Medical Coding (Nov 2025) and Applied Pharmacotherapeutics, "
    "Evidence-Based Approach (Aug 2025) - [Training Institute Name]",
]

WORKSHOPS = [
    "Industrial Training, IND-SWIFT Limited - production, QA, GMP documentation and SOP systems.",
    "Delegate, National Pharmacovigilance Week, Sept 2024 - current PV regulatory landscape, PvPI "
    "structure and ADR monitoring centre (AMC) reporting workflow in India.",
    "Workshop on Ethics in Biomedical Research & Meta-Analysis, Lovely Professional University "
    "(Aug 2024); participant, ICP 2024 and WeCARE 2025 scientific conferences.",
]

ADDITIONAL = [
    "Notice period: [30/60/90 days or Immediate joiner]. Open to pan-India relocation "
    "(Hyderabad, Bengaluru, Chennai, Pune, Mumbai, Noida/Gurugram) and to rotational or night "
    "shifts supporting global PV operations. Languages: English (professional), Hindi (native).",
]
