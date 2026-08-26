# Klyara — The Day-by-Day Plan
### Every day from today to day 90. Dated, timed, and written so it can be done without thinking.

*Launch: Monday 7 September 2026. Day 90: Saturday 5 December 2026.*

---

## How to use this

Each day has **one thing** — if the day goes wrong and you only do one item, do that one. Times are
realistic, not aspirational. Weekends are mostly empty on purpose: a 90-day plan that eats every
Saturday gets abandoned in week three.

`docs/NN` references point at the other documents in this pack.

**Symbols:** 🔴 blocking · ⚠️ hard deadline · 💷 costs money · 👥 needs the other founder · 🕐 has a waiting period

---

## Added since this plan was first written

Four things arrived after the first version and they are slotted into the days below. If you have
already started the plan, these are the catch-up items.

| What | Where it slots | Why it matters |
|---|---|---|
| `web/tools.html` — four working tools | Sat 29 Aug, with the schema | Ten pages already link to it. Until it is live those are broken links, and it is the thing every outbound message gives away. |
| `docs/21` — pricing, scope and quoting | Sun 6 Sep, with the sales pack | The scope schedule goes out with every engagement letter from client 1. Retrofitting scope onto an existing client is the hardest conversation in this business. |
| `docs/22` — competitor and price benchmark | Sun 6 Sep, same sitting | Adds the "founding client rate" wording, which costs nothing now and is worth the whole price increase later. |
| `docs/23` — outreach and partners | Week 1 onwards, as a standing weekly block | The content works in month four. This is what produces clients in month one. |

**One standing addition to every week from Week 1:** the outbound rhythm in `docs/23 §PART 7`.
Two early-morning call blocks, two email blocks, one partner coffee, twenty minutes of group
answering four days a week. Roughly four hours. Put it in the diary as recurring now — it is the
single highest-yield block in the whole ninety days and it is the first thing to get skipped.

---

# PHASE 0 — Now until launch (Wed 26 Aug – Sun 6 Sep)

*Twelve days. Roughly 16 hours of work. Two items have waiting periods attached and both start this week.*


### Wednesday 26 August  ·  ⏱ 2h

**One thing:** Kill the testimonials and start the two things with a waiting list.

1. **Remove the five homepage testimonials.** Marcus B., Dean W., Sam O., Priya T., Jodie F. Replace with the honest-new-firm block in `docs/07 §Option B`. This is not optional and nothing else in this plan matters until it is done.
2. Read `docs/07` top to bottom. It is 15 minutes and it is the only document that describes a legal exposure.
3. Go through the site and future-tense every claim that is not true today: certifications, '24/7 answering', the AI services, the client portal. `docs/07` has the checklist.
4. Create `social@klyara.com`. Put it in Bitwarden. Turn on 2FA.
5. Buy `tryklyara.com` (~£10). Do not point it anywhere yet.


### Thursday 27 August  ·  ⏱ 2h

**One thing:** Start the ICB practice licence. It is the AML route and it is 28 days.

1. **Apply for the ICB Practice Licence.** £94 application + £206 annual, and it *includes* MLR supervision at no extra cost. Processing is stated at 28 days. See `docs/17 §2` for why this beats registering with HMRC directly (£300 + £400 per premises, up to 45 days).
2. Get Professional Indemnity Insurance quotes — it is a condition of the licence. ICB members get a discounted route.
3. Whichever route you take, **write the date you applied on a wall**. Every 'when can we take clients' decision keys off it.
4. Start the Google Business Profile claim. Do not finish it today if you do not have the address decision made — but start it, because verification is 5–14 days.


### Friday 28 August  ·  ⏱ 1h 30m

**One thing:** Analytics and pixels, so you are collecting from day one.

1. Install GA4 on klyara.com. Set two conversions: `book_call` and `download_guide`.
2. Verify Google Search Console (domain property) and submit the sitemap.
3. Install the Meta Pixel. Yes, with zero ad budget. The retargeting audience you do not collect this month does not exist next month.
4. Install the LinkedIn Insight Tag.
5. Check every calculator page is in the sitemap. `docs/08 §10` has the full technical list.


### Saturday 29 August  ·  ⏱ 2h

**One thing:** Publish `web/tools.html`, then the schema. Ten pages already link to the tools page.

1. Paste the `AccountingService` block from `docs/08 §1` into the site-wide head. Fill in the bracketed address and founding date.
2. Paste `WebSite` on the homepage (`docs/08 §2`).
3. Paste `FAQPage` on the MTD page (`docs/08 §3`) — your 16 questions are currently earning nothing.
4. Validate each page at `search.google.com/test/rich-results`. Ten seconds a page, and it catches the typos that silently kill a whole block.


### Sunday 30 August  ·  ⏱ rest

**One thing:** Rest. Genuinely.

1. Nothing. You have a 90-day run starting in a week and starting tired is a bad trade.


### Monday 31 August  ·  ⏱ 2h

**One thing:** Publish the Guildford page.

1. Upload `web/construction-bookkeeping-guildford.html`. Paste the page body into your template and delete the inline CSS — it is only there so the file stands alone for review.
2. Replace `[CAL_LINK]` with your Cal.com URL and `[STREET]`/`[POSTCODE]` in the schema.
3. Upload two images the schema points at: `assets/logo/klyara-mark-disc-512.png` and a 1200×630 crop of `assets/banners/x-header-1500x500.png` as `/assets/og/klyara-og.png`.
4. Link to it from the homepage footer and the services page. An orphan page ranks for nothing.
5. Submit the URL in Search Console.


