# Tailoring notes — SumUp, Bank Web squad (full-stack, Sofia)

Source of truth for every claim here: [`../BASE-FACTS.md`](../BASE-FACTS.md). Nothing in this version is invented.

## Files

| File | Use it for |
|---|---|
| `Yash_Prakash_Mishra_Fullstack_Engineer_React_Node.pdf` | The version to upload. Two pages, A4, selectable text. |
| `resume.html` | Source of truth for the PDF. Edit this, then run `../render-pdf.sh sumup-bank-web-fullstack`. |
| `resume.md` | Same content in Markdown. |
| `resume.txt` | Plain text, for forms that ask you to paste a resume. |

## How this differs from the Deel version, and why

The Deel role was backend-only. This one is **frontend-core full-stack**: "React and TypeScript are core to this role," with genuine full-stack capability as the second requirement. Same facts, almost inverted emphasis.

**Title and summary flipped to lead with React.** Deel's version opened on "money-moving systems"; this one opens on "React and TypeScript on the front, Node.js and PostgreSQL behind them," then immediately names the Lenskart rebuild. A screener for this role is checking for React depth in the first two lines.

**Lenskart is restored to four full bullets** and moved to the front of the reader's attention via the summary. On the Deel version it was cut to two and treated as a stepping stone. Here it is the single strongest piece of evidence for "delivering production-ready features end-to-end, not just isolated UI components" — you owned an entire market launch's shopping flows, not a component library.

**Novatr now leads with "Web surfaces & full-stack ownership"** rather than payments. The freemium Next.js platform, the BFF contract ownership, the JWT service across three surfaces, and the Socket.io real-time engine were scattered or buried in the original resume; they are now the first thing read under your current role. The BFF bullet is deliberately phrased around *defining* contracts, because the job description distinguishes "defining API contracts, working with backend proxies, and owning integrations" from merely consuming them — a BFF layer is exactly a backend proxy, so name it as one in interviews.

**A dedicated "Back-office & internal tooling" group.** The squad explicitly owns "the back-office tooling that powers the support teams." Your RBAC across 5+ internal tools, the CMS with content lifecycle workflows, and the multi-tenant admin surfaces are direct hits, and they were previously spread across unrelated sections. This group may be the most underrated part of your fit.

**Payments reframed as integrations and modernisation.** The job description asks for contributions to "architectural improvements, component refactoring, and stack migrations that reduce technical debt." Your ClickHouse migration is literally a stack migration off a legacy system, so it is now framed that way instead of as a data-migration achievement. The payment gateway work is framed around *owning* integrations end-to-end.

**Production support and code review are made explicit.** The job description lists PR review and incident participation as actual responsibilities. "Pull-request review" now appears in both the skills block and the team bullet, and the observability row names circuit breakers, self-healing retries and on-call incident reduction — all of which you already had, none of which was previously visible as operational ownership.

**Banking-domain curiosity is evidenced, not claimed.** The posting says banking products "have intricate user flows and edge cases, and you enjoy digging into them." Rather than asserting curiosity, the OLX Autos state-machine bullet now says what makes those flows hard: a wrong state transition costs real money.

**Relocation is addressed up front.** This is an office-first role in Sofia and you are in India, which is the most likely reason a recruiter discards the application without reading further. The header says you are open to relocating, and the Additional section addresses the remote-to-office transition directly instead of leaving it as an unanswered question.

## Gaps worth closing before you submit

Ordered by how likely each one is to cost you the application.

1. **Work authorisation for Bulgaria.** This is the real gate, and no resume wording solves it. Decide your answer before applying: are you seeking visa sponsorship (Bulgaria has an EU Blue Card route), do you already hold an EU permit, or would you relocate at your own cost? If SumUp sponsors, say so plainly in the cover letter or application question. If you leave it ambiguous, a recruiter will assume the expensive answer.

2. **End-to-end and React-specific testing.** The posting names "unit, integration, snapshot, and end-to-end" tests explicitly. You have Jest, Supertest and Mocha — solid, but backend-flavoured, with no React Testing Library, no snapshot testing, and no Cypress or Playwright. I did not add any of them. This is the clearest technical gap for a frontend-core role, and it is also the most fixable: adding Playwright or RTL coverage to the BullMQ Dashboard would give you a public, demonstrable answer within one focused push, and it would let you add the tooling to `BASE-FACTS.md` honestly.

3. **Recency of production React.** Your titles since 2022 read backend. A sharp interviewer will ask when you last wrote React in production. Your honest answer is the Novatr freemium Next.js platform and the 2025 BullMQ Dashboard on the App Router — both are on the resume for exactly this reason. Be ready to talk about modern React specifically: hooks, Server Components, streaming, and why you chose the App Router. If your Novatr React work is more substantial than one platform launch, tell me and I will expand that bullet.

4. **Accessibility.** The posting makes accessibility a PR-review criterion, and you have no a11y work anywhere in your history, so I claimed none. If you have done any — semantic markup, ARIA, keyboard navigation, screen-reader testing, contrast audits — it is worth a clause in the Lenskart bullets. If not, expect it as an interview question and do not bluff it.

5. **A second backend language.** Node is valued here, which you have, so this is softer than it was for Deel. But the broader ecosystem is Kotlin, Java, Go and Angular, and "familiarity with most of them is a plus." You have none of the four. If you have touched any, add it. Otherwise lean on the multi-stack point you *can* make honestly: you already work across TypeScript, Node, PostgreSQL, ClickHouse, Kafka and Redis, which is the transferable part.

6. **Modern state management.** Redux is what your resume shows, and Redux in 2021 is a different thing from the current ecosystem. If you have used React Query, SWR, Zustand or modern Context patterns, add them to the State & Real-time row.

7. **AI tooling.** Listed as a plus. If you use Cursor, Copilot or similar in your actual workflow, that is a cheap, honest addition — and given this repository, it is presumably true.

## Applying

Upload `Yash_Prakash_Mishra_Fullstack_Engineer_React_Node.pdf`. The filename already reads correctly to a human reviewer.

If there is a cover letter or "why this role" field, the strongest thing you have for *this specific squad* is not the payments platform — it is the combination of owning a market launch's entire shopping flow at Lenskart and building back-office tooling that support teams operate. That is the Bank Web squad's exact remit: a merchant-facing dashboard plus the internal tooling behind it. Lead with that pairing, and mention BullMQ Dashboard as evidence you build operational tooling unprompted, because that is an unusual thing for a candidate to have shipped publicly.
