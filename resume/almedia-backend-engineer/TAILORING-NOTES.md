# Tailoring notes — Almedia, Backend Engineer (Berlin)

Job posting: [jobs.ashbyhq.com/almedia/d01f25b1-5e12-4f0d-9356-e60b33187ce7](https://jobs.ashbyhq.com/almedia/d01f25b1-5e12-4f0d-9356-e60b33187ce7). €80K–140K plus equity, Berlin, **on-site** (not hybrid). AdTech: they pay a community of 80M+ users for engaging with advertisers' products.

Source of truth for every claim: [`../BASE-FACTS.md`](../BASE-FACTS.md).

## This is the best stack match of the four

Worth saying plainly, because the last one was the opposite. Their stack is TypeScript, Node.js, **NestJS** and **Jest** — you have all four in production, and NestJS specifically is not something most candidates have. Add MySQL, MongoDB, Redis, WebSockets, Docker, microservices and REST, and you already work in most of what they run. What they ask for under "what you'll bring" is hands-on Node.js in production, strong web development, an understanding of scalable systems, production experience with most of their stack, an ownership mindset, and English. You clear all six without stretching anything.

They also say they "actively encourage AI-assisted development" and name Claude, Cursor and Copilot. This is the first posting in the set where the AI-tooling item is both asked for and true, so it has its own skills row rather than being buried.

## The rewards platform is the lead, and that is the main insight here

Almedia's entire business is paying 80M users for engaging with advertisers. Which means their hardest backend problem is almost certainly **payout fraud**: people gaming an incentive system for something with cash value, at scale.

You built exactly that. The referral and rewards platform at Novatr does identity verification, fraud prevention, audit trails and automatic payouts through Xoxoday. In your original resume it was a single bullet, three-quarters of the way down, under a heading about referrals. Here it opens your current role, and the second bullet spells out *why* it was hard: anything handing out cash value gets gamed, so every reward carries a trail of who earned it, why, and what was checked.

If you take one thing into the interview from these notes, it is that. A backend engineer who has already shipped fraud-screened automated payouts is unusually well matched to an incentivised-engagement company, and nobody will spot it from the old resume.

## The human touch, and what it cost

You asked for this one to read like a person wrote it. What changed:

- **First person, and actual sentences.** "I build backend services in Node.js and TypeScript, mostly with NestJS" instead of "Backend engineer with 5+ years of expertise in...". The other three versions open with a keyword-dense paragraph; this one opens with a voice.
- **Bold used about ten times, not a hundred.** Only the numbers are emphasised. Heavy bolding is the single clearest tell of a resume written by a tool, and stripping it out changes how the page feels more than any wording does.
- **Plain verbs.** Built, wrote, moved, set up, rebuilt — not architected, leveraged, spearheaded, drove.
- **Headings in sentence case**: "About me", "What I work with", "Other things". The all-caps tracked headings in the other versions read corporate.
- **Specifics that only a person would write.** A webhook handler "that stopped paging people at 3am". A rollback path "I actually tested". A dashboard built because "debugging jobs blind annoyed me", used by teams worldwide, "which still surprises me". The CMS bullet now starts with the problem — cohort setup was slow and broke often — instead of the solution.
- **A closing line about what you want**, which is normal in Berlin startup applications and would be out of place at Deel.

The cost: it is less keyword-dense than the other versions, and it names Almedia in the second paragraph. **Do not reuse this file for another company** without editing that line. If Almedia turns out to screen through a strict keyword filter, the SumUp or Doctolib version is the safer shape — but for a bootstrapped startup on Ashby, a human is reading this, and a resume that sounds like a human is an advantage.

## Check these two things before you send

1. **"Per-tenant configuration deciding which features each client got."** I wrote it that way because the posting asks about feature flagging, and multi-tenant config usually does gate features. If your tenant configuration was really only branding and settings rather than turning features on and off, reword it — it is the one line here that leans on an assumption about your system rather than a stated fact.

2. **The AI tooling row.** You do use Cursor, or these resumes would not exist. But the row says Claude and Copilot too, and it says "daily". Trim it to whatever is actually true; they will ask how you use it, and "I run Cursor with Claude for implementation and review" is a better answer than a list.

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