### Tuesday 1 September  ·  ⏱ 2h

**One thing:** Brevo, and the DNS that has to propagate before you send anything.

1. Create the Brevo account. `docs/05 §1` explains why Brevo over the alternatives and when to migrate off it.
2. Add the SPF, DKIM and DMARC records from `docs/05 §4`. **DMARC at `p=none` to start.** Do not go straight to reject.
3. Create the six lists from `docs/05 §2`: Newsletter, MTD Guide, Launch Kit, Solo Waitlist, Clients, Partners.
4. Add the seven contact attributes. Doing this now is ten minutes; retrofitting it onto a mixed list in November is a bad afternoon.
5. Set the sender: `Craig at Klyara <craig@klyara.com>`. Never `no-reply@`.


### Wednesday 2 September  ·  ⏱ 2h

**One thing:** Load the email sequences while you have quiet.

1. Build the three-email welcome sequence (`docs/05 §5`).
2. Build the five-email MTD guide sequence (`docs/05 §6`).
3. Build the four-email Launch Kit sequence (`docs/05 §7`).
4. Paste `email/template.html` in as a custom template and `email/signature.html` into Gmail.
5. **Start the warm-up.** Day 1–3 is 20 sends: yourself, both founders, friends, the partner accountant. The ramp in `docs/05 §4` is not optional — a cold domain that suddenly sends 2,000 emails goes to spam and takes months to recover.


### Thursday 3 September  ·  ⏱ 2h

**One thing:** Set up the profiles you can do without waiting on anything.

1. Decide the handle. Order of preference: `klyara` → `klyarahq` → `klyara_uk` → `getklyara`. **Whatever you land on, use it everywhere**, even where a better one is free.
2. LinkedIn Company Page — copy in `docs/02 §2`, logo `assets/avatars/klyara-avatar-linkedin-512.png`, cover `assets/banners/linkedin-company-1128x191.png`.
3. Rebuild Craig's personal LinkedIn: headline, About, banner, Featured, custom URL, creator mode on. Copy in `docs/02 §3`. **This profile does more work than the company page — LinkedIn gives personal posts several times the reach.**
4. Get a real headshot. On site, in a van, in hi-vis. Not a suit, not a logo, not AI.


### Friday 4 September  ·  ⏱ 2h 30m

**One thing:** The rest of the estate.

1. Facebook Page (`docs/02 §4`) + set both founders as admins. Businesses lose pages when the one admin leaves.
2. Instagram, converted to a Professional account → auto-creates Threads.
3. X, YouTube (+ the five playlists), TikTok (Business account).
4. Reddit ×2 — Craig's human account and the brand account. **Then stop. Read only for three weeks.** `docs/01 §Reddit Protocol`.
5. Bluesky (+ verify the domain via DNS TXT — free, ten minutes, real trust signal), Pinterest, Snapchat (claim and leave), Nextdoor.


### Saturday 5 September  ·  ⏱ 1h

**One thing:** Directories. Boring, one-off, and they compound.

1. Lock the NAP string from `docs/02` and never vary it by a character.
2. Trustpilot, Yell, FreeIndex, Bing Places, Apple Business Connect.
3. Then Cylex, Scoot, Thomson Local, Hotfrog, 192.com.
4. Surrey-specific: Surrey Chambers enquiry, Business Surrey, thebestof Guildford (`docs/11 §6`).


### Sunday 6 September  ·  ⏱ 1h

**One thing:** Load the week and then stop.

1. Register on the forums — profiles only, **no signature yet**: Screwfix Community, UK Business Forums, BookaBuilderUK, ContractorsTalk, UKPlumbersForums, ElectriciansForums.
2. Request to join 12–15 Facebook groups (`docs/01 §Facebook groups` has the search strings and the vetting rule). Approval can take days, so ask now.
3. Schedule tomorrow's launch posts. Manually — you are not buying a scheduler until month two, and posting by hand for a month teaches you what a scheduler hides.
4. Read `docs/09` — the sales pack. Tomorrow the phone might ring.
5. Read `docs/21` and `docs/22`. Then do three small things that take twenty minutes between them and are very hard to add later: put **"founding client rate, held for twelve months"** on the pricing page; put the **£285 bought-separately comparison** on the pricing page and in the proposal template; and diarise the price review for **1 September 2027**.
6. Attach `assets/sales/Klyara-Schedule-of-Services.pdf` to the engagement letter template so it goes out with client 1, not client 12.
7. Print `assets/print/Klyara-Trade-Counter-Card-A4-4up.pdf` — A4 at 100%, no scaling, trim to the crop marks. Fifty sheets is two hundred cards and costs about £15. They go on merchant trade counters in Week 2 (`docs/23 §PART 5`).
8. Put the `docs/23 §PART 7` outbound blocks into the diary as recurring appointments. Do this now, while it is quiet.

---

# THE 90 DAYS

*Launch Monday 7 September. Day 90 is Saturday 5 December.*

## The weekly rhythm — it repeats every week, forever

```
Mon 07:30  Anchor post + GBP post + reply to weekend comments     30 min
Tue        Short video, native upload to each platform            20 min
Wed 17:30  Carousel + the community slot (no links)               45 min
Thu        Long video or the week's big piece                     2h
Fri 16:00  Practical post + production hour + log the numbers     90 min
Sat        One light human post                                   15 min
Sun        Week-ahead deadlines post                              20 min
```

