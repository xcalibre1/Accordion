# ATS + Recruiter Audit of the Existing CV (Aparna Mishra)

Audited file: `Aparna_Mishra_CV.pdf` (2 pages, text-based PDF)
Target roles: Drug Safety Associate / Pharmacovigilance Associate / PV Specialist (India, 0–1 year)
Reference job descriptions used: Clarivate (Associate PV Specialist, Noida), IQVIA (Safety Associate
Trainee, Kochi), Accenture (PV Services New Associate, Bengaluru), ICON (Graduate PV Associate,
Chennai/Trivandrum), 4C Pharma (Senior DSA, Bengaluru/Mysuru/Hyderabad), plus generic Argus-based
DSA postings.

## Verdict

| Dimension | Score | Comment |
|---|---|---|
| Machine readability (will the parser read it) | 8 / 10 | Single column, real text, no tables or images. Fundamentally safe. |
| Field extraction (will fields land correctly) | 6 / 10 | No location; a page-number footer; "Expected" graduation date now stale. |
| Keyword match vs live PV job descriptions | 5.5 / 10 | Strong on MedDRA/VigiFlow/WHO-UMC; missing roughly half of the phrases these JDs actually use. |
| Recruiter/human screening in 7 seconds | 5 / 10 | No target job title, and the only paid role reads as 100% analytical chemistry with no bridge to drug safety. |

Short version: the CV is **not going to be rejected by the parser**, but it is **losing the keyword
match and the human skim**. The gap is not formatting — it is vocabulary and positioning.

## What already works (keep doing this)

- Single-column, reverse-chronological, standard headings — exactly what Workday, Taleo, iCIMS,
  Greenhouse and Naukri expect.
- Real selectable text, no graphics, icons, tables, text boxes, skill bars or photos.
- A genuine PV vocabulary base already present: MedDRA (SOC/HLT/PT), VigiFlow, WHO-UMC, Naranjo,
  GVP, ICH-E2A, ICH-E2B, RMP, signal detection, ICSR.
- Quantified project outcomes (>90% reproducibility, 4 treatment groups, p < 0.05) and a
  Springer Nature (Q1) co-authorship — genuinely differentiating for a fresher.
- Rotational shift readiness is mentioned, which is a hard requirement in most PV operations JDs.

## Issues, in priority order

### Critical — fix before the next application

1. **No location anywhere on the CV.** Location is one of the first fields an ATS extracts and one of
   the first filters a recruiter applies (PV hiring in India is concentrated in Hyderabad, Bengaluru,
   Chennai, Pune, Mumbai, Noida/Gurugram). A resume with no city is often scored as an incomplete
   profile. *Fix: city + state in the contact block, plus an explicit "open to relocation" line.*
2. **"May 2026 (Expected)" is now in the past.** Read in August 2026, this says either "she did not
   finish" or "this resume has not been touched in a year". *Fix: state the M.Pharm as completed, with
   CGPA.*
3. **No target job title on the page.** Recruiters search their ATS by title strings
   ("drug safety associate", "pharmacovigilance associate"). Nothing on the CV contains those exact
   strings as a headline. *Fix: a headline line directly under the name.*
4. **Roughly half the vocabulary of live PV JDs is missing.** Absent terms that appear repeatedly in
   the reference postings: case intake, triage, duplicate check/search, case creation, data entry,
   seriousness assessment, expectedness/listedness, follow-up, quality check (QC), CIOMS I,
   MedWatch 3500A, E2B(R3) XML, WHO-DD (drug coding), spontaneous/solicited/literature cases, SUSAR,
   special situations, PSUR/PBRER, DSUR, line listings, EudraVigilance, Veeva Vault Safety,
   NDCT Rules 2019, PvPI reporting timelines, Good Documentation Practice, ALCOA+ data integrity.
   Keyword scoring is literal — "MedDRA coding" present but "duplicate check" absent means those
   points are simply not earned. *Fix: the rewritten Core Skills block plus the PV practicum bullets.*
