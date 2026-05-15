<div align="center">

# 👶 CareConnect

### A three-tier childcare ecosystem — Flutter

*Connecting parents, babysitters, and administrators through a unified platform with rigorous SRS-driven architecture.*

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![Status: Archived](https://img.shields.io/badge/Status-Archived-lightgrey.svg)]()
[![Platform: Flutter](https://img.shields.io/badge/Platform-Flutter-02569B?logo=flutter&logoColor=white)]()
[![Backend: Supabase](https://img.shields.io/badge/Backend-Supabase-3ECF8E?logo=supabase&logoColor=white)]()
[![Database: PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-336791?logo=postgresql&logoColor=white)]()
[![Apps: 3](https://img.shields.io/badge/Apps-Mother%20%2B%20Babysitter%20%2B%20Admin-blueviolet.svg)]()
[![Standard: IEEE 830](https://img.shields.io/badge/Standard-IEEE%20830%20SRS-orange.svg)]()

</div>

---

> [!NOTE]
> **This is a showcase repository.** The source code for all three apps is private. This repository documents a three-tier childcare ecosystem built with comprehensive software-requirements engineering. For inquiries, please contact me directly.

---

## 📖 The Problem

Childcare is one of the most stressful daily problems for modern families — and the current solutions are deeply fragmented:

- **For parents**, especially working mothers, finding trustworthy and qualified childcare on demand is a constant logistical and emotional burden. Existing options live on Facebook groups, Instagram DMs, and word-of-mouth referrals.
- **For babysitters**, there is no professional platform that respects their schedule, builds their reputation, and helps them earn a real, recurring income.
- **For platform operators**, there is no clean way to moderate quality, manage payment records, and curate educational content for the children being cared for.

Our research, conducted via interviews and surveys with four target personas — working mothers, non-working mothers, babysitters, and mobile families — revealed a need for an integrated, three-sided solution.

---

## ✨ The Solution

**CareConnect** is an integrated three-app ecosystem built on a unified Supabase backend:

```
┌────────────────────────────────────────────────────────┐
│                    CareConnect Platform               │
├──────────────────┬──────────────────┬─────────────────┤
│   Mother App     │  Babysitter App  │  Admin Panel    │
│   (Parents)      │  (Providers)     │  (Platform)     │
└──────────────────┴──────────────────┴─────────────────┘
              ↓                ↓               ↓
       ┌─────────────────────────────────────────┐
       │     Supabase (PostgreSQL + Auth + RT)   │
       └─────────────────────────────────────────┘
              ↓                ↓               ↓
   ┌──────────────────┐  ┌──────────────┐  ┌─────────────┐
   │  Google Maps API │  │ WhatsApp API │  │ Digital Lib │
   └──────────────────┘  └──────────────┘  └─────────────┘
```

Each app is tuned to its persona's workflow but shares the same data layer, ensuring real-time consistency across the platform.

---

## 🏗️ Three Apps, One Ecosystem

### 👩‍👧 1. Mother App — for Parents

The primary consumer-facing app. Features include:

- **Account & child management** — register multiple children with detailed profiles (weight, height, allergies, medical info)
- **Babysitter discovery & booking** — search by location, time, and qualifications using Google Maps integration
- **Task list creation** — assign specific activities for the babysitter to complete during the session (coloring, reading, tidy-up)
- **Vaccination tracking** — age-based vaccine schedule with automatic reminders
- **Sleep tracking** — log sleep patterns with quality assessment (excellent / good / poor) based on age
- **Meal tracking** — record meals with stage-appropriate nutritional guidance
- **Medical appointment management** — schedule and view appointment history
- **Rating & reviews** — post-session feedback for babysitters
- **Digital library access** — curated educational content for children
- **WhatsApp integration** — direct communication with booked babysitter

### 👩‍🍼 2. Babysitter App — for Providers
*Co-developed with [@shaha123s](https://github.com/shaha123s)*

The provider-side counterpart with workflow tuned for babysitter operations:

- **Account management** — profile, certifications, qualifications, hourly rate
- **Booking inbox** — view, accept, or reject incoming booking requests
- **Task list execution** — view the mother's pre-assigned tasks and mark each as "done" or "not done" in real time
- **Schedule management** — upcoming and past bookings
- **Reviews & feedback** — view mother feedback to improve service quality

### 🛡 3. System Admin Panel — for Operators

The platform-control app for administrators:

- **User management** — review, edit, activate, or deactivate mother and babysitter accounts
- **Payment records review** — full transparency over all booking-related transactions
- **Comment moderation** — review and remove inappropriate reviews to maintain platform safety
- **Digital library content management** — upload, categorize, and curate educational materials available to parents

---

## 🎯 Four Target Personas

Our requirements engineering was driven by deep research with four user personas:

| Persona | Primary Needs | Our Solution |
|---|---|---|
| **Working mothers** | Reliable, on-demand childcare; peace of mind during work hours | Verified babysitter pool, real-time updates, task lists |
| **Non-working mothers** | Time for self-care; structured educational activities for children | Digital library, sleep/meal tracking, occasional booking |
| **Babysitters** | Predictable income; reputation building; safe communication | Booking inbox, ratings, WhatsApp integration, schedule management |
| **Mobile families** | Continuity of care across locations | Location-aware search, portable health/activity records |

---

## 🧰 Tech Stack

### Mobile (Frontend)
| Concern | Choice | Why |
|---|---|---|
| Framework | **Flutter** | Cross-platform, mature Arabic typography |
| Language | **Dart** | Null-safety, async-friendly |
| State Management | **Provider** | Lightweight, reactive, well-documented |
| Design | **Material Design + Custom** | Industry-standard UX patterns |
| Responsive UI | **LayoutBuilder** | Phone + tablet adaptive layouts |
| Design Tool | **Figma** | Component library + interactive prototype |

### Backend & Data
| Layer | Choice | Why |
|---|---|---|
| Backend-as-a-Service | **Supabase** | Free tier, PostgreSQL-native, realtime support |
| Database | **PostgreSQL** | Relational integrity, stored procedures, full-text search |
| Auth | **Supabase Auth + OAuth** | Social sign-in (Google, Facebook) ready |
| Storage | **Supabase Storage** | Child photos, certifications, ID documents |
| Realtime sync | **Supabase Realtime** | Live booking status updates across apps |

### External Integrations
| Service | Purpose |
|---|---|
| **Google Maps API** | Babysitter discovery by location, distance, navigation |
| **WhatsApp API** | Direct mother-babysitter communication |
| **Babysitter App API** (internal) | Cross-app booking and task synchronization |
| **Digital Library API** | Educational content delivery |

### Security & Compliance
- **OAuth 2.0** for delegated authentication
- **AES encryption** for sensitive data at rest
- **RBAC (Role-Based Access Control)** — three distinct roles (Mother / Babysitter / Admin)
- **HTTPS + TLS** for all API traffic
- **GDPR & CCPA** compliance design

---

## 🎨 Design

Full design system, screen flows, and interactive prototype:

🔗 **[CareConnect Figma — full design & prototype](https://www.figma.com/design/8nNCv2zMnDqGnqq0y9z0i0/Care-connect?t=lLHVpV4sLyX1ayFT-0)**

Includes:
- Color tokens and typography for all three apps
- Component library
- Screen-by-screen flows for parent journey, babysitter journey, and admin journey
- Interactive transitions

---

## 📊 Project Scale

| Metric | Value |
|---|---|
| Apps in the ecosystem | **3** (Mother + Babysitter + Admin) |
| User personas | **4** (verified via interviews + surveys) |
| Distinct user roles | 3 (RBAC-enforced) |
| External integrations | 4 (Maps, WhatsApp, Babysitter API, Digital Library) |
| Documentation standard | **IEEE 830 SRS** |
| Bilingual | Arabic (RTL) + English |
| Compliance frameworks | GDPR, CCPA |

---

## 🚀 Demo

> Demo assets coming as the platform is revived.

- 🎨 **Figma prototype:** [Open design](https://www.figma.com/design/8nNCv2zMnDqGnqq0y9z0i0/Care-connect?t=lLHVpV4sLyX1ayFT-0)
- 📱 Mother App APK: *coming soon*
- 📱 Babysitter App APK: *coming soon*
- 🛡 Admin Panel: *internal-only*
- 🎥 Video walkthrough (all three apps): *coming soon*

In the meantime, see [screenshots/](screenshots/) for visual previews.

---

## 🔐 Trust & Safety Model

A childcare platform lives or dies on trust. Key safeguards engineered into the system:

| Concern | Mitigation |
|---|---|
| Unverified babysitters | Required certification upload + admin review |
| Underage babysitter risk | Age verification on signup |
| Inappropriate reviews | Admin moderation workflow with delete privilege |
| Account abuse | Admin can deactivate any account |
| Data leaks across users | RBAC + Supabase RLS policies |
| Communication safety | WhatsApp integration preserves chat history |
| Payment disputes | All transactions visible in admin payment records |
| PII protection | AES-256 encryption at rest |

---

## 🗂️ Project Documentation

This project was developed with rigorous software requirements engineering. The full documentation set includes:

| Document | Audience | Purpose |
|---|---|---|
| [Architecture](docs/architecture.md) | Engineers | System design, sequence diagrams, integration map |
| [Tech Stack](docs/tech-stack.md) | Engineers | Full breakdown with rationale |
| [Engineering Decisions (ADRs)](docs/ENGINEERING-DECISIONS.md) | Senior Engineers | Documented architectural decisions |
| [Case Study](case-study.md) | All | Problem, approach, outcome, lessons learned |
| [Impact](IMPACT.md) | Grant Reviewers | Social impact framework |
| [Business Model](BUSINESS-MODEL.md) | Accelerators / Investors | Marketplace economics |
| [Timeline](TIMELINE.md) | All | Project milestones |
| [Contributors](CONTRIBUTORS.md) | All | Team and acknowledgements |
| [Security Policy](SECURITY.md) | Engineers / Auditors | Disclosure process |

The original SRS document follows **IEEE 830 standards** and is available on request.

---

## 📚 Project Documentation

This repository contains a complete documentation set:

| Document | Audience | Purpose |
|---|---|---|
| [Architecture](docs/architecture.md) | Engineers | Three-app system design, sequence diagrams, RBAC matrix |
| [Tech Stack](docs/tech-stack.md) | Engineers | Full technology breakdown with rationale |
| [Engineering Decisions (ADRs)](docs/ENGINEERING-DECISIONS.md) | Senior Engineers | 10 documented architectural decisions |
| [Case Study](case-study.md) | All | Problem, approach, outcome, lessons learned |
| [Impact & Theory of Change](IMPACT.md) | Grant Reviewers | SDG alignment, outcome metrics, target programs |
| [Business Model](BUSINESS-MODEL.md) | Accelerators / Investors | Revenue streams, market, unit economics |
| [Timeline](TIMELINE.md) | All | Project milestones and post-archive roadmap |
| [Contributors](CONTRIBUTORS.md) | All | Team, co-developer, stakeholders |
| [Security Policy](SECURITY.md) | Engineers / Auditors | Disclosure process, RBAC matrix |
| [Press Kit](press-kit/) | Reviewers / Journalists | Single-page PDF + markdown source |

The original IEEE 830 SRS document is available on request.

---

## 👥 Team Contributions

| App | Role | Collaborator |
|---|---|---|
| **Mother App** | Solo design + development | — |
| **Babysitter App** | Co-developer | [@shaha123s](https://github.com/shaha123s) |
| **Admin Panel** | Solo design + development | — |
| **Shared backend** | Architecture + design | — |
| **SRS documentation** | Sole author | — |
| **Figma design system** | Designer | — |

---

## 📬 Contact

- **Email:** moznjamous9@gmail.com
- **GitHub:** [@Mozn-jamous](https://github.com/Mozn-jamous)
- **LinkedIn:** [Mozn Jamous](https://www.linkedin.com/in/mozn-jamous)

For partnership opportunities to revive and scale the platform, or to discuss the three-tier marketplace architecture, please reach out directly.

---

## 📄 License

This repository and all its contents are © 2026 Mozn Jamous. **All rights reserved.** See [LICENSE](LICENSE).

The source code is private. The Babysitter App was co-developed with [@shaha123s](https://github.com/shaha123s); this showcase describes my contributions only and does not assign ownership of the joint Babysitter App.

---

<div align="center">

*Built in Damascus.* 🇸🇾

</div>