**The Wednesday community slot is the one people cancel. Don't.** It is the slot that builds the
pipeline, and it is slow precisely because it works.

---

## Month 1 — Launch (Days 1–30)


### Day 1 — Mon 7 Sep  ·  ⏱ 3h

**One thing:** Launch. Post the anchor, then answer every reply for the rest of the day.

1. 07:30 — Publish the Day 1 anchor post to **Craig's LinkedIn** and pin it. Full copy in `docs/03 Day 1`. This is the single most important post of the month.
2. 07:45 — Company Page version, X, Facebook Page, Instagram (`assets/posts/post-day01-launch.png`).
3. 08:00 — First Google Business Profile post (`docs/13 W1`). Button: Learn more.
4. Through the day: reply to **every** comment within the hour. Reach on day one is decided by early engagement.
5. Send Newsletter #0 to your warm-up list of ~20: 'we're live'. Keep the warm-up ramp going.
6. 🕐 Chase the GBP verification if the postcard/video step has not arrived.


### Day 2 — Tue 8 Sep  ·  ⏱ 1h 30m

**One thing:** Short video out, and start the accountant list.

1. Post `video/01-mtd-caught-you.mp4` to TikTok, Reels and YouTube Shorts. Upload **natively to each** — never cross-post a watermarked file. Caption in `docs/03 Day 2`.
2. Add a trending audio at low volume from the platform's own commercial library. The videos are silent by design so you can.
3. X post: the gross-income trap (`docs/03 Day 2`).
4. Build the accountant target list: search 'accountants Guildford / Woking / Godalming / Farnham', take the first two pages of each, prioritise **two-to-six partner firms**. Target 20. `docs/11 §8`.


### Day 3 — Wed 9 Sep  ·  ⏱ 1h 30m

**One thing:** Carousel, and your first community contribution.

1. Instagram carousel + LinkedIn document post: `assets/carousel/mtd-6slides/` (6 slides). Caption in `docs/03 Day 3`. For LinkedIn, upload the slides as a PDF so it renders as a document.
2. Facebook version.
3. 17:30 — **First community slot.** Pick one forum. Answer one question properly using `docs/15`. **No link. No signature.** Adapt the opening line — copy-paste answers read as copy-paste answers.


### Day 4 — Thu 10 Sep  ·  ⏱ 2h 30m

**One thing:** Record the first long video. It is the asset everything else cuts from.

1. Record *'Making Tax Digital for Builders: Are You In?'* — full script in `docs/04`. Seven minutes. Phone on a tripod is fine; audio matters more than video.
2. Upload with the description and timestamps from `docs/04`. Add to the 'Making Tax Digital' playlist.
3. LinkedIn announce post — **link in the first comment, not the post.** LinkedIn suppresses posts with outbound links.
4. Newsletter #1 goes out 07:00 (`docs/05 §8 №1`). Check the warm-up ramp allows the volume.


### Day 5 — Fri 11 Sep  ·  ⏱ 1h 30m

**One thing:** The deadline thread. This is the format that gets saved and shared.

1. X thread: every MTD date, 7 tweets (`docs/03 Day 5`).
2. Facebook + the deadline graphic `assets/posts/post-deadline-calendar.png`.
3. 16:00 — **Production hour.** Write next week's anchor post. Record one short video on your phone.
4. Log the four numbers for week 1 (`docs/06 §3`). Even if they are all zero — the habit is the point.


### Day 6 — Sat 12 Sep  ·  ⏱ 30m

**One thing:** Light. One human post.

1. Instagram Stories, 3 frames + Facebook: the Saturday post in `docs/03 Day 6`.
2. Nothing else.


### Day 7 — Sun 13 Sep  ·  ⏱ 45m

**One thing:** Week-ahead post. Sets up the CIS deadline.

1. LinkedIn + X + GBP: the week-ahead post (`docs/03 Day 7`). It flags the 19 September CIS deadline.
2. ⚠️ Note for yourself: **19 September is a Saturday.** Anyone filing CIS should work to Friday 18th.


### Day 8 — Mon 14 Sep  ·  ⏱ 2h

**One thing:** Week 2 anchor: CIS in real numbers.

1. 07:30 — Anchor post to LinkedIn, X, Facebook (`docs/03 Day 8`), plus GBP (`docs/13 W2`).
2. Post `assets/posts/post-cis-penalties.png` with it.
3. **Send the first 10 accountant partnership emails** (`docs/11 §8`), with `assets/sales/Klyara-For-Accountants-Partnership.pdf` attached. Ten today, ten Thursday — do not blast 20 at once, because the first ten will teach you something.
4. Reply to everything.


### Day 9 — Tue 15 Sep  ·  ⏱ 1h 30m

**One thing:** Video, and the merchant round prep.

1. Post `video/02-cis-20-vs-30.mp4` to TikTok, Reels, Shorts.
2. 💷 Order 250 A5 merchant cards from `assets/print/merchant-card-A5-300dpi.png`. **Add a QR code first**, pointing at the Guildford page with `?utm_source=merchant&utm_medium=qr&utm_campaign=slyfield`. Without the UTM you will never know if it worked. ~£30–45.
3. Plan the Slyfield route for Thursday: Selco (Slyfield Industrial Estate), Travis Perkins, Jewson, Howdens.


### Day 10 — Wed 16 Sep  ·  ⏱ 1h 30m

**One thing:** CIS carousel + community.

1. Instagram + LinkedIn document: `assets/carousel/cis-7slides/`.
2. 17:30 — Community slot. Two forum answers or two Facebook group answers. Still no links.


