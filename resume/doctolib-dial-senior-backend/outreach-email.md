# Outreach email — Doctolib, DIAL / Phone Assistant

Read [`../OUTREACH-GUIDE.md`](../OUTREACH-GUIDE.md) first: apply through the portal before sending this, and find the DIAL or Phone Assistant engineering manager specifically rather than any Doctolib manager.

Attach `Yash_Prakash_Mishra_Senior_Backend_Engineer_Node_TypeScript.pdf`.

---

## Version A — use this if you have started the LLM project

This is the stronger version, and the reason to start that project this week. Do not send it otherwise.

**Subject:** Senior backend engineer for Phone Assistant — five years cutting manual admin work

> Hi [Name],
>
> I've applied for the Senior Software Engineer role on the DIAL team and wanted to introduce myself directly.
>
> I've spent five years in Node.js and TypeScript removing administrative work from people's days. At OLX Autos I replaced a fully manual loan-closure process covering 10,000+ active loans in Chile; at Novatr, a webhook reconciliation pipeline cut manual error resolution by 80%. Reducing admin burden for practitioners is that same problem, pointed at healthcare.
>
> For the Phone Assistant specifically, I've built a provider-agnostic integration layer across four payment providers — runtime provider selection, circuit breakers, retry with backoff, idempotent and deduplicated event handling. Designing around a dependency that's occasionally slow, occasionally unavailable and never quite deterministic is familiar ground, and it's the part of shipping LLM features I'd be useful on immediately.
>
> Where I'm short: I haven't shipped LLM features in production yet. I'm building an eval-backed triage feature into the open-source queue dashboard I maintain — structured outputs, tool calling, guardrails, provider fallback, scorers in CI — so it's a gap I'm closing deliberately rather than talking around.
>
> I'd relocate to Berlin. Resume attached. Worth a conversation?
>
> Best,
> Yash Prakash Mishra
> +91 84007 93384 · github.com/xcalibre1

---

## Version B — use this if you have not started the LLM project

Same email with the fourth paragraph cut. It is weaker, because it leaves the manager to notice the gap on their own — but a vague claim is worse than an absent one.

**Subject:** Senior backend engineer for Phone Assistant — five years cutting manual admin work

> Hi [Name],
>
> I've applied for the Senior Software Engineer role on the DIAL team and wanted to introduce myself directly.
>
> I've spent five years in Node.js and TypeScript removing administrative work from people's days. At OLX Autos I replaced a fully manual loan-closure process covering 10,000+ active loans in Chile; at Novatr, a webhook reconciliation pipeline cut manual error resolution by 80%. Reducing admin burden for practitioners is that same problem, pointed at healthcare.
>
> For the Phone Assistant specifically, I've built a provider-agnostic integration layer across four payment providers — runtime provider selection, circuit breakers, retry with backoff, idempotent and deduplicated event handling. Designing around a dependency that's occasionally slow, occasionally unavailable and never quite deterministic is familiar ground, and I'd expect it to be the part of shipping LLM features I'm most useful on early.
>
> I'm coming to LLM application work from the reliability side rather than the research side, and I'd rather be straight about that than oversell it. I'd relocate to Berlin. Resume attached — worth a conversation?
>
> Best,
> Yash Prakash Mishra
> +91 84007 93384 · github.com/xcalibre1

---

## LinkedIn variant

For a connection-request note, which caps at 300 characters:

> Hi [Name] — applied for the Senior SWE role on DIAL. Five years in Node/TypeScript cutting manual ops work: replaced a manual loan-closure process for 10,000+ loans, cut manual error resolution 80% via webhook reconciliation. Would relocate to Berlin. Worth a chat about Phone Assistant?

For an InMail or a message after connecting, use Version A or B as-is.

---

## If they reply

The two questions you will get are *"tell me about the LLM gap"* and *"why healthcare."* Have both ready before you send.

For the first: shipping LLM features in production is largely the problem of depending on something non-deterministic and occasionally unavailable — timeouts, degradation, fallback, cost ceilings, and knowing whether a change made things better. You have been doing exactly that with payment providers for three years: circuit breakers, idempotency, reconciliation, and a provider abstraction that made switching providers a config change. What you have not done is prompt and eval design, and you should say so plainly and then say what you are doing about it.

For the second: you have no healthcare experience, so do not invent an origin story. The honest answer is stronger — lending taught you to build systems where a wrong state transition has real consequences for a real person, with explicit legal states, explicit rejections and an audit trail on every change. That instinct transfers to healthcare better than enthusiasm does.

Their loop is recruiter screen, live coding, system design, behavioural, and a reference check. System design is where you are strongest: the provider abstraction, the webhook reconciliation pipeline, and the zero-downtime migration off the legacy payments system are all senior-level stories with real trade-offs. Prepare the provider-failover one specifically as an answer about LLM provider reliability.
