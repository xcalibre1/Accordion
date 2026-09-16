# Tailoring notes — NavVis, Full-Stack Software Engineer (Munich, hybrid)

NavVis IVION: a browser-based platform for exploring photorealistic digital twins. Stack is **Java, Spring, Hibernate, TypeScript, Angular, PostgreSQL/PostGIS**. Full visa and relocation support for international candidates.

Source of truth for every claim: [`../BASE-FACTS.md`](../BASE-FACTS.md).

## Read this first: the backend language is a real gap

Every other version in this folder was a matter of reordering facts. This one is not, and it would be dishonest to hand you a polished PDF without saying so.

The first line under "what will help you succeed" is **"Expertise in Java, Spring, Hibernate"**. You have none of the three. Five years of backend work, all of it on Node and TypeScript. No amount of wording fixes that, and this resume does not try to — there is no Java claim anywhere in it.

So treat this as a **stretch application**, not a likely shortlist. Send it anyway, because the rest of the match is genuinely good and the cost of applying is an hour. But go in knowing which question decides the screening call, and have an answer ready.

## What actually matches, and it is more than you would guess

Read the posting past that first bonus line and the overlap is substantial:

- **3+ years of experience delivering complex systems.** You have 5+, on payments, lending and multi-tenant platforms. Comfortably over the bar, which is unusually low for the scope described.
- **Frontend: TypeScript with "either Angular, React or Vue.js."** They wrote that themselves. React satisfies it outright, and the Lenskart rebuild plus the Novatr Next.js work is real production React and TypeScript.
- **PostgreSQL and scalable, data-intensive services.** Probably your strongest single match. Schema design, zero-downtime migrations, query optimization, plus a payments history migration onto ClickHouse. "Data-intensive" is exactly the ClickHouse work.
- **Delivering APIs and SDKs, and gathering developer feedback to guide improvements.** BullMQ Dashboard is the answer here and it is a good one: a developer tool with real external users whose roadmap came from their issue reports. Most candidates cannot evidence the feedback half of that requirement at all. The reusable PDF library at OLX is the internal-library version of the same thing.
- **Define technical roadmaps and drive consensus cross-functionally.** Leading 5 engineers, owning architecture decisions, being technical point of contact for 5+ enterprise clients and for the Chile operations team across a 9-hour gap.
- **Mentoring engineers of varying experience levels.** Stated almost word-for-word in the posting; the last bullet of the Novatr section answers it in their vocabulary.
- **Bonus: AWS.** Yes. **Bonus: 3D/WebGL.** Partially, via WebXR — see below. **Bonus: C++.** Listed, with a caveat.

## The two bridges this version leans on

**1. NestJS is the Spring of the Node world, and that is not a marketing line.** NestJS took its dependency-injection container, module system and decorator-based controllers directly from Angular, which in turn drew that architecture from Spring. So when you describe DI-managed providers, explicit module boundaries and decorated controllers, a Spring engineer recognises every concept — the annotations differ, the design does not. The same goes for Sequelize and Prisma against Hibernate: ORM-mapped entities, migrations, the N+1 problem, lazy versus eager loading.

That is why the first bullet of the current role is the NestJS architecture bullet rather than payments, and why it ends by naming Spring explicitly. It is the one sentence that makes a Java reviewer think "this person would be productive in our codebase in a month" instead of "wrong stack, next". **Be ready to defend it in detail** — if you cannot talk about how DI containers resolve dependencies, or what a module boundary buys you, the bullet backfires.

Bonus: this is also the honest answer to Angular. You have not written Angular, but NestJS's mental model *is* Angular's, so it is the shortest hop of any React developer's.

**2. WebXR is your only 3D credential, so it leads Lenskart.** Their whole product is 3D in a browser. WebXR sits on WebGL, and immersive try-on means interactive 3D product rendering client-side. It was one bullet near the bottom of your original resume; here it is the first thing under Lenskart, phrased to make the browser-3D connection explicit.

