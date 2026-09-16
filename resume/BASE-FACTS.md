# Base facts — the single source of truth for every tailored resume

Every claim in every tailored version must trace back to something in this file. Tailoring means **reordering, regrouping, reframing and trimming** these facts to match a job description — never inventing new ones. If a job description asks for something that is not here, it goes in [Known gaps](#known-gaps) instead, and the tailored version's notes tell Yash to fill it in himself.

Keep this file updated as the career progresses; the per-company folders are derived artifacts.

## Identity

- **Name:** Yash Prakash Mishra
- **Contact:** +91 84007 93384 · mishra.yash3443@gmail.com
- **Links:** linkedin.com/in/yash-prakash-mishra-34063016a · github.com/xcalibre1
- **Location:** India (IST). Fully remote for 5 years.
- **Experience:** **5.1 years of employment** as of September 2026 — Lenskart 12 months, OLX Autos 12 months, Novatr 37 months and counting. First role April 2021, so the span is 5.4 years with a three-month gap between OLX Autos and Novatr. Write this as "5+ years"; recompute it whenever a version is refreshed, since several roles list a 5-year minimum and an out-of-date figure can fail a filter. (The original resume said "4.10 years", which was correct in early 2026 and is now stale.)
- **Education:** B.Tech Computer Science, Rajkiya Engineering College, Sonbhadra — Jul 2016 to Jun 2020

## Novatr — Aug 2023 to present

Backend Developer, promoted to Senior Software Engineer. Remote. Y Combinator-backed EdTech SaaS for professional upskilling; product runs 24/7 on AWS. Led a team of 5 engineers.

**Stack:** Node.js, TypeScript, NestJS, Express.js, Next.js, React.js, PostgreSQL, ClickHouse, Redis, Apache Kafka, BullMQ, Socket.io, Passport.js, opossum, axios-retry, AWS (EC2, S3, SQS, KMS, IAM), Docker

### Payments
- Gateway-agnostic payments platform integrating 4 providers (Razorpay, Stripe, Affirm, Jodo). Strategy and Factory patterns for runtime gateway selection; new gateways onboard without touching core logic. Owned the integration POC for each provider.
- Idempotent transaction handling throughout.
- Centralised webhook handler for all 4 gateways: self-healing retry logic, event deduplication, status reconciliation over Kafka. **Cut manual error resolution by 80%.**
- Circuit breaker (opossum) and retry (axios-retry) for failover across gateways.
- Referral and rewards platform: PAN verification, fraud prevention, audit trails, Xoxoday programmatic payouts. **+25% referral conversions**, eliminated all manual reward processing.

### Platform and architecture
- B2C-to-B2B transition: multi-tenant system (NestJS, PostgreSQL) with tenant-level data isolation, configuration management, enterprise onboarding workflows. **Onboarded 5+ enterprise clients** as technical point of contact.
- Centralised RBAC spanning **5+ internal tools**: role inheritance, permission scoping, audit logging. **Reduced access incidents by 60%.**
- Multi-layer JWT authentication service (Passport.js): token issuance, rotation, validation across **Admin, LMS and BFF surfaces**.
- CMS backend (NestJS, PostgreSQL) with content lifecycle workflows and versioning. **Reduced cohort creation time by 85%**, eliminated recurring on-call incidents.

### Web surfaces
- Launched a **freemium LMS platform** (Node.js, Next.js, React.js, TypeScript) as a lead-generation funnel, driving new user acquisition and conversion across enterprise client cohorts.
- Real-time quiz engine (Node.js, Socket.io, Redis) for live cohort sessions: low-latency concurrent interactions, graceful degradation under load.

### Data and events
- Kafka-based event pipelines (with BullMQ) for payments, user lifecycle events and transactional email; decoupled services, improved fault tolerance.
- **Zero-downtime migration** of payments data off a legacy system onto a ClickHouse-backed unified platform. Node.js ETL with schema validation, integrity checks, rollback strategy.

### Ways of working
- Led a team of 5: architecture decisions, code reviews, delivery timelines on core product infrastructure.
- Worked directly with enterprise clients, translating business requirements into technical architecture.

## OLX Autos — May 2022 to May 2023

Software Engineer. Remote. Used-car financing infrastructure for Latin America — FinTech lending.

**Stack:** Node.js, TypeScript, Express.js, PostgreSQL, MySQL, Sequelize, REST APIs, PDFKit, Handlebars, Docker, AWS

- Foreclosure and manual repayment flows in the **Loan Management System**, automating loan closure and repayment tracking for **10,000+ active loans in Chile**; replaced a fully manual process. Technical point of contact for the Chile operations team (9+ hour time-zone gap from IST).
- **Loan lifecycle state machine APIs** with validation guards at each transition. **Cut manual intervention by 40%.**
- Risk analysis and scoring workflows in the **Loan Origination System**. **Reduced credit approval time by 30%**, improved decision auditability.
- Reusable PDF generation library (PDFKit, Handlebars) for programmatic invoices in loan disbursement workflows. Cut invoice errors, **saved 10+ hours weekly**.

## Lenskart — Apr 2021 to Apr 2022

Software Engineer (Frontend). India's largest eyewear retailer. Exit reason: project concluded on successful UAE market launch.

**Stack:** React.js, Redux, TypeScript, JavaScript (ES6+), Next.js, HTML5, CSS3, Webpack, WebXR, REST APIs, Node.js (BFF)

- Owned and led the **complete rebuild of core shopping flows** — homepage, cart, checkout, order tracking — in React.js, Redux and TypeScript for the UAE market. **30% faster launch**, improved Lighthouse scores. Primary frontend point of contact for the UAE client go-live.
- Route-based code splitting, tree shaking and bundle analysis (Webpack): reduced initial JS payload, improved time-to-interactive across all key pages.
- Integrated **WebXR** immersive try-on components and Google reCAPTCHA: improved engagement, reduced fraudulent checkout attempts.
- Worked against a Node.js BFF layer.

## BullMQ Dashboard — open-source project, 2025

github.com/xcalibre1/bullmq-dashboard

**Stack:** Next.js (App Router), TypeScript, Node.js, Redis, ioredis, BullMQ, Express.js, Docker, CSS, SVG, Server-Sent Events

- **Problem it solves:** tools like Bull Board give visibility into queues but no operational control — no retrigger with an edited payload, no bulk retry, no real-time updates.
- Next.js + TypeScript dashboard with Server-Sent Events for live queue stats, an editable JSON payload editor, and a 24-hour throughput chart in pure SVG.
- Next.js App Router API routes with a Redis singleton via ioredis and a BullMQ `Queue` instance cache for near-zero per-request overhead.
- Docker + docker-compose for one-command self-hosting.
- Adopted by engineering teams globally. Features payload field search, bulk retry, promote, pause, resume.

## Skills inventory

Grouped so a tailored version can pull the relevant rows and drop the rest.

- **Languages:** TypeScript, JavaScript (ES6+), SQL, C++
- **Runtime and backend:** Node.js, Express.js, NestJS, Fastify, BullMQ, opossum, axios-retry, Passport.js
- **Frontend:** React.js, Next.js (App Router), Redux, Webpack, WebXR, HTML5, CSS3, SVG
- **Databases:** PostgreSQL, MySQL, MongoDB, ClickHouse, Redis, Sequelize, Prisma
- **Messaging and events:** Apache Kafka, BullMQ, AWS SQS, event-driven architecture, webhooks, Server-Sent Events, Socket.io
- **Auth and security:** JWT, Passport.js, RBAC, OAuth2, token lifecycle management
- **Architecture:** microservices, distributed systems, saga pattern, idempotent API design, RESTful API design, multi-tenant architecture, HLD/LLD, design patterns (Strategy, Factory, Singleton, Observer), BFF pattern
- **Cloud and DevOps:** AWS (EC2, S3, CloudFront, SQS, IAM, KMS), Docker, Kubernetes (basic), CI/CD, Jenkins, GitHub Actions, Apache Airflow
- **Observability:** ELK Stack, distributed tracing, structured logging
- **Testing and tools:** Jest, Supertest, Mocha, integration testing, Postman, Swagger, Git, Jira, Confluence, Retool
- **Interests:** distributed systems, payments infrastructure, developer tooling, open source, full-stack Node.js

## Known gaps

Things job descriptions keep asking for that the facts above do not support. Not to be written into any resume until Yash confirms them — and if he does, they belong in this file first.

| Gap | Asked for by | Status |
|---|---|---|
| **Production LLM feature work** — prompting, tool calling, structured outputs, guardrails, fallbacks | Doctolib (**required, hands-on**) | **Absent.** Nothing in five years touches LLMs. The single biggest blocker for AI-adjacent roles. |
| **Evaluation frameworks for AI features** — eval datasets, scorers, regression tracking (Braintrust, promptfoo) | Doctolib (**required**) | **Absent.** |
| **Kubernetes in production** on a major cloud | Doctolib (**required**) | **Weak.** "Basic"/"working knowledge" only; never operated a service on it. |
| Python | Doctolib (required, "some"), Deel (a second language would satisfy) | **Absent.** |
| Speech pipelines (ASR, TTS, streaming audio), voice agents | Doctolib (bonus) | **Absent.** |
| Telephony and real-time comms (SIP, RTP, WebRTC) | Doctolib (bonus, explicitly teachable) | **Absent** — and explicitly not required, so low priority. |
| A second server-side language actually used in production (Python, Go, Java, Kotlin, Ruby) | Deel (required), SumUp (valued) | **Unconfirmed.** C++ is listed as a language but no experience bullet uses it. |
| **Java, Spring, Hibernate** | NavVis (**required, "expertise"**) | **Absent.** All five years of backend work are Node/TypeScript. NestJS transfers the architecture (DI, modules, decorators) and Sequelize/Prisma transfer the ORM concepts, but nothing transfers the language. Decisive blocker for any JVM shop. |
| Angular | NavVis (accepts React or Vue instead), SumUp (plus) | **Absent but not blocking** where React is accepted. NestJS is modelled on Angular's architecture, so it is the shortest hop available. |
| PostGIS / geospatial data | NavVis (required for the data layer; geospatial listed as bonus) | **Absent.** PostgreSQL is strong; spatial types, GiST indexes and spatial functions are not. Cheap to close. |
| 3D graphics / WebGL | NavVis (bonus) | **Partial.** WebXR try-on integration at Lenskart is real and browser-side, but it is component integration, not renderer or shader work. State the depth precisely. |
| SDKs (as distinct from APIs) | NavVis (required, with developer feedback loops) | **Effectively covered.** Reusable PDF library at OLX plus BullMQ Dashboard, whose roadmap came from user issue reports. The feedback half is genuinely strong evidence. |
| Kotlin / Go familiarity | SumUp (plus) | **Unconfirmed.** |
| End-to-end testing (Cypress, Playwright) | SumUp (explicit), Doctolib (explicit) | **Unconfirmed.** Only Jest/Supertest/Mocha are evidenced. Asked for by every role so far. |
| Snapshot testing, React Testing Library | SumUp (explicit) | **Weak.** Jest is evidenced; React-specific test tooling is not. |
| Accessibility (WCAG, ARIA, screen readers) | SumUp (PR review criterion) | **Unconfirmed.** No a11y work in any bullet. |
| Serverless on AWS (Lambda, API Gateway, Step Functions, EventBridge) | Deel (plus) | **Unconfirmed.** Only EC2, S3, SQS, KMS, IAM, CloudFront. |
| Hard transaction volume / throughput figure for the payments platform | Deel, SumUp | **Missing.** Only percentage improvements exist, no absolute volume. |
| A specific PostgreSQL query-optimization win (index, rewrite, partitioning, with before/after latency) | Deel (explicit) | **Missing.** Claimed as a skill, never demonstrated in a bullet. |
| Multi-currency / FX / tax / regulatory compliance work | Deel, SumUp | **Unconfirmed.** The Chile lending work is a plausible source. |
| AI tooling in the engineering workflow (Cursor, Copilot, Claude) | SumUp (plus), Almedia (**expected** — "we actively encourage AI-assisted development") | **Effectively confirmed** for Cursor. Claimed as a skills row in the Almedia version; trim the specific tools to whatever is actually true. |
| GraphQL | Almedia (in their stack) | **Absent.** REST and BFF contract design are the nearest transferable thing. |
| gRPC | Almedia (in their stack) | **Absent.** |
| RabbitMQ, Google Pub/Sub | Almedia (in their stack) | **Not a real gap.** Kafka, BullMQ and SQS cover the concepts; name the difference rather than hiding it. |
| BigQuery | Almedia (in their stack) | **Not a real gap.** ClickHouse is the same class of columnar analytical store, and there is a migration onto it to talk about. |
| Datadog | Almedia (in their stack) | **Not a real gap.** ELK, structured logging and distributed tracing are the same concepts. |
| A/B testing and feature-flagging platforms | Almedia ("what you'll do") | **Absent.** Per-tenant configuration and RBAC are the nearest shape; no experimentation platform integrated. |
| Absolute scale figures (users, requests/sec, transaction volume) | Almedia (80M+ users), Deel, SumUp | **Missing.** Every metric is a percentage or in the thousands. Not fixable by wording — talk about patterns instead. |
| Modern state management beyond Redux (React Query, Zustand, Context patterns) | SumUp | **Unconfirmed.** |
| Depth on Kubernetes | Listed as "basic" originally | **Weak.** Softened to "working knowledge"; drop it if he cannot discuss it. |

## The one project that closes most of the gaps

Several gaps above recur across every application, and one focused project would close four of them at once — see [`doctolib-dial-senior-backend/TAILORING-NOTES.md`](doctolib-dial-senior-backend/TAILORING-NOTES.md) for the full version.

In short: add **LLM-powered failure triage to BullMQ Dashboard** (structured outputs, tool calling into the existing queue operations, guardrails requiring confirmation before mutating a queue, fallback when the provider times out), back it with a real **evaluation set and scorers wired into CI**, write that **eval harness in Python**, deploy it to **managed Kubernetes** with a Helm chart and GitHub Actions, and add **Playwright** end-to-end tests.

That converts production LLM work, eval frameworks, Python, Kubernetes and e2e testing from absent to defensible — on a repository that already has real users. Update this file when it ships and rebuild every version.

There is a second, much smaller project with a similar payoff for JVM shops, described in [`navvis-fullstack-engineer/TAILORING-NOTES.md`](navvis-fullstack-engineer/TAILORING-NOTES.md): a **Spring Boot service with Hibernate entities over PostgreSQL + PostGIS**, serving geospatial features to a small **Angular** client. That is a weekend rather than a month, and it closes Java, Spring, Hibernate, PostGIS and Angular in one repository — five rows of the table above, four of which are also the second-language gap that Deel and SumUp ask about.

## Tailoring checklist

For each new job description:

1. Read the job description for its **top three signals** — the things a screener is actually filtering on. Put them in the title, the first sentence of the summary, and the first skills rows.
2. Decide whether the role is **backend-led, frontend-led or full-stack**, and order the Lenskart and Novatr web work accordingly. This is the single biggest lever, because the same history reads very differently depending on what leads.
3. Pull the matching facts from this file. **Reorder and regroup; do not invent.** Reuse the job description's own vocabulary only where a fact already supports it.
4. Put unmatched requirements in the version's `TAILORING-NOTES.md` under gaps, and add anything new to the table above.
5. Keep it to two pages. Trim the least relevant facts rather than shrinking the type.
6. Run `./render-pdf.sh <version-dir>` and check the page count and the page-break positions.
