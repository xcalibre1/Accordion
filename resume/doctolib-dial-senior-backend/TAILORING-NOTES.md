# Tailoring notes — Doctolib, Senior Software Engineer, DIAL / Phone Assistant (Berlin)

Source of truth for every claim here: [`../BASE-FACTS.md`](../BASE-FACTS.md).

## Read this first

This is the first of the three applications where the resume alone probably will not get you shortlisted, and you should know that going in rather than finding out through silence.

The role's core responsibility is shipping LLM-based features end-to-end — prompting, tool calling, structured outputs, guardrails, fallbacks — and owning their quality through evaluation datasets and scorers. It is listed under "who you are" as **hands-on production experience**, not as a nice-to-have. You have none, anywhere in five years of history. The second requirement, **proven experience deploying and operating services on Kubernetes** on a major cloud, is also absent: your Kubernetes exposure is "basic", and I have not inflated it.

Everything else you clear comfortably, and in some places you exceed it: 5+ years of Node.js and TypeScript, PostgreSQL data modeling and migrations, real-time systems, event-driven architecture with Kafka, distributed-systems debugging with real observability, and CI/CD with GitHub Actions. The posting does say "if you don't have the exact profile described below, but you feel this job description matches your skill set, we still encourage you to apply," which is a genuine invitation and worth taking. But a resume cannot manufacture two missing hard requirements, and I will not write claims you cannot defend in a live coding and system design loop.

