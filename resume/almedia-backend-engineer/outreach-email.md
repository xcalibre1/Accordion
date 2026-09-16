# Outreach email — Almedia, Backend Engineer

Read [`../OUTREACH-GUIDE.md`](../OUTREACH-GUIDE.md) first. Apply through the Ashby form before sending this.

Almedia is small enough that the engineering lead or a founder may well read it themselves, so this one is worth sending. Attach `Yash_Prakash_Mishra_Backend_Engineer_Node_NestJS.pdf`.

**Subject:** Backend engineer — built fraud-screened automated payouts, would like to do it at your scale

> Hi [Name],
>
> I've applied for the Backend Engineer role. One thing from my background lines up with Almedia closely enough that it seemed worth a direct note.
>
> I built the referral and rewards platform at Novatr: identity verification, fraud prevention, audit trails, and automatic payouts through Xoxoday, with nobody approving a reward by hand. The payouts were the easy part. The hard part was that anything handing out something with cash value gets gamed, so every reward had to carry a record of who earned it, why, and what was checked before it went out. Referral conversions went up 25%.
>
> Rewarding 80 million people for engaging with advertisers sounds like that problem with several more zeros on it.
>
> The rest is a fair match too: five years of Node.js and TypeScript, most of it NestJS, with Jest, MySQL, MongoDB, Redis, WebSockets and Docker. I've also built a payments platform across four providers behind one runtime-selected interface, which is mostly a lesson in what happens when a third party times out mid-request.
>
> I'd relocate to Berlin for the on-site setup. Resume attached — worth a conversation?
>
> Best,
> Yash Prakash Mishra
> +91 84007 93384 · github.com/xcalibre1

---

## LinkedIn variant

Under 300 characters, for a connection-request note:

> Hi [Name] — applied for the Backend Engineer role. I built a rewards platform with identity checks, fraud screening and automatic payouts (+25% referral conversions). Paying 80M users for engaging with ads looks like that with more zeros. 5 yrs Node/NestJS/TS. Would relocate to Berlin.

---

## Notes on this draft

**The third paragraph is the whole email.** One line, standing alone, drawing the parallel between what you built and what they do. Everything else is supporting detail. If you trim this email, trim around that sentence and keep it where it is.

**"The payouts were the easy part" is doing real work.** It signals you understand which half of the problem is hard, which is the difference between someone who integrated a payout API and someone who has thought about incentive fraud. That distinction is probably the most valuable thing you have to offer this particular company.

**Say something about speed if you get a reply.** The posting is unusually direct about culture: not a regular job, push harder, aiming to be Germany's second bootstrapped unicorn. Leading five engineers at a YC-backed startup while owning payments, rewards, RBAC and a zero-downtime migration is the honest answer, and it is a good one.

**Settle the visa question before you send.** The role is on-site in central Berlin with no remote option, and equity is explicitly for Berlin-based employees, so relocation is the deal rather than a detail. At €80–140K an EU Blue Card is realistic, but know whether you are asking them to sponsor one and say so plainly. Leaving it vague invites the cheapest assumption.

**Expect a question about scale.** They serve 80M+ users and your numbers are percentages and thousands. Do not talk around it. The useful answer is that the patterns are the same at any size — idempotency, deduplication, pub/sub decoupling, circuit breakers — and that you would like to work somewhere the numbers force you to get them right.
