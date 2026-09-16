# Outreach email — SumUp, Bank Web squad

Read [`../OUTREACH-GUIDE.md`](../OUTREACH-GUIDE.md) first. Look for the Bank Web or Banking domain engineering manager in Sofia specifically.

Attach `Yash_Prakash_Mishra_Fullstack_Engineer_React_Node.pdf`.

**Subject:** Bank Web squad — full-stack engineer who's shipped merchant flows and the back-office behind them

> Hi [Name],
>
> I've applied for the full-stack role on the Bank Web squad. The posting describes owning both the dashboard merchants use daily and the back-office tooling behind it, and that pairing is unusually close to what I've actually done.
>
> On the merchant side: at Lenskart I owned the rebuild of the core shopping flows — homepage, cart, checkout, order tracking — in React, Redux and TypeScript for the UAE market launch, as the frontend point of contact through go-live. Full flows in production, not isolated components.
>
> On the back-office side: at Novatr I built centralised RBAC spanning 5+ internal tools with role inheritance, permission scoping and audit logging, which cut access incidents by 60%. I also define the Node.js BFF contracts our web surfaces run on, so I'm used to owning the proxy layer rather than just consuming whatever the backend returns.
>
> I maintain an open-source BullMQ operations dashboard (Next.js, TypeScript, SSE) that engineering teams use to debug queue failures — a reasonable sample of how I think about tooling for the people running a system.
>
> I'd relocate to Sofia for the office-first setup. Resume attached — worth a conversation?
>
> Best,
> Yash Prakash Mishra
> +91 84007 93384 · github.com/xcalibre1

---

## LinkedIn variant

Under 300 characters, for a connection-request note:

> Hi [Name] — applied for the Bank Web full-stack role. I've owned merchant-facing flows (React/TS rebuild of cart + checkout for a market launch) and the back-office behind them (RBAC across 5+ internal tools, -60% access incidents). Would relocate to Sofia. Worth a chat?

---

## Before you send

**Settle your relocation answer first.** This is office-first in Sofia and you are in India, so it is the first thing the manager will think about. Decide whether you need visa sponsorship via the EU Blue Card route, already hold an EU permit, or would relocate at your own cost — and if you need sponsorship, say so in the email rather than letting them assume the expensive answer and quietly move on. The draft above says you would relocate but does not address sponsorship; add one clause once you know your position.

**Expect a testing question.** The posting names unit, integration, snapshot and end-to-end tests. You have Jest, Supertest and Mocha, which is backend-flavoured, and no Playwright, Cypress or React Testing Library. Do not raise it unprompted in the email, but have an honest answer ready — and ideally add Playwright coverage to the BullMQ dashboard before the interview, because then the honest answer comes with a link.

**Accessibility too.** They make it a pull-request review criterion. If you have done none, say so rather than bluffing; it is a learnable gap and bluffing it in a code review conversation ends badly.
