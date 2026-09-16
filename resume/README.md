# Resume workspace

Tailored resume versions for Yash Prakash Mishra, one directory per target role.

## Versions

| Directory | Role | Positioning | Upload this |
|---|---|---|---|
| `deel-backend-engineer/` | Deel — Backend Engineer (Node.js) | Backend-led. Payments and FinTech first, frontend condensed. | `Yash_Prakash_Mishra_Backend_Engineer_Node.pdf` |
| `sumup-bank-web-fullstack/` | SumUp — Bank Web squad (full-stack, Sofia) | Frontend-core full-stack. React/TypeScript first, back-office tooling and API contracts surfaced. | `Yash_Prakash_Mishra_Fullstack_Engineer_React_Node.pdf` |
| `doctolib-dial-senior-backend/` | Doctolib — Senior SWE, DIAL / Phone Assistant (Berlin) | Backend-led, reliability and real-time first, with the administrative-burden-reduction track record as the hook. **Two hard requirements are unmet — read that version's notes.** | `Yash_Prakash_Mishra_Senior_Backend_Engineer_Node_TypeScript.pdf` |

Each directory contains `resume.html` (the source), `resume.md`, `resume.txt`, the rendered PDF, `TAILORING-NOTES.md` explaining what was emphasised for that job description and which of its requirements the experience does not yet cover, and `outreach-email.md` with a ready-to-send draft for the hiring manager.

## Shared pieces

- **[`OUTREACH-GUIDE.md`](OUTREACH-GUIDE.md)** — how to find the right hiring manager, when to send, how to follow up, and what makes the per-company drafts work.
- **[`BASE-FACTS.md`](BASE-FACTS.md)** — the single source of truth. Every accomplishment, metric and skill, plus a table of known gaps that job descriptions keep asking for and the facts do not support. Tailoring reorders and reframes these facts; it never invents new ones. **Update this file when anything changes in the actual career** — the per-company versions are derived from it.
- **`shared/resume.css`** — one print stylesheet for every version, so they stay visually consistent. Density knobs (`--body-size`, `--body-leading`) are CSS variables a version can override inline if its content needs a different fit.
- **`render-pdf.sh`** — renders HTML to A4 PDF via headless Chrome.

## Rendering

```bash
./render-pdf.sh                          # every version
./render-pdf.sh sumup-bank-web-fullstack # one version
```

Requires Chrome or Chromium on `PATH`, or `CHROME_BIN` set. If `pdfinfo` is installed (`apt install poppler-utils`) the script also prints the page count, which is the thing to check after editing — two pages is the target.

To eyeball page breaks: `pdftoppm -png -r 70 <dir>/*.pdf /tmp/page`.

## Adding a version for a new job description

1. Read the job description and decide whether the role is backend-led, frontend-led or full-stack. That single decision drives most of the rewrite, since the same history reads very differently depending on which work leads.
2. Copy the closest existing version's directory, then rewrite the title, summary and skills order against the new job description, pulling facts from `BASE-FACTS.md`.
3. Add a `pdf_name_for` case in `render-pdf.sh` so the output filename reads well to a recruiter.
4. Write `TAILORING-NOTES.md`: what was emphasised and why, and — more importantly — which requirements are not evidenced, so they can be confirmed or addressed rather than quietly faked. Add an `outreach-email.md` alongside it.
5. Add any newly requested-but-missing requirement to the gaps table in `BASE-FACTS.md`.
6. Render, check the page count, and check where the pages break.

The full checklist lives at the bottom of `BASE-FACTS.md`.