Paired with it, the Webpack code-splitting and time-to-interactive work is reframed as what it is for a company shipping photorealistic digital twins: **asset-heavy pages are a payload problem**, and you have shipped that optimization before. Do not oversell this. You integrated WebXR components; you did not write shaders or a renderer. If they ask about WebGL internals, say so plainly.

## Two things to check before you send

1. **"Currently learning: Java, Spring Boot, Hibernate, PostGIS."** This row exists because a Java-shop reviewer needs one reason not to reject on language alone, and it is the only honest way to give them one. **If you have not started, either start this week or delete the row.** A single Spring Boot service with Hibernate entities against PostgreSQL — a weekend, following the official guides — makes it true and gives you something concrete to say. Left on the resume untouched, it is a lie that gets found in the first five minutes of a screening call.

2. **"C++ (foundational, non-production)."** Your original resume listed C++ flat among your languages, which implies more than is true. They ask for "working knowledge... occasionally required for specific projects", so it is worth keeping, but qualified. If you genuinely cannot write and debug C++ today, drop it rather than explain it.

## Gaps

| They ask for | You have | What to do |
|---|---|---|
| **Java, Spring, Hibernate (expertise)** | Nothing | **The decisive gap.** See the project below. Do not claim it; name the transferable architecture instead. |
| Angular | React, plus NestJS (same architectural model) | The posting accepts React, so it is not a blocker. Say the NestJS/Angular lineage yourself — it reads as insight, not excuse. |
| PostGIS / geospatial data | PostgreSQL, no spatial extensions | Bonus, not required. Closeable in an evening: PostGIS is Postgres plus geometry types, spatial indexes (GiST) and functions. |
| 3D graphics / WebGL | WebXR try-on integration | Bonus, and partially met. Real but shallow — be precise about the depth. |
| C++ | Foundational only | Bonus. Qualified on the resume; drop it if you cannot use it. |
| SDKs specifically | Reusable internal libraries, an open-source tool with external users | Close enough to claim honestly, and the developer-feedback half is genuinely strong. |
| Absolute scale figures | Percentages and thousands | Same as every other application. Talk about patterns, not numbers. |

## The project that would change this application

One focused build closes **four** of the gaps above at once, and it maps onto their product almost suspiciously well:

> A **Spring Boot** service with **Hibernate** entities over **PostgreSQL + PostGIS**, exposing a REST API that serves geospatial features — points of interest on a floor plan, say — consumed by a small **Angular** client that renders them on a map.

That single repository converts Java, Spring, Hibernate, PostGIS and Angular from absent to demonstrable, and it lets you open a cover letter with "I built this against your stack because I wanted to understand your problem" rather than asking them to trust a transfer argument. Add basic WebGL rendering and you have touched their bonus list too.

You already know how to design the service layer, model the data and define the API. What you would be learning is syntax and framework idiom, which is the easy part and exactly what your Node experience makes fast. This is the highest-leverage item on your list right now — and unlike the LLM project recommended in the Doctolib notes, it is a weekend rather than a month.

If you ship it, add it to `BASE-FACTS.md`, put it in the Selected Projects section here, and re-send. That version is a plausible shortlist; this one is a long shot.

## Applying

Upload `Yash_Prakash_Mishra_Fullstack_Engineer_TypeScript_PostgreSQL.pdf`.

Three things about this posting worth using:

- **They offer full visa and relocation support for international candidates**, stated outright. That removes the question mark that hangs over the Berlin applications, and the resume header says you are open to relocating to Munich so nobody has to guess.
- **The process is a screening call plus up to four interview rounds.** The screening call is where the Java question lands. Decide your answer before you apply, and make it specific: which concepts transfer, what you have already built in Spring, how long you think ramping would take.
- **Your recruiting partner is named in the posting — Johnny.** Use the name in your application and in any follow-up; see [`outreach-email.md`](outreach-email.md).
