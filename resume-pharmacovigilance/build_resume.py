#!/usr/bin/env python3
"""Render the pharmacovigilance resume to ATS-safe .docx, .pdf and .txt.

Usage:
    pip install python-docx reportlab
    python3 build_resume.py

Design rules enforced here (all of them are ATS parser requirements):
  * single column, no tables, no text boxes, no images, no icons
  * contact details in the document body, never in a header/footer
  * standard section headings, reverse-chronological order
  * standard fonts at 10-11pt, plain bullets, ASCII-only punctuation
  * dates as "Mon YYYY - Mon YYYY" on the same line as the role
"""

import re
import sys
from pathlib import Path

import resume_content as C

OUT_DIR = Path(__file__).parent
BASENAME = "Aparna_Mishra_Pharmacovigilance_Resume"

BULLET = "\u2022 "
PLACEHOLDER_RE = re.compile(r"\[[^\]]+\]")


# --------------------------------------------------------------------------- #
# Section model shared by every renderer
# --------------------------------------------------------------------------- #
def sections():
    """Yield (heading, blocks) where a block is one of:
    ("para", text) | ("bullets", [text]) | ("entry", head_left, head_right, [bullets])
    """
    yield "PROFESSIONAL SUMMARY", [("para", C.SUMMARY)]

    yield "CORE SKILLS", [("labeled", label, items) for label, items in C.SKILLS]

    exp_blocks = []
    for job in C.EXPERIENCE:
        org_line = " | ".join(x for x in [job["org"], job["location"]] if x)
        exp_blocks.append(("entry", job["title"], job["dates"], job["bullets"], org_line))
    yield "PROFESSIONAL EXPERIENCE", exp_blocks

    pv_blocks = [("italic", C.PV_TRAINING["note"])]
    for e in C.PV_TRAINING["entries"]:
        org_line = " | ".join(x for x in [e["org"], e["location"]] if x)
        pv_blocks.append(("entry", e["title"], e["dates"], e["bullets"], org_line))
    yield C.PV_TRAINING["heading"], pv_blocks

    edu_blocks = []
    for ed in C.EDUCATION:
        edu_blocks.append(
            ("entry", ed["degree"], ed["dates"], [ed["detail"]], ed["institute"])
        )
    yield "EDUCATION", edu_blocks

    proj_blocks = []
    for p in C.PROJECTS:
        proj_blocks.append(("entry", p["title"], p["dates"], p["bullets"], p["org"]))
    yield "RESEARCH & ACADEMIC PROJECTS", proj_blocks

    yield "PUBLICATIONS", [("bullets", C.PUBLICATIONS)]
    yield "CERTIFICATIONS", [("bullets", C.CERTIFICATIONS)]
    yield "TRAININGS, WORKSHOPS & CONFERENCES", [("bullets", C.WORKSHOPS)]
    yield "ADDITIONAL INFORMATION", [("bullets", C.ADDITIONAL)]


# --------------------------------------------------------------------------- #
# DOCX
# --------------------------------------------------------------------------- #
def build_docx(path):
    from docx import Document
    from docx.enum.text import WD_TAB_ALIGNMENT, WD_LINE_SPACING
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt, Inches, RGBColor

    BODY_PT = 9.2
    LINE_PT = 10.4

    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.45)
        section.bottom_margin = Inches(0.45)
        section.left_margin = Inches(0.5)
        section.right_margin = Inches(0.5)
    content_width = Inches(7.5)

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(BODY_PT)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.EXACTLY
    normal.paragraph_format.line_spacing = Pt(LINE_PT)

    def para(text="", size=BODY_PT, bold=False, italic=False, space_before=0, space_after=1.5,
             align=None):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(space_before)
        pf.space_after = Pt(space_after)
        if align is not None:
            p.alignment = align
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.size = Pt(size)
        return p

    def bottom_border(p):
        pPr = p._p.get_or_add_pPr()
        borders = OxmlElement("w:pBdr")
        bottom = OxmlElement("w:bottom")
        bottom.set(qn("w:val"), "single")
        bottom.set(qn("w:sz"), "6")
        bottom.set(qn("w:space"), "1")
        bottom.set(qn("w:color"), "000000")
        borders.append(bottom)
        pPr.append(borders)

    def heading(text):
        p = para(text, size=9.8, bold=True, space_before=3.5, space_after=1)
        bottom_border(p)
        return p

    def bullet(text):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent = Inches(0.18)
        pf.first_line_indent = Inches(-0.18)
        pf.space_after = Pt(1.2)
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        pf.line_spacing = Pt(LINE_PT)
        run = p.add_run(BULLET + text)
        run.font.size = Pt(BODY_PT)
        return p

    def entry_head(left, right):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(3)
        pf.space_after = Pt(0)
        pf.tab_stops.add_tab_stop(content_width, WD_TAB_ALIGNMENT.RIGHT)
        r = p.add_run(left)
        r.bold = True
        r.font.size = Pt(BODY_PT)
        r2 = p.add_run("\t" + right)
        r2.bold = True
        r2.font.size = Pt(BODY_PT)
        return p

    # Header block (in the body, as ATS parsers require)
    para(C.NAME, size=16, bold=True, space_after=1)
    para(C.HEADLINE, size=10, bold=True, space_after=1)
    for line in C.CONTACT:
        para(line, size=9, space_after=0)

    for head, blocks in sections():
        heading(head)
        for block in blocks:
            kind = block[0]
            if kind == "para":
                para(block[1], space_after=1.5)
            elif kind == "labeled":
                p = doc.add_paragraph()
                p.paragraph_format.space_after = Pt(1.5)
                r = p.add_run(block[1] + ": ")
                r.bold = True
                r.font.size = Pt(BODY_PT)
                r2 = p.add_run(block[2])
                r2.font.size = Pt(BODY_PT)
            elif kind == "italic":
                para(block[1], italic=True, space_after=1.5)
            elif kind == "bullets":
                for b in block[1]:
                    bullet(b)
            elif kind == "entry":
                _, left, right, bullets, sub = block
                entry_head(left, right)
                if sub:
                    para(sub, size=BODY_PT, italic=True, space_after=1.5)
                for b in bullets:
                    bullet(b)

    doc.save(path)
    return path


