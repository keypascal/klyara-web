# Klyara — Marketing Ops Playbook
### Tools, rhythm, measurement, and the things nobody put on the list
*Prepared 28 August 2026 · launch Monday 14 September 2026*

---

# 1. Scheduling tool — the decision

## Month 1: post manually. Buy nothing.

You have thirty days of content and roughly two posts a day. That is about fifteen minutes a day of
manual posting, and doing it by hand for a month teaches you things a scheduler hides: which platform
mangles line breaks, where hashtags actually go, what time your audience is awake, and which channels
are worth the effort at all.

Buying a scheduler in week one means paying to automate channels you haven't yet proved.

## Month 2 onward: Metricool, Starter tier.

**Why Metricool over Buffer, Publer or Hootsuite for Klyara specifically:**

It's the only mainstream scheduler that natively posts to **Google Business Profile** alongside
TikTok, Threads, Bluesky, Pinterest, YouTube, Instagram, Facebook and LinkedIn.

That matters because GBP is your highest-ROI channel and its posts expire after seven days — meaning
it needs posting *every week, forever*. A tool that can't schedule GBP leaves your single best
channel as a permanent manual chore, which is exactly the chore that stops happening in a busy month.

Everything else is secondary to that.

**The catch, stated plainly:** on Metricool, X/Twitter is a paid add-on above the plan price, and the
free tier excludes LinkedIn and X entirely. So budget the Starter plan plus, if you want it, the X
add-on. Expect roughly **£20–£28/month** all in. Against the Build Manual's £180–£245 fixed monthly
cost, that is proportionate for the channel that drives local search.

**Cheaper alternative if that's over budget:** schedule the eight channels Metricool's plan covers,
and post X manually. X is ten seconds a day and you post once. That saves the add-on entirely.

**Verify pricing at signup.** These figures come from a Buffer-published comparison — a competitor's
numbers about a competitor — and every tool in this category repriced in the last two years.

**Do not buy Hootsuite.** Enterprise pricing for a two-person firm, and you'd be paying for approval
workflows and team seats you have no use for.

---

# 2. The weekly operating rhythm

Two hours a week, in three fixed slots, forever. If it isn't diarised it won't happen.

**This is the steady state, not the launch month.** Days 1–30 run at 9–11 hours a week and days 31–90
taper to 6–8; the full seven-day version is in `docs/16`. The three slots below are what survives a
bad week and what you keep after day 90.

## Monday, 07:30–08:00 — Post & prime (30 min)
- Publish the week's anchor post to LinkedIn (Craig), Company Page, X, Facebook
- Publish the weekly GBP post
- Reply to every comment from the weekend
- Check the calendar for this week's dates and adjust if a deadline moved

*This slot is 07:30 and stays 07:30 — the post is written and scheduled the previous Friday, so it
holds the slot. The cold-call block in `docs/23 §PART 7` runs **08:00–08:30 Monday and Wednesday**,
straight after this one, so the two do not collide in the diary.*

## Wednesday, 17:30–18:00 — Community (30 min)
- One genuine contribution to a forum or subreddit. **No link.**
- Answer questions in two Facebook groups
- Reply to every LinkedIn comment and DM
- This is the slot that builds the pipeline. It is also the first slot people cancel. Don't.

## Friday, 16:00–17:00 — Produce & schedule (60 min)
- Record one short video on a phone (or render one from the kit)
- Write next week's anchor post
- Schedule everything for the coming week
- Log the four numbers (below)

**Total: 30 + 30 + 60 = 120 minutes, two hours a week.** Not two hours a day. Add roughly one hour a
month for the monthly review in section 3, so about **nine hours a month**. If the steady state grows
beyond that, either it's working and you hire, or you're overproducing for channels that aren't
returning.

---

# 3. Measurement — four numbers, logged weekly, reviewed monthly

Log them every Friday in the KPI workbook, two minutes. Review the trend at each month end —
Tue 13 October, Thu 12 November, Sat 12 December. Ignore followers. Followers are not a business metric and this audience is small by definition.

| Number | Where | Target by month 3 |
|---|---|---|
| **Discovery calls booked** | Cal.com | 8–12/month |
| **Cost per booked call** | Ad spend ÷ booked calls | Under £40. Kill ads above it. |
| **Guide downloads** | Brevo list growth | 60–100/month |
| **GBP: calls + direction requests + website clicks** | GBP Insights | Growing month on month |

Everything else is diagnostic, not a goal.

## UTM scheme — use it from post one

