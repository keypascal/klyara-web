> **Historical document — written 24 August 2026, before the app existed.** Kept for its business
> strategy, its pricing reasoning and its compliance timeline, which all still stand. Its technical and
> hosting decisions do **not**: klyara.com is not WordPress on a Fasthosts package (it is a static site
> served by a Cloudflare Worker), and the client portal was not built in Lovable and does not sit on
> Netlify (it is React + Supabase on Cloudflare Pages). For anything about how the site or the app
> actually works, the current sources of truth are `05_Website/HANDOVER.md` for the website and
> `12_App/klyara-portal/HANDOVER.md` for the app.
>
> Launch anchor has since moved to **Monday 14 September 2026** (setup Tuesday 1 – Sunday 13 September
> 2026; Day 90 is Saturday 12 December 2026). "Day 0" in Part 8 below means 24 August 2026, not launch day.

# Klyara — Build Manual & Business Plan (v3)

*Supersedes v2. Prices and rules verified August 2026. Read Part 0 first — it lists everything v2 got wrong or missed.*

---

## PART 0 — WHAT CHANGED FROM v2 (the gap audit)

### Things v2 missed entirely

1. **Making Tax Digital for Income Tax is LIVE (April 2026) — and v2 never mentions it.** This is the biggest miss in the document. Sole traders and landlords with qualifying income over £50,000 must now keep digital records and file quarterly updates via MTD software. The threshold drops to **£30,000 in April 2027** and **£20,000 in April 2028**. Gross income counts — a subbie invoicing £55k who takes home £44k after CIS deductions is in scope. This is (a) a compliance obligation Klyara must service, (b) the single best marketing hook available ("HMRC now wants your figures every quarter — we handle it"), and (c) a structural gift: quarterly filing makes monthly bookkeeping *mandatory-adjacent* instead of optional. The April 2027 £30k wave is a pre-built pipeline of panicking subcontractors. New product tier added (Part 4).

2. **HMRC Agent Services Account (ASA) + client authorisations.** v2's compliance table stops at AML registration. But to actually file VAT returns, MTD ITSA updates, or run CIS as an agent, Klyara needs an **Agent Services Account — which itself requires AML supervision to be in place first**, plus per-client authorisation (64-8 / digital handshake). The real critical path is: **AML supervision → ASA → client authorisations → file anything.** Each link adds days-to-weeks. Now sequenced in Part 8.

3. **Founders' agreement.** Two founders, no shareholders' agreement, no equity split on paper, no IP assignment, no leaver provisions. This kills more small companies than competition does. One-page heads of terms in week 1, proper shareholders' agreement before client 5. Cover: split, vesting/leaver terms, who owns the code and brand, deadlock, drag/tag.

4. **Operating AML compliance, not just registering.** MLR 2017 requires a written firm-wide risk assessment, documented policies & procedures, client due diligence (ID checks) on every client, and ongoing monitoring. HMRC inspects. v2 treats AML as a registration fee; it's an operating discipline. Per-client ID verification tooling needed from client 1.

5. **Companies House identity verification (ECCTA).** Directors must verify identity with Companies House — mandatory for new directors since Nov 2025; existing directors must verify by their next confirmation statement (deadlines running through autumn 2026). Both founders do this in week 1. Free, fast, blocks filings if ignored.

6. **Klyara's own VAT registration.** Not addressed in v2. Decision: **register voluntarily from day 1.** Clients are VAT-registered businesses who reclaim it, so there's zero price friction, and Klyara reclaims input VAT on the whole software stack. Quote all prices ex-VAT.

7. **Onboarding fees.** v2's pricing has no setup fee. Every new client arrives with months of catch-up mess. Charge a one-off **onboarding/catch-up fee (£250–£750** depending on backlog; Solo's onboarding was later set at £149), positioned as "we clean up the past so the monthly fee only covers the future." This is standard practice and pure margin protection.

