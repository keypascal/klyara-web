#!/usr/bin/env python3
"""
build-admin.py — one source of truth for the Klyara hidden admin panel.

Copies the finished deliverables out of /root/klyara/v2/out/ into
site/assets/docs/<folder>/, renders a first-page PNG preview for every PDF,
and regenerates:

    assets/data/library.json   the document library index  (+ library.js shim)
    assets/data/plan.json      the 90-day plan             (+ plan.js shim)
    assets/data/bplan.json     the business plan reader    (+ bplan.js shim)

The .js shims carry the identical payload on a `window.KLY_*` global so the
panel also works from a file:// URL, where fetch() is blocked.

Run:  python3 site/build-admin.py
"""
import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))          # /root/klyara/site
PROJ = os.path.dirname(ROOT)                                # /root/klyara
OUT = os.path.join(PROJ, "v2", "out")
DOCS_MD = os.path.join(PROJ, "docs")
DEST = os.path.join(ROOT, "assets", "docs")
PREV = os.path.join(DEST, "_prev")
DATA = os.path.join(ROOT, "assets", "data")
sys.path.insert(0, os.path.join(PROJ, "v2", "lib"))
import dates as D  # noqa: E402

# ---------------------------------------------------------------- folders ---
FOLDERS = [
    ("01_Start_Here", "Start here", "The map, the plan, and the decisions only you can make."),
    ("02_Business_Plan", "Business plan", "The plan itself, the market, the risks and the benchmark."),
    ("03_Financials", "Financials", "The model, the workbook and the summary of the numbers."),
    ("04_Brand", "Brand", "Print-ready stationery, cards, leaflets and email signatures."),
    ("05_Operations", "Operations", "How the firm runs, sells, prices and onboards."),
    ("06_Stationery", "Stationery", "Invoices, quotes, POs, timesheets — blank and worked."),
    ("07_Forms_and_Contracts", "Forms and contracts", "Engagement, terms, privacy, hiring and complaints."),
    ("08_Marketing", "Marketing", "Channels, calendars, video, email, SEO and the answer bank."),
    ("09_Assets", "Assets", "Images, cards and social artwork."),
]
FOLDER_TITLE = {k: t for k, t, _ in FOLDERS}

FMT_ORDER = ["PDF", "DOCX", "XLSX", "PPTX", "HTML", "TXT", "PNG", "SVG", "JPG", "CSV"]
OFFICE = {"DOCX", "XLSX", "PPTX"}

# One line saying what each thing is. Keyed by file stem; the *index* is walked
# from disk, this only supplies the prose.
DESC = {
 "00_START_HERE": ("Start here", "The map of the whole pack: what is in it, what is not, and the running order."),
 "14_the_90_day_plan": ("The 90-day plan", "Everything sequenced into one ordered list, with owners and decision gates."),
 "16_day_by_day_plan": ("Day by day, 90 days", "Every day from 1 September to day 90, dated, timed, one thing per day."),
 "18_what_i_need_from_you": ("What I need from you", "The thirty decisions only Key and Craig can make, grouped into one session."),
 "Klyara_Business_Plan": ("Business plan", "Fourteen sections: market, offer, pricing, capacity, regulation, risk and milestones."),
 "Klyara_Business_Plan_Summary": ("Business plan summary", "The deck version — the same plan in slides for a bank or a partner."),
 "17_market_intelligence": ("Market intelligence", "Verified facts with sources, market size, how buyers decide, and what could not be verified."),
 "20_risk_register": ("Risk register", "The fourteen things that actually kill this, ranked, with an early warning sign each."),
 "22_competitor_and_price_benchmark": ("Competitor and price benchmark", "Real published UK prices, sourced, and where Klyara sits against them."),
 "Klyara_Financial_Model": ("Financial model", "The workbook: revenue build, costs, break-even and the client ramp, all live formulas."),
 "Klyara_Financial_Summary": ("Financial summary", "The numbers in plain English, for anyone who will not open a spreadsheet."),
 "06_ops_playbook": ("Ops playbook", "Tools, the weekly rhythm, UTMs, the review engine and the twelve missing pieces."),
 "07_website_audit": ("Website audit", "One legal exposure and six conversion fixes, in priority order."),
 "09_sales_pack": ("Sales pack", "Discovery script, seven diagnostic questions, ten objections and the qualify-out list."),
 "12_client_onboarding_pack": ("Client onboarding pack", "Signed to live in five working days: the runbook and the five client emails."),
 "21_pricing_scope_and_quoting": ("Pricing, scope and quoting", "What is in each tier, the rate card, and the three-strike scope-creep script."),
 "25_the_monthly_client_report": ("The monthly client report", "The one thing a client actually receives, and why it is the retention story."),
 "26_the_review_engine": ("The review engine", "Every word of the ask, the replies, and the Google Q&A entries to seed."),
 "01_channel_map": ("Channel map", "Every platform, forum and directory ranked by return per hour, with each one's rules."),
 "02_account_setup_pack": ("Account setup pack", "Copy-paste profile fields for fourteen platforms, written to exact character limits."),
 "03_content_calendar": ("Content calendar, days 1–30", "Full copy for every channel every day. Not outlines."),
 "24_content_calendar_month_2": ("Content calendar, days 31–60", "Month two in full, built around the November MTD deadline."),
 "04_video_pack": ("Video pack", "Scripts, shot lists and the honest answer on AI presenters."),
 "05_email_programme": ("Email programme", "Provider decision, the sequences, and the fortnightly newsletters."),
 "08_seo_schema_pack": ("SEO and schema pack", "Paste-ready JSON-LD, title tags, keyword clusters and the pages to build next."),
 "10_brand_guidelines": ("Brand guidelines", "Extracted from the live site, not invented. Hand this to anyone who touches the brand."),
 "11_guildford_local_pack": ("Guildford local pack", "The town page, the merchants, the citations, the partners and the press list."),
 "13_gbp_year_of_posts": ("A year of Google posts", "Fifty-two Google Business Profile posts, dated against the real deadline calendar."),
 "15_answer_bank": ("Answer bank", "Pre-written answers for forums and groups — the reason the community plan survives."),
 "19_ai_visibility_playbook": ("AI visibility playbook", "Where Klyara stands in AI answers, and the monthly test to keep checking."),
 "23_outreach_and_partners": ("Outreach and partners", "LinkedIn and cold-email sequences, phone scripts, and the partner programme terms."),
}

