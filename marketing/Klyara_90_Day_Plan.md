# Klyara — The 90-Day Plan
### One ordered list. Everything in the pack, sequenced, with owners and dependencies.

*Prepared 28 August 2026. Twenty-two documents is a lot to hold in your head. This is the running order.*

**Assume:** setup phase **Tuesday 1 – Sunday 13 September 2026**, launch **Monday 14 September 2026**,
day 90 **Saturday 12 December 2026**. Guildford. ICB practice licence applied for 1 September, so AML
supervision lands around **Tuesday 29 September**.
**Owner column:** K = Key, C = Craig, — = either.
**Phase boundaries and dates match `docs/16`.** Where the two differ, `docs/16` carries the detail and wins.

---

# PHASE 0 — Setup (Tue 1 Sep – Sun 13 Sep)

*Thirteen days, about 22 hours. Everything here is blocking. Nothing in Phase 1 works properly until
these are done. Two items have waiting periods and both start on day one.*

| # | Do | When | Owner | Doc | Why it's blocking |
|---|---|---|---|---|---|
| 1 | **Apply for the ICB practice licence.** £94 application, £206 licence, £167–£200 membership. | Tue 1 Sep | C | `17 §1` | 28-day processing. Klyara cannot carry on bookkeeping by way of business until supervision is in place. Longest lead time in the plan. |
| 2 | **Pull the homepage testimonials.** Replace with the honest-new-firm block. | Wed 2 Sep | K | `07` | Legal and regulatory. Everything else is downstream of the site being defensible, and a licence application is about to be read. |
| 3 | Audit every other site claim for present-tense truth. Future-tense what isn't live. | Wed 2 Sep | K | `07` | Same reason |
| 4 | Create `social@klyara.com`, into Bitwarden, 2FA on | Wed 2 Sep | — | `02` | Every platform signup runs through it |
| 5 | Buy `tryklyara.com` (about £10) | Wed 2 Sep | K | Build Manual §0.9 | Cold outreach must never use the main domain |
| 6 | **Claim the Google Business Profile and start verification** | Thu 3 Sep | C | `11` | 5–14 day wait. The address decision cannot be changed later without re-verifying. |
| 7 | Request three PII insurance quotes, in writing | Tue 1 Sep | C | `18 §11` | A condition of the ICB licence, so it cannot wait for the licence |
| 8 | Paste the JSON-LD onto every page. Validate each in the Rich Results test. | w/c 7 Sep | K | `08` | Needs to be indexed before traffic arrives |
| 9 | Install Meta Pixel, LinkedIn Insight Tag, GA4, Search Console | w/c 7 Sep | K | `06`, `08` | The audience you don't collect from day one is gone permanently |
| 10 | Publish the Guildford landing page | w/c 7 Sep | K | `11`, `web/` | The only page with buying intent behind it |
| 11 | Add newsletter capture after every calculator result | w/c 7 Sep | K | `07` | Highest-intent capture point on the site, currently doing nothing |
| 12 | Set up Brevo. SPF, DKIM, DMARC at `p=none`. Start the warm-up. | Thu 3 Sep | K | `05` | DNS propagation plus a ramp — start now or the first send lands in spam |

**Rows 1 to 6 are the first three days.** The rest spread across the remaining ten.

---

# PHASE 1 — Week 1 (Mon 14 – Sun 20 September)

## Monday 14 September — launch day

