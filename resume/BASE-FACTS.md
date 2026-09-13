# Base facts — the single source of truth for every tailored resume

Every claim in every tailored version must trace back to something in this file. Tailoring means **reordering, regrouping, reframing and trimming** these facts to match a job description — never inventing new ones. If a job description asks for something that is not here, it goes in [Known gaps](#known-gaps) instead, and the tailored version's notes tell Yash to fill it in himself.

Keep this file updated as the career progresses; the per-company folders are derived artifacts.

## Identity

- **Name:** Yash Prakash Mishra
- **Contact:** +91 84007 93384 · mishra.yash3443@gmail.com
- **Links:** linkedin.com/in/yash-prakash-mishra-34063016a · github.com/xcalibre1
- **Location:** India (IST). Fully remote for 4+ years.
- **Experience:** 4.9 years (first role April 2021)
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
| A second server-side language actually used in production (Python, Go, Java, Kotlin, Ruby) | Deel (required), SumUp (valued) | **Unconfirmed.** C++ is listed as a language but no experience bullet uses it. |
| Kotlin / Java / Go / Angular familiarity | SumUp (plus) | **Unconfirmed.** |
| End-to-end frontend testing (Cypress, Playwright) | SumUp (explicit) | **Unconfirmed.** Only Jest/Supertest/Mocha are evidenced. |
| Snapshot testing, React Testing Library | SumUp (explicit) | **Weak.** Jest is evidenced; React-specific test tooling is not. |
| Accessibility (WCAG, ARIA, screen readers) | SumUp (PR review criterion) | **Unconfirmed.** No a11y work in any bullet. |
| Serverless on AWS (Lambda, API Gateway, Step Functions, EventBridge) | Deel (plus) | **Unconfirmed.** Only EC2, S3, SQS, KMS, IAM, CloudFront. |
| Hard transaction volume / throughput figure for the payments platform | Deel, SumUp | **Missing.** Only percentage improvements exist, no absolute volume. |
| A specific PostgreSQL query-optimization win (index, rewrite, partitioning, with before/after latency) | Deel (explicit) | **Missing.** Claimed as a skill, never demonstrated in a bullet. |
| Multi-currency / FX / tax / regulatory compliance work | Deel, SumUp | **Unconfirmed.** The Chile lending work is a plausible source. |
| AI tooling in the engineering workflow (Cursor, Copilot) | SumUp (plus) | **Unconfirmed**, though likely true. |
| Modern state management beyond Redux (React Query, Zustand, Context patterns) | SumUp | **Unconfirmed.** |
| Depth on Kubernetes | Listed as "basic" originally | **Weak.** Softened to "working knowledge"; drop it if he cannot discuss it. |

## Tailoring checklist

For each new job description:

1. Read the job description for its **top three signals** — the things a screener is actually filtering on. Put them in the title, the first sentence of the summary, and the first skills rows.
2. Decide whether the role is **backend-led, frontend-led or full-stack**, and order the Lenskart and Novatr web work accordingly. This is the single biggest lever, because the same history reads very differently depending on what leads.
3. Pull the matching facts from this file. **Reorder and regroup; do not invent.** Reuse the job description's own vocabulary only where a fact already supports it.
4. Put unmatched requirements in the version's `TAILORING-NOTES.md` under gaps, and add anything new to the table above.
5. Keep it to two pages. Trim the least relevant facts rather than shrinking the type.
6. Run `./render-pdf.sh <version-dir>` and check the page count and the page-break positions.