```
?utm_source=<platform>&utm_medium=<type>&utm_campaign=<campaign>&utm_content=<detail>

utm_source:    linkedin | facebook | instagram | x | tiktok | youtube | gbp | reddit
               | forum | email | merchant | print
utm_medium:    social | email | organic | cpc | print | qr
utm_campaign:  launch30 | mtd_q3 | newsletter | evergreen | partners
utm_content:   day01 ... day30 | nl01 ... nl12 | seq_mtd_e3
```

**Print gets UTMs too.** Merchant cards and van livery carry a QR code pointing at
`klyara.com/?utm_source=merchant&utm_medium=qr&utm_campaign=trade_counter` — otherwise you will
never know whether the £40 print run worked, and you'll either stop doing the thing that's working or
keep doing the thing that isn't.

## Set up before the first post
- Google Analytics 4 on klyara.com
- Google Search Console (verify the domain, submit the sitemap)
- Meta Pixel — install even with zero ad budget. It's building the retargeting audience from day one.
- LinkedIn Insight Tag — same reasoning
- Cal.com conversion tracking

---

# 4. Google Ads — built and paused ⛔ HOLD

Per the Build Manual: £500 credit, but these are **match offers** — you spend ~£400 to receive £500.
Budget for the spend, not the credit.

**⛔ HOLD — do not switch these on until AML supervision is granted.** Applied Tue 1 September,
28 days, expected around Tue 29 September; the switch is the day the licence number is in hand, not
the expected date. Marker defined once in `docs/00 §⛔ HOLD`. You cannot advertise for bookkeeping
clients you are not yet permitted to serve. Build the campaigns, load the copy, leave them paused.

## Structure
Search only. No Display, no Performance Max, no Search Partners. 10–15 mile radius. Exact and phrase
match only — broad match will burn the whole budget on "quickbooks login" in a fortnight.

## Ad group 1 — MTD *(likely cheapest CPC, highest urgency)*
```
Keywords: [mtd accountant] [making tax digital sole trader] [mtd for income tax help]
          "mtd accountant [town]" "making tax digital bookkeeper"

H1: MTD Quarterly Filing Sorted
H2: For Builders & Subcontractors
H3: Fixed Fee From £59 + VAT
D1: HMRC wants an update every 3 months. We keep the records and file them. Construction specialists.
D2: Free 15-minute call. We'll tell you if you're even in scope. No jargon, no hourly billing.
→ klyara.com/making-tax-digital.html
```

## Ad group 2 — CIS
```
Keywords: [cis accountant] [cis returns] [cis tax return help] "cis accountant [town]"
          "construction industry scheme accountant"

H1: CIS Returns Filed By The 19th
H2: Every Month, Fixed Fee
H3: Construction Specialists Only
D1: Verification, 20/30% deductions, materials splits, monthly returns. Never miss the 19th again.
D2: From £199/month + VAT. Free 15-minute call. No hourly billing, no surprise invoices.
→ klyara.com/services/
```

## Ad group 3 — Bookkeeping for builders
```
Keywords: [bookkeeper for builders] [construction bookkeeping] [builders accountant]
          "bookkeeper for construction [town]"

H1: Bookkeeping For Building Firms
H2: CIS, VAT & Payroll Handled
H3: Run The Jobs. We Run The Rest.
D1: Receipts snapped on your phone. Monthly P&L you can actually read. CIS filed on time.
D2: Fixed monthly pricing from £59 + VAT. Free 15-minute discovery call.
→ klyara.com
```