5. **The Dr. Reddy's role does not bridge to drug safety.** Five of six bullets are LC-MS, method
   validation and instrumentation; the sixth ("gaining cross-functional exposure … that complement
   academic research and pharmacovigilance training") is vague filler. A PV hiring manager reads this
   as "analytical chemist, wrong pipeline". *Fix: keep the work truthful but lead the bullets with the
   transferable competencies PV actually screens for — GDP/ALCOA+ documentation, SOP adherence,
   escalation of discrepant results, audit-readiness, deadline compliance, cross-functional
   coordination.*

### Important — costs shortlists

6. **Hedging words sit next to the most valuable keywords.** "Argus Safety / Aris-G / LSMV
   (Awareness)", "MedDRA (Academic)", "SAS Clinical (Conceptual)" — repeated three times across two
   sections. Honesty is right, but repeating the disclaimer next to every tool makes the whole skill
   set read as theoretical. *Fix: say it once, in controlled language ("hands-on: VigiFlow;
   foundational training: Oracle Argus Safety, ArisGlobal ARISg, Veeva Vault Safety") and let the
   practicum bullets carry the evidence.*
7. **No single block that proves PV depth.** The evidence is scattered across Core Competencies,
   Certifications and Trainings, so nothing shows *what she actually did* in PV training.
   *Fix: a dedicated "Pharmacovigilance Training & Case-Processing Exposure" section with real task
   bullets — the same section a recruiter uses to justify a fresher shortlist.*
8. **Skills are duplicated.** "Core Competencies" and "Technical & Software Skills" repeat VigiFlow,
   Argus, MedDRA, PubMed/Embase. That is a third of a page spent twice. *Fix: one consolidated,
   categorised Core Skills block.*
9. **Recruiter decision fields missing:** notice period, current location, preferred locations,
   languages. Indian PV recruiters ask all four in the first call and filter on them in Naukri.
   *Fix: a short Additional Information block.*
10. **The summary spends its best line on the wrong metric.** ">90% reproducible research with zero
    ethical violations" is a bench-research metric; the first three lines should establish target
    role, degree, PV training and regulatory knowledge. *Fix: metric moved down into the project.*
11. **Justification phrases oversell.** "directly mirroring PV adverse event documentation
    practices", "demonstrates … regulatory-standard documentation skills" (on a publication),
    "skills directly applicable to PV signal management and risk communication" (on a marketing
    project). Interviewers push back on this. *Fix: one restrained transferability statement where
    it is defensible, and drop the marketing-project claim entirely.*

### Minor — polish

12. **Page-number footer ("-- 1 of 2 --").** Many parsers drop header/footer content; some inject it
    mid-text. Nothing important is there, so just remove it.
13. **Inconsistent date formats** ("2022 – 2023" vs "Aug 2019 – May 2023"). Taleo in particular is
    sensitive to date consistency. *Fix: `Mon YYYY - Mon YYYY` throughout.*
14. **No CGPA / percentage.** Indian screeners frequently filter on academics; leaving it out invites
    the assumption it is weak.
15. **Soft-skill block at the end** ("Attention to Detail | Analytical Thinking | …") adds little on
    its own. *Fix: folded into Core Skills so the terms are still indexed without a standalone
    section.*
16. **File name.** `Aparna_Mishra_CV.pdf` carries no keywords and no role. *Fix:*
    `Aparna_Mishra_Pharmacovigilance_Resume.pdf`.
17. **Three-idea bullets.** Several bullets bundle method development + documentation + compliance.
    One idea per bullet parses better and skims better.

## What the rewrite changes, section by section

| Original | Rewritten | Why |
|---|---|---|
| Name + contacts (no city) | Name + **role headline** + city, relocation, shift line + contacts | Title-string search, location filter |
| Professional Summary (research-metric led) | Summary led by target role, PV process chain, guidelines, databases | Front-loads the terms recruiters search |
| Core Competencies + Technical & Software (overlapping) | One **Core Skills** block in 8 labelled categories | Removes duplication, adds ~30 missing JD phrases |
| Professional Experience (pure AR&D) | Same facts, re-angled to documentation, data integrity, SOP, escalation, deadlines | Builds the AR&D → PV bridge honestly |
| — | **PV Training & Case-Processing Exposure** (new) | Gives a fresher something concrete to shortlist |
| Education (Expected 2026) | Education (completed, CGPA) | Removes the stale-date red flag |
| Research & Academic Projects (3, incl. marketing) | 2 projects, tighter, marketing project dropped | Space reallocated to PV content |
| Publications / Certifications / Trainings | Kept, condensed, training institute named | Same credibility, less space |
| Professional Competencies (soft skills) | Folded into Core Skills | Section earns its space |
| — | **Additional Information** (notice period, locations, shifts, languages) | Answers the recruiter's first three questions |

## Honesty guardrail

The rewrite deliberately labels the PV section as *certification practicum and academic training,
not industry case-processing experience*, and marks Argus/ARISg/Veeva as **foundational training**
while VigiFlow stays **hands-on**. This matters twice over: PV employers do background and reference
checks, and the first interview is a technical screen that a padded resume will not survive. Every
claim in the new resume is defensible in an interview — the gain comes from using the industry's own
vocabulary for work that was genuinely done, not from inventing experience.

## Self-check before every application

1. Open the PDF, `Ctrl+A` → `Ctrl+C` → paste into Notepad. If the order is readable and nothing is
   missing, an ATS can read it. (Do this after any edit in Word.)
2. Paste the job description and the resume text into a free keyword comparison tool (Jobscan,
   ResyMatch, or simply diff the noun phrases by hand) and aim for 75%+ of the JD's hard skills.
3. Confirm the file name, the headline, the location line and the notice period are all current.
4. Confirm no `[square bracket]` placeholders remain.
