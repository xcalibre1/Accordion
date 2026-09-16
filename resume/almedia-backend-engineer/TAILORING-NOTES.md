# Tailoring notes — Almedia, Backend Engineer (Berlin)

Job posting: [jobs.ashbyhq.com/almedia/d01f25b1-5e12-4f0d-9356-e60b33187ce7](https://jobs.ashbyhq.com/almedia/d01f25b1-5e12-4f0d-9356-e60b33187ce7). €80K–140K plus equity, Berlin, **on-site** (not hybrid). AdTech: they pay a community of 80M+ users for engaging with advertisers' products.

Source of truth for every claim: [`../BASE-FACTS.md`](../BASE-FACTS.md).

## This is the best stack match of the four

Worth saying plainly, because the last one was the opposite. Their stack is TypeScript, Node.js, **NestJS** and **Jest** — you have all four in production, and NestJS specifically is not something most candidates have. Add MySQL, MongoDB, Redis, WebSockets, Docker, microservices and REST, and you already work in most of what they run. What they ask for under "what you'll bring" is hands-on Node.js in production, strong web development, an understanding of scalable systems, production experience with most of their stack, an ownership mindset, and English. You clear all six without stretching anything.

They also say they "actively encourage AI-assisted development" and name Claude, Cursor and Copilot. This is the first posting in the set where the AI-tooling item is both asked for and true, so it has its own skills row rather than being buried.

## The rewards platform is the lead, and that is the main insight here

Almedia's entire business is paying 80M users for engaging with advertisers. Which means their hardest backend problem is almost certainly **payout fraud**: people gaming an incentive system for something with cash value, at scale.

You built exactly that. The referral and rewards platform at Novatr does identity verification, fraud prevention, audit trails and automated payouts through Xoxoday. In your original resume it was a single bullet, three-quarters of the way down, under a heading about referrals. Here it opens your current role, and the second bullet spells out *why* it was hard: anything distributing items of cash value is an active target for abuse, so every reward carries a record of who earned it, on what basis, and which checks passed before payout.

If you take one thing into the interview from these notes, it is that. A backend engineer who has already shipped fraud-screened automated payouts is unusually well matched to an incentivised-engagement company, and nobody will spot it from the old resume.

## Voice

Same professional register as the Deel, SumUp and Doctolib versions: third person, standard section headings, key terms and numbers in bold. An earlier draft of this version was written in a chatty first-person voice with sentence-case headings and asides like "which still surprises me"; it was worse, and it is gone.

**No company name appears anywhere in the resume.** The earlier draft named Almedia in the summary, which was a mistake — a resume should read as a description of you, not as a letter to one employer. Company-specific framing belongs in the outreach email and the interview, which is where it now lives.

Tailoring here is done through ordering and selection instead: the rewards and fraud work leads, the skills rows are sequenced to match their stack, and AI-assisted development gets its own row. All of that is invisible to anyone reading it cold, which is the point.

## Check these two things before you send

1. **"Per-tenant configuration governing feature availability."** Phrased that way because the posting asks about feature flagging, and multi-tenant config usually does gate features. If your tenant configuration was really only branding and settings rather than turning features on and off, reword it — it is the one line here that leans on an assumption about your system rather than a stated fact.

2. **The AI-Assisted Development row.** You do use Cursor, or these resumes would not exist. But the row also claims Claude and Copilot. Trim it to whatever is actually true; they will ask how you use it, and a specific answer beats a list of three tools.

## Gaps

Smaller than any previous application, and none of them are stated requirements.

| Their stack | You | What to do |
|---|---|---|
| GraphQL | Not used | Genuine gap. REST and BFF contract design transfer, but say so honestly. |
| gRPC | Not used | Same. Worth an afternoon of reading before an interview. |
| RabbitMQ, Google Pub/Sub | Kafka, BullMQ, SQS | Not a real gap. Say "Kafka and BullMQ, so brokers and pub/sub are familiar, though not those two specifically." Nobody sensible will care. |
| BigQuery | ClickHouse | Also fine. Both are columnar analytical stores and you migrated a payments history onto one. Make that comparison yourself. |
| Datadog | ELK, distributed tracing | Same concepts, different vendor. |
| GitLab CI | GitHub Actions, Jenkins | Same. |
| Kubernetes | "Working knowledge" | Listed in their stack, and DevOps/SRE background is a "what makes you a great fit" bonus rather than a requirement. Still the weakest item, and still not inflated. |
| A/B testing and feature flagging | Nothing direct | Listed under "what you'll do", so expect it as a question. Honest answer: you have built per-tenant configuration and RBAC, so the shape is familiar, but you have not integrated an experimentation platform. |
| Scale in absolute numbers | Percentages only | 80M users is much bigger than anything on your resume. You cannot fix this with wording, so do not try. Talk about the patterns instead: Kafka pipelines, idempotency, deduplication, circuit breakers. |

The Kubernetes and GraphQL gaps are the two worth actually closing, and the LLM project already recommended in the Doctolib notes would cover Kubernetes as a side effect.

## Applying

Upload `Yash_Prakash_Mishra_Backend_Engineer_Node_NestJS.pdf`. Ashby forms are usually short, so the resume carries most of the weight.

Two things about this company that should shape your framing. They are **bootstrapped and profitable from day one**, and the posting says they want to become "Germany's second bootstrapped unicorn" while describing itself as not a regular job where people "push harder". That is a speed-and-ownership culture, and your best evidence for it is leading five engineers at a YC-backed startup while owning payments, rewards, RBAC and a migration. Say that you ship fast and own things end to end, because they asked for exactly that, and you can back it.

Second, **equity is only offered to Berlin-based employees** and the role is on-site in central Berlin. Relocation is not optional here and there is no remote fallback, so settle your visa position before applying — an EU Blue Card at that salary band is realistic, but you should know whether you are asking them to sponsor it. The resume says you are happy to relocate; make the sponsorship question explicit in the application or the email rather than leaving them to guess.