## Negatives — load before launch
```
free, jobs, salary, course, training, qualification, software, login, template, spreadsheet,
diy, apprenticeship, what is, definition, calculator, hmrc login, xero login, quickbooks login,
sage login, refund calculator, tax rebate, umbrella company, cis rebate
```
*(Note "calculator" and "tax rebate" as negatives — your own free calculators pull that traffic
organically for £0. Don't pay for it too.)*

## Kill rule
Review at £150 spent. **Above £40 per booked call, pause and go back to organic.** The Build Manual
sets £15–£40 as acceptable; stick to it. Outbound, GBP and referrals cost nothing.

---

# 5. Local press release — ⛔ HOLD, send the day AML lands (expected around Tue 29 September)

Local business editors will run this for free. It's a real story with a date on it.

```
FOR IMMEDIATE RELEASE

New Guildford firm targets the tax change catching out local builders

GUILDFORD, [DATE] — Thousands of self-employed builders and subcontractors across Surrey are now
required to report to HMRC four times a year instead of once, under Making Tax Digital for Income
Tax — and many do not yet realise it applies to them.

The rules took effect in April 2026 for sole traders and landlords with qualifying income above
£50,000. The threshold falls to £30,000 in April 2027 and £20,000 in April 2028, bringing the
majority of working subcontractors into scope.

A new Guildford-based firm, Klyara, has been set up specifically to handle the change for
construction businesses.

"The part that catches people out is that HMRC measures your gross invoices, not what lands in your
bank," said Craig [SURNAME], founder of Klyara. "If you're a subcontractor with twenty per cent taken
off at source, your bank balance is telling you you're under the threshold when your invoices say
you're over it. Most subcontractors we speak to assume they are out of scope, and a lot of them are
not."

Klyara provides bookkeeping, CIS returns, VAT reverse charge coding, payroll and quarterly MTD filing
for construction firms on a fixed monthly fee, starting at £59 plus VAT.

The firm has published a free fifteen-page guide to the changes, together with a set of free
calculators covering CIS deductions, job margins and VAT, at klyara.com. Neither requires
registration.

"There's a lot of noise about this and not much plain English," said [SURNAME]. "We'd rather people
worked out where they stand for free than paid someone to be told they were fine."

ENDS

Notes to editors:
Klyara provides back-office services to construction businesses across Surrey.
Contact: Craig [SURNAME], hello@klyara.com, 020 8058 1496
High-resolution logo and images available on request.
```

**Send to:** the local paper's business desk, the county business magazine, the local chamber
newsletter, regional BBC/ITV business email, and any local business podcast. Email the editor
directly by name, subject line `Story: tax change hitting Surrey builders from April`.

*Fill `[DATE]` with the send date and `[SURNAME]` with Craig's surname before this goes anywhere
(`docs/18 §4`). If Klyara trades from a town other than Guildford, swap the town and county throughout.*

---

# 6. Podcast pitch — under 100 words, sent 20 times

UK construction and trades podcasts need guests constantly. Craig's angle is differentiated. This
template gets replies because it leads with the host's audience, not with Klyara.

```
Subject: Guest idea — the tax change most of your listeners don't know applies to them

Hi [NAME],

HMRC now wants quarterly updates from any sole trader over £50k — and it's measured on gross
invoices, before CIS. Most subbies think they're out and aren't. Threshold drops to £30k next April.

I do the books for building firms and I could do 20 minutes on who's caught, what it actually
involves, and the three things to do before April. No pitch.

Craig — klyara.com

```

**Pitch list to build:** search "UK construction podcast", "trades podcast UK", "builders podcast",
"self employed UK podcast" on Spotify and Apple Podcasts. Target twenty. Expect three replies and one
booking — that's a normal, good result, and one episode is worth more than a month of posting.

---

# 7. Accountant partnership outreach — the highest-value channel here

The Build Manual's Layer D. This is the fastest route to clients 1–5 and it also solves the
continuity-cover requirement. Send twenty of these.

```
Subject: Monthly bookkeeping for your construction clients

Hi [NAME],

Quick one, and it's a partnership question rather than a pitch.

I do monthly bookkeeping, CIS and MTD filing for construction firms — that's all I do. No year-end
accounts, no corporation tax, no self-assessment. I deliberately stop where you start.

If you've got building clients whose monthly bookkeeping is more trouble than it's worth to you — the
CIS returns, the reverse charge coding, the receipts that arrive in February — I'd take them on and
hand you clean books at year end.

Two-way referral, 10% of the monthly fee for as long as the client stays, and I'd be glad to discuss
a mutual continuity arrangement, which I gather we both need on file.

Worth twenty minutes?

Craig
klyara.com | 020 8058 1496
```

**The commission is 10% ongoing, not a one-off finder's fee** — the terms are in `docs/23` and the
rationale in `docs/18 §29`. On a Trade client that is £19.90 a month, £239 a year, for as long as
they stay.

**Why this works:** it opens by removing the threat. Accountants ignore firms that look like
competitors and engage with firms that make their difficult clients easier. "I stop where you start"
is the whole pitch.

---

# 8. Merchant trade counter campaign — about £40, highest local ROI on this list

The A5 card is rendered at 300dpi in `assets/print/merchant-card-A5-300dpi.png`.

**Run:** 250 cards, roughly £30–£45 online. Add a QR code to the file pointing at the UTM'd URL before
printing.

**Placement:** Travis Perkins, Jewson, Selco, MKM, Buildbase, Howdens, and every independent merchant
within 15 miles. Ask the counter manager — most say yes to a bookkeeping card because it isn't
competing with anything they sell.

**The better move while you're there:** ask the counter manager which local firms are growing. They
know, because they see the account volumes. That conversation is worth more than the cards.

**Track it:** the QR's UTM tells you if it worked. Without it, don't bother printing them.

---

# 9. The review engine

Reviews are the highest-converting asset a local service business has, and Klyara has none. Fix it
deliberately, from client one.

- **Ask at handover of the first month's reports**, not at signing. That's when the value has just
  landed.
- **Text the link, on the spot.** An ask without a link is homework.
- **Google first, always.** Trustpilot second. Nothing else.
- **Target: two a month, forever, aiming at twenty-plus.** BrightLocal has 47% of consumers refusing
  to use a business with fewer than twenty reviews (`docs/17 §3`), so twenty is the number that
  matters, not ten. Recency beats volume after that.
- **Never** offer anything in return, write them yourself, or buy them. For a firm holding clients'
  financial data, a faked review is not a small problem.
- **Reply to every one**, including any bad one, within 24 hours. Prospects read the replies more
  carefully than the reviews.

**Pre-client alternative:** you cannot review a bookkeeping service you haven't used, and you must not
fake it. But you *can* ethically publish: the partner accountant's written endorsement of Craig's
CIS work, testimonials from previous employers or clients about Craig personally (clearly labelled as
such), and Craig's certifications. Use those until real reviews exist.

---

# 10. Things you didn't ask for, that you're missing

Ordered by what they'd cost you to keep missing.

1. **A disclaimer line in every piece of content.** You're publishing tax guidance publicly as a
   firm whose AML supervision has not landed yet. Every post, video and email needs the "general information, not advice for your
   circumstances, rules change" line. It's in the templates — don't strip it out because it's ugly.

2. **A written content approval step.** One person writes, the other reads before it goes out. A
   wrong CIS rate published under a bookkeeper's name is a professional problem, not a typo.

3. **The `tryklyara.com` outreach domain isn't bought yet** (Manual Part 0 #9). Buy it on
   Wednesday 2 September, about £10. Cold outreach starts before you will remember.

4. **The contractor lead magnet is now built — publish it.** The MTD guide and the Digital Launch Kit
   both speak to solo operators. The 5–15-person firm on Trade or Pro at £199–£329/mo ex VAT had no
   magnet aimed at it, so *"The Contractor's CIS Compliance Pack"* was written:
   `assets/lead-magnets/Klyara-Contractors-CIS-Compliance-Pack.pdf`. Put it behind a form on
   `/cis-pack.html` and point the CIS ad group at that page instead of the services page. It targets
   the tier that pays five times what Solo does.

5. **No case study format.** Your first three clients are worth more as written case studies than as
   revenue. Agree it at onboarding: "In three months, can I write up what we found?" Structure:
   the situation, what we found in the first month, what changed, the number. Anonymise if needed.

6. **Nobody owns social.** Two founders means it's nobody's job by default. Name one owner for the
   two-hour weekly rhythm and put it in the founders' heads of terms alongside everything else.
   The plan assumes Craig; confirm it (`docs/18 §20`).

7. **No brand safety plan for a bad comment.** At some point someone will post that HMRC disagrees
   with something you wrote, or that an accountant did them wrong. Decide now: correct factual errors
   publicly and promptly, take specific complaints to DM, never argue, never delete unless it's abuse.

8. **The calculators aren't being marketed as the asset they are.** Twelve free calculators is a
   strong SEO and link-building asset and you're treating it as a footnote. Each one should
   be its own indexed page with its own title tag ("CIS Deduction Calculator — Klyara"), and each is
   independently linkable from forums and Reddit, where a *tool* is welcome in places a *service*
   would be removed. This is the single best organic-link opportunity you have.

9. **No email capture on the calculator pages.** People using a CIS calculator are your exact buyer at
   the exact moment of pain. One optional field — "want the deadline reminders emailed?" — after they
   get the result, never before.

10. **A LinkedIn newsletter.** Free, and LinkedIn notifies every one of your connections when you
    publish an issue. Mirror the fortnightly newsletter there once the list is running. It's the
    highest-leverage free distribution on the platform and almost nobody in this sector uses it.

11. **You should be recording the discovery calls** (with consent). Six calls in, you'll have the
    exact language your buyers use for their own problems — which is what the next thirty days of
    content should be written in, rather than in the language I've guessed at here.

12. **No plan for what happens when it works.** The Manual puts Craig's ceiling at 20–25 full-service
    clients and the hire trigger at 15; the KPI model crosses 15 around April 2027. Decide the
    waitlist policy *before* you need it — it is better to hold a founding-rate waitlist than to take
    on client 26 badly and lose client 4.
