# Tailoring notes — Deel, Backend Engineer (Node.js)

## Files

| File | Use it for |
|---|---|
| `yash-mishra-deel-backend-engineer.pdf` | The version to upload. Two pages, A4, selectable text. |
| `yash-mishra-deel-backend-engineer.html` | The source of truth for the PDF. Edit this, then re-run `./render-pdf.sh`. |
| `yash-mishra-deel-backend-engineer.md` | Same content in Markdown, for quick editing or pasting elsewhere. |
| `yash-mishra-deel-backend-engineer.txt` | Plain text, for application forms that ask you to paste a resume or that parse uploads badly. |
| `render-pdf.sh` | Regenerates the PDF from the HTML using headless Chrome. |

## What changed from the original resume, and why

**Positioning.** The old title was "Senior Software Engineer" with no specialism, and the summary opened with "scalable Node.js full-stack applications." Deel is hiring a backend engineer for payroll and payments. The new title is "Senior Software Engineer — Backend (Node.js · TypeScript · PostgreSQL)" and the summary opens on money-moving systems, idempotency, and the payments platform. A recruiter screening for this role sees a match in the first line.

**Frontend is de-emphasised, not hidden.** Lenskart went from six lines of React detail to two, and the second bullet reframes it around the Node.js BFF work and explains the move into backend — which turns a "why is there a frontend year here?" question into a deliberate narrative. React/Next/Redux stay in a "Frontend (secondary)" skills row, which is useful since the job description explicitly mentions collaborating with frontend engineers.

**Bullets now use the job description's own vocabulary** where your real work already supports it: idempotency, concurrency, high transaction volumes, input validation, queue-based systems, JWT, multi-tenant architecture, design patterns, query optimization, data migrations, data modeling. Nothing was invented — every claim traces back to something already on your resume. For example, "validation guards at each transition" became "input validation guards at every transition," and the idempotency work that was buried in a sub-clause became its own bullet.

**Payments come first inside the Novatr role**, grouped under "Payments & money movement," "Scalability, data & reliability," and "Platform & API engineering." The old resume mixed a freemium LMS launch and a CMS in among the payment work. The freemium LMS bullet was cut as the least relevant item for this role.

**FinTech is now explicit.** OLX Autos is labelled "Used-car financing infrastructure for Latin America (FinTech)" so the domain match is visible without the reader inferring it from "loan management system."

**Remote and async collaboration are evidenced, not asserted.** Deel is a 7,000-person distributed company and the job description calls out async collaboration twice. Rather than claiming to be a good remote worker, the resume points at the Chile operations team across a 9+ hour gap, the UAE go-live, and 5 years fully remote.

**Skills are reordered backend-first** and grouped to mirror the job description's own headings (databases, scalability, high-volume performance, API development, auth). Recruiters and keyword filters both scan this block.

**Length.** Two pages, tightened to remove whitespace. At 5+ years, two full pages is right; three pages with a half-empty last page reads as padding.

## Gaps worth closing before you submit

These are the places where the job description asks for something your resume does not currently evidence. Only add them if they are true — fabricating any of it will surface in the interview.

1. **"Experience in at least one other server-side language."** Your resume lists C++, but nothing in your experience section shows server-side work in it. If you have used Python, Go, Java, or Ruby in any professional or serious side capacity, add it to the Languages row and ideally attach it to one bullet. This is a stated requirement, so a screener may filter on it.
2. **Serverless on AWS (bonus).** You list EC2, S3, SQS, KMS, IAM — no Lambda, API Gateway, Step Functions, or EventBridge. If you have touched any of them, add them to the Cloud row; this is called out as a "brownie points" item.
3. **A hard volume number for the payments platform.** You have a percentage for error reduction but no transaction volume, throughput, or value processed. "Processed N transactions/month" or "₹X crore in annual volume" would directly answer the "high-volume performance" requirement. Add it if you can defend the figure.
4. **A concrete PostgreSQL query optimization win.** The job description asks for a "SQL guru, particularly with PostgreSQL, handling query optimization." The resume claims it in the skills row but never demonstrates it in a bullet. If you have one — an index or query rewrite that took a p95 from X to Y, or a partitioning decision — it is worth a bullet, probably in the Novatr "Scalability, data & reliability" group.
5. **Kubernetes.** I softened "Kubernetes (basic)" to "(working knowledge)". If you cannot hold a five-minute conversation about it, delete it rather than risk the credibility hit.
6. **Multi-currency or compliance exposure.** Deel pays workers in ~100 currencies across 150+ countries. Anything you have done with currency handling, FX, tax, or regulatory constraints (the Chile lending work is a plausible source) is unusually relevant and currently invisible.

## Applying

Upload the PDF and keep the filename descriptive — `Yash_Prakash_Mishra_Backend_Engineer_Node.pdf` reads better to a human reviewer than the repo filename. The PDF has real selectable text and a single-column flow, so applicant tracking systems will parse it; the skills block does use a two-column layout, so if a form's preview mangles it, paste the `.txt` version instead.

The job description mentions automated screening tools. That is a reason to keep the wording plain and the keywords honest and in context — which the rewrite does — not a reason to stuff a keyword block at the bottom. Keyword lists divorced from experience are exactly what both human and automated screens penalise.

Finally, the posting says input is valued from discovery through deployment and emphasises business-focused development. If there is a cover letter or "why Deel" field, the strongest thing you have is the gateway-agnostic payments platform: a design decision made so the business could onboard new payment providers without engineering rework. That is the same problem Deel solves at a much larger scale, and it is a better answer than restating the resume.