# Brand folder: generated names are descriptive, so derive and gloss by pattern.
PATTERNS = [
 (r"^Klyara-Brand-One-Pager", "Brand one-pager", "The brand on one A4 sheet: colour, type, logo rules and voice."),
 (r"^Klyara-Business-Cards?-", "Business cards", "Print artwork for the business cards."),
 (r"^Klyara-Compliment-Slips?", "Compliment slips", "Print artwork for the compliment slips."),
 (r"^Klyara-Email-Signature", "Email signature", "HTML and plain-text email signature, with install notes."),
 (r"^Klyara-Envelope-", "Envelope artwork", "Print artwork and printer guide for the envelopes."),
 (r"^Klyara-Leaflet-", "A5 leaflet", "The leaflet for trade counters and letterboxes."),
 (r"^Klyara-Letterhead-", "Letterhead", "A4 letterhead, print artwork and an editable Word version."),
 (r"^Klyara-Print-Specification", "Print specification", "Stock, finish, bleed and colour for every printed item."),
 (r"^Klyara-Service-Sheets?-", "Service sheet", "One sheet per plan, for handing over in person."),
 (r"^Klyara_Invoice_Template", "Invoice template", "Klyara's own invoice, blank and as a worked example."),
 (r"^Klyara_Credit_Note", "Credit note", "Credit note template, blank and as a worked example."),
 (r"^Klyara_Quote_Estimate", "Quote / estimate", "Quote and estimate template, blank and as a worked example."),
 (r"^Klyara_Purchase_Order", "Purchase order", "Purchase order template, blank and as a worked example."),
 (r"^Klyara_Receipt_Template", "Receipt", "Receipt template, blank and as a worked example."),
 (r"^Klyara_Job_Sheet", "Job sheet / work order", "The job sheet a crew fills in on site."),
 (r"^Klyara_Statement_of_Account", "Statement of account", "Customer statement, with live totals."),
 (r"^Klyara_Timesheet", "Weekly timesheet", "Weekly hours, with the totals calculated."),
 (r"^Klyara_Expense_Claim", "Expense claim", "Expense claim form, with the totals calculated."),
 (r"^Klyara-Client-Intake-Form", "Client intake form", "What is asked of a new client before anything is set up."),
 (r"^Klyara-New-Client-Questionnaire", "New client questionnaire", "The longer questionnaire that follows the intake form."),
 (r"^Klyara-Engagement-Letter", "Engagement letter", "The letter of engagement, with the schedule of services."),
 (r"^Klyara-Terms-and-Conditions", "Terms and conditions", "Klyara's terms of business."),
 (r"^Klyara-Privacy-Notice", "Privacy notice", "The UK GDPR privacy notice for clients and site visitors."),
 (r"^Klyara-Complaints-Procedure", "Complaints procedure", "How a complaint is handled, and in what time."),
 (r"^Klyara-Complaints-Form", "Complaints form", "The form a client uses to raise a complaint."),
 (r"^Klyara-Subcontractor-Agreement", "Subcontractor agreement", "The agreement for anyone doing work for Klyara."),
 (r"^Klyara-Subcontractor-Onboarding-Pack", "Subcontractor onboarding pack", "Everything a new subcontractor signs and supplies."),
 (r"^Klyara-Employment-Contract", "Employment contract and hire pack", "Contract, statement of particulars and the hiring checklist."),
 (r"^Klyara-Offer-Letter", "Offer letter", "The offer letter template for a first hire."),
]


