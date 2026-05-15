# Security Policy

CareConnect handles sensitive information about families, children, and care providers. We treat security as a primary product concern, not an afterthought.

## Supported Versions

| Version | Status | Security Updates |
|---|---|---|
| 1.x (MVP — university project submission) | Active | ✅ Yes |
| Pre-release | Deprecated | ❌ No |

## Reporting a Vulnerability

If you discover a security vulnerability in CareConnect, **do not open a public GitHub issue.**

Report it privately by emailing:

📧 **asaierafi@clinlab.ai**

Subject line: `[SECURITY] CareConnect — Brief description`

Include:
- A clear description of the issue and its potential impact
- Steps to reproduce
- Any proof-of-concept code (please redact PII)
- Your contact information for follow-up

### Response Timeline

| Action | Target Timeline |
|---|---|
| Acknowledgement of receipt | Within 48 hours |
| Initial assessment | Within 5 business days |
| Fix timeline (severity-dependent) | Critical: 7 days · High: 14 days · Medium: 30 days |
| Public disclosure | Coordinated with reporter, after fix is shipped |

## Security Practices Built Into CareConnect

### Authentication & Authorization
- **JWT tokens** with role claims and refresh-token rotation
- **bcrypt password hashing** (work factor ≥ 12)
- **OAuth 2.0** providers (Google, Facebook)
- **RBAC with three roles** (mother / babysitter / admin) enforced at the database layer
- **Token storage** in platform-secured keychains (`flutter_secure_storage`)

### Database
- **Row-Level Security** policies on every table, scoped by user role and ownership
- **No raw SQL** from clients; all writes go through validated Supabase queries
- **Cascade deletes** for GDPR right-to-erasure compliance
- **Daily backups** with point-in-time recovery (Supabase managed)

### API & Network
- **HTTPS / TLS 1.3** required for all endpoints
- **Rate limiting** on authentication and booking endpoints
- **No API keys in client builds** — Google Maps and other commercial APIs proxied through Supabase Edge Functions
- **Signed URLs** for Supabase Storage objects

### Sensitive Data
- **AES-256 encryption** for sensitive fields at rest
- **PII stripping** in logs and analytics
- **Photo storage** uses signed URLs with short expiry
- **Child medical information** access logged for audit

### Mobile Client
- **No sensitive data in shared_preferences** — secure storage for tokens and PII
- **Certificate pinning** (planned for production release)
- **Obfuscation** of release builds (Dart `--obfuscate`)
- **Jailbreak / root detection** (planned)

### Admin Panel
- **Separate admin role** with elevated audit logging
- **Two-factor authentication** required (planned for production)
- **All admin actions logged** in an immutable audit table

## RBAC Matrix

| Action | Mother | Babysitter | Admin |
|---|---|---|---|
| View own children | ✅ | ❌ | ✅ |
| View own bookings | ✅ | ✅ (own) | ✅ |
| Create booking | ✅ | ❌ | ❌ |
| Accept/reject booking | ❌ | ✅ | ❌ |
| Edit task list | ✅ (creator) | ❌ | ❌ |
| Mark task done | ❌ | ✅ (assigned) | ❌ |
| Post review | ✅ (after booking) | ❌ | ❌ |
| Delete review | ❌ | ❌ | ✅ |
| View all users | ❌ | ❌ | ✅ |
| Deactivate user | ❌ | ❌ | ✅ |
| Manage library content | ❌ | ❌ | ✅ |
| View payment records | own | own | ✅ all |

## Out of Scope

The following are explicitly **not** in scope for security reports:

- Issues requiring physical access to an unlocked device
- Social engineering against admins or babysitters
- Denial of service caused by extreme call volume to free-tier services
- Vulnerabilities in upstream open-source dependencies (please report those to upstream maintainers)
- Findings already documented in this file
- Issues with WhatsApp deep linking (out of our control)

## Compliance Status

| Framework | Status |
|---|---|
| **GDPR** | Design-aligned (right to access, portability, erasure implemented) |
| **CCPA** | Design-aligned (opt-out flows in place) |
| **WhatsApp Business policy** | Compliant |
| **Apple App Store guidelines** | Targeted for V2 |
| **Google Play guidelines** | Targeted for V2 |

## Past Disclosures

No security advisories at this time.

## Security Roadmap

- [ ] Two-factor authentication for admins
- [ ] Background-check API integration for babysitter verification
- [ ] Certificate pinning in mobile clients
- [ ] Jailbreak / root detection
- [ ] Bug bounty program (post-public-release)
- [ ] Annual third-party security audit
