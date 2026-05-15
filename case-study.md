# CareConnect — Case Study

## Context

Childcare in Damascus and the broader Arab world runs on informal networks. Family, neighbors, Facebook groups, and Instagram DMs are the entire infrastructure. The result is a market with deep trust problems, no professional path for skilled babysitters, and a documented tax on working mothers' careers.

CareConnect was developed to address this directly: as a three-tier marketplace, anchored in verified credentials, transparent reviews, and an admin moderation layer.

The work was developed by **Mozn Jamous** (solo on the Mother App, Admin Panel, shared backend, design system, and SRS documentation) and **Shahab ([@shaha123s](https://github.com/shaha123s))** (co-developer on the Babysitter App). The project was documented to IEEE 830 standards.

## The Challenge

Build a system that:

1. **Earns trust on both sides.** Mothers need to trust babysitters. Babysitters need to trust the platform. Operators need tools to maintain quality.
2. **Models three workflows cleanly.** Parent booking, provider operations, and admin moderation are fundamentally different.
3. **Coordinates real-time across three apps.** A booking confirmed in the Mother App must appear instantly in the Babysitter App; a task marked done must update live in the Mother App.
4. **Respects regional payment constraints.** No in-app payment gateway is feasible in our market for V1.
5. **Works in Arabic with cultural awareness.** RTL, dialect-friendly UI, family-structure respect.
6. **Generates a clean audit trail** for any incident.

## The Approach

### Three apps, one backend

Instead of building a single multi-role app, we chose **three separate Flutter apps** sharing one Supabase backend. Each app's UX is tuned for its persona; the data is unified.

### Database-layer RBAC

We learned from prior projects that client-side role checks are a security anti-pattern. So we enforced **all authorization at the Supabase database layer via Row Level Security (RLS) policies**. No client-side `if (user.role === 'admin')` checks. The database is the single source of truth.

### Stakeholder-driven personas

Before writing a single line of code, we interviewed and surveyed four target personas: working mothers, non-working mothers, babysitters, and mobile families. The findings shaped every feature priority. For example: the WhatsApp integration was a direct response to "we already chat with our nanny on WhatsApp — please don't make us learn another tool."

### IEEE 830 SRS

Multi-app coordination is unforgiving of vague requirements. We documented the system using the IEEE 830 Software Requirements Specification standard. The result was a ~30-page document including use case diagrams, sequence diagrams, activity diagrams, ERD, and architecture decisions. This investment paid back during implementation: dozens of edge cases were caught at the document stage rather than as bugs.

### WhatsApp instead of custom chat

We considered building in-app messaging. We rejected it: our users already live in WhatsApp. Building a competing chat experience would have been months of work for a feature people don't need. We use **WhatsApp deep links** for direct mother-babysitter communication after booking confirmation.

### Cash + bank transfer in V1

Regional payment infrastructure made in-app gateways infeasible. We supported **cash and bank transfer** with admin-recorded transaction logs. This avoided regulatory complexity and is the most familiar payment method for our users anyway.

### Three apps coordinated via Supabase Realtime

Polling would have drained batteries and felt sluggish. Custom WebSockets would have reinvented the wheel. We used **Supabase Realtime channels** for live booking status updates and task list synchronization. Sub-second updates across all three apps.

## Trade-offs

| Decision | Trade-off |
|---|---|
| Three apps vs. one multi-role app | More dev effort; vastly better UX per persona |
| Provider state management | Lower ceiling than Riverpod/BLoC; sufficient for our complexity |
| Supabase over Firebase | Free tier more generous; Postgres familiar; RLS cleaner |
| WhatsApp over custom chat | Saves months of dev; chat history lives outside our system (privacy benefit; audit-trail tradeoff) |
| Cash + bank transfer in V1 | No regulatory burden; no in-app payment UX |
| FlutterFlow scaffolding (early prototypes) | Fast V0; refactor debt for V2 |

## Outcome

- **Functional three-app MVP** by V1 freeze date (Feb 2025)
- **Complete IEEE 830 SRS document** (~30 pages) submitted with the system
- **Full Figma design system** for all three apps
- **15+ database tables** with RLS policies for three roles
- **Co-developed Babysitter App** with @shaha123s — cross-app integration tested
- **Stakeholder validation** through interviews and surveys with all four personas
- **V1 archived in Feb 2025** pending business decision on revival

## What We Learned

- **Stakeholder interviews are non-negotiable.** They saved us from over-building entire feature sets.
- **Database-layer RBAC is the only RBAC that survives contact with reality.** Client-side checks always rot.
- **WhatsApp wins over custom chat.** Always. Especially in MENA.
- **Three-app coordination needs ritual.** Daily syncs with @shaha123s were essential.
- **IEEE 830 is worth the up-front cost.** The discipline catches edge cases at the document layer rather than at the bug layer.
- **Cash-and-bank-transfer payments are a feature, not a limitation.** They avoid regulatory complexity that would have killed the project.
- **FlutterFlow accelerates v1, blocks v3.** The same pattern we've seen on other projects.

## What's Next

- **Revival decision** — pivot, scale, or sunset
- **If revived:** manual Flutter refactor; native payment gateway; background-check API
- **First-city pilot** in Damascus with 30 babysitters and 100 families
- **Grant applications** targeting women's economic empowerment funders
- **Adjacent verticals** — elder care, tutoring (same two-sided pattern)

---

*The Mother App, Admin Panel, shared backend, design system, and SRS were developed solely by Mozn Jamous. The Babysitter App was co-developed with [@shaha123s](https://github.com/shaha123s).*
