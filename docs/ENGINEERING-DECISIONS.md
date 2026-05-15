# Engineering Decisions (ADRs)

This document captures the architectural and engineering decisions made during CareConnect's development. Each entry follows the **Architecture Decision Record** format: context, decision, alternatives considered, consequences.

---

## ADR-001: Three Apps Instead of One Multi-Role App

**Status:** Accepted

### Context
A two-sided childcare marketplace involves at least three distinct user workflows: parents booking care, providers delivering care, and platform operators moderating quality. Trying to serve all three in one app would either bloat the UI or compromise each workflow.

### Decision
Build **three separate Flutter applications** — Mother App, Babysitter App, and Admin Panel — sharing a single Supabase backend.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Single multi-role app | Different workflows; bloated UI |
| Two apps (consumer + provider) | No clear surface for admin moderation |
| Web admin only | Loses real-time alignment with mobile UX |

### Consequences
- Each app's UX is optimized for its user
- Three apps to maintain (offset by shared backend)
- Network effects per app type (e.g., babysitter onboarding amplifies parent value)
- Cleaner role boundaries for security

---

## ADR-002: Supabase Over Firebase

**Status:** Accepted

### Context
We needed managed authentication, a relational database with strong query power, file storage, and realtime synchronization across three apps. Two clear contenders: Firebase and Supabase.

### Decision
Use **Supabase** as the unified backend.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Firebase | Strong, but pricing scales aggressively; Firestore's NoSQL doesn't fit our relational data (bookings ↔ mothers ↔ children ↔ babysitters); Firebase Rules less expressive than Postgres RLS |
| Custom backend (Node + Postgres) | Too much ops work for a graduation-scale project |
| AWS Amplify | Steeper learning curve; vendor lock-in higher |

### Consequences
- Native Postgres → relational integrity preserved
- RLS gives clean RBAC at the database layer
- Free tier sufficient for the pilot
- Future migration to self-hosted Postgres is straightforward

---

## ADR-003: Provider for State Management

**Status:** Accepted

### Context
We needed a state management approach across three apps that:
- Team members could ramp up on quickly
- Supported testable view-models
- Did not impose heavy code-generation burdens

### Decision
Use **Provider** across all three apps.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Riverpod | Stronger option but code-gen overhead in a small team |
| BLoC | More boilerplate; steeper learning curve |
| MobX | Less idiomatic for Flutter as of project start |
| `setState` only | Insufficient for cross-page state sharing |

### Consequences
- Fast onboarding for new developers
- Adequate for our state complexity
- May migrate to Riverpod if state complexity grows in V2

---

## ADR-004: Wallet / Cash + Bank Transfer Instead of In-App Payment Gateway

**Status:** Accepted (V1)

### Context
Regional payment infrastructure in Syria is constrained. Adding Stripe or PayPal would require operational and regulatory work outside the scope of a graduation-tier project.

### Decision
Support **cash and bank transfer** payments recorded manually in the booking flow; defer integrated payment gateways to V2.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Stripe/PayPal | Operationally complex in our region |
| Local payment gateways | Adoption fragmented across MENA |
| Crypto | Compliance risk; user education burden |

### Consequences
- V1 ships without payment-processing regulatory burden
- Admin Panel records all transactions for transparency
- Path open to V2 integration with regional gateways

---

## ADR-005: WhatsApp for Mother-Babysitter Communication

**Status:** Accepted

### Context
Our users live in WhatsApp. Building a custom chat module is technically possible but adds friction and replicates an experience they already have.

### Decision
**Deep-link to WhatsApp** for mother-babysitter communication after booking confirmation.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Custom in-app chat | Replicates existing user behavior; harder to launch |
| Email | Not native to our users' habits |
| SMS | Costly at scale |

### Consequences
- Zero communication-feature engineering
- Familiar UX
- Chat history lives outside our system (privacy benefit; audit-trail tradeoff)
- Future: optional in-app chat as a paid feature

---

## ADR-006: Google Maps Over Mapbox

**Status:** Accepted

### Context
Location-based babysitter search needs reliable mapping, geocoding, and navigation.

### Decision
Use **Google Maps Platform**.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Mapbox | Excellent, but coverage in MENA cities slightly weaker than Google |
| OpenStreetMap | Free, but quality and POI data inconsistent in our region |
| Apple Maps | iOS-only |

### Consequences
- High-quality maps and accurate distances
- Cost scales with usage (monitored via billing alerts)
- Server-side API key prevents client exposure

---

## ADR-007: RBAC Enforced at Database Layer (RLS)

**Status:** Accepted

### Context
A three-app system with three distinct roles is a recipe for client-side authorization bugs. Hardcoded role checks scattered across UI code lead to security holes.

### Decision
Enforce **all access control at the Supabase database layer via Row Level Security policies**. No client-side role checks for sensitive operations.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Client-side role checks | Trivially bypassed; documented anti-pattern |
| Middleware-layer enforcement | Possible, but introduces another layer of policies to maintain |
| Custom permission service | Reinventing what Supabase RLS already provides |

### Consequences
- Single source of truth for access control
- Bypassing the database is the only way to bypass authorization
- Policy changes are atomic and auditable
- All three apps benefit from the same enforcement

---

## ADR-008: IEEE 830 SRS Documentation

**Status:** Accepted

### Context
A multi-app system with four user personas, multiple integrations, and compliance requirements deserves rigorous up-front documentation.

### Decision
Document the system using the **IEEE 830 Software Requirements Specification** standard, including use cases, sequence diagrams, activity diagrams, and ERD.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Lean / agile-only docs | Would lose the multi-app coordination benefit |
| User stories only | Insufficient depth for non-functional requirements |
| Custom format | Reinventing the wheel |

### Consequences
- Easier hand-off to reviewers, supervisors, and partners
- Reusable as a template for future projects
- Up-front investment pays off in implementation alignment

---

## ADR-009: Arabic-First with Bilingual Support

**Status:** Accepted

### Context
Our target users are Arabic speakers, but English support is necessary for admin operators, international partners, and reviewers.

### Decision
Design every flow **Arabic-first with RTL**, then layer English (LTR) as a secondary localization.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| English-first | Inverts the actual user need |
| Arabic-only | Excludes English-speaking operators |
| Auto-translate via API | Quality unacceptable for childcare-related content |

### Consequences
- RTL layout is the default, not an afterthought
- All content reviewed by native speakers
- Future dialect support (Levantine, Gulf) is a clean extension

---

## ADR-010: Cross-App Realtime Sync via Supabase

**Status:** Accepted

### Context
A booking created in the Mother App must appear immediately in the Babysitter App. A task marked done in the Babysitter App must update live in the Mother App. Polling would waste battery and bandwidth.

### Decision
Use **Supabase Realtime channels** for cross-app synchronization of bookings, task lists, and reviews.

### Alternatives Considered
| Option | Why we passed |
|---|---|
| Polling | Battery drain and stale data |
| Custom WebSocket server | Reinventing Supabase Realtime |
| Push notifications only | Latency and delivery uncertainty |
| Server-Sent Events | Less mature on mobile |

### Consequences
- Sub-second updates across apps
- Battery and data-friendly
- Supabase handles connection management

---

## Open Questions / Future ADRs

The following decisions are deferred to future iterations:

- **In-app payment gateway** (V2 — Stripe / regional providers)
- **In-app chat** as an optional paid feature
- **Webhooks** for clinic integration
- **Multi-tenant isolation** for nursery-scale deployments
- **On-device tracking** for activity monitoring via smartwatch APIs
- **Background-check API** integration for babysitter verification