So: apply, because the cost is low and the non-AI half of your profile is strong. But treat [the plan below](#the-highest-leverage-thing-you-can-do) as the real work. It converts this from a long shot into a credible application, and it compounds across every AI-adjacent role you apply to after this one — which, in 2026, is most of them.

## Files

| File | Use it for |
|---|---|
| `Yash_Prakash_Mishra_Senior_Backend_Engineer_Node_TypeScript.pdf` | The version to upload. Two pages, A4. |
| `resume.html` | Source of truth for the PDF. Edit, then run `../render-pdf.sh doctolib-dial-senior-backend`. |
| `resume.md` / `resume.txt` | Markdown and plain text equivalents. |

## What this version emphasises, and why

**Your real hook is that you delete administrative work.** This role exists to reduce "administrative burden for health professionals." Across three companies you have: manual error resolution down 80%, manual intervention down 40%, a fully manual loan-closure process replaced outright for 10,000+ loans, 10+ hours a week returned to an operations team, manual reward processing eliminated, and cohort creation 85% faster. Those numbers were scattered across your original resume as incidental percentages. Here they are collected into the first two sentences of the summary, because they are the most Doctolib-relevant thing about you and they are all verifiable. This is the framing to lead with in the recruiter screen too.

**Reliability engineering is positioned as the transferable skill it genuinely is.** The job asks for "fallback strategies" and "handling real-world failure modes" in LLM features. You built a provider-agnostic layer over four payment providers with runtime selection, circuit breakers, retry with backoff, event deduplication and idempotent paths — which is structurally the same problem as routing across LLM providers with timeouts, degradation and fallback. The resume states what you built, factually, under a group heading named "Third-party integrations, fallbacks & failure modes." I deliberately did **not** write the analogy into the resume, because asserting AI-adjacency you haven't shipped reads as padding. **Make the analogy out loud in the interview instead** — it is a strong answer to "how would you handle an LLM provider degrading mid-call," and it is the single best bridge you have from your experience to theirs.

**Real-time is pulled forward.** The Phone Assistant is a real-time voice product, and "designing for real-time performance" is in the first responsibility. Your Socket.io and Redis quiz engine with low-latency concurrent sessions and graceful degradation is your only real-time production evidence, so it gets its own group rather than sitting as a one-line afterthought.

**State machines with validation guards are framed as guardrails.** The OLX Autos bullet now spells out explicit legal states, explicit rejections and a per-change audit trail. That is the same instinct guardrails on LLM output require, and in a regulated domain it is a credibility signal for healthcare.

**OLX Autos is labelled "regulated, high-stakes workflows"** rather than FinTech. You have no healthcare experience, but lending is the closest analogue you have: auditability, compliance pressure, and a wrong state transition costing real money. That is a better bridge to healthcare than "FinTech."

**BullMQ Dashboard is reframed as production-debugging tooling** — "the tooling I wanted while debugging distributed job failures on call" — because the posting explicitly asks for debugging distributed systems in production with strong observability.

**Berlin relocation and English fluency are in the header.** Both are stated requirements (the posting asks for fluent English, and the role is Berlin hybrid with relocation support offered), and both are cheap to answer up front.

## Before you submit

1. **Delete the "Currently learning" line if it is not true.** The Additional section says you are currently learning LLM application engineering, streaming audio and voice pipelines. Stating an interest is honest and it signals direction, which matters for a team that will otherwise wonder why a payments engineer is applying to an AI voice product. But if you have not actually touched any of it, cut the line — an interviewer *will* ask what you've built, and "nothing yet" after that line is worse than never having written it.

2. **Kubernetes stays as "working knowledge."** Do not upgrade this wording. They ask for proven operation of services on K8s, so a screener may filter on it, and you will lose either way if you overclaim and then cannot answer. Better to be honestly short on one requirement than caught inflating it.

3. **Python is absent.** The role wants Node/TypeScript "with some Python." You have none on record. See the plan below for the cheapest honest fix.

4. **End-to-end testing is still missing** — same gap as the SumUp application. They ask for unit, integration *and* e2e, and you have Jest, Supertest and Mocha.

## The highest-leverage thing you can do

One focused project closes four of these gaps at once, and it builds on something you already own and that already has users.

**Add an LLM-powered failure triage feature to BullMQ Dashboard.** When jobs fail in a queue, have it classify the failure, extract the relevant fields from the payload and stack trace as a **structured output**, suggest a corrected payload, and offer a retry — with **tool calling** into the existing queue operations you already built (retry, promote, pause), **guardrails** so it can never mutate a queue without explicit confirmation, and a **fallback** to a cheaper model or a plain heuristic when the provider times out. You already have the operational surface; this is the reasoning layer on top.

Then do the part most candidates skip, which is exactly what this role is asking for: **build an evaluation set.** Collect a few dozen real failed-job examples, write scorers for classification accuracy and payload-extraction correctness, and wire it into CI so a prompt change that regresses the suite fails the build. Braintrust has a free tier and is named in the posting; promptfoo is a fine alternative. **Write the eval harness in Python** and your "some Python" gap closes in the same stroke.

Finally, **deploy it to managed Kubernetes** — EKS, GKE or AKS — with a Helm chart and a GitHub Actions pipeline, and add **Playwright** end-to-end tests against the deployed dashboard.

That one project, shipped publicly, converts the four gaps above into resume bullets you can defend under questioning: production LLM feature work with evals and guardrails, Python, Kubernetes on a major cloud, and e2e testing. It is also a far better interview story than any course or certificate, because it is operational tooling with real users solving a real problem — which is the same reason the dashboard is already worth putting on your resume. When it is done, tell me and I will fold it into `BASE-FACTS.md` and rebuild every version.

## Applying

Upload `Yash_Prakash_Mishra_Senior_Backend_Engineer_Node_TypeScript.pdf`.

Note that Doctolib asks applicants to **exclude photos and age** from applications to reduce bias. This resume has neither, so it is compliant as-is — but check anything else you attach, and do not add a photo.

The interview loop is recruiter screen, live coding, system design, behavioural, plus a reference check. Your system design round is where you are strongest: the payments provider abstraction, the webhook reconciliation pipeline and the zero-downtime migration are all genuinely senior-level design stories with real trade-offs. Prepare the provider-failover one specifically as an answer to LLM provider reliability.

If there is a cover letter or motivation field, do not spend it apologising for the AI gap. Spend it on the administrative-burden narrative: you have spent five years replacing manual back-office processes with reliable automated ones, in domains where being wrong has real consequences, and this role is that same problem pointed at healthcare. Then name the reliability parallel — that shipping LLM features in production is largely an exercise in handling a non-deterministic, occasionally unavailable dependency, which is the problem you have been solving with circuit breakers, idempotency and reconciliation for three years.