### Day 11 — Thu 17 Sep  ·  ⏱ 3h

**One thing:** Record the reverse charge video, send the second ten emails.

1. Record *'The VAT Domestic Reverse Charge, Explained Once and Properly'* (`docs/04`). Nine minutes.
2. LinkedIn long post on the reverse charge (`docs/03 Day 11`) — the five tests and the end-user rule.
3. Send accountant emails 11–20.
4. 🕐 If GBP is still not verified, chase it today. It is now over two weeks.


### Day 12 — Fri 18 Sep  ·  ⏱ 1h 30m

**One thing:** ⚠️ CIS deadline messaging.

1. Post the deadline warning across X, Facebook, GBP, LinkedIn (`docs/03 Day 12`). **Say Friday, not Saturday** — the 19th falls on a weekend.
2. Use `assets/posts/post-nil-return.png`. The nil-return point is the one that saves people £100.
3. 16:00 — Production hour.


### Day 13 — Sat 19 Sep  ·  ⏱ 30m

**One thing:** Light + the question post.

1. The 'what's the worst bit of admin in your week' post (`docs/03 Day 13`). Genuine question, genuine replies. This one usually gets the most comments of the month.


### Day 14 — Sun 20 Sep  ·  ⏱ 45m

**One thing:** Week ahead. Money week next.

1. Week-ahead post (`docs/03 Day 14`) — flags Tue 22 Sep electronic CIS payment and the 15 days to quarter end.


### Day 15 — Mon 21 Sep  ·  ⏱ 2h

**One thing:** Week 3 anchor: you are not a bank.