def pretty(stem):
    if stem in DESC:
        return DESC[stem]
    for pat, title, desc in PATTERNS:
        if re.match(pat, stem):
            tail = re.sub(pat, "", stem).strip("-_ ")
            tail = tail.replace("-", " ").replace("_", " ").strip()
            t = f"{title} — {tail}" if tail else title
            return (t, desc)
    t = re.sub(r"^\d+[_-]", "", stem).replace("_", " ").replace("-", " ").strip()
    return (t[:1].upper() + t[1:], "Part of the delivery pack.")


# ------------------------------------------------------------- 1. staging ---
def stage():
    copied = 0
    if not os.path.isdir(OUT):
        sys.exit(f"missing source: {OUT}")
    SKIP = {"05_Website"}          # the site must never stage a copy of itself
    for folder in sorted(os.listdir(OUT)):
        if folder in SKIP: continue
        src = os.path.join(OUT, folder)
        if not os.path.isdir(src):
            continue
        dst = os.path.join(DEST, folder)
        os.makedirs(dst, exist_ok=True)
        for name in sorted(os.listdir(src)):
            s = os.path.join(src, name)
            if not os.path.isfile(s):
                continue
            d = os.path.join(dst, name)
            if (not os.path.exists(d)) or os.path.getmtime(s) > os.path.getmtime(d):
                shutil.copy2(s, d)
                copied += 1
    print(f"  staged {copied} file(s) into assets/docs/")


def previews():
    made = 0
    for folder in sorted(os.listdir(DEST)):
        src = os.path.join(DEST, folder)
        if folder.startswith("_") or not os.path.isdir(src):
            continue
        pdir = os.path.join(PREV, folder)
        os.makedirs(pdir, exist_ok=True)
        for name in sorted(os.listdir(src)):
            if not name.lower().endswith(".pdf"):
                continue
            stem = os.path.splitext(name)[0]
            png = os.path.join(pdir, stem + ".png")
            if os.path.exists(png) and os.path.getmtime(png) > os.path.getmtime(os.path.join(src, name)):
                continue
            subprocess.run(
                ["pdftoppm", "-f", "1", "-l", "1", "-r", "36", "-png", "-singlefile",
                 os.path.join(src, name), os.path.join(pdir, stem)],
                check=False, capture_output=True)
            if os.path.exists(png):
                made += 1
    print(f"  rendered {made} preview(s)")