| Do | Owner | Doc |
|---|---|---|
| Publish the Day 1 anchor post to LinkedIn (Craig's profile — pin it), Company Page, X, Facebook, Instagram | C | `03` |
| First GBP post | C | `13 W1` |
| Sign up: LinkedIn Company Page, Facebook Page, Instagram → Threads, X | — | `02` |
| Rebuild Craig's personal LinkedIn — headline, About, banner, featured, creator mode on | C | `02` |
| Warm-up blast to the ~20-name deliverability list: "we're live". Not an issue of the programme — that starts with `docs/05 №1 (Thu 17 Sep)`. | K | `05` |

## Rest of week 1

| Do | Owner | Doc |
|---|---|---|
| Remaining platform signups: YouTube + playlists, TikTok, Reddit ×2, Bluesky (+ domain verify), Pinterest, Snapchat, Nextdoor | — | `02` |
| Directory tier 1: Trustpilot, Yell, FreeIndex, Bing Places, Apple Business Connect | — | `02` |
| Forum registrations — profiles only, no signature yet | C | `01` |
| Request to join 12–15 Facebook groups | C | `01` |
| Run the Day 2–7 content | C | `03` |
| **Reddit: read only. Post nothing.** | C | `01` |
| `docs/05 №1 (Thu 17 Sep)` — the gross income trap. 07:00. | K | `05` |
| ⚠️ **CIS return for the month to 5 September.** The 19th is a Saturday, so work to Friday 18th. | C | `12` |

---

# PHASE 2 — Weeks 2–4 (Mon 21 September – Sun 11 October)

## The weekly rhythm starts and never stops

Steady state, once the launch month is behind you:

```
Mon 07:30  Anchor post + GBP post + reply to weekend comments      30 min
Wed 17:30  One forum/Reddit contribution (no link) + group answers 30 min
Fri 16:00  Record a video, write next week's anchor, schedule      60 min
```

**Two hours.** The launch month runs heavier — 9–11 hours a week, and `docs/16` has the full seven-day
version. This three-slot version is what you fall back to and what you keep forever. The cold-call
block from `docs/23 §PART 7` sits at **08:00–08:30 Monday and Wednesday**, straight after the Monday
anchor post — the post is scheduled the previous Friday, so it keeps 07:30.

**The newsletter grid, fixed.** Fortnightly Thursdays, 07:00, from `docs/05 №1 (Thu 17 Sep)`. Inside
the ninety days: №1 Thu 17 Sep, №2 Thu 1 Oct, №3 Thu 15 Oct, №4 Thu 29 Oct, №5 Thu 12 Nov,
№6 Thu 26 Nov, №7 Thu 10 Dec. Never a Friday, and it does not move for a deadline. `docs/05 №8`
sends Thu 17 Dec — a week after №7, pulled forward off Christmas Eve so it lands while the sites are
still open — and fortnightly resumes with №9 on Thu 14 Jan. Always cite a send as number **and**
date.

## Week 2 (21–27 September) — CIS and reverse charge

| Do | Owner | Doc |
|---|---|---|
| Run Days 8–14 content | C | `03` |
| **Slyfield merchant round** — Selco, Travis Perkins, Jewson, Howdens. Cards out, ask counter managers who's growing. | C | `11 §7` |
| Print 250 A5 cards, about £40, with the QR and UTM added first | K | `assets/print/` |
| **Send 20 accountant partnership emails** with the partner one-pager attached | C | `11 §8` |
| Surrey citations: Chambers enquiry, Business Surrey, thebestof Guildford | — | `11 §6` |
| Directory tier 2: Cylex, Scoot, Thomson Local, Hotfrog, 192.com | — | `02` |
| 🕐 **AML supervision expected around Tue 29 September.** Chase weekly from day 28. | C | `17 §1` |

## Week 3 (28 September – 4 October) — Getting paid

| Do | Owner | Doc |
|---|---|---|
| Run Days 15–21 content | C | `03` |
| Publish Surrey + Woking town pages | K | `web/` |
| Follow up every accountant who didn't reply. Once. | C | `11 §8` |
| Forums: add the signature once you've posted 8–10 genuine answers | C | `01` |
| Second merchant lap — Woking, Godalming, Farnham | C | `11 §7` |
| `docs/05 №2 (Thu 1 Oct)` — four days to quarter end. 07:00. | K | `05` |

## Week 4 (5–11 October) — Quarter end

| Do | Owner | Doc |
|---|---|---|
| Run Days 22–28 content — the seven-job checklist, one a day | C | `03` |
| **Mon 5 October — MTD quarter ends (6 Jul – 5 Oct).** | C | `03` |
| No newsletter this week. `docs/05 №2 (Thu 1 Oct)` went in week 3; `docs/05 №3 (Thu 15 Oct)` is next. | K | `05` |
| Publish Godalming + Farnham pages | K | `web/` |
| Publish the quarter-end checklist as its own page with HowTo schema | K | `08` |
| **Reddit: start commenting.** Target 30–40 genuine comments over the next fortnight. No links. | C | `01` |
| Draft the press release, hold it | K | `06 §5` |
| Pitch 20 podcasts | C | `06 §6` |

---

# PHASE 3 — Days 29–60 (Mon 12 October – Thu 12 November)

| Do | Owner | Doc |
|---|---|---|
| Days 29–30, then Month 2 themes: gross payment status, pricing, first employee, the 7 Nov countdown | C | `03` |
| **Buy Metricool**, about £20–£28/month — you now know which channels earn their slot | K | `06 §1` |
| `docs/05 №3 (Thu 15 Oct)`, `docs/05 №4 (Thu 29 Oct)` and `docs/05 №5 (Thu 12 Nov)` | K | `05` |
| GBP posts W5–W9 | C | `13` |
| Build the "which tier am I?" helper on the pricing page | K | `07` |
| Cut homepage CTAs to one primary per section | K | `07` |
| Per-page `og:image` from `assets/posts/` | K | `07` |
| Calculator page titles, metas and `SoftwareApplication` schema — all twelve | K | `08` |
| **Mon 19 October — CIS return, month to 5 October.** | C | `12` |
| **Sat 7 November — the MTD quarterly update is due.** Run the countdown on the posts, not by email: the fortnightly grid puts the next send on `docs/05 №5 (Thu 12 Nov)`, five days after, which is why that issue is written as "the MTD update you missed". The cadence does not move for a deadline. | C | `03`, `05` |
| **Reddit: first text post, if the rules permit and karma allows** | C | `01` |
| Surrey Chambers event, or Guildford & Waverley Business Question Time | — | `11 §7` |
| Review the four numbers at the end of month 1 (Tue 13 October) | K | `06 §3` |

## The moment AML supervision lands (expected Tue 29 September)

Everything below is written and waiting. Do it the same week.

| Do | Doc |
|---|---|
| Swap every `⛔ HOLD` CTA to the live version — site, ads, emails, content calendar, directories. All of them, the same day. Marker defined in `docs/00 §⛔ HOLD`. | `01`, `03`, `05`, `06`, `11` |
| Turn Google Ads on — three ad groups, negatives loaded, £40/booked-call kill rule | `06 §4` |
| Send the press release to Surrey Advertiser, Chambers, local outlets | `06 §5` |
| Add the professional body and supervision line to the email signature | `05 §10` |
| List on Find-a-ProAdvisor, Xero Advisor Directory, FreeAgent, the ICB directory | `01`, `11 §6` |
| Open Bark.com if lead economics work | `01` |
| Update the site's "qualified" claims to what is now true | `07` |

---

# PHASE 4 — Days 61–90 (Fri 13 November – Sat 12 December)

| Do | Owner | Doc |
|---|---|---|
| Month 3 themes: year-end planning, capital allowances, the January hole, 31 Jan countdown | C | `03` |
| `docs/05 №6 (Thu 26 Nov)` and `docs/05 №7 (Thu 10 Dec)`. Thursdays, 07:00 — never a Friday. | K | `05` |
| GBP W10–W13 | C | `13` |
| **Thu 19 November — CIS return, month to 5 November.** | C | `12` |
| First clients onboarded — run the five-day runbook properly, every time | C | `12` |
| Ask every client for a Google review at the first report handover | C | `06 §9` |
| First case study agreed with client 1 | C | `06 §10` |
| Review the four numbers at the end of month 2 (Thu 12 November). Kill or scale accordingly. | K | `06 §3` |
| Full re-score of the risk register at day 90 (Sat 12 December) | K | `20` |

---

# The decision gates

Don't carry on doing something that isn't working because it's in the plan.

| When | Question | If no |
|---|---|---|
| **Thu 17 September** (14 days after claiming) | Is GBP verified? | Chase it. Nothing local works until it is, and it is the single most common launch failure. |
| **Tue 29 September** (28 days after applying) | Has the ICB licence landed? | Chase weekly. Keep publishing. Do not take bookkeeping work until it is in place. |
| **Tue 13 October** (end of month 1) | Four or more discovery calls from Guildford postcodes? | Almost always GBP verification. Check that before changing content. |
| **£150 of ad spend** | Cost per booked call under £40? | Pause ads. Organic, GBP and referrals cost nothing. |
| **Thu 12 November** (end of month 2) | Any accountant partnership conversations live? | Send 20 more. This channel is the fastest route to clients 1–5 and 20 emails is a small sample. |
| **Sat 12 December** (day 90) | 8–12 booked calls a month? | Cut the bottom half of the channel map and put those hours into the top half. |
| **Sat 12 December** (day 90) | Proposals converting above 25%? | Do not cut prices. Record three calls and listen to whether you're diagnosing or describing. |
| **Any time** | More than two hours a week on social, once the launch month is over? | Either it's working and you hire, or you're overproducing for channels that aren't returning. |

---

# What good looks like at day 90 (Sat 12 December)

```
Google Business Profile   verified, 13 weekly posts, 5+ real reviews (standing target 20+)
Website                   5 local pages indexed, schema on everything, capture on the calculators
Email list                150–400 subscribers, 8 sends (warm-up blast plus №1–№7), 35%+ open
LinkedIn                  13 anchor posts, Craig's profile doing the work
Reddit / forums           40+ genuine contributions, account healthy, first links earned
Partnerships              20+ accountants contacted, 2–4 conversations, 1 referral arrangement
Merchants                 250 cards out, 2 counter managers who know your name
Clients                   3–5 onboarded, each live within 5 working days
Calls                     8–12 booked per month, under £40 each
Case studies              1 agreed, 2 more diarised
```

**If the only thing you achieve is GBP verified, the Guildford page live with schema, twenty
accountant emails sent and the weekly rhythm actually running — that is a successful 90 days.**
Everything else compounds off those four.

---

# The honest risk list

Once, plainly, then it's your call. Full register with owners and triggers in `docs/20`.

1. **The testimonials.** Until they're off, everything else is building on a liability.
2. **AML timing.** The whole revenue plan sits behind it. Applied 1 September, 28-day processing,
   supervision expected around 29 September. Until it lands Klyara cannot carry on bookkeeping by way
   of business at all — so the waitlist is the pipeline, and you keep publishing regardless.
3. **Craig is the whole product.** Every channel here is fronted by one person. That's why it works,
   and it's also the single point of failure. The continuity arrangement isn't paperwork.
4. **Two founders, no signed agreement.** Build Manual §0.3. Not marketing, but it kills more small
   firms than competition does, and marketing that works makes it more urgent, not less.
5. **Capacity arrives faster than hiring.** Craig's ceiling is 20–25 full-service equivalents and the
   hire trigger is 15. Decide the waitlist policy before you need it.
6. **This pack assumes Guildford.** If you trade from somewhere else, the local pack and the five web
   pages need the town swapped. The generator makes that a ten-minute job, but somebody has to
   remember to do it.
