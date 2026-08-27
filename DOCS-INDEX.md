# klyara-web

Working repo for Klyara — Cloudflare Worker and the full documentation set.

The **website source** lives in [`keypascal/Klyara-WebSite`](https://github.com/keypascal/Klyara-WebSite)
and is not mirrored here on purpose: two copies of 457 site files in two repos drift apart within a
week. This repo holds the things the site repo does not.

| Folder | Contents |
|---|---|
| `worker/` | Cloudflare Worker (to be added) |
| `marketing/` | 24 launch, SEO, pricing, sales and ops documents |
| `build/` | Klyara Build Manual & Business Plan |
| `app/` | Client portal decision, app build plan, Lovable prompt |
| `misc/` | Content generator script, Craig intake notes |
| `uni/` | Klyara Uni — the internal handbook, live at `klyara.com/uni` |

---

## marketing/

**Start with `Klyara_Launch_Pack_START_HERE.md`, then `Klyara_90_Day_Plan.md`.**

### Plan and running order
- `Klyara_Launch_Pack_START_HERE.md` — index of the whole pack, what's built, what's outstanding
- `Klyara_90_Day_Plan.md` — everything sequenced across 90 days with owners and decision gates
- `Klyara_Day_By_Day_90_Days.md` — every day dated and timed, with a "one thing" per day
- `Klyara_Day_By_Day_90_Day_Plan.md` — earlier revision of the above, kept for reference
- `Klyara_What_I_Need_From_You.md` — the 30 decisions that need Key, grouped into one working session

### Content and channels
- `Klyara_Channel_Map.md` — every platform, subreddit, forum and directory ranked by return per hour
- `Klyara_Account_Setup_Pack.md` — copy-paste profile fields for 14 platforms, to exact character limits
- `Klyara_Content_Calendar_30day.md` — 30 dated days, full copy for every channel
- `Klyara_GBP_Year_Of_Posts.md` — 52 Google Business Profile posts tied to the deadline calendar
- `Klyara_Email_Programme.md` — provider decision, deliverability DNS, sequences, a year of newsletters
- `Klyara_Video_Pack.md` — vertical video set, YouTube scripts, Shorts extraction plan
- `Klyara_Answer_Bank.md` — 22 pre-written community answers for Reddit, forums and Facebook groups

### Search and site
- `Klyara_SEO_Schema_Pack.md` — paste-ready JSON-LD, titles and meta, keyword clusters
- `Klyara_Website_Audit.md` — audit of klyara.com; read the CRITICAL section first
- `Klyara_Guildford_Local_Pack.md` — Guildford & Surrey local pages, citations, partnerships, press

### Money
- `Klyara_Pricing_Scope_and_Quoting.md` — what's in and out of each tier, rate card, scope-creep script
- `Klyara_Competitor_Price_Benchmark.md` — sourced UK market prices, gathered 26 Aug 2026
- `Klyara_Sales_Pack.md` — discovery call script, diagnostic questions, ten objections answered
- `Klyara_Outreach_and_Partners.md` — LinkedIn and cold-email sequences, phone scripts, partner terms

### Running it
- `Klyara_Ops_Playbook.md` — weekly rhythm, UTM scheme, ads, press, review engine
- `Klyara_Client_Onboarding_Pack.md` — signed-to-live runbook, onboarding emails, monthly rhythm
- `Klyara_Brand_Guidelines.md` — colour, type, the mark, layout, voice
- `Klyara_Market_Intelligence.md` — verified compliance facts, market size, competitors, and what is unverified
- `Klyara_Risk_Register.md` — the fourteen things that actually kill this, scored

## build/

- `Klyara_Build_Manual_v3_3.md` — Build Manual & Business Plan (v3)
- `Klyara_Build_Manual_v3_2.md` — byte-identical to v3_3; the same content was saved twice under two
  version names. Kept so the repo mirrors the project rather than silently dropping a path.

## app/

- `Klyara_Portal_Platform_Decision.md` — client portal platform decision
- `Klyara_App_Build_Plan.md` — app build plan
- `Lovable_Prompt_1.md` — Lovable build prompt

## uni/

Klyara Uni — the internal handbook. This folder is the only copy. Behind Cloudflare Access since 27 August 2026.

- `index.html` — the front door: what is in the Uni, what is coming, how to add a guide
- `portal-build-playbook.html` — guide 01. The client portal at app.klyara.com: the whole stack,
  how the site and the app connect, Lovable versus building it ourselves, running costs, Direct
  Debit versus cards, and the route into the app stores. Nine chapters, interactive
- `portal-platform-decision.md` — guide 02. The written decision record (same file as
  `app/Klyara_Portal_Platform_Decision.md`)
- `portal-user-guide.html` — guide 03. For clients: getting in, installing it on a phone,
  sending a receipt, what the status labels mean, what to do when something goes wrong
- `portal-admin-guide.html` — guide 04. For Craig: the morning routine, onboarding a client,
  the receipt inbox address per platform, publishing, troubleshooting, and the rules

## misc/

- `content4.py` — content generator script
- `Craig_First_Info.md` — Craig intake notes, converted from the original .docx

---

## Notes

- Source of truth for all of the above is the **klyara.com Claude project**. This repo is the backup
  and the version history; edits made here do not flow back to the project automatically.
- The two build-manual PDFs in the project (`KlyaraBuildManualv2.pdf`, `KlyaraBuildManualv3.pdf`) are
  not in this repo — binaries could not be transferred over the current link. v3 is covered by the
  markdown in `build/`; v2 has no markdown equivalent.
