"""
Generate a professional press-kit PDF for CareConnect.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.colors import HexColor

NAVY = HexColor("#1E40AF")
ACCENT = HexColor("#3B82F6")
LIGHT_BG = HexColor("#F2F4F8")
WARM = HexColor("#B45F06")
DARK_TEXT = HexColor("#1F2937")
GREY = HexColor("#6B7280")

styles = getSampleStyleSheet()
TITLE = ParagraphStyle("T", parent=styles["Title"], fontName="Helvetica-Bold",
                       fontSize=28, textColor=NAVY, alignment=TA_LEFT, spaceAfter=2)
SUBTITLE = ParagraphStyle("S", parent=styles["Normal"], fontName="Helvetica",
                          fontSize=11, textColor=ACCENT, alignment=TA_LEFT, spaceAfter=10)
TAGLINE = ParagraphStyle("Tg", parent=styles["Normal"], fontName="Helvetica-Oblique",
                         fontSize=10, textColor=GREY, alignment=TA_LEFT, spaceAfter=14)
H_SECTION = ParagraphStyle("HS", parent=styles["Normal"], fontName="Helvetica-Bold",
                           fontSize=11, textColor=NAVY, alignment=TA_LEFT,
                           spaceBefore=6, spaceAfter=4)
BODY = ParagraphStyle("B", parent=styles["Normal"], fontName="Helvetica",
                      fontSize=9, textColor=DARK_TEXT, alignment=TA_LEFT,
                      leading=12, spaceAfter=4)
BODY_SMALL = ParagraphStyle("BS", parent=BODY, fontSize=8, leading=10, textColor=GREY)


def make_box(content, bg=LIGHT_BG, border=True):
    from reportlab.lib import colors
    t = Table([[content]], colWidths=[None])
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]
    if border:
        style.append(("BOX", (0, 0), (-1, -1), 0.5, NAVY))
    t.setStyle(TableStyle(style))
    return t


def header_band(canvas_obj, doc):
    canvas_obj.saveState()
    width, height = A4
    canvas_obj.setFillColor(NAVY)
    canvas_obj.rect(0, height - 18*mm, width, 18*mm, fill=1, stroke=0)
    canvas_obj.setFillColor(white)
    canvas_obj.setFont("Helvetica-Bold", 14)
    canvas_obj.drawString(20*mm, height - 12*mm, "CareConnect — Press Kit")
    canvas_obj.setFont("Helvetica-Oblique", 9)
    canvas_obj.drawRightString(width - 20*mm, height - 12*mm,
                               "Three-Tier Childcare Marketplace")
    canvas_obj.setFillColor(GREY)
    canvas_obj.setFont("Helvetica-Oblique", 7)
    canvas_obj.drawCentredString(width / 2, 10*mm,
        "github.com/Mozn-jamous/careconnect-platform-showcase · moznjamous9@gmail.com · linkedin.com/in/mozn-jamous")
    canvas_obj.restoreState()


doc = SimpleDocTemplate(
    r"c:\Users\mesho\OneDrive\Desktop\portfolio-showcase\careconnect-platform-showcase\press-kit\CareConnect-Press-Kit.pdf",
    pagesize=A4,
    topMargin=25*mm, bottomMargin=15*mm,
    leftMargin=16*mm, rightMargin=16*mm,
    title="CareConnect Press Kit",
    author="Mozn Jamous",
)

flow = []
flow.append(Paragraph("👶 CareConnect", TITLE))
flow.append(Paragraph("A Three-Tier Childcare Marketplace — Flutter + Supabase + IEEE 830 SRS",
                     SUBTITLE))
flow.append(Paragraph(
    "Three integrated Flutter apps (Mother + Babysitter + Admin Panel) on a unified Supabase backend, "
    "connecting parents with verified babysitters under transparent admin moderation.", TAGLINE))

problem_html = (
    "<b>The Problem.</b> Childcare in Arabic-speaking regions is dominated by informal "
    "networks — Facebook groups, word-of-mouth — with no trust verification, no reputation "
    "portability for providers, and no quality oversight. Working mothers reduce hours or "
    "exit the workforce; skilled babysitters earn unpredictable income; children miss "
    "structured enriching care."
)

solution_html = (
    "<b>The Solution.</b> Three Flutter apps on a unified Supabase backend: a Mother App "
    "for discovery and booking, a Babysitter App (co-developed with @shaha123s) for "
    "providers, and an Admin Panel for platform operators. Realtime sync, Google Maps "
    "discovery, WhatsApp communication, RBAC at the database layer."
)

two_col = Table(
    [[Paragraph(problem_html, BODY), Paragraph(solution_html, BODY)]],
    colWidths=[(A4[0] - 32*mm) / 2 - 4*mm] * 2,
    style=TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]),
)
flow.append(two_col)
flow.append(Spacer(1, 8))

# Three apps
flow.append(Paragraph("🏗️ Three Apps, One Ecosystem", H_SECTION))
apps_data = [
    ["App", "Audience", "Key Features"],
    ["Mother App", "Parents", "Discovery, booking, task list, vaccines, sleep/meal tracking"],
    ["Babysitter App", "Providers", "Booking inbox, certifications, task execution, ratings"],
    ["Admin Panel", "Operators", "User management, payment audit, moderation, library curation"],
]
apps_table = Table(apps_data, colWidths=[3.5*cm, 3*cm, 10*cm])
apps_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT_BG, white]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
]))
flow.append(apps_table)
flow.append(Spacer(1, 8))

# SDG / Market / Team triple
sdgs_p = Paragraph(
    "<b>🌍 SDG Alignment</b><br/>"
    "• SDG 5 — Gender Equality (5.4, 5.b)<br/>"
    "• SDG 8 — Decent Work (8.3, 8.5)<br/>"
    "• SDG 4 — Early Childhood Dev (4.2)<br/>"
    "• SDG 10 — Reduced Inequalities (10.2)",
    BODY)
market_p = Paragraph(
    "<b>📊 Market</b><br/>"
    "• <b>TAM:</b> ~$600M (40M MENA households)<br/>"
    "• <b>SAM:</b> $50M (Levant + Gulf + Egypt)<br/>"
    "• <b>SOM (3 yr):</b> $1.5M–$3.5M<br/>"
    "• <b>Model:</b> Subscriptions + per-booking commission",
    BODY)
team_p = Paragraph(
    "<b>👥 Team</b><br/>"
    "• <b>Mozn Jamous</b> — Mother App, Admin, backend, SRS<br/>"
    "• <b>Shahab</b> ([@shaha123s]) — Babysitter App co-dev<br/>"
    "• <b>Hiring (post-pilot):</b> mobile eng, growth lead",
    BODY)

triple = Table(
    [[make_box(sdgs_p), make_box(market_p), make_box(team_p)]],
    colWidths=[(A4[0] - 32*mm) / 3 - 3*mm] * 3,
    style=TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]),
)
flow.append(triple)
flow.append(Spacer(1, 8))

# Tech Stack
flow.append(Paragraph("🧰 Technology Stack", H_SECTION))
tech_data = [
    ["Layer", "Choice", "Why"],
    ["Mobile (3 apps)", "Flutter + Provider", "Cross-platform, single language, mature RTL"],
    ["Backend", "Supabase + PostgreSQL", "Realtime, RLS, free tier, relational integrity"],
    ["Auth", "Supabase Auth + OAuth", "Email + Google + Facebook"],
    ["Access Control", "RBAC enforced via RLS", "Database-layer single source of truth"],
    ["Maps", "Google Maps Platform", "Strong MENA city coverage"],
    ["Communication", "WhatsApp Business API", "Matches user habits"],
    ["Security", "JWT + bcrypt + AES-256", "Industry-standard"],
    ["Documentation", "IEEE 830 SRS", "Full requirements engineering"],
]
tech_table = Table(tech_data, colWidths=[3*cm, 5*cm, 8.5*cm])
tech_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT_BG, white]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
]))
flow.append(tech_table)
flow.append(Spacer(1, 8))

# CTA
cta_p = Paragraph(
    "<b>We are actively seeking:</b><br/>"
    "Women's economic empowerment grants (UN Women, World Bank, Cherie Blair Foundation) · "
    "MENA accelerator partnerships (Misk, MBRF, Flat6Labs, Antler MENA) · "
    "Early-childhood development funders (ELMA Foundation, Grand Challenges Canada) · "
    "Clinic and nursery partnerships in Damascus and Gulf cities for pilot deployment.",
    BODY)
flow.append(make_box(cta_p, bg=HexColor("#FFF8E1"), border=True))

flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "<i>Childcare is the invisible infrastructure that enables every other form of work. "
    "CareConnect is our contribution to making that infrastructure visible, accountable, "
    "and economically empowering for everyone involved.</i>", BODY_SMALL))

doc.build(flow, onFirstPage=header_band, onLaterPages=header_band)
print("Generated: CareConnect-Press-Kit.pdf")
