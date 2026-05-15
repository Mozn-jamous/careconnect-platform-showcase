# Press Kit

This folder contains shareable assets for journalists, grant reviewers, accelerators, investors, and partners interested in CareConnect.

## Files

| File | Use |
|---|---|
| `CareConnect-Press-Kit.pdf` | **Single-page PDF** — share with grant reviewers, journalists, accelerators |
| `one-pager.md` | Markdown source for the press kit content |
| `generate_press_kit_pdf.py` | Script that builds the PDF (uses `reportlab`) |

## Quick Use

1. **Reviewing the project for a grant?** Open `CareConnect-Press-Kit.pdf` — it contains everything you need in one page.
2. **Writing about the project?** Use `one-pager.md` as a quote source and the [main README](../README.md) for technical depth.
3. **Investor due diligence?** Pair this kit with [BUSINESS-MODEL.md](../BUSINESS-MODEL.md), [IMPACT.md](../IMPACT.md), and [ENGINEERING-DECISIONS.md](../docs/ENGINEERING-DECISIONS.md).

## Press Contact

**Mozn Jamous**
asaierafi@clinlab.ai
linkedin.com/in/mozn-jamous

## Regenerating the PDF

```bash
pip install reportlab
python generate_press_kit_pdf.py
```

## Key Facts (Fast Reference)

- **Project name:** CareConnect
- **Type:** Three-tier childcare marketplace (Mother + Babysitter + Admin apps)
- **Audience:** Arabic-speaking families and babysitters in MENA
- **Standards:** IEEE 830 SRS documentation
- **Stack:** Flutter · Provider · Supabase · PostgreSQL · OAuth · Google Maps · WhatsApp
- **Team:** Mozn Jamous (Mother App, Admin, Backend, SRS) + @shaha123s (Babysitter App co-developer)
- **Status:** V1 archived (Feb 2025); pending revival decision