1. 07:30 — The late payment anchor post (`docs/03 Day 15`), plus the X thread, Facebook, GBP (`docs/13 W3`).
2. Use `assets/posts/post-late-payment.png` and `post-retentions.png`.
3. The Facebook version has a comment-bait ('comment RETENTION and I'll send the tracker'). **Actually send it** to everyone who comments, within the hour.
4. 💷 Statutory interest is 8% over base. **Base rate is 3.75% as at 30 July 2026**, so that is 11.75% — check it hasn't moved before you quote a number publicly. Next BoE decision 17 September.


### Day 16 — Tue 22 Sep  ·  ⏱ 1h 30m

**One thing:** Retentions video + the Slyfield round.

1. Post `video/03-retentions.mp4`.
2. **The Slyfield merchant round.** Cards to Selco, Travis Perkins, Jewson, Howdens. Ask each counter manager which local firms are busy — they see the account volumes and they will tell you. That conversation is worth more than the cards.
3. Write down every firm name they mention. That is your prospect list.


### Day 17 — Wed 23 Sep  ·  ⏱ 1h 30m

**One thing:** Getting-paid carousel + community.

1. Instagram + LinkedIn: `assets/carousel/getpaid-6slides/`.
2. 17:30 — Community slot. You should be at 10–15 genuine answers by now.
3. Publish `web/cis-accountant-surrey.html`. Link it from the Guildford page and the services page.


### Day 18 — Thu 24 Sep  ·  ⏱ 3h

**One thing:** The cash flow video, and the first follow-up.

1. Record *'Why Your Building Firm Is Always Skint'* (`docs/04`). Use the Day 18 LinkedIn post as the spine — it is written to be read aloud.
2. LinkedIn: the four cash drains post (`docs/03 Day 18`).
3. **Follow up every accountant who has not replied. Once.** One line: 'Just checking this reached you — happy to leave it if the timing's wrong.'
4. Newsletter #2 (`docs/05 §8 №2`).


### Day 19 — Fri 25 Sep  ·  ⏱ 1h 30m

**One thing:** Give the tracker away.

1. Post the free retention tracker across X, Facebook, LinkedIn (`docs/03 Day 19`).
2. Post two calculator cards from `assets/tools/` into relevant forums — **a free tool is welcome where a service link gets removed.** This is the whole reason the calculators matter.
3. 16:00 — Production hour.


### Day 20 — Sat 26 Sep  ·  ⏱ 30m

**One thing:** Light.

1. The 'best builders aren't the ones who do well' post (`docs/03 Day 20`).


### Day 21 — Sun 27 Sep  ·  ⏱ 45m

**One thing:** ⚠️ Week ahead — quarter end week.

1. Week-ahead post (`docs/03 Day 21`). Flags Mon 5 Oct quarter end and Sat 7 Nov update.
2. Publish `web/construction-bookkeeping-woking.html`.


### Day 22 — Mon 28 Sep  ·  ⏱ 2h

**One thing:** Quarter-end countdown starts. This is the conversion week.

1. 07:30 — Anchor: seven days to quarter end (`docs/03 Day 22`), all channels + GBP (`docs/13 W4`).
2. `assets/posts/post-quarter-end.png`.
3. From today, **one checklist job a day for seven days.** Each is a post and each is genuinely useful. This week produces more replies than the other three combined.


### Day 23 — Tue 29 Sep  ·  ⏱ 1h 30m

**One thing:** Checklist 2 + video.

1. Checklist day 2 — receipts (`docs/03 Day 23`), all channels.
2. Post `video/04-quarter-end-countdown.mp4`.


### Day 24 — Wed 30 Sep  ·  ⏱ 1h 30m

**One thing:** Checklist 3 + the big carousel.

1. Checklist day 3 — mixed-use costs (`docs/03 Day 24`).
2. Instagram + LinkedIn: `assets/carousel/quarterend-8slides/` (8 slides — the strongest set in the pack).
3. 17:30 — Community slot.
4. Publish `web/construction-bookkeeping-godalming.html`.


### Day 25 — Thu 1 Oct  ·  ⏱ 3h

**One thing:** Checklist 4 + the quarter-end video.

1. Checklist day 4 — reconcile (`docs/03 Day 25`).
2. Record *'Quarter-End in Under an Hour'* (`docs/04`).
3. Publish the quarter-end checklist as its own page with the `HowTo` schema from `docs/08 §7`. This one earns links.
4. Publish `web/construction-bookkeeping-farnham.html`. That is all five local pages live.


### Day 26 — Fri 2 Oct  ·  ⏱ 1h 30m

**One thing:** Checklist 5 — the CIS one that matters most.

1. Checklist day 5 — CIS reconciliation (`docs/03 Day 26`). This is the highest-value post in the whole 30 days for subcontractors.
2. 16:00 — Production hour. Write the Day 28 conversion post carefully.
3. Log the four numbers for month 1.


### Day 27 — Sat 3 Oct  ·  ⏱ 45m

**One thing:** Checklist 6 — the two-minute check.

1. Checklist day 6 — the reverse charge check (`docs/03 Day 27`).


### Day 28 — Sun 4 Oct  ·  ⏱ 1h 30m

**One thing:** Checklist 7. The ask.

1. The conversion post (`docs/03 Day 28`). **Use the ⛔ HOLD version unless AML supervision is confirmed** — waitlist and founding rate, not 'book a call to engage'.
2. All channels. This is the post the month has been building to.
3. Reply to every single response today, personally.


### Day 29 — Mon 5 Oct  ·  ⏱ 1h

**One thing:** ⚠️ Quarter end. And 30 days of numbers.

1. The quarter-closed post (`docs/03 Day 29`) + GBP (`docs/13 W5`).
2. **Month 1 review.** Booked calls, cost per call, guide downloads, GBP calls/directions/clicks. Against target: 4+ Guildford-postcode calls.
3. If it is under 4 — check GBP verification is actually live before you change anything else. It is the cause about nine times in ten.


### Day 30 — Tue 6 Oct  ·  ⏱ 1h 30m

**One thing:** Recap, and buy the scheduler.

1. The 30-day recap post (`docs/03 Day 30`) — everything in one place. It gets saved.
2. 💷 **Now buy Metricool.** You have posted by hand for a month and you know which channels earn their slot. ~£20–28/mo. `docs/06 §1`.
3. Load weeks 5–8 of GBP posts (`docs/13`) and next week's content into it.
4. Write down the three things that worked and the three that did not. Month 2 drops the bottom three.

---

## Month 2 — Build (Days 31–60)

*Two things usually happen this month: AML supervision lands, and your first clients arrive. Both
change the plan — see the two boxes below.*

> **🔴 The moment AML supervision is confirmed, do all of this in the same week:**
> swap every `⛔ HOLD` CTA to the live version across site, ads, emails and calendar · turn Google Ads
> on with the £40/booked-call kill rule · send the press release to Surrey Advertiser and the Chambers ·
> add the supervision line to the email signature · list on Find-a-ProAdvisor, Xero Advisor Directory,
> FreeAgent and the ICB directory · update the site's 'qualified' claims to what is now true.
> Details in `docs/14 §Phase 3`.

> **🔴 The moment client 1 signs:** run the five-day onboarding runbook in `docs/12` exactly. Track
> days-from-signing-to-live. Target is five. If it drifts past ten the runbook is not being followed.


### Day 31 — Wed 7 Oct  ·  ⏱ 1h 30m

**One thing:** Month 2 starts. Gross payment status week.

1. Anchor: gross payment status — the three tests and why most who'd pass never apply (`docs/03 Month 2 W1`, content in `assets/lead-magnets/` §Gross status).
2. GBP post W6 (`docs/13`).
3. Publish the gross payment status page — the text is already written in the CIS Compliance Pack. Copy and reformat, do not rewrite.


### Day 32 — Thu 8 Oct  ·  ⏱ 1h

**One thing:** Video + second merchant lap.

1. Post `video/05-reverse-charge.mp4`.
2. Second merchant lap: Woking, Godalming, Farnham branches. Restock the cards that went.


### Day 33 — Fri 9 Oct  ·  ⏱ 1h 15m

**One thing:** Community + tools.

1. Community slot. Post two more calculator cards into forums where tools are welcome.
2. Check: are you at 25+ genuine community contributions? If not, you are behind on the slowest channel.


### Day 34 — Sat 10 Oct  ·  ⏱ 2h

**One thing:** Long video + the contractor magnet goes live.

1. Record the gross payment status video (10 min) or repurpose the Skint video if you are short of time.
2. **Publish `/cis-pack.html`** with `assets/lead-magnets/Klyara-Contractors-CIS-Compliance-Pack.pdf` behind a one-field form. This magnet targets the £199–£329 tier, which your other two magnets do not.
3. Wire it to a Brevo list and a short nurture sequence.


### Day 35 — Sun 11 Oct  ·  ⏱ 1h 30m

**One thing:** Practical + numbers.

1. Practical post: the CIS calculator.
2. Production hour.
3. Log the numbers.


### Day 36 — Mon 12 Oct  ·  ⏱ 30m

**One thing:** Light.

1. One human post.


### Day 37 — Tue 13 Oct  ·  ⏱ 30m

**One thing:** Week ahead.

1. Week-ahead post. Flags Mon 19 Oct CIS return.


### Day 38 — Wed 14 Oct  ·  ⏱ 2h

**One thing:** Pricing week.

1. Anchor: the three costs that never make it into a quote (`docs/05 §8 №6` has the full text — reuse it as a post).
2. GBP W7.
3. **Build the 'which tier am I?' helper on the pricing page** (`docs/07 §Conversion 3`). Three questions, recommends a tier, pre-fills the booking. Half a day of dev and it will move more revenue than any other single change on the site.


### Day 39 — Thu 15 Oct  ·  ⏱ 1h

**One thing:** Video + review engine.

1. Post `video/06-late-payment.mp4`.
2. If you have any clients: ask each for a Google review at the report handover. Text the link on the spot. `docs/06 §9`.


### Day 40 — Fri 16 Oct  ·  ⏱ 1h 15m

**One thing:** Community + reddit escalation.

1. Community slot. **If you are past 30 comments and the sub allows it, post your first Reddit text post.** Long-form, useful, no link in the body. `docs/01 §Reddit Protocol`.


### Day 41 — Sat 17 Oct  ·  ⏱ 2h

**One thing:** Long video + homepage conversion fix.

1. Record or repurpose.
2. **Cut the homepage to one primary CTA per section** (`docs/07 §Conversion 2`). Nineteen competing CTAs is a menu, not a conversion path.


### Day 42 — Sun 18 Oct  ·  ⏱ 1h 30m

**One thing:** Practical + per-page OG images.

1. Practical post.
2. Set per-page `og:image` using `assets/posts/*.png`. Every share this month currently uses the generic image.
3. Production hour + numbers.


### Day 43 — Mon 19 Oct  ·  ⏱ 1h

**One thing:** ⚠️ CIS deadline day.

1. CIS return deadline post (month to 5 Oct). GBP W7 deadline version.
2. If you have clients: their returns go in today, not tomorrow.


### Day 44 — Tue 20 Oct  ·  ⏱ 30m

**One thing:** Week ahead.

1. Week-ahead post.


### Day 45 — Wed 21 Oct  ·  ⏱ 2h

**One thing:** First employee week.

1. Anchor: what taking on your first person actually costs (`docs/15 §19` has the substance).
2. GBP W8.
3. **Calculator page SEO** — titles, metas and `SoftwareApplication` schema for all twelve (`docs/08 §6`). This is the long-tail engine and it is a two-hour job.


### Day 46 — Thu 22 Oct  ·  ⏱ 1h

**One thing:** Video + podcast pitches.

1. Post a short video.
2. **Pitch 20 podcasts** using the 40-word template in `docs/06 §6`. Expect three replies and one booking — that is a normal, good result, and one episode beats a month of posting.


### Day 47 — Fri 23 Oct  ·  ⏱ 1h 15m

**One thing:** Community.

1. Community slot. Answer bank `docs/15`.


### Day 48 — Sat 24 Oct  ·  ⏱ 2h

**One thing:** Long video + Chambers.

1. Record.
2. Surrey Chambers event, or Guildford & Waverley Business Question Time. Go to one. `docs/11 §7`.


### Day 49 — Sun 25 Oct  ·  ⏱ 1h 30m

**One thing:** Practical + numbers + Newsletter #3.

1. Practical post.
2. Newsletter #3.
3. Production hour + numbers.


### Day 50 — Mon 26 Oct  ·  ⏱ 30m

**One thing:** Light.

1. Human post.


### Day 51 — Tue 27 Oct  ·  ⏱ 30m

**One thing:** Week ahead — flag 7 November.

1. Week-ahead post. **The 7 November MTD deadline is now two weeks out.** Start the countdown.


### Day 52 — Wed 28 Oct  ·  ⏱ 2h

**One thing:** 7 November countdown week 1.

1. Anchor: two weeks to the MTD update. What to do if you are behind.
2. GBP W9 (`docs/13`).
3. This is the highest-urgency content window of the whole 90 days. Use it.


### Day 53 — Thu 29 Oct  ·  ⏱ 1h

**One thing:** Video.

1. Short video on the MTD deadline.


### Day 54 — Fri 30 Oct  ·  ⏱ 1h 15m

**One thing:** Community + town page check.

1. Community slot.
2. Check Search Console: are the five local pages indexed and getting impressions? If not, check they are linked from somewhere and resubmit.


### Day 55 — Sat 31 Oct  ·  ⏱ 2h

**One thing:** Long video + case study.

1. Record.
2. If you have three clients: **agree the first case study.** 'In three months, can I write up what we found?' Structure in `docs/06 §10`.


### Day 56 — Sun 1 Nov  ·  ⏱ 1h 30m

**One thing:** Practical + numbers.

1. Practical post.
2. Production hour.
3. **Month 2 review.** Booked calls, cost per call, list growth, GBP actions, clients onboarded. Against target: 6–8 calls.


### Day 57 — Mon 2 Nov  ·  ⏱ 2h

**One thing:** ⚠️ Five days to the MTD deadline.

1. Anchor: the 40-minute version for people who have not started (`docs/05 §8 №5` has the copy).
2. All channels. GBP.
3. Newsletter #5 goes out Thursday, two days before the deadline — that timing is deliberate.


### Day 58 — Tue 3 Nov  ·  ⏱ 1h

**One thing:** Video + reminders.

1. Short video: the deadline.
2. If you have clients in MTD: their updates go in this week, not on the 7th.


### Day 59 — Wed 4 Nov  ·  ⏱ 1h 15m

**One thing:** Community + deadline answers.

1. Community slot. MTD deadline questions will be everywhere this week — this is the best community opportunity of the quarter.


### Day 60 — Thu 5 Nov  ·  ⏱ 2h

**One thing:** Newsletter #5 + long video.

1. Newsletter #5: 'MTD update due Saturday' (`docs/05 §8 №5`).
2. Record.


---

## Month 3 — Convert (Days 61–90)

*The 7 November deadline, then the seasonal run into January. This month has the strongest content
of the year in it and the first real numbers to judge the whole thing on.*


### Day 61 — Fri 6 Nov  ·  ⏱ 1h 30m

**One thing:** Day before the deadline.

1. The 'if it isn't done, here's the fastest legitimate route' post. All channels.
2. Reply to everything — panic drives engagement and this is the day people ask.


### Day 62 — Sat 7 Nov  ·  ⏱ 45m

**One thing:** ⚠️ 7 November. MTD quarterly update due.

1. Deadline-day post: file something reasonable on time rather than something perfect late. It is a summary of totals, not a return.
2. GBP post.
3. If you have MTD clients, everything is already filed. If it is not, today is not the day to discover that.


### Day 63 — Sun 8 Nov  ·  ⏱ 30m

**One thing:** Week ahead.

1. Week-ahead post. Next up: 19 Nov CIS.


### Day 64 — Mon 9 Nov  ·  ⏱ 2h

**One thing:** Pricing and margin week.

1. Anchor: what that job actually cost you (`docs/05 §8 №6`).
2. GBP W10.
3. Post-deadline is a good week to publish something evergreen — the urgency audience has just been served.


### Day 65 — Tue 10 Nov  ·  ⏱ 1h

**One thing:** Video + reviews.

1. Short video.
2. Review asks: target 2/month, forever. Google first, Trustpilot second, nothing else.


### Day 66 — Wed 11 Nov  ·  ⏱ 1h 15m

**One thing:** Community.

1. Community slot. You should be at 40+ contributions and able to link occasionally where rules allow.


### Day 67 — Thu 12 Nov  ·  ⏱ 2h

**One thing:** Long video + internal linking.

1. Record.
2. Internal linking pass: every local page links to the MTD page, the CIS service page, the tools page, and each other. Orphan pages rank for nothing.


### Day 68 — Fri 13 Nov  ·  ⏱ 1h 30m

**One thing:** Practical + numbers + Newsletter #6.

1. Practical post.
2. Newsletter #6.
3. Production hour + numbers.


### Day 69 — Sat 14 Nov  ·  ⏱ 30m

**One thing:** Light.

1. Human post.


### Day 70 — Sun 15 Nov  ·  ⏱ 30m

**One thing:** Week ahead.

1. Week-ahead. Flags Thu 19 Nov CIS.


### Day 71 — Mon 16 Nov  ·  ⏱ 2h

**One thing:** CIS + statements week.

1. Anchor: chase your CIS deduction statements now, not in February.
2. GBP W11.
3. This is genuinely the right week for it — contractors still remember October jobs.


### Day 72 — Tue 17 Nov  ·  ⏱ 1h

**One thing:** Video.

1. Short video on deduction statements.


### Day 73 — Wed 18 Nov  ·  ⏱ 1h 15m

**One thing:** Community + partner follow-up.

1. Community slot.
2. **Second round of accountant outreach.** Another 20 firms, or a second contact to the first 20. Twenty emails is a small sample and this is your best channel.


### Day 74 — Thu 19 Nov  ·  ⏱ 1h

**One thing:** ⚠️ CIS deadline (month to 5 Nov).

1. Deadline post, all channels.
2. Client returns filed.


### Day 75 — Fri 20 Nov  ·  ⏱ 1h 30m

**One thing:** Practical + numbers.

1. Practical post.
2. Production hour + numbers.


### Day 76 — Sat 21 Nov  ·  ⏱ 30m

**One thing:** Light.

1. Human post.


### Day 77 — Sun 22 Nov  ·  ⏱ 30m

**One thing:** Week ahead.

1. Week-ahead. December is coming and the January hole content starts next week.


### Day 78 — Mon 23 Nov  ·  ⏱ 2h

**One thing:** The January hole. Best seasonal content of the year.

1. Anchor: plan for January now (`docs/05 §8 №7` has the full text). This post lands harder than anything else in the quarter because it is genuinely frightening and genuinely fixable.
2. GBP W12.
3. All channels, plus a video.


### Day 79 — Tue 24 Nov  ·  ⏱ 1h

**One thing:** Video + capital allowances.

1. Short video on the January hole.
2. Second post: buying a van before 5 April, and why the invoice date decides the tax year (`docs/05 §8 №11`).


### Day 80 — Wed 25 Nov  ·  ⏱ 1h 15m

**One thing:** Community.

1. Community slot.


### Day 81 — Thu 26 Nov  ·  ⏱ 2h

**One thing:** Long video + year-end content.

1. Record: 'What to do before the tax year ends'.
2. Publish it as a page too — it will get search traffic every February.


### Day 82 — Fri 27 Nov  ·  ⏱ 1h 30m

**One thing:** Practical + numbers + Newsletter #7.

1. Practical post.
2. Newsletter #7: the January hole.
3. Production hour + numbers.


### Day 83 — Sat 28 Nov  ·  ⏱ 30m

**One thing:** Light.

1. Human post.


### Day 84 — Sun 29 Nov  ·  ⏱ 30m

**One thing:** Week ahead.

1. Week-ahead post.


### Day 85 — Mon 30 Nov  ·  ⏱ 2h

**One thing:** Shutdown checklist week.

1. Anchor: the nine-item shutdown checklist (`docs/05 §8 №8`).
2. GBP W13.
3. Highly practical, highly shared, and it positions you for January enquiries.


### Day 86 — Tue 1 Dec  ·  ⏱ 1h

**One thing:** Video.

1. Short video: get every invoice out before the 18th.


### Day 87 — Wed 2 Dec  ·  ⏱ 1h 15m

**One thing:** Community + 90-day reviews.

1. Community slot.
2. **Run the 90-day review with every client onboarded in September** (`docs/12 Email 5`). Twenty minutes each. This is where the £199 client becomes the £366 client.


### Day 88 — Thu 3 Dec  ·  ⏱ 2h

**One thing:** Case study + planning.

1. Write up the first case study properly.
2. Draft the month 4–6 content themes off the back of what actually got engagement, not what you assumed would.


### Day 89 — Fri 4 Dec  ·  ⏱ 2h

**One thing:** The 90-day review of the business.

1. **Full review against `docs/14 §What good looks like at day 90`.** Be honest about every line.
2. Cut the bottom half of the channel map. You now have real data on which channels produce calls and which produce nothing.
3. Decide the month 4–6 plan.


### Day 90 — Sat 5 Dec  ·  ⏱ 1h

**One thing:** Day 90. Write down what you learned.

1. Final numbers: booked calls/month, cost per call, clients, list size, reviews, community contributions.
2. Write a one-page honest note: what worked, what did not, what you would not do again.
3. **Then book the session with me.** The list of what I need from you is in `docs/18`.

---

# The fallback plan — if a week goes wrong

It will. A big job lands, someone's off sick, the week disappears. Here is what to protect and what
to drop, in order.

**Never drop (25 minutes a week):**
```
Monday GBP post          5 min   Posts expire after 7 days. A stale profile reads as "gone bust".
Monday anchor post      15 min   The one post that carries the week.
Reply to comments        5 min   Not replying is worse than not posting.
```

**Drop in this order when you have to:**
```
1. The Saturday light post      — nobody notices
2. The Sunday week-ahead        — merge it into Monday
3. Instagram and TikTok         — lowest direct return of the set
4. The long video               — batch two next week instead
5. The carousel                 — reuse an old one
6. The community slot           — LAST. It is slow, it compounds, and stopping resets it.
```

**Never drop the community slot for two weeks running.** Reddit and forum credibility decays and the
accounts go quiet in a way that is visible.

---

# Total time commitment, honestly

| Period | Hours/week | What it covers |
|---|---|---|
| Phase 0 (pre-launch) | ~16 hours total | One-off setup, most of it never repeated |
| Days 1–30 | 9–11 h/wk | Launch month, heaviest by design |
| Days 31–60 | 7–8 h/wk | Plus client onboarding when it starts |
| Days 61–90 | 6–7 h/wk | The rhythm is established and the library is built |
| Steady state | **2–3 h/wk** | Monday anchor, Wednesday community, Friday production |

If it is taking more than three hours a week after day 90, either it is working and you hire, or you
are overproducing for channels that are not returning. Both have obvious answers.

---

# The printable week

Pin this up. It is the whole system.

```
┌──────────────────────────────────────────────────────────────┐
│  MON 07:30   Anchor post → LinkedIn, X, FB, IG               │
│              GBP post (expires in 7 days — never skip)       │
│              Reply to everything from the weekend            │
├──────────────────────────────────────────────────────────────┤
│  TUE         Short video → TikTok, Reels, Shorts             │
│              Native upload to each. Never cross-post.        │
├──────────────────────────────────────────────────────────────┤
│  WED 17:30   Carousel → Instagram + LinkedIn document        │
│              COMMUNITY SLOT — one real answer, no link       │
├──────────────────────────────────────────────────────────────┤
│  THU         The week's big piece — long video or page       │
│              Newsletter, on the fortnight                    │
├──────────────────────────────────────────────────────────────┤
│  FRI 16:00   Practical post (a tool, a template, a date)     │
│              PRODUCTION HOUR — next week written & scheduled │
│              LOG THE FOUR NUMBERS                            │
├──────────────────────────────────────────────────────────────┤
│  SAT         One light human post. 15 minutes.               │
│  SUN         Week-ahead deadlines post. 20 minutes.          │
└──────────────────────────────────────────────────────────────┘

THE FOUR NUMBERS, every Friday:
   Booked discovery calls  ·  Cost per booked call
   Guide downloads         ·  GBP calls + directions + clicks
```

---

# The hard dates inside these 90 days

Everything with ⚠️ against it in the plan above.

| Date | Day | What |
|---|---|---|
| Fri 18 Sep | 12 | CIS return for month to 5 Sep — **the 19th is a Saturday, work to Friday** |
| Tue 22 Sep | 16 | CIS/PAYE electronic payment |
| Mon 5 Oct | 29 | MTD quarter ends (6 Jul – 5 Oct) |
| Mon 19 Oct | 43 | CIS return, month to 5 Oct |
| **Sat 7 Nov** | **62** | **MTD quarterly update due** — the biggest date in the window |
| Thu 19 Nov | 74 | CIS return, month to 5 Nov |
| Fri 18 Dec | — | Last useful invoicing day before the Christmas shutdown |

*Verified against the standard quarterly periods and the CIS monthly cycle. Where a deadline falls on
a weekend, work to the last working day before it.*