# ------------------------------------------------------------- 2. library ---
def library():
    items = []
    counts = {}
    for key, title, blurb in FOLDERS:
        src = os.path.join(DEST, key)
        if not os.path.isdir(src):
            counts[key] = 0
            continue
        groups = {}
        for name in sorted(os.listdir(src)):
            p = os.path.join(src, name)
            if not os.path.isfile(p):
                continue
            stem, ext = os.path.splitext(name)
            ext = ext.lstrip(".").upper()
            if ext == "JPEG":
                ext = "JPG"
            groups.setdefault(stem, []).append((ext, name, os.path.getsize(p)))
        for stem in sorted(groups):
            t, d = pretty(stem)
            fmts = sorted(groups[stem], key=lambda f: FMT_ORDER.index(f[0]) if f[0] in FMT_ORDER else 99)
            formats = [{"ext": e, "path": f"assets/docs/{key}/{n}", "bytes": b} for e, n, b in fmts]
            prev_png = os.path.join(PREV, key, stem + ".png")
            preview = f"assets/docs/_prev/{key}/{stem}.png" if os.path.exists(prev_png) else None
            pdf = next((f for f in formats if f["ext"] == "PDF"), None)
            img = next((f for f in formats if f["ext"] in ("PNG", "JPG", "SVG")), None)
            kind = "pdf" if pdf else ("image" if img else ("office" if any(f["ext"] in OFFICE for f in formats) else "file"))
            items.append({
                "folder": key, "stem": stem, "title": t, "desc": d,
                "kind": kind, "preview": preview,
                "view": (pdf or img or formats[0])["path"],
                "formats": formats,
                "search": (stem + " " + t + " " + d + " " + FOLDER_TITLE[key]).lower(),
            })
        counts[key] = len([i for i in items if i["folder"] == key])
    folders = [{"key": k, "title": t, "blurb": b, "count": counts.get(k, 0)} for k, t, b in FOLDERS]
    total_bytes = sum(f["bytes"] for i in items for f in i["formats"])
    return {
        "generated": dt.date.today().isoformat(),
        "folders": folders,
        "items": items,
        "totals": {"documents": len(items),
                   "files": sum(len(i["formats"]) for i in items),
                   "megabytes": round(total_bytes / 1048576, 1)},
    }


# ---------------------------------------------------------------- 3. plan ---
INLINE = [
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
    (re.compile(r"\*\*([^*]+)\*\*"), r"<b>\1</b>"),
    (re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])"), r"<i>\1</i>"),
]
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
FLAGS = [("blocking", "\U0001F534"), ("deadline", "⚠"), ("cost", "\U0001F4B7"),
         ("both", "\U0001F465"), ("wait", "\U0001F550")]


def rich(s):
    s = html.escape(s.strip())
    s = LINK.sub(r'<a class="a-line" href="\2" target="_blank" rel="noopener">\1</a>', s)
    for pat, rep in INLINE:
        s = pat.sub(rep, s)
    return s


SYMS = re.compile("^(?:[\U0001F534\u26a0\ufe0f\U0001F4B7\U0001F465\U0001F550]\\s*)+")


def flags_of(s):
    return [k for k, sym in FLAGS if sym in s]


def strip_syms(s):
    return SYMS.sub("", s)


MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}

PHASES = [
    {"key": "setup", "name": "Setup", "sub": "Tue 1 – Sun 13 September",
     "note": "Thirteen days, and the first day either of you works on this. Two items have waiting periods and both start on day one."},
    {"key": "m1", "name": "Month 1 — Launch", "sub": "Days 1–30",
     "note": "Publish, and start talking to people. Thirty days of content, and the outbound rhythm begins."},
    {"key": "m2", "name": "Month 2 — Build", "sub": "Days 31–60",
     "note": "Two things usually happen this month: AML supervision lands, and the first clients arrive."},
    {"key": "m3", "name": "Month 3 — Convert", "sub": "Days 61–90",
     "note": "The November deadline, then the seasonal run into January. The first real numbers to judge it on."},
]


