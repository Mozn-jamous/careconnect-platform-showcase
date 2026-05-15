# CareConnect — Tech Stack

The full technical breakdown of the CareConnect three-app ecosystem.

## Mobile Client (Flutter — All Three Apps)

| Concern | Choice | Why |
|---|---|---|
| Framework | **Flutter** | Cross-platform, single codebase for iOS/Android, mature Arabic typography |
| Language | **Dart** | Null-safety, async/await, strong typing |
| State Management | **Provider** | Lightweight, well-documented, sufficient for our complexity |
| Routing | **Built-in Navigator 2.0** | Standard, declarative |
| UI Foundation | **Material Design + custom theming** | Industry-standard UX patterns |
| Responsive Layout | **LayoutBuilder + MediaQuery** | Phone + tablet adaptive layouts |
| HTTP | **http + custom REST clients** | Talks to Supabase + external APIs |
| Image handling | **cached_network_image, image_picker** | Caching + camera/gallery uploads |
| Maps | **google_maps_flutter** | Babysitter discovery |
| Communication | **url_launcher** | WhatsApp deep links |
| Local persistence | **shared_preferences** | Session and preferences |

## Backend & Data

| Layer | Choice | Why |
|---|---|---|
| Backend-as-a-Service | **Supabase** | Free tier, PostgreSQL-native, realtime channels |
| Database | **PostgreSQL** | Relational integrity, JSONB, stored procedures, FTS |
| Auth | **Supabase Auth + OAuth** | Email + Google + Facebook sign-in |
| Storage | **Supabase Storage** | Child photos, certifications, ID documents |
| Realtime sync | **Supabase Realtime** | Live booking + task list updates across apps |
| Migrations | **Supabase CLI** | Versioned, reproducible schema changes |

## External Integrations

| Service | Purpose | Notes |
|---|---|---|
| **Google Maps Platform** | Babysitter discovery, distance, navigation | Commercial API; server-side key |
| **WhatsApp Business API** | Direct mother-babysitter communication | Deep-link based |
| **Babysitter App** (cross-app) | Booking + task list sync | Shared Supabase backend |
| **Digital Library API** | Educational content for children | Custom REST |

## Security & Compliance

| Component | Technology |
|---|---|
| Auth tokens | **JWT** with role claims and refresh rotation |
| Password storage | **bcrypt** (work factor ≥ 12) |
| Data at rest | **AES-256** encryption for sensitive fields |
| Data in transit | **HTTPS / TLS 1.3** for all endpoints |
| Access control | **RBAC** with three roles (mother / babysitter / admin) |
| Database-layer enforcement | **Supabase RLS policies** |
| Compliance frameworks | **GDPR**, **CCPA** (design-aligned) |

## DevOps & Quality

| Tool | Purpose |
|---|---|
| **GitHub** | Source control, branching, code review |
| **Figma** | UI/UX design (full design system + prototype) |
| **VS Code** | Primary IDE |
| **Postman** | API testing & documentation |

## Documentation Standards

| Standard | Use |
|---|---|
| **IEEE 830** | Software Requirements Specification (SRS) — followed for the full SRS document |
| **C4 model** (selectively) | High-level architecture diagrams |
| **REST architectural style** | All HTTP APIs |
| **UML 2.x** | Use case, sequence, activity, class diagrams |

## Why NOT these alternatives?

| Alternative | Why we passed |
|---|---|
| **Firebase** | Considered seriously; Supabase free tier more generous, Postgres more familiar, RLS cleaner than Firebase Rules |
| **React Native** | Less mature Arabic typography; team velocity stronger with Flutter |
| **In-app payment gateway** (Stripe/PayPal) | Regional payment infrastructure constraints in V1; cash + bank transfer suffices |
| **Self-hosted backend** | Too much ops work; Supabase gives us 80% of what we'd build at 5% the cost |
| **Custom OAuth** | Supabase Auth + provider SDKs are battle-tested |
| **NoSQL (MongoDB)** | Our data is inherently relational (bookings, mothers, children) |
| **Riverpod / BLoC** | Provider is sufficient for our state complexity |

## Fonts

Arabic and English fonts:
- **Cairo** — primary UI font for headings and body
- **System default** — fallback for performance-critical screens

## Localization

- **Arabic (primary)** with full RTL layout
- **English (secondary)** with LTR layout
- **flutter_localizations** for date/number formatting
- **i18n** keys organized by feature module