8. **Continuity cover for Craig.** Single fee-earner. PI insurers and professional bodies expect a continuity arrangement (a named practitioner who steps in if Craig is hit by a bus/scaffold). Solve via the local-accountant partnership (#23) — make continuity mutual and written.

9. **Email deliverability & domain hygiene.** SPF, DKIM, DMARC on klyara.com from day 1 or the invoice-chasing emails land in spam. **Cold outreach goes from a separate domain** (e.g. tryklyara.com) so the main domain's reputation is never burned. Password manager + MFA on every service; registrar lock on the domain.

10. **Data protection operations.** ICO fee is in v2, but not: privacy notice, data processing terms in the engagement letter, subprocessor list (Supabase — **choose the EU/UK region at project creation, it can't be moved later** — Dext, Brevo, Intuit), retention policy, breach procedure. One afternoon of documents; I'll draft.

11. **Trademark/name check.** Search the UK IPO register for "Klyara" conflicts in classes 35/36 before spending on brand. £170 to file if clear. Cheap insurance on the whole identity.

### Things v2 got materially wrong (numbers corrected)

| Item | v2 said | Reality (Aug 2026) | Consequence |
|---|---|---|---|
| QBO ProAdvisor wholesale | ~30% off | **UK "bill my firm" = 50% off ongoing** (Intuit UK accountant plans page) | Margin per Essentials client ≈ **£16/mo**, not £10. Better than modelled. |
| AML cost | "~£300+/yr" | **£300 application + £400/premises/yr + £40 approval per tested person ≈ £740 year 1**, ~£400/yr after | Budget it properly. Small-business (<£5k turnover) waiver won't apply for long. |
| Fasthosts reseller | "a few £/mo" | **~£50/mo + VAT after the 6-month free intro** | Reseller account only pays if hosting resale is real. Decision below. |
| Dext | "~£24/mo retail, partner cheaper" | Practice pricing is per-client, ≈ **£8/client/mo** at the 50-client tier (£391/mo for 50), and the entry tiers are chunky for a 3-client firm. Dext killed unlimited plans in 2023. | Don't start on Dext. Decision below. |
| Hey Jodie retail | "resell £49–£99" | Jodie sells **direct to the public at £49/mo unlimited**. White-label partners price **£80–£120/mo** (£50–£80 margin on wholesale). | You cannot retail at £49 — that's Jodie's own price. Klyara price: **£79/mo** (bundled value: it's inside the portal, wired to the Klyara number, backed by a human who knows their business). |
| QBO payroll | Assumed outsourced bureau only | **QBO Advanced Payroll (£8/mo + £1/employee) handles CIS payroll**, and ProAdvisors get payroll discounts + a free Payroll Core sub for the firm | Simple PAYE/CIS payrolls can run in-house on QBO at trivial cost. Bureau only for complexity/BACS. Better margin, fewer moving parts. |

### Decisions committed (v2 left these open — v3 closes them)

- **Receipt capture at launch: QBO's built-in receipt snap (free) via the Klyara portal flow.** Adopt Dext only when client count/complexity justifies ~£8/client — likely around client 10–15. The portal-first architecture (Part 2) makes the back-end swappable; clients never notice.
- **Hosting: skip the Fasthosts reseller account at launch.** One ordinary hosting package for klyara.com (~£5–£10/mo). Open the reseller account the week the **first care-plan client signs** — the 6-month free intro then covers the ramp instead of burning during the pre-revenue build.
- **Vendasta: killed.** ~$500+/mo platform cost, USD pricing, and it solves a problem (vendor sprawl) you don't have at <25 clients. The stitched stack in this doc is cheaper and you own every relationship. Revisit at 40+ clients if ops drag.
- **Xero: supported from day 1 for inbound clients, standardise new clients on QBO.** Many builders arrive already on Xero; refusing them is throwing money away. Xero partner programme is free; Craig learns both. (v2 deferred this to month 4–6 — wrong, it's a day-1 sales objection.)
- **AML route: join ICB or AAT (Craig's choice by qualification fit) and get supervised via the body**, rather than naked HMRC MLR registration. Costs are similar all-in, but the body brings: practice licence credibility, template policies/risk assessments (solves gap #4 above), CPD, a letters/engagement library, and continuity-arrangement framework. Fall back to direct HMRC registration only if membership timelines are worse.
- **Payroll: QBO Advanced Payroll in-house for standard PAYE+CIS; get one bureau quote (Bookd) as overflow/backup only.**

---

## PART 1 — STRATEGY

Unchanged in essence from v2 — the back office for small builders; bookkeeping is the wedge; Craig's CIS/reverse-charge specialism is the moat; add-ons attach at near-zero CAC — **with one upgrade:**

**MTD is now the front door.** The pitch order changes:

1. **"Over £50k self-employed? HMRC wants quarterly digital updates — now."** (live since April 2026)
2. **"Under £50k? You're in from April 2027 at £30k."** (book them now at a founding rate)
3. Then the classic pains: CIS/reverse charge, late payment, missed calls, no web presence.

MTD converts bookkeeping from a "nice to have" into a legal requirement with a deadline. No competitor messaging needed — HMRC does the fear marketing for free. Every piece of content, every ad group, every merchant-noticeboard card leads with it.

Target client unchanged: 5–20-person construction firm, PAYE + CIS mix, VAT-registered, local — **plus a new secondary segment: sole-trader subbies over the MTD threshold** (high volume, low touch, serviced by a productised tier — Part 4).

---

## PART 2 — ARCHITECTURE

| Layer | What | Built with | Cost | Notes |
|---|---|---|---|---|
| Marketing site | klyara.com | WordPress on a standard Fasthosts package | ~£5–£10/mo | Reseller account deferred (Part 0) |
| Client portal | Login, reports, receipt upload, add-on store | Lovable + Supabase (**EU/UK region**) | ~£25/mo + Supabase free→$25 | GitHub sync ON day 1 |
| Books | Bookkeeping engine | QuickBooks Online Accountant | Free portal; **50% off** bill-my-firm wholesale | + Xero partner (free) for inbound Xero clients |
| MTD ITSA filing | Quarterly updates for sole traders | QBO Sole Trader (HMRC-recognised for MTD ITSA) | £10 list → £5 wholesale | The Solo tier engine |
| Receipt capture | Photo/email → books | **QBO receipt snap at launch** → Dext later | £0 → ~£8/client | Portal is the front; back-end swappable |
| Payroll + CIS | PAYE + CIS processing | **QBO Advanced Payroll** | £8/mo + £1/employee (less ProAdvisor discount) | Bureau (Bookd) as backup only |
| Comms/chasing | Reminders, email/SMS | Brevo free tier + QBO reminders | £0→£15/mo | SPF/DKIM/DMARC before first send |
| Booking | Discovery calls | Cal.com | Free | |
| Email (ours) | @klyara.com | Zoho Mail free / Fasthosts mailboxes | £0–£5/mo | Never self-host mail |
| Outreach domain | Cold email | tryklyara.com (or similar) | ~£10/yr | Protects main domain reputation |
| Security | All services | Bitwarden + MFA everywhere + registrar lock | £0–£3/mo | Non-negotiable — you hold clients' financial data |

Receipt flow (v3): builder snaps receipt in the Klyara portal → Supabase → forwarded into QBO receipt capture (or the client's Dext inbox once Dext is adopted) → Craig reviews. Client sees Klyara everywhere. Identical UX either way — that's the point of owning the portal.

---

## PART 3 — SERVICE CATALOGUE (updated numbers only; v2's links remain valid)

**Layer A — Financial core**

1. **Bookkeeping / VAT / CIS / management reports — Own.** QBO UK list (ex-VAT): Sole Trader £10 · Simple Start £16 · Essentials £33 · Plus ~£47–£56 · Advanced ~£115+. **Bill-my-firm = 50% off ongoing** → Essentials costs you ~£16.50, worth £33+ inside the package → **~£16/mo software margin per client** before service fees. Intuit runs 50–75%-off new-customer promos — time client onboarding to them where possible. Craig does ProAdvisor certification week 1 (free, ~a day, Find-a-ProAdvisor listing = inbound leads).
2. **MTD ITSA quarterly filing — Own. NEW.** QBO Sole Trader plan per client (~£5 wholesale). Four quarterly updates + end-of-year final declaration. Productised, templated, high volume. This is the Solo tier (Part 4).
3. **Receipt capture — Own→WL.** QBO snap free now; Dext at ~£8/client when volume justifies (~client 10–15).
4. **Payroll + CIS — Own (QBO Advanced Payroll) with bureau backup.** In-house cost per client ≈ £8 + £1/head, less discount. Charge £5–£8/payslip as before → margin now lands with Klyara instead of a bureau. Bookd quote on file as overflow. Never hold client money; BACS via client's own bank or bureau.

**Layer B — Digital** (4–8 in v2): unchanged in structure. Corrections: hosting resold at £10–£20/mo/site *once the reseller account opens* (trigger: first care-plan client); care plans £29–£59/mo remain the recurring gold; SEO/GBP retainers £149–£399/mo; "Google Ready" £249 one-off stays the first digital upsell.

**Layer C — AI** (10–16 in v2): structure unchanged. Corrections: **AI receptionist retails at £79/mo** (Jodie's own direct price is £49 — Klyara's version is bundled into the number, the portal, and a human relationship; agency partners typically charge £80–£120, so £79 is the aggressive end of normal). Human answering, chatbot (£29–£59/mo), reviews (£39–£79/mo), content (£99–£179/mo — revised down from £99–£249), video (£149–£399/ea) all stand. Invoice chasing stays free inside Trade/Pro — it's the stickiest feature in the stack and costs ~£0.

**Layer D — Referral** (17–23 in v2): all stand. Guardrails tightened:
- **Insurance:** introducer status only — pass name and contact details, *never* advise, recommend a specific policy, or help complete proposals. Cross that line and it's FCA-regulated activity. Script it: "I'll have [broker] call you — they know 10-man CIS firms."
- **Energy:** introducer, not TPI/broker — same as v2.
- **Finance (Bibby construction finance, Team Factors, Nucleus):** business lending intros are non-regulated; still the highest-value referral in the stack because the books tell you who needs it before they know.
- **Year-end accountant partnership:** now also carries the **continuity arrangement** (Part 0 #8) — mutual, in writing, alongside the 10–15% two-way referral fee.

---

## PART 4 — KLYARA PRICING (v3)

**New tier at the bottom, onboarding fee across the board, AI in every tier.**

| | **Klyara Solo** £59/mo *(NEW)* | **Klyara Start** £99/mo | **Klyara Trade** £199/mo | **Klyara Pro** £329/mo |
|---|---|---|---|---|
| Who | Sole-trader subbie, MTD-mandated | Micro Ltd, simple books | The 5–15-person firm (the target) | VAT+CIS complexity, wants it all handled |
| Bookkeeping + reconciliation | Light-touch quarterly | ✓ monthly | ✓ | ✓ |
| **MTD ITSA quarterly filing** | ✓ (the product) | — | — | — |
| Receipt capture app | ✓ | ✓ | ✓ | ✓ |
| P&L | Quarterly | Monthly | Monthly + balance sheet | Full management pack |
| VAT | — | — | ✓ + return prep | ✓ + return prep |
| CIS | Deduction tracking | — | ✓ bookkeeping | ✓ returns + verification |
| Invoice chasing (AI) | — | — | ✓ | ✓ |
| Business phone number | — | — | — | ✓ |
| Client portal | ✓ | ✓ | ✓ | ✓ + priority |
| **Onboarding fee (one-off)** | £149 | £250 | £350–£500 | £500–£750 |

Solo economics: ~£5 software cost, templated quarterly workflow, maybe 1–1.5 hrs/quarter once set up → ~£54/mo margin at scale, and every Solo client is a future Start/Trade client the day they go Ltd or hire. **April 2027 (£30k threshold) is the Solo land-grab — start the waitlist now at a locked founding rate.**

Add-on menu: AI receptionist **£79** · human answering per-call · payroll £5–£8/payslip · website £499+ build, £29–£59/mo care · SEO £149–£399/mo · chatbot £29–£59/mo · reviews £39–£79/mo · content £99–£179/mo (revised from £99–£249) · video £149–£399/ea · email £3–£5/mailbox · Layer D free to the client.

Pricing mechanics: three visible tiers (Solo advertised separately to its segment); Trade engineered as the obvious middle; annual = 1 month free via GoCardless DD (~1% capped); **annual price-review clause in the engagement letter**; **late-records surcharge** (records after the 10th = £25 — makes the deadline real); everything quoted **ex-VAT** (Klyara VAT-registered day 1).

Worked example, Trade client at month 12: £199 core + £79 receptionist + £39 care plan + £16 QBO margin + £5 phone commission + £8 insurance renewal + ~£20 amortised finance referral ≈ **£366/mo**. Ten Trade-grade clients ≈ £3.6k MRR on ~£600 costs. Twenty Solos on top ≈ +£1.2k MRR for ~2 days/quarter of templated work.

---

## PART 5 — COMPLIANCE (rebuilt — this is the real critical path)

**The chain: professional body / AML supervision → Agent Services Account → per-client authorisation → file. Nothing revenue-generating happens until the first link closes. Start it today.**

| # | Item | Detail | Cost | Time |
|---|---|---|---|---|
| 1 | **AML supervision** | Preferred: ICB or AAT membership + practice licence (brings template policies, risk assessment, engagement letters, continuity framework). Fallback: HMRC MLR direct — £300 application + £400/premises/yr + £40/person approval test | ~£400–£740 yr 1 either route | **Weeks — the critical path.** No bookkeeping-by-way-of-business until supervised. Waitlist + deposits meanwhile. |
| 2 | **Agent Services Account** | Needed to file MTD VAT, MTD ITSA, and act as CIS agent. Requires AML supervision in place. Then authorise each client (64-8 / digital handshake) | Free | Days once AML done; bake client authorisation into onboarding checklist |
| 3 | **Firm-wide AML operations** | Written risk assessment, policies & procedures, CDD on every client (ID verification tool — e.g. via the professional body's partner or Credas/SmartSearch tier), ongoing monitoring, records | ~£1–£3/check | Templates from the body; I draft the risk assessment |
| 4 | **ICO registration** | Data protection fee | £40–£60/yr | Same day |
| 5 | **GDPR pack** | Privacy notice, engagement-letter data clauses, subprocessor list (Supabase EU/UK, Intuit, Brevo, later Dext), retention policy, breach procedure | Free (I draft) | One afternoon |
| 6 | **Company + ECCTA** | Klyara Ltd (SIC 69201 + 62012); **both directors complete Companies House identity verification** | £14.99 via Tide | Days; IDV is quick, mandatory |
| 7 | **Founders' agreement** | Heads of terms week 1 (split, vesting, IP assignment to the company, leaver, deadlock); full shareholders' agreement before client 5 | £0 now; ~£500–£1k solicitor later | Week 1 |
| 8 | **VAT registration (Klyara)** | Voluntary, day 1 — clients reclaim, Klyara reclaims input VAT on the stack | Free | Days |
| 9 | **Engagement letter** | v2/TradeCount letter redrafted: Klyara branding, portal/data clauses, agent-authorisation scope, price-review clause, late-records surcharge, 30-day notice | Free (I redraft) | Day 1–3 |
| 10 | **PI insurance** | Via the chosen broker partner; declare continuity arrangement | £15–£40/mo | Week 1–2 |
| 11 | **Continuity cover** | Written mutual arrangement with the partner accountant | Free | With #23 partnership |
| 12 | **Trademark check** | UK IPO search "Klyara" classes 35/36; file if clear | £170 | 1 hr search |
| 13 | Stances | VoIP = dealer, not provider-of-record · Energy = introducer, not TPI · Insurance = pure introducer (no advice) · PECR: B2B cold email with ID + opt-out, from the outreach domain · **Never hold client money** | — | — |

---

## PART 6 — BUILD RUNBOOKS

**6.1 Website — Day 1–3.** As v2 (WordPress, Kadence, Elementor, Rank Math, Fluent Forms, Cal.com, Wordfence) with changes: standard hosting package not reseller; **SPF/DKIM/DMARC configured before anything sends**; pages add **"Making Tax Digital for builders"** as a primary landing page alongside Bookkeeping & CIS. Blog seeds reordered — MTD first: "MTD for CIS subcontractors: what April 2026 changed" · "Earning £30k+? You're in MTD from April 2027" · then CIS explained, reverse charge, 5 reasons builders get paid late.

**6.2 Client portal (Lovable) — Day 2–5.** As v2 spec (Supabase auth + RLS, dashboard, receipt upload, docs, add-on store-as-enquiry). Additions: **create the Supabase project in the EU/UK region** (cannot be moved later); GitHub sync on before the first prompt; one small feature per prompt. Ship ugly by day 5.

**6.3 Receipt pipeline — Day 3.** Portal upload → Supabase → QBO receipt capture (→ Dext leg swapped in later). Test end-to-end with a real crumpled diesel receipt before calling it done.

**6.4 Brand — Day 1.** As v2 (navy/graphite + safety orange, heavy geometric sans, van-livery-legible mark) — *after* the 1-hour IPO trademark search.

**6.5 Onboarding runbook — NEW, before client 1.** Checklist per client: engagement letter e-signed → CDD/ID check → GoCardless mandate → QBO subscription added (bill-my-firm, during an Intuit promo if one's running) → agent authorisation submitted (VAT/CIS/ITSA as applicable) → portal login issued → receipt flow demoed on their phone → onboarding fee invoiced. Target: signed-to-live in 5 working days, blocked only by HMRC authorisation post.

---

## PART 7 — SALES & MARKETING

**7.1 The message hierarchy.** ① MTD deadline (fear + date) ② "Never do CIS returns again" ③ "Never miss a call from site" ④ "Get paid faster." Craig the construction specialist fronts everything.

**7.2 Google Ads (£500 credit — note these credits are match offers: spend ~£400 to receive £500; budget accordingly).** Structure as v2 (Search only, 10–15 mile radius, exact/phrase) with ad-group changes: ① "MTD for sole traders / MTD accountant [town]" — *new, likely cheapest CPC with highest urgency* ② "construction bookkeeper [town]" ③ "CIS accountant / CIS returns" ④ "bookkeeper for builders". Same negatives + add: xero login, quickbooks login, hmrc login. Landing pages: MTD ads → MTD page; everything else → Bookkeeping & CIS page. KPI: cost per booked call, £15–£40 acceptable.

**7.3 Free channels.** As v2 (GBP weekly, trade Facebook groups, merchant noticeboards, Checkatrade angle, Companies House SIC-code cold list at 20/day *from the outreach domain*, £50/£50 referral scheme, accountant partnership, reviews engine on Klyara itself) — plus: **HMRC's MTD comms do the awareness for you; ride every news cycle with a same-day GBP post and group comment.**

**7.4 Sales infrastructure — NEW.** Discovery-call script (I draft): current bookkeeping setup → MTD exposure check (income, structure) → CIS pain → phone/web quick audit → quote from the three tiers on the call. Proposal = one-page PDF + engagement letter e-sign + GoCardless link in a single email. Qualify out: sub-£20k hobbyists, anyone wanting credit, anyone who won't do DD.

---

## PART 8 — TIMELINE (resequenced around the compliance chain)

**Day 0 (TODAY)**
- ☐ **Start AML route: ICB/AAT membership application (Craig) — the critical path**
- ☐ ECCTA identity verification, both directors · ☐ Company formation if not done · ☐ VAT registration · ☐ ICO fee
- ☐ Founders' heads of terms (one page, signed)
- ☐ IPO trademark search → confirm klyara.com + buy outreach domain
- ☐ Order standard hosting; QBO Accountant sign-up; Craig starts ProAdvisor cert; Xero partner sign-up
- ☐ Lovable Pro; Supabase project **EU/UK region**
- ☐ Applications out in parallel: Tide, SumUp, VoIP dealer ×2, insurance introducer ×2, energy introducer, Bibby + Team Factors, Hey Jodie white-label demo, Time Assistant, Bookd (backup quote only)
- ☐ Brand direction (I deliver) · ☐ Target town → local-SEO copy

**Day 1–3** — WP live-ish; SPF/DKIM/DMARC; sitemap + Home + Bookkeeping/CIS + **MTD page** + Pricing copy (I deliver); GBP verification requested; Lovable auth + upload; engagement letter redrafted; GDPR pack drafted; onboarding checklist built.

**Day 4–7** — All pages live; portal MVP at app.klyara.com; Cal.com embedded; receipt pipeline tested end-to-end; Ads built and PAUSED; discovery script + proposal template done; first partner approvals land.

**Weeks 2–6** — AML/practice licence lands → **ASA created → first clients authorised → deliver**. Target 3–5 clients incl. 2+ Solo (fast, templated, testimonial-generating). Seed reviews → Ads ON. Hey Jodie white-label portal configured; first receptionist demo client. Solo waitlist campaign for the April 2027 £30k wave opens.

**Weeks 6–12** — Stripe checkout in the add-on store; payroll live on QBO Advanced Payroll; first website build + care plan → open Fasthosts reseller (6 free months start now, against real revenue); shareholders' agreement executed; 10-client target; kill/scale Ads on cost-per-booked-call.

---

## PART 9 — FINANCIAL MODEL

**9.1 Fixed monthly (lean launch, ex-VAT)**

| Item | £/mo |
|---|---|
| Hosting (standard) | £5–£10 |
| Lovable + Supabase | £25–£45 |
| Receipt capture | £0 (QBO) → £8/client when Dext adopted |
| SE Ranking + BrightLocal | ~£70 (defer BrightLocal until first SEO retainer — then ~£40 to start) |
| Brevo / misc / Bitwarden | £0–£18 |
| HeyGen + ElevenLabs (when video starts) | ~£25 |
| AML/body + ICO + PI amortised | ~£55–£75 |
| **Total** | **~£180–£245** |

**9.2 Break-even & targets.** Fixed costs covered by client 2 on Trade (or client 4 counting Solos). 10 mixed clients ≈ £2.5–£3.5k MRR; + 20 Solos ≈ +£1.2k. 25 full-service clients ≈ £7–£9k MRR with the referral book compounding underneath. Referral one-offs stay classified as acceleration fuel, not base plan. Onboarding fees ≈ £3–£5k of one-off cash across the first 10 clients — this funds the entire launch stack.

**9.3 KPIs (weekly, one page).** Booked calls · call→client conversion · MRR + add-on attach (≥1.5/client by month 3) · cost per booked call · **Solo waitlist size** (the 2027 pipeline) · onboarding cycle time (signed→live, target 5 days) · reviews count · churn (~0) · **hours/client/month** (capacity truth — see 9.4).

**9.4 Capacity — NEW.** Assume 3–5 hrs/client/mo full-service, ~1.5 hrs/quarter per Solo once templated. Craig solo ceiling ≈ **20–25 full-service equivalents**. Hire trigger: part-time bookkeeper at 15 confirmed clients (v2 said the same — but now it's derived, not asserted, and the weekly KPI watches it).

---

## PART 10 — RISKS & MITIGATIONS

| Risk | Mitigation |
|---|---|
| AML/practice-licence delay blocks launch | Started day 0; waitlist + deposits; build/marketing fill the wait; Solo waitlist monetises attention before delivery is legal |
| ASA/authorisation lag per client | In the onboarding checklist day 1 of each engagement; set client expectation ("HMRC's post takes a week") |
| Founder dispute | Heads of terms week 1, shareholders' agreement by client 5, IP assigned to the company |
| Craig single point of failure | Continuity arrangement with partner accountant, in writing; payroll on QBO not in Craig's head; documented runbooks per client |
| Scope creep (23 services, 2 people) | Month 1 sells only: Core tiers + AI receptionist + website + phone number. Everything else "coming soon" in the store |
| Partner quality burns brand | Trial every WL service on Klyara itself first; named backup per category |
| QBO price rises | 50% wholesale absorbs shocks; annual price-review clause passes the rest through |
| Intuit/Xero AI eats basic bookkeeping | Sell judgement + compliance + the relationship, not data entry; MTD/CIS complexity is exactly what auto-categorisation doesn't solve |
| Ads underperform | Kill fast at >£40/booked call; outbound + GBP + referrals are £0; revisit at 10+ reviews |
| Deliverability collapse from cold email | Separate outreach domain; main domain never sends cold |
| Local copycat | Speed + specialism + owning "construction back office [region]" and now "MTD for builders [region]" before it's a category |

---

## PART 11 — ROADMAP

**Now → next weekend:** everything in Part 8. My deliverables in order: ① brand options ② sitemap + Home/Bookkeeping-CIS/**MTD**/Pricing copy ③ Lovable build ④ engagement letter + GDPR pack + founders' heads of terms ⑤ discovery script + ad + outbound copy.

**Months 2–3:** add-on store with billing · payroll in-house · 10 clients · first website builds → reseller account opens · reputation engine on every client · shareholders' agreement signed.

**Months 4–6:** 25-client push · **Solo waitlist conversion sprint ahead of April 2027 (£30k threshold)** · Dext adoption decision at ~10–15 clients · part-time bookkeeper hire at 15 · VoIP dealer→white-label review only if commission book justifies billing ownership · Lovable PWA "add to home screen" (free) before any native-app talk.

**Months 6–12:** second territory, same playbook · "Klyara-in-a-box" onboarding productised · job-costing/quoting integration as add-on #24 · **April 2027: MTD £30k wave lands — the Solo pipeline converts** · year-1 target: 40–60 clients (mix full-service + Solo), £12–£20k MRR, referral book covering fixed costs several times over.

**18–24 months:** the default construction back office for the region — books at the core, portal opened daily, ten-plus attached services, compounding commission book, and a Solo base that upgrades itself to Ltd-company full-service clients on a conveyor.

---

## APPENDIX — MASTER SIGN-UP SHEET (v3 changes only; v2 sheet otherwise stands)

| Change | Detail |
|---|---|
| ICB — bookkeepers.org.uk / AAT — aat.org.uk | **NEW: AML supervision + practice licence route (preferred)** |
| HMRC Agent Services Account — gov.uk "create agent services account" | **NEW: required before any agent filing** |
| Companies House IDV — gov.uk "verify your identity Companies House" | **NEW: both directors, week 1** |
| UK IPO trademark search — gov.uk/search-for-trademark | **NEW: 1 hour, before brand spend** |
| QBO Advanced Payroll (in QBOA) | **Replaces bureau as default payroll**; Bookd = backup quote |
| Xero partner — xero.com/uk/partner-programmes | **NEW: day-1 sign-up, inbound Xero clients** |
| Dext | **Deferred** to ~10–15 clients; QBO receipt snap until then |
| Fasthosts reseller | **Deferred** until first care-plan client; standard package now |
| Vendasta | **Removed** |
| Hey Jodie white-label | Retail at **£79/mo** (their direct price is £49 — bundle, don't undercut yourself) |
| Everything else (VoIP, Tide, SumUp, insurance, energy, finance, GoCardless, Brevo, SE Ranking, BrightLocal, Time Assistant, Botsify/Stammer, Reviewly, HeyGen/ElevenLabs) | As v2 |

*Prices verified August 2026. Intuit, Dext and Fasthosts all reprice frequently — confirm at sign-up and time onboarding to promos.*
