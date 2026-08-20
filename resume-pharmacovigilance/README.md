# Pharmacovigilance Resume Package — Aparna Mishra

An ATS-optimised resume rebuilt for pharmacovigilance / drug safety roles in India, plus the audit
that explains every change and the supporting job-search material.

## Files

| File | What it is |
|---|---|
| `Aparna_Mishra_Pharmacovigilance_Resume.pdf` | **Primary resume.** 2 pages, text-based PDF, single column. Use for email applications and portals that accept PDF. |
| `Aparna_Mishra_Pharmacovigilance_Resume.docx` | Word version, identical content. Use for Naukri uploads and any portal that asks for `.docx` (Taleo-era systems parse Word best). |
| `Aparna_Mishra_Pharmacovigilance_Resume.txt` | Plain text. Paste into "copy your resume here" boxes and use for keyword checks. |
| `ATS_AUDIT.md` | Audit of the original CV: what passed, what failed, severity, and the fix applied. |
| `KEYWORD_MAP.md` | The job-description keyword checklist, coverage before/after, where each term now sits, and how to tailor per posting. |
| `JOB_SEARCH_PLAYBOOK.md` | Internal-transfer strategy, target companies, Naukri/LinkedIn setup, skill gaps to close, interview question bank, 30-day plan. |
| `COVER_LETTER.md` | Cover letter, application email, internal-transfer note, LinkedIn and referral templates. |
| `resume_content.py` | All resume text in one place — **edit here**, not in the .docx. |
| `build_resume.py` | Regenerates the .docx, .pdf and .txt from `resume_content.py`. |

## Fill these in before sending anything

Every one of these appears as `[bracketed text]` in the documents. The build script prints the list
of remaining placeholders each time it runs.

| Placeholder | What to put |
|---|---|
| `[City, State]` and `[City]` | Current city (contact line and the Dr. Reddy's location line). Location is a primary ATS filter — do not leave it blank. |
| `[Training Institute Name]` | The institute that issued the Clinical Research & Pharmacovigilance and other certifications. A named institute is far more credible than an unnamed certificate. |
| `[N]` | Number of simulated/mock ICSRs processed during certification training. Use the real number; if it was not tracked, replace the phrase with "processing simulated ICSRs" and drop the count. |
| `[X.XX/10]` and `[X.XX]` | M.Pharm CGPA and B.Pharm percentage/CGPA. |
| `[30/60/90 days or Immediate joiner]` | Actual notice period. Keep it accurate and update it as it changes. |

Also verify two facts:

1. **M.Pharm specialisation.** The resume says *Pharmacology*, matching the original CV. If the degree
   is officially awarded in **Pharmacovigilance** (or Pharmacology with a pharmacovigilance
   specialisation printed on the marksheet), change it in `EDUCATION` — an exact "M.Pharm
   Pharmacovigilance" string is a significant keyword and credibility gain.
2. **Current job title at Dr. Reddy's.** The resume uses "Research & Development Apprentice —
   Analytical Research & Development (AR&D)". Use the exact title on the appointment letter (e.g.
   "Trainee — Analytical R&D", "Apprentice Chemist"). ATS systems and background checks compare this.

## How to edit and rebuild

```bash
pip install python-docx reportlab
python3 build_resume.py
```

Edit `resume_content.py` and rerun — the three output files stay in sync and the ATS-safe formatting
rules stay enforced. Editing the `.docx` directly in Word is fine too, but then the `.pdf`/`.txt`
will drift, so prefer editing the Python file when making substantive changes.

If Word is used to re-export a PDF, keep it as "Save as PDF" (text) — never "print to image" or a
scan.

## What changed versus the original CV, in one paragraph

The original CV was already formatted safely for parsers, so the rebuild is about vocabulary and
positioning, not layout. It adds a role headline and a location line (both are hard ATS filters),
replaces the stale "Expected May 2026" education line, consolidates two overlapping skills blocks
into one categorised Core Skills section, and raises job-description keyword coverage from 30 of 111
tracked terms to all 111 — adding the phrases live postings actually use (case intake, triage,
duplicate check, seriousness and expectedness assessment, quality check, CIOMS I, MedWatch 3500A,
E2B(R3), WHO-DD, PSUR/PBRER/DSUR, EudraVigilance, Veeva Vault Safety, NDCT Rules 2019, PvPI
timelines). The Dr. Reddy's role keeps every factual detail but leads with the competencies drug
safety screens for — Good Documentation Practice, ALCOA+ data integrity, SOP adherence, escalation of
discrepant results, deadline compliance — which is what turns "analytical chemist" into "credible PV
candidate". A new "Pharmacovigilance Training & Case-Processing Exposure" section gives a recruiter
something concrete to shortlist, and an Additional Information block answers the notice period,
location and shift questions that otherwise cost a first phone call.

## Important: nothing here overstates experience

The PV section is explicitly labelled as certification practicum and academic training, not industry
case-processing experience. VigiFlow is marked hands-on; Argus Safety, ARISg and Veeva Vault Safety
are marked foundational training. Every claim is defensible in a technical interview and in a
background check — which matters, because PV employers run both. The shortlist gain comes from using
the industry's own vocabulary for work that was genuinely done.

The fastest way to strengthen the resume further is listed in `JOB_SEARCH_PLAYBOOK.md`, section 5:
a hands-on Oracle Argus Safety course converts the single most-requested keyword in every job
description from "foundational" to "trained, hands-on".