def parse_plan():
    path = os.path.join(DOCS_MD, "16-day-by-day-plan.md")
    lines = open(path, encoding="utf-8").read().split("\n")
    days, cur, phase = [], None, "setup"
    hard, in_hard = [], False

    def flush():
        nonlocal cur
        if cur:
            days.append(cur)
            cur = None

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("## Month 1"):
            flush(); phase = "m1"; continue
        if line.startswith("## Month 2"):
            flush(); phase = "m2"; continue
        if line.startswith("## Month 3"):
            flush(); phase = "m3"; continue
        if line.startswith("# The hard dates"):
            flush(); in_hard = True; continue
        if in_hard:
            m = re.match(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", line)
            if m and "---" not in m.group(1) and m.group(1) != "Date":
                hard.append({"when": rich(m.group(1)), "day": m.group(2).strip("* "),
                             "what": rich(m.group(3))})
            continue
        if line.startswith("### "):
            head = line[4:]
            mday = re.match(r"^Day (\d+)\s+—\s+(.+)$", head)
            msetup = re.match(r"^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s+(\d+)\s+September\b(.*)$", head)
            if not (mday or msetup):
                flush(); continue
            bits = [b.strip() for b in head.split("·")]
            hours = next((b.replace("⏱", "").strip() for b in bits if "⏱" in b), "")
            meta = [rich(b) for b in bits[1:] if "⏱" not in b]
            flush()
            if mday:
                n = int(mday.group(1))
                date = D.day(n)
                cur = {"n": n, "phase": phase, "date": date.isoformat(),
                       "weekday": date.strftime("%a"), "label": f"Day {n}",
                       "long": D.fmt(date), "hours": hours, "meta": meta,
                       "one": "", "tasks": [], "notes": [], "flags": []}
            else:
                date = dt.date(2026, 9, int(msetup.group(2)))
                assert date.strftime("%A") == msetup.group(1), f"weekday mismatch {head}"
                cur = {"n": None, "phase": "setup", "date": date.isoformat(),
                       "weekday": date.strftime("%a"), "label": date.strftime("%a %-d %b"),
                       "long": D.fmt(date), "hours": hours, "meta": meta,
                       "one": "", "tasks": [], "notes": [], "flags": []}
            continue
        if cur is None:
            continue
        if not line.strip():
            continue
        m1 = re.match(r"^\*\*One thing:\*\*\s*(.+)$", line)
        if m1:
            body = m1.group(1)
            cur["flags"] = sorted(set(cur["flags"]) | set(flags_of(body)))
            cur["one"] = rich(strip_syms(body)); continue
        mt = re.match(r"^(\d+)\.\s+(.+)$", line)
        if mt:
            body = mt.group(2)
            fl = flags_of(body)
            cur["flags"] = sorted(set(cur["flags"]) | set(fl))
            cur["tasks"].append({"t": rich(strip_syms(body)), "flags": fl}); continue
        if line.startswith(">"):
            cur["notes"].append(rich(line.lstrip("> ").strip())); continue
        if cur["tasks"] and line.startswith("   "):
            cur["tasks"][-1]["t"] += " " + rich(line)
            continue
        cur["notes"].append(rich(line))
    flush()

    setup_days = [d for d in days if d["phase"] == "setup"]
    numbered = [d for d in days if d["n"]]
    assert len(numbered) == 90, f"expected 90 numbered days, parsed {len(numbered)}"
    assert len(setup_days) == 13, f"expected 13 setup days, parsed {len(setup_days)}"

    milestones = [
        {"date": D.SETUP_START.isoformat(), "title": "Setup starts",
         "note": "ICB practice licence application in, Google Business Profile claim started. Nothing is scheduled before this day."},
        {"date": dt.date(2026, 9, 29).isoformat(), "title": "AML supervision expected",
         "note": "28 days after the ICB application. Nothing revenue-generating happens before it lands."},
        {"date": D.LAUNCH.isoformat(), "title": "Launch — Day 1",
         "note": "The anchor post goes out, and the ninety days start."},
        {"date": dt.date(2026, 10, 13).isoformat(), "title": "End of Month 1",
         "note": "Day 30. First month of content published, outbound rhythm established."},
        {"date": dt.date(2026, 11, 7).isoformat(), "title": "MTD quarterly update due",
         "note": "The biggest date in the window. 7 November is a Saturday, so work to Friday 6 November."},
        {"date": dt.date(2026, 11, 12).isoformat(), "title": "End of Month 2",
         "note": "Day 60. Supervision and first clients usually land inside this month."},
        {"date": D.DAY90.isoformat(), "title": "Day 90",
         "note": "Full re-score against what actually happened."},
    ]
    return {
        "generated": dt.date.today().isoformat(),
        "anchors": {"setupStart": D.SETUP_START.isoformat(), "setupEnd": D.SETUP_END.isoformat(),
                    "launch": D.LAUNCH.isoformat(), "day90": D.DAY90.isoformat()},
        "phases": PHASES, "days": days, "milestones": milestones, "hardDates": hard,
        "legend": [{"k": "blocking", "sym": "\U0001F534", "label": "Blocking"},
                   {"k": "deadline", "sym": "⚠", "label": "Hard deadline"},
                   {"k": "cost", "sym": "\U0001F4B7", "label": "Costs money"},
                   {"k": "both", "sym": "\U0001F465", "label": "Needs both founders"},
                   {"k": "wait", "sym": "\U0001F550", "label": "Waiting period"}],
    }


# ------------------------------------------------------- 4. business plan ---
def parse_bplan():
    from docx import Document
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    src = os.path.join(OUT, "02_Business_Plan", "Klyara_Business_Plan.docx")
    doc = Document(src)
    imgdir = os.path.join(DEST, "02_Business_Plan", "figures")
    os.makedirs(imgdir, exist_ok=True)
    for f in os.listdir(imgdir):
        os.remove(os.path.join(imgdir, f))

    sections, cur, cover, seen = [], None, [], {}

    def add(block):
        (cur["blocks"] if cur else cover).append(block)

    def size(p):
        for r in p.runs:
            if r.font.size:
                return round(r.font.size.pt, 1)
        return None

    for child in doc.element.body.iterchildren():
        tag = child.tag.split("}")[-1]
        if tag == "tbl":
            t = Table(child, doc)
            rows = [[c.text.strip() for c in r.cells] for r in t.rows]
            if len(rows) == 1 and len(rows[0]) == 1:
                # docxkit renders a callout as a one-cell table: title on line 1, body after
                lines = [l.strip() for l in rows[0][0].split("\n") if l.strip()]
                if lines:
                    add({"t": "callout", "title": rich(lines[0]),
                         "body": [rich(l) for l in lines[1:]]})
            elif rows:
                add({"t": "table", "head": rows[0], "rows": rows[1:]})
            continue
        if tag != "p":
            continue
        p = Paragraph(child, doc)
        blips = re.findall(r'r:embed="([^"]+)"', child.xml)
        if blips:
            rid = blips[0]
            if rid not in seen:
                part = doc.part.related_parts[rid]
                ext = os.path.splitext(part.partname)[1] or ".png"
                name = f"fig-{len(seen)+1:02d}{ext}"
                open(os.path.join(imgdir, name), "wb").write(part.blob)
                seen[rid] = name
            add({"t": "figure", "src": f"assets/docs/02_Business_Plan/figures/{seen[rid]}", "cap": ""})
            continue
        txt = p.text.strip()
        if not txt:
            continue
        sz = size(p)
        style = p.style.name
        if sz == 21.0:
            m = re.match(r"^(\d+)\.\s+(.*)$", txt)
            cur = {"n": int(m.group(1)) if m else len(sections) + 1,
                   "title": m.group(2) if m else txt, "blocks": []}
            sections.append(cur)
            continue
        if sz == 14.5:
            add({"t": "h3", "x": rich(txt)}); continue
        if sz == 7.5:
            tgt = (cur["blocks"] if cur else cover)
            if tgt and tgt[-1]["t"] == "figure":
                tgt[-1]["cap"] = rich(txt)
            else:
                add({"t": "cap", "x": rich(txt)})
            continue
        if style in ("List Bullet", "List Number"):
            tgt = (cur["blocks"] if cur else cover)
            if tgt and tgt[-1]["t"] == "list" and tgt[-1]["ord"] == (style == "List Number"):
                tgt[-1]["items"].append(rich(txt))
            else:
                add({"t": "list", "ord": style == "List Number", "items": [rich(txt)]})
            continue
        lead = bool(p.runs and p.runs[0].font.bold)
        add({"t": "p", "x": rich(txt), "lead": lead})

    files = []
    for name in sorted(os.listdir(os.path.join(DEST, "02_Business_Plan"))):
        fp = os.path.join(DEST, "02_Business_Plan", name)
        if os.path.isfile(fp) and name.startswith("Klyara_Business_Plan"):
            files.append({"ext": os.path.splitext(name)[1].lstrip(".").upper(),
                          "path": f"assets/docs/02_Business_Plan/{name}",
                          "bytes": os.path.getsize(fp)})
    nfig = sum(1 for s in sections for b in s["blocks"] if b["t"] == "figure")
    ntab = sum(1 for s in sections for b in s["blocks"] if b["t"] == "table")
    return {"generated": dt.date.today().isoformat(), "cover": cover,
            "sections": sections, "downloads": files,
            "stats": {"sections": len(sections), "figures": nfig, "tables": ntab}}


# --------------------------------------------------------------- 5. write ---
def write(name, glob, payload):
    os.makedirs(DATA, exist_ok=True)
    j = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(DATA, name + ".json"), "w", encoding="utf-8").write(j)
    open(os.path.join(DATA, name + ".js"), "w", encoding="utf-8").write(
        f"/* generated by build-admin.py — file:// fallback for {name}.json */\n"
        f"window.{glob}={j};\n")
    print(f"  wrote assets/data/{name}.json  ({len(j)/1024:.0f} KB)  + .js shim")


def main():
    print("staging deliverables …")
    stage()
    previews()
    print("building indexes …")
    write("library", "KLY_LIBRARY", library())
    write("plan", "KLY_PLAN", parse_plan())
    write("bplan", "KLY_BPLAN", parse_bplan())
    print("done.")


if __name__ == "__main__":
    main()
