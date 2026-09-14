# Outreach email — Deel, Backend Engineer (Node.js)

Read [`../OUTREACH-GUIDE.md`](../OUTREACH-GUIDE.md) first.

Attach `Yash_Prakash_Mishra_Backend_Engineer_Node.pdf`.

A note on expectations: Deel hires at very high volume through a structured process, and the posting says outright that it uses automated decision tools with human oversight. Cold outreach is less likely to change the outcome here than at Doctolib or SumUp, where the teams are named and smaller. Still worth one message to the right engineering manager in the payments or payroll org — just send it *after* applying through the portal, and put your effort into the application itself.

**Subject:** Backend engineer (Node/TS) — built a gateway-agnostic payments platform across four providers

> Hi [Name],
>
> I've applied for the Backend Engineer role and wanted to flag one thing from my background that lines up closely with what Deel does.
>
> At Novatr I architected a gateway-agnostic payments platform in Node.js and TypeScript across four providers — Stripe, Razorpay, Affirm and Jodo — using Strategy and Factory patterns for runtime gateway selection, so onboarding a new provider doesn't touch core logic. Every path is idempotent, so retries, duplicate webhooks and client re-submissions are safe under concurrent load, and a centralised webhook handler with event deduplication and Kafka-based reconciliation cut manual error resolution by 80%. Circuit breakers keep checkout alive when a provider degrades.
>
> Before that I built loan servicing at OLX Autos: foreclosure and repayment flows for 10,000+ active loans in Chile, replacing a fully manual process, with state machine APIs guarded at every transition.
>
> Deel moves money in ~100 currencies across 150+ countries, so provider abstraction, idempotency and reconciliation are presumably daily concerns rather than edge cases. That's the work I want to be doing.
>
> Resume attached. Happy to talk whenever suits.
>
> Best,
> Yash Prakash Mishra
> +91 84007 93384 · github.com/xcalibre1

---

## LinkedIn variant

Under 300 characters:

> Hi [Name] — applied for the Backend Engineer role. I built a gateway-agnostic payments platform in Node/TS across 4 providers (Stripe, Razorpay, Affirm, Jodo): runtime gateway selection, idempotent paths, webhook dedup + Kafka reconciliation, -80% manual error resolution. Worth a chat?

---

## Before you send

**The role requires a second server-side language**, and you only have C++ listed with no production use. If you have used Python, Go, Java or Ruby anywhere real, get it onto the resume before you send this. If not, expect the question and answer it straight.

**Two numbers would strengthen this email considerably**, and you may already have them: the transaction volume or value the payments platform handles, and one concrete PostgreSQL optimisation with a before-and-after latency. The posting asks for high-volume performance and calls for a "SQL guru" on query optimisation, and right now your evidence for both is percentage improvements rather than absolute scale. If you can defend real figures, add them to the resume and swap one into the second paragraph here.