# --------------------------------------------------------------------------- #
# PDF (text-based, selectable text -> parseable by ATS)
# --------------------------------------------------------------------------- #
def build_pdf(path):
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import (
        BaseDocTemplate,
        Frame,
        HRFlowable,
        PageTemplate,
        Paragraph,
        Spacer,
    )
    from xml.sax.saxutils import escape

    page_w, page_h = A4
    lm = rm = 0.5 * inch
    tm = bm = 0.4 * inch

    doc = BaseDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=lm,
        rightMargin=rm,
        topMargin=tm,
        bottomMargin=bm,
        title="Aparna Mishra - Pharmacovigilance / Drug Safety Resume",
        author="Aparna Mishra",
        subject="Pharmacovigilance, Drug Safety, ICSR Case Processing",
    )
    frame = Frame(lm, bm, page_w - lm - rm, page_h - tm - bm, id="body",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame])])

    base = dict(fontName="Helvetica", fontSize=9.2, leading=10.9, spaceAfter=1.5,
                textColor="black")
    st_name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=16, leading=18,
                             spaceAfter=1)
    st_headline = ParagraphStyle("headline", fontName="Helvetica-Bold", fontSize=9.6,
                                 leading=11.5, spaceAfter=1)
    st_contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.7, leading=10.3)
    st_head = ParagraphStyle("head", fontName="Helvetica-Bold", fontSize=9.8, leading=11.5,
                             spaceBefore=4.5, spaceAfter=1)
    st_body = ParagraphStyle("body", alignment=TA_LEFT, **base)
    st_italic = ParagraphStyle("italic", fontName="Helvetica-Oblique", fontSize=9.2,
                               leading=10.9, spaceAfter=1.5)
    st_bullet = ParagraphStyle("bullet", alignment=TA_LEFT, leftIndent=11,
                               bulletIndent=0, **base)
    st_entry = ParagraphStyle("entry", fontName="Helvetica-Bold", fontSize=9.5, leading=11.2,
                              spaceBefore=3.5, spaceAfter=0)

    story = [Paragraph(escape(C.NAME), st_name), Paragraph(escape(C.HEADLINE), st_headline)]
    for line in C.CONTACT:
        story.append(Paragraph(escape(line), st_contact))

    def rule():
        return HRFlowable(width="100%", thickness=0.6, color="black",
                          spaceBefore=0.5, spaceAfter=2)

    for head, blocks in sections():
        story.append(Paragraph(escape(head), st_head))
        story.append(rule())
        for block in blocks:
            kind = block[0]
            if kind == "para":
                story.append(Paragraph(escape(block[1]), st_body))
            elif kind == "labeled":
                story.append(
                    Paragraph(
                        f"<b>{escape(block[1])}:</b> {escape(block[2])}", st_body
                    )
                )
            elif kind == "italic":
                story.append(Paragraph(escape(block[1]), st_italic))
            elif kind == "bullets":
                for b in block[1]:
                    story.append(Paragraph(escape(b), st_bullet, bulletText="\u2022"))
            elif kind == "entry":
                _, left, right, bullets, sub = block
                story.append(
                    Paragraph(f"{escape(left)} | {escape(right)}", st_entry)
                )
                if sub:
                    story.append(Paragraph(escape(sub), st_italic))
                for b in bullets:
                    story.append(Paragraph(escape(b), st_bullet, bulletText="\u2022"))
        story.append(Spacer(1, 0))

    doc.build(story)
    return path


# --------------------------------------------------------------------------- #
# Plain text (for Naukri/Workday paste boxes and quick keyword checks)
# --------------------------------------------------------------------------- #
def build_txt(path):
    lines = [C.NAME, C.HEADLINE]
    lines += list(C.CONTACT)
    for head, blocks in sections():
        lines += ["", head, "-" * len(head)]
        for block in blocks:
            kind = block[0]
            if kind in ("para", "italic"):
                lines.append(block[1])
            elif kind == "labeled":
                lines.append(f"{block[1]}: {block[2]}")
            elif kind == "bullets":
                lines += [f"- {b}" for b in block[1]]
            elif kind == "entry":
                _, left, right, bullets, sub = block
                lines.append("")
                lines.append(f"{left} | {right}")
                if sub:
                    lines.append(sub)
                lines += [f"- {b}" for b in bullets]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def report_placeholders(text):
    found = sorted(set(PLACEHOLDER_RE.findall(text)))
    if found:
        print("\nPlaceholders still to fill in before sending the resume:")
        for f in found:
            print(f"  {f}")
    else:
        print("\nNo placeholders left.")


def main():
    docx_path = build_docx(OUT_DIR / f"{BASENAME}.docx")
    pdf_path = build_pdf(OUT_DIR / f"{BASENAME}.pdf")
    txt_path = build_txt(OUT_DIR / f"{BASENAME}.txt")
    for p in (docx_path, pdf_path, txt_path):
        print(f"wrote {p.name} ({p.stat().st_size / 1024:.1f} KB)")
    report_placeholders(txt_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
