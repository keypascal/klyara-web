# Klyara — Email Programme
### Provider decision, full sequences, 24 newsletters (a full year), signature, deliverability

---

# PART 1 — The provider decision

## Use Brevo. Start today, free.

You asked for a decision, so: **Brevo**, and don't spend another hour comparing.

**Why it's right for Klyara specifically:**

1. **It's already in the Build Manual's stack.** One less vendor relationship, one less subscription
   to reconcile, and the architecture in Part 2 already assumes it.
2. **Pricing model fits the shape of this list.** Brevo charges by *emails sent*, not by contacts
   held. Klyara's list will be thousands of subscribers receiving two emails a month — a
   contact-priced provider (Mailchimp, Kit) charges you for every subscriber every month whether you
   email them or not. On a fortnightly newsletter, send-based pricing is materially cheaper, and the
   gap widens as the list grows.
3. **EU-based (France).** You're handling UK small-business contact data under UK GDPR, with an ICO
   registration and a subprocessor list in the engagement letter. An EU processor is a shorter
   conversation than a US one, and it matches the Supabase EU/UK region decision already made.
4. **Transactional email is in the same account.** Portal password resets, receipt-upload
   confirmations, invoice reminders — all from one platform, one set of DNS records, one reputation
   to manage. This matters more than it sounds: split your sending across two providers and you
   maintain two domain reputations.
5. **SMS in the same account.** "CIS return due Friday" as a text is going to outperform email with
   this audience by a wide margin. Having it sit in the same tool as the email automation means you
   can build one workflow, not two integrations.
6. **The automation builder is on the low tiers.** Kit and Mailchimp gate real automation behind
   expensive plans. You need branching workflows from day one for the lead-magnet sequences.

**What I considered and rejected:**

- **MailerLite** — genuinely nice, slightly better editor, comparable price. Rejected only because
  Brevo's transactional + SMS in one account is worth more to Klyara than a nicer editor. If you
  already hated Brevo's UI, this is the switch.
- **Kit (ConvertKit)** — built for creators selling courses. Contact-priced, and you'd pay for the
  half of the list that never opens anything. Wrong shape.
- **Mailchimp** — expensive, contact-priced, and has been steadily removing things from lower tiers.
  No reason to choose it in 2026.
- **Zoho Campaigns** — cheap and pairs with Zoho Mail (already in the stack for mailboxes). Genuine
  runner-up on cost. Rejected because the automation builder is weaker and the deliverability
  reputation is a step below Brevo's.

**The self-hosted answer, since I know you'll ask:** **Listmonk + Amazon SES.** Listmonk is
MIT-licensed, single Go binary, runs on the VPS you already have, and SES sends at roughly $0.10 per
thousand emails. At 10,000 subscribers getting two emails a month it costs pennies against tens of
pounds for Brevo, and you own the data outright.

**Don't do it yet.** Not because it's wrong — because at launch you have no list, no sending
reputation, and a compliance chain to close. SES will also put you in a sandbox and make you justify
your sending before granting production access, which is another queue to sit in during a launch
month. Run Brevo until the list passes about **5,000 subscribers**, then migrate. Set that as a
written trigger the same way the Manual sets the Dext trigger at 10–15 clients. The migration is
straightforward: export CSV, import to Listmonk, re-point DNS.

**Cost expectation:** free while you're under 300 emails/day (that's a 4,000-person list on a
fortnightly send, comfortably). First paid tier lands somewhere around £7–9/month. Confirm current
pricing at signup — every provider in this space repriced at least once in the last two years.

---

# PART 2 — List architecture

Set these up before you write a single email. Retrofitting segmentation onto a mixed list is
miserable.

## Lists

| List | Source | Gets |
|---|---|---|
| **Newsletter** | Site signup form | Fortnightly newsletter + welcome sequence |
| **MTD Guide** | `/guide.html` download | 5-email MTD nurture, then joins Newsletter |
| **Launch Kit** | `/launch-kit.html` download | 4-email digital nurture, then joins Newsletter |
| **Solo Waitlist** | MTD-threshold enquirers | Founding-rate sequence, quarterly MTD reminders |
| **Clients** | Onboarding | Operational emails only. **Never** marketing sends. |
| **Partners** | Accountants, brokers | Quarterly partner update |

## Contact attributes to capture from day one

```
FIRSTNAME        - personalisation, and it noticeably lifts open rates
BUSINESS_TYPE    - sole_trader | ltd | partnership
TRADE            - builder | electrician | plumber | groundworks | roofing | other
CIS_ROLE         - contractor | subcontractor | both | neither
MTD_STATUS       - in_2026 | in_2027 | in_2028 | out | unknown
SOURCE           - which magnet or channel
TOWN             - local segmentation for GBP/ads alignment
```

**Ask for the absolute minimum on the form.** Email and first name. That's it. Every extra field
costs you conversions. Everything else gets enriched later via a one-question email (Newsletter #3
does exactly this).

## Automation logic

```
Downloads MTD Guide
  → send Guide immediately (transactional)
  → 5-email MTD sequence over 12 days
  → tag MTD_STATUS from link clicks in email 2
  → move to Newsletter list
  → if clicked "I think I'm in scope" → also add to Solo Waitlist

Downloads Launch Kit
  → send Kit immediately
  → 4-email sequence over 10 days
  → move to Newsletter list

Joins Newsletter directly
  → 3-email welcome over 6 days
  → fortnightly newsletter from the next scheduled send

Books a discovery call
  → confirmation + prep email immediately
  → reminder 24h before
  → suppress from all marketing until the call outcome is logged
```

## Suppression rules — non-negotiable

- **Clients never receive marketing sends.** A client getting a "join the waitlist" email is a
  credibility event you can't undo.
- **Anyone with a call booked** is suppressed from marketing until the outcome is recorded.
- **Hard bounces removed immediately**, soft bounces after three.
- **Unengaged after 6 months** (no open, no click) → one re-permission email → remove. A clean list
  of 800 outperforms a dirty list of 4,000, and this is what keeps you out of spam folders.

---

# PART 3 — Compliance, plainly

You're a bookkeeping firm holding contact data. Get this right the first time.

- **UK GDPR / PECR.** B2B email to corporate subscribers (ltd companies, LLPs) can go on legitimate
  interests. **Sole traders and partnerships are treated as individuals** — they need consent.
  Since most of your Solo audience *is* sole traders, **run the whole list on consent**. Simpler,
  safer, and a consented list performs better anyway.
- **Every email needs:** an unsubscribe link that works in one click, your trading name, and a
  postal address. Brevo handles the mechanics; you supply the address.
- **No pre-ticked boxes.** Ever.
- **Cold outreach goes from `tryklyara.com`**, never the main domain. This is already in the Build
  Manual and it's the single most important deliverability decision in the whole plan.
- **Record consent**: date, time, IP, form. Brevo logs this. Don't delete it.
- **Data processing:** add Brevo to the subprocessor list in the engagement letter and the privacy
  notice, alongside Supabase, Intuit and the rest.

---

# PART 4 — Deliverability setup (do this before the first send)

```dns
; SPF — one record only, never two
klyara.com.  TXT  "v=spf1 include:spf.brevo.com ~all"

; DKIM — Brevo generates the exact values; add both
mail._domainkey.klyara.com.  TXT  "k=rsa; p=<from Brevo>"

; DMARC — start at none, watch reports for two weeks, then tighten
_dmarc.klyara.com.  TXT  "v=DMARC1; p=none; rua=mailto:dmarc@klyara.com; pct=100; adkim=r; aspf=r"

; After two clean weeks of reports:
_dmarc.klyara.com.  TXT  "v=DMARC1; p=quarantine; rua=mailto:dmarc@klyara.com; pct=100"

; Then, once confident:
_dmarc.klyara.com.  TXT  "v=DMARC1; p=reject; rua=mailto:dmarc@klyara.com"

; BIMI — optional, later. Needs p=quarantine or stricter plus a VMC certificate.
; Puts the Klyara mark next to every email in Gmail. Worth it at scale, not at launch.
```

**Warm-up schedule.** A brand-new domain that suddenly sends 2,000 emails goes straight to spam. Ramp:

| Days | Max sends/day | Send to |
|---|---|---|
| 1–3 | 20 | Yourself, both founders, friends, the partner accountant |
| 4–7 | 50 | Earliest and warmest subscribers |
| 8–14 | 150 | Most engaged segment |
| 15–21 | 400 | Broaden |
| 22+ | Full list | Normal sending |

**Sender identity:**
```
From name:     Craig at Klyara
From address:  craig@klyara.com
Reply-to:      craig@klyara.com   ← a real monitored inbox, not no-reply
```
A person's name in the From field outperforms a brand name substantially in B2B. And **never use
`no-reply@`** — it suppresses replies, replies are the strongest positive deliverability signal there
is, and for a service business the replies *are* the leads.

**Subject line rules for this audience:**
- Under 45 characters — most will read on a phone, on site, in daylight
- No emoji in the subject. This audience reads them as spam.
- No ALL CAPS, no "FREE", no exclamation marks, no "act now"
- A date or a number in the subject beats a clever line every time

---
---

# PART 5 — SEQUENCE A: Newsletter welcome (3 emails, 6 days)

*Trigger: signs up to the fortnightly newsletter directly.*

---

## A1 — Immediate
**Subject:** `You're in. Here's what to expect.`
**Preview text:** `Two emails a month. Every deadline before it bites.`

```
Hi {{FIRSTNAME}},

Thanks for signing up.

Here's the deal, so you know exactly what you've agreed to:

Two emails a month. That's it. Not two a week, not one every time I have a thought.

Each one has the deadlines coming up, one thing worth knowing about CIS, VAT, MTD or getting paid,
and nothing else. No filler, no "10 productivity hacks", no motivational quotes.

If a fortnight goes by and I haven't got anything useful, you won't hear from me. I'd rather send
eleven emails a year that you read than twenty-four you delete.

Three things you can have right now, free, no forms:

📘 The MTD guide — 15 pages, plain English, whether you're in scope and what to do
   klyara.com/guide.html

🧮 Twelve calculators — job margin, CIS deduction, VAT, day rate, deadline checker
   klyara.com/tools.html

🧰 The Digital Launch Kit — 16 pages on winning work online, for firms that rely on word of mouth
   klyara.com/launch-kit.html

One more thing: hit reply and tell me what you do — builder, sparks, plumber, groundworks,
whatever it is. It takes you five seconds and it means I stop sending you things that don't apply to
you.

Craig
Klyara — the back office for small construction firms

P.S. Signing up gets you 10% off your first three months if you ever come on board. No expiry, no
pressure. It'll be here when you want it.
```

---

## A2 — Day 3
**Subject:** `The MTD thing that catches subbies out`
**Preview text:** `Your bank balance is telling you the wrong number.`

```
Hi {{FIRSTNAME}},

One thing, because it's caught out more people than anything else I've written about this year.

Making Tax Digital for Income Tax started in April 2026 for anyone with qualifying income over
£50,000. Most people know that bit.

Here's the bit they don't:

Qualifying income is measured GROSS. Before expenses. And before CIS deductions.

So:

  You invoiced          £55,000
  CIS took (20%)        £11,000
  You banked            £44,000

  HMRC counts           £55,000

You're over the threshold. You're in MTD. And your bank statement spent the entire year telling you
that you weren't.

If you're anywhere near that line, go and look at your gross invoices for 2024/25 — that's the year
HMRC assesses for the April 2026 start.

And if you're comfortably under: the threshold drops to £30,000 in April 2027 and £20,000 in April
2028. For a lot of subcontractors that's not a question of if, it's when.

The full guide is here, free, no email needed — you're already on the list:
klyara.com/guide.html

If you want me to just tell you whether you're in scope, reply with your rough gross invoicing for
last year and I'll tell you straight. Two minutes, no pitch.

Craig
```

---

## A3 — Day 6
**Subject:** `Quick question — what do you actually do?`
**Preview text:** `One click. It stops me emailing you irrelevant things.`

```
Hi {{FIRSTNAME}},

Short one.

I'd rather send you things that apply to you than things that don't, so — one click:

  → I'm a sole trader / self-employed
  → I run a limited company
  → I'm a subcontractor (CIS deducted from me)
  → I'm a contractor (I deduct from subbies)
  → I'm both

[each of these is a link that tags the contact and thanks them]

That's the whole email. Click one and you're done.

The next newsletter goes out on {{NEXT_SEND_DATE}}. It'll have every deadline for the month and one
thing worth knowing.

Craig

P.S. If none of those fit — reply and tell me. I read them all.
```

---
---

# PART 6 — SEQUENCE B: MTD Guide download (5 emails, 12 days)

*Trigger: downloads the MTD guide. This is your highest-intent audience — they've self-identified as
worried about MTD. Treat it accordingly.*

---

## B1 — Immediate (transactional)
**Subject:** `Your MTD guide`
**Preview text:** `Attached, and the two pages worth reading first.`

```
Hi {{FIRSTNAME}},

Here's the guide: [DOWNLOAD THE MTD GUIDE →]

Fifteen pages. If you only read two of them, read pages 4 and 5 — that's the "are you actually in
scope" bit, and it's where most people find out something they didn't expect.

The short version, in case you're on site and can't open a PDF:

• MTD for Income Tax started April 2026 at £50,000 qualifying income
• April 2027 it drops to £30,000. April 2028, £20,000.
• Qualifying income is GROSS — before expenses, before CIS
• You send HMRC a summary every three months, then a final declaration on 31 January
• Quarters end 5 Jul / 5 Oct / 5 Jan / 5 Apr
• Updates are due 7 Aug / 7 Nov / 7 Feb / 7 May

Over the next couple of weeks I'll send you four more emails: whether you're in scope, what a
quarterly update actually involves, what "digital records" means in practice, and what to do if
you're behind.

Then I'll stop, and you'll just get the fortnightly newsletter like everyone else.

Craig
Klyara — the back office for small construction firms
020 8058 1496

P.S. If you'd rather just ask a human whether MTD applies to you, reply to this email. I answer them
myself and there's no pitch on the end of it.
```

---

## B2 — Day 2
**Subject:** `Are you actually in scope? One question.`
**Preview text:** `It's not the number in your bank.`

```
Hi {{FIRSTNAME}},

Let's settle it.

Add up your GROSS self-employment income for the 2024/25 tax year. Gross means:

  ✓ Before any expenses
  ✓ Before CIS deductions
  ✓ Before anything at all

Add any gross rental income to it.

Is that number over £50,000?

  → YES, over £50,000        (you're in MTD now — click here)
  → Between £30k and £50k    (you're in from April 2027 — click here)
  → Between £20k and £30k    (you're in from April 2028 — click here)
  → Under £20,000            (you're out for now — click here)

[each tags MTD_STATUS and sends a short tailored reply]

Two things people get wrong at this exact point:

1. They use their bank balance. If CIS is deducted from you, your bank balance is roughly 20% below
   the number HMRC is using. That gap is what puts people over the line without realising.

2. They forget the rental income. It's added to self-employment income, not assessed separately. A
   builder invoicing £40,000 with a flat bringing in £12,000 gross is over £50,000 and in scope now.

Click whichever one fits and I'll send you the bit that's actually relevant to you.

Craig
```

---

## B3 — Day 5
**Subject:** `What a quarterly update actually involves`
**Preview text:** `Less than you think. Genuinely.`

```
Hi {{FIRSTNAME}},

People hear "four submissions a year instead of one" and picture four tax returns.

It isn't that. Not close.

WHAT A QUARTERLY UPDATE IS

A summary of your income and expenses for that three-month period, by category, sent from compatible
software. Totals. That's the whole thing.

WHAT IT ISN'T

  ✗ Not a tax return
  ✗ Not a tax calculation
  ✗ Nothing to pay
  ✗ Not final — you can correct it later
  ✗ No reliefs or adjustments needed at this stage

All the actual tax work still happens once a year, at the final declaration on 31 January. That
hasn't changed.

SO WHAT HAS ACTUALLY CHANGED?

The records. Not the return.

You now have to keep digital records as you go, rather than assembling them in one panic in January.
And practically, that's the whole reform. HMRC wants the bookkeeping to happen throughout the year
rather than retrospectively — and asking for four updates is how they make sure it does.

If your books are already up to date monthly, MTD is about twenty minutes a quarter.

If your books are a carrier bag in the van, MTD isn't four times the work — it's four times the
panic. And that's the real reason to fix it.

Next email: what "digital records" actually means, because it's more specific than people assume and
a spreadsheet may or may not be enough.

Craig
```

---

## B4 — Day 8
**Subject:** `Does a spreadsheet count?`
**Preview text:** `Sometimes. But probably not the way you're using it.`

```
Hi {{FIRSTNAME}},

Most asked question I get on MTD. Straight answer:

A spreadsheet can be part of a compliant setup — but only if it's linked to software that can submit
to HMRC, via what HMRC calls "bridging software", with digital links between the two.

"Digital links" is the important phrase. It means the data has to move electronically. Copying a
figure from a spreadsheet and typing it into something else breaks the chain, and that's not
compliant no matter how accurate the number is.

So in practice, for most builders: a spreadsheet plus bridging software is more moving parts, more
things to go wrong, and more cost than just using proper software from the start.

WHAT DIGITAL RECORDS ACTUALLY REQUIRE

  ✓ Each sale recorded digitally — date, amount, category
  ✓ Each purchase recorded digitally — date, amount, category
  ✓ Records kept as you go, not reconstructed later
  ✓ Data flowing digitally from record to submission, no re-typing

  ✗ You do NOT have to photograph every receipt — but you do have to keep them, and photographing
    them is far easier than keeping paper in a van

THE ONE THING THAT MAKES ALL OF THIS EASY

Connect your business bank account to your software. Properly connected, feeding automatically — not
exported and typed in.

That single change does about 80% of the work of digital record-keeping on its own, and it takes ten
minutes. If you do nothing else after reading this, do that.

Next one is the last of these, and it's for anyone who's reading this thinking "I'm already behind".

Craig
```

---

## B5 — Day 12
**Subject:** `If you're already behind`
**Preview text:** `It's recoverable. Here's the order to do it in.`

```
Hi {{FIRSTNAME}},

Last one in this series.

If you're reading these thinking "this all applies to me and I've done none of it" — that's most
people, and it's genuinely recoverable. It's a weekend, not a crisis.

Here's the order. Don't do them out of order, because each one makes the next one easier.

1. CONNECT THE BANK FEED. Every business account. Ten minutes. Does most of the work.

2. RECEIPTS. Every photo on your phone, every bit of paper in the van. One sitting. You're only
   entering the ones that aren't already on the bank feed, so it's faster than it sounds.

3. RECONCILE. Zero unmatched transactions. This is where you find the payment that came in that you
   never matched to an invoice — and were about to chase.

4. CIS STATEMENTS. Chase every missing payment and deduction statement now, while the contractor
   still remembers the job. Every unevidenced pound of CIS is tax you pay twice.

5. REVERSE CHARGE CHECK. Last ten sales invoices, four questions each. Two minutes. Highest-value
   two minutes on the list.

6. THE NUMBER. Margin by job, what you're owed by age, retentions outstanding, bank vs 30 days out.

That's it. That's the whole quarter-end routine, and once you've done it once it takes under an hour
each time.

The full checklist is on the site as one page, free: klyara.com

⛔ HOLD-UNTIL-AML CTA:
If you'd rather not do it at all — that's what Klyara is. Bookkeeping, CIS, reverse charge coding,
payroll and the MTD filing, handled monthly for a fixed fee from £59 + VAT. We open for clients
shortly and I'm holding a founding rate for the first ten firms on the list. Reply "LIST" and I'll
add you. No payment, no commitment.

✅ POST-AML CTA:
If you'd rather not do it at all — that's what Klyara is. Bookkeeping, CIS, reverse charge coding,
payroll and MTD filing, handled monthly for a fixed fee from £59 + VAT.
Book a free 20-minute call: [BOOK A CALL →]
I'll tell you what your situation actually needs, and if that's nothing, I'll tell you that too.

Either way, you're on the fortnightly list now. Two emails a month, every deadline before it bites.

Craig
```

---
---

# PART 7 — SEQUENCE C: Digital Launch Kit download (4 emails, 10 days)

*Trigger: downloads the Launch Kit. Different intent — these people want more work, not tax help.
Do not lead with tax.*

---

## C1 — Immediate
**Subject:** `Your Digital Launch Kit`
**Preview text:** `Start with section 2. It's the one that pays.`

```
Hi {{FIRSTNAME}},

Here it is: [DOWNLOAD THE DIGITAL LAUNCH KIT →]

Sixteen pages on winning construction work without relying entirely on word of mouth.

If you only do one thing from it, do section 2 — the Google Business Profile setup. It's free, it
takes about forty minutes, and for a local building firm it will outperform anything else in the
document, including a website.

Genuinely. A verified Google Business Profile with a dozen real reviews will bring you more work than
a £2,000 website with none.

Over the next week and a bit I'll send you three more: what actually makes a builder's website
convert, how to get reviews without feeling like a nuisance, and the quoting problem that costs firms
more work than anything else.

Craig
Klyara — the back office for small construction firms
020 8058 1496
```

---

## C2 — Day 3
**Subject:** `Why builders' websites don't get enquiries`
**Preview text:** `It's almost never the design.`

```
Hi {{FIRSTNAME}},

I look at a lot of building firms' websites. The ones that don't get enquiries almost never have a
design problem.

They have these problems, in this order:

1. NO PHONE NUMBER AT THE TOP
Your customer is on a phone, standing in a kitchen they want extending. They want to tap a number.
If they have to scroll or find a contact page, a third of them are gone. Number top right, tappable,
on every page.

2. NO PHOTOS OF ACTUAL WORK
Stock photos of a generic kitchen tell them nothing. Twelve phone photos of jobs you've actually
finished tell them everything. Bad lighting is fine. Real is what matters.

3. NO AREA NAMED
"We cover the local area" ranks for nothing and reassures nobody. Name the towns. "Extensions and
loft conversions in [town], [town] and [town]." That's both the SEO and the reassurance, in one line.

4. NO PRICES, NOT EVEN A RANGE
You don't have to quote. But "most of our extensions run between £X and £Y" filters out the people
who were never going to proceed and massively increases the quality of the ones who call. Every firm
resists this and every firm that does it gets better enquiries.

5. NO REVIEWS ON THE PAGE
Not a link to reviews. The actual words, on the page, with names. It's the single highest-converting
element on any trades website.

None of that is design. All of it is content, and all of it you can fix this week on the site you've
already got.

Next: getting reviews without feeling like a pest.

Craig
```

---

## C3 — Day 6
**Subject:** `Asking for reviews without feeling like a pest`
**Preview text:** `The timing matters more than the wording.`

```
Hi {{FIRSTNAME}},

Every builder I know hates asking for reviews. Here's how to make it painless.

THE TIMING IS THE WHOLE THING

Ask when the customer is happiest. That's not when the invoice is paid — it's the moment the job is
finished and they're standing in it, looking at it.

That's the window. It's about forty-eight hours wide and most people miss it entirely, then ask
three weeks later by email when the feeling's gone.

THE ASK — say this, out loud, on site

"Really glad you're happy with it. Can I ask a favour — would you mind putting a couple of lines on
Google? It's the main way people find us. I'll text you the link now so you don't have to look for
it."

Then text the link before you leave. From your phone, standing there.

The "I'll text you the link now" is doing all the work. An ask without a link is a request for
homework, and homework doesn't get done.

WHERE TO SEND THEM

Google, first and always. It feeds your Business Profile, it shows in search results, and it's the
one prospects actually look at. Trustpilot second if you want it. Ignore everything else.

THE NUMBERS THAT MATTER

Ten reviews is the threshold where a listing starts looking established. Twenty-five and you're
credible. Beyond that it's about recency more than volume — five reviews in the last three months
beats forty from two years ago.

Two a month, forever. That's the target. It's one ask a fortnight.

NEVER

Don't offer anything in exchange. Don't write them yourself. Don't buy them. For a firm that
eventually wants a bookkeeper handling its money, being caught faking reviews is not a small thing.

Last one on Friday — the quoting problem.

Craig
```

---

## C4 — Day 10
**Subject:** `The quote that loses you the job`
**Preview text:** `It's usually the fourth day, not the price.`

```
Hi {{FIRSTNAME}},

Last one from this series.

Most lost jobs aren't lost on price. They're lost on speed and on how the quote arrives.

SPEED
A quote sent within 24 hours wins dramatically more often than the same quote sent four days later.
Not because it's better — because by day four the customer has two others and you've become the one
who seemed less bothered.

If you can't get a full quote out in 24 hours, send a holding message the same day: "Thanks for
seeing me today — I'll have a full quote to you by Thursday." That single text keeps you in it.

FORMAT
A number in a text message is not a quote. It's a number. And it gets compared to other numbers,
which is a competition you can only lose.

A quote should have: what's included, what isn't, how long it'll take, when you could start, payment
stages, and the number. On a document with your name on it.

The same price, presented properly, wins against a cheaper number in a text more often than you'd
believe. You are not selling the price — you're selling the impression that you'll turn up and do
what you said.

FOLLOW UP ONCE
One message, three or four days later: "Just checking you got the quote — happy to talk through any
of it." That's it. One.

Most firms send none. A handful send five and become the desperate one. One is right.

THE THING NOBODY DOES
Ask why, when you lose. "No problem at all — do you mind me asking, was it price or timing?"

Half will tell you. And if the answer is consistently timing rather than price, you've just found out
that you don't have a pricing problem, you have a scheduling problem — and you've been dropping your
prices to fix the wrong thing.

That's the series done. You're on the fortnightly list now — two emails a month, deadlines and one
useful thing.

Craig

P.S. If the reason the quotes are slow is that you're doing the books at eleven at night, that's a
fixable problem and it's the one we actually solve. klyara.com
```

---
---

# PART 8 — THE FORTNIGHTLY NEWSLETTER: 12 issues, six months, full copy

**Name:** *The Klyara Fortnightly*
**Cadence:** Every other Thursday, 07:00 UK. Builders read email before the day starts or after
they've packed up. 07:00 puts you at the top of the inbox when the phone comes off the charger.

**Fixed structure — never vary it. Familiarity is why people keep opening.**
```
1. DATES        — every deadline in the next fortnight. Always first. This is why they subscribed.
2. ONE THING    — the single useful piece. 300–500 words.
3. THE TOOL     — one calculator or template, linked.
4. FROM THE SITE— one link to a guide, video or post.
5. SIGN-OFF     — Craig, one line, one soft CTA.
```

**Schedule:**

| # | Date | Theme |
|---|---|---|
| 1 | Thu 10 Sep 2026 | The gross income trap |
| 2 | Thu 24 Sep 2026 | Quarter end is coming |
| 3 | Thu 8 Oct 2026 | Quarter closed — the 33-day window |
| 4 | Thu 22 Oct 2026 | Gross payment status |
| 5 | Thu 5 Nov 2026 | ⚠️ Two days to the MTD deadline |
| 6 | Thu 19 Nov 2026 | Pricing: what a job actually costs you |
| 7 | Thu 3 Dec 2026 | The January hole |
| 8 | Thu 17 Dec 2026 | Shutdown checklist |
| 9 | Thu 7 Jan 2027 | 31 January, and payments on account |
| 10 | Thu 21 Jan 2027 | ⚠️ Ten days |
| 11 | Thu 4 Feb 2027 | Capital allowances before 5 April |
| 12 | Thu 18 Feb 2027 | The £30,000 threshold is coming |

---

## №1 — Thursday 10 September 2026
**Subject:** `19 Sep, and the MTD trap`
**Preview:** `Your bank balance is telling you the wrong number.`

```
📅 DATES

Sat 19 Sep — CIS return + payment, month to 5 Sep (22nd if paying electronically)
Mon 5 Oct  — MTD quarter ends (6 Jul – 5 Oct)
Sat 7 Nov  — that quarter's update due to HMRC

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the number HMRC uses isn't the one in your bank

Making Tax Digital for Income Tax started in April 2026 for anyone with qualifying income over
£50,000. Most people know that part.

Here's the part that's caught out more subcontractors than anything else I've written about this
year: qualifying income is measured GROSS. Before expenses, and before CIS deductions.

  Invoiced      £55,000
  CIS took      £11,000
  You banked    £44,000
  HMRC counts   £55,000

You're in. Your bank statement said otherwise for twelve months.

The other thing people miss: rental income is added to it, not assessed separately. A builder
invoicing £40,000 with a flat bringing in £12,000 gross is over the line right now.

Go and look at your gross invoices for 2024/25 — that's the year HMRC assesses for the April 2026
start. If it's over £50,000, you're already in, and your first update was due on 7 August.

If it wasn't, look at the year after: the threshold drops to £30,000 in April 2027 and £20,000 in
April 2028.

━━━━━━━━━━━━━━━━━━━━━━━

🧮 THE TOOL: CIS deduction calculator
Work out gross-to-net either way round, including the materials split.
→ klyara.com/tools.html

📄 FROM THE SITE: the 15-page MTD guide. Free, no form.
→ klyara.com/guide.html

━━━━━━━━━━━━━━━━━━━━━━━

That's it. Back in a fortnight.

Craig
Klyara — the back office for small construction firms
Reply to this if you want me to tell you whether MTD has caught you. No pitch on the end of it.
```

---

## №2 — Thursday 24 September 2026
**Subject:** `11 days to quarter end`
**Preview:** `A weekend now, or a crisis in November.`

```
📅 DATES

Mon 5 Oct  — MTD quarter ends (6 Jul – 5 Oct) — 11 days
Mon 19 Oct — CIS return + payment, month to 5 Oct
Sat 7 Nov  — MTD quarterly update due

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the seven-job quarter end

If you're in MTD, everything from 6 July to 5 October needs to be in digital records by a week on
Monday. If July and August are currently photos on a phone and a bag in the van, that's fixable this
week. It is not fixable on 6 November.

One job a day. Each under twenty minutes.

1. BANK FEED — connect every business account. Connected and feeding, not exported and typed. Ten
   minutes, and it does about 80% of the work on its own.

2. RECEIPTS — every photo in the camera roll, every bit of paper. One sitting with the kettle on.
   Fuel, parking, tools under £100, trade counter on the personal card, PPE, the Sunday emergency run.

3. MIXED USE — van, phone, home office, workwear. Pick a defensible split, apply it consistently,
   write down why you picked it. HMRC has never objected to a consistent, defensible number.

4. RECONCILE — zero unmatched transactions. Watch for payments in that you never matched to an
   invoice. Nine times out of ten that's money you already had and were about to chase for.

5. CIS STATEMENTS — chase every missing one now, while the contractor still remembers the job. In
   February they won't. Every unevidenced pound of CIS is tax you pay twice.

6. REVERSE CHARGE — last ten sales invoices, four questions each. Two minutes, and it's the
   highest-value two minutes on this list.

7. THE NUMBER — margin by job, what you're owed by age, retentions outstanding, bank vs 30 days out.

Do one a day and you're closed off by next Thursday, six weeks ahead of the deadline.

━━━━━━━━━━━━━━━━━━━━━━━

🧮 THE TOOL: deadline checker — put your dates in, get reminders
→ klyara.com/tools.html

📄 FROM THE SITE: the quarter-end checklist as one printable page
→ klyara.com

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №3 — Thursday 8 October 2026
**Subject:** `Quarter closed. 30 days.`
**Preview:** `Plus: the retention money you've written off.`

```
📅 DATES

Mon 19 Oct — CIS return + payment, month to 5 Oct
Sat 7 Nov  — MTD quarterly update due — 30 days
Tue 5 Jan  — next MTD quarter ends

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: go and count your retentions

The quarter's closed and the update isn't due for a month, so here's something more profitable to do
with the next twenty minutes.

Count your retentions. Not "roughly". Actually count them.

Three percent or five percent held back on jobs that finished a year and a half ago. Defects
liability period long over. Nobody ever asked for it back, so nobody ever sent it.

Every firm I take on finds somewhere between four and fifteen thousand pounds they'd mentally written
off. Some of it genuinely isn't recoverable. A surprising amount of it is just sitting there because
nobody made the phone call.

Here is the entire system:

  Job  |  Amount held  |  Release date

That's it. Three columns. Put every retention on it. Diarise the release date. Ask on the day it
falls due — not three months later when you remember, by which point you're the awkward one bringing
up old business.

Firms that get their retentions back aren't tougher negotiators. They're the ones who wrote it down.

And while you're at it: the same list works for what you're holding from your subbies. If you're
sitting on retentions from subcontractors whose defects period ended, pay them. It costs you nothing
in the long run and it's the reason good subbies pick up your calls first.

━━━━━━━━━━━━━━━━━━━━━━━

🧮 THE TOOL: retention tracker template. Free, no email.
→ klyara.com/tools.html

📄 FROM THE SITE: "Why your building firm is always skint" — the four things that drain cash while the
P&L says you're fine.
→ klyara.com

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №4 — Thursday 22 October 2026
**Subject:** `Are you lending HMRC £24,000?`
**Preview:** `Gross payment status, and the three tests.`

```
📅 DATES

Thu 19 Nov — CIS return + payment, month to 5 Nov
Sat 7 Nov  — MTD quarterly update due — 16 days
Tue 5 Jan  — next MTD quarter ends

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: gross payment status

If you're a subcontractor having 20% deducted from every invoice, and you qualify for gross payment
status but have never applied — you are lending HMRC a lot of money, interest free, for up to a year.

On £120,000 of labour invoicing, that's £24,000 sat with HMRC instead of in your account. You get it
back. But you get it back after you file, which could be eighteen months after you earned it.

Meanwhile you're borrowing to buy materials.

THE THREE TESTS

BUSINESS TEST — you carry out construction work in the UK, and you run it through a bank account.
Straightforward for anyone actually trading.

TURNOVER TEST — your construction turnover excluding VAT and materials must be above the threshold
(currently £30,000 for a sole trader, and £30,000 per director or partner for companies and
partnerships, with an alternative company test). Check the current figures before applying.

COMPLIANCE TEST — this is the one that catches people. You must have filed and paid everything on
time in the last twelve months. Returns, PAYE, CIS, corporation tax, the lot. HMRC does allow a
small number of minor slips, but a pattern of late filing fails you.

WHY MOST PEOPLE WHO'D PASS HAVE NEVER APPLIED

No reason. They've never thought about it, or they tried once years ago, failed the compliance test,
and never went back.

If you failed before: the compliance test looks at the last twelve months. Twelve clean months and
you can apply again.

WORTH KNOWING: HMRC reviews gross status annually. Miss deadlines and it can be withdrawn — and
losing it midway through a year is considerably worse than never having had it, because your cash
flow has already adjusted.

Which is the real argument for having someone file on time every month, but I would say that.

━━━━━━━━━━━━━━━━━━━━━━━

🧮 THE TOOL: CIS calculator — see what 20% is actually costing you across a year
→ klyara.com/tools.html

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №5 — Thursday 5 November 2026 ⚠️
**Subject:** `MTD update due Saturday`
**Preview:** `Two days. Here's the 40-minute version.`

```
📅 DATES

⚠️ Sat 7 Nov — MTD quarterly update DUE (6 Jul – 5 Oct) — 2 DAYS
Thu 19 Nov — CIS return + payment, month to 5 Nov
Tue 5 Jan  — next MTD quarter ends

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: if it isn't done, here's the fastest legitimate route

Your quarterly update for 6 July to 5 October is due Saturday.

If you've been keeping records as you go, this is a ten-minute job — check the categories, submit.

If you haven't, here is the order that gets you there fastest:

1. Connect the bank feed. If you do nothing else, do this. It pulls three months of transactions in
   automatically and it's most of the job.

2. Categorise in bulk. Don't do it transaction by transaction. Sort by description, select all the
   fuel, categorise in one go. Then all the merchants. Then all the subbies. Twenty minutes.

3. Add the cash and personal-card purchases that aren't on the feed. Don't hunt for perfection —
   get the significant ones in.

4. Submit.

REMEMBER WHAT THIS SUBMISSION IS

It's a summary of totals. It isn't final, there's nothing to pay, and you can correct it later. The
actual tax work happens at the final declaration on 31 January.

So: submitting something reasonable on time beats submitting something perfect late. Get it in, then
tidy it up.

IF YOU GENUINELY CAN'T

Submit what you have. HMRC's late-submission penalties work on points — one late update is not a
disaster, but a habit of them is. And the correction mechanism exists precisely because HMRC expects
figures to be refined later.

Then spend December setting it up properly so January's quarter isn't the same weekend.

━━━━━━━━━━━━━━━━━━━━━━━

📄 FROM THE SITE: the full quarter-end checklist, one page
→ klyara.com

━━━━━━━━━━━━━━━━━━━━━━━

Craig

Reply if you're stuck. I'd rather answer a question on a Thursday than hear about a penalty in
January.
```

---

## №6 — Thursday 19 November 2026
**Subject:** `What that job actually cost you`
**Preview:** `The three costs nobody puts in the quote.`

```
📅 DATES

Thu 19 Nov — CIS return + payment, month to 5 Nov — TODAY
Mon 21 Dec — CIS return + payment, month to 5 Dec (19th is a Saturday)
Tue 5 Jan  — MTD quarter ends

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the three costs that never make it into the quote

Most building firms price labour and materials, add a percentage, and call it a quote. Then wonder
why a busy year produced no money.

Three things are missing.

1. YOUR OWN TIME, PRICED PROPERLY

Not the hours on the tools. The quoting, the site visits, the phone calls, the ordering, the chasing,
the arguing about the variation. If you're on site four days and in the office two, you're charging
for four days of a six-day week. Every job carries that overhead whether you price it or not.

Rule of thumb that works: for every day on site, budget half a day of everything else. Then decide
whether it's in the rate or in the overhead — but decide, don't ignore it.

2. THE COST OF BEING PAID LATE

An invoice paid in 60 days instead of 30 is a job you funded for an extra month. If you're on an
overdraft or a credit card to bridge it, that's real interest. If you're not, it's still real —
it's the job you couldn't take because the cash was tied up.

Price the customer's payment behaviour, not just the work. The main contractor who pays in 75 days
is not the same job as the private client who pays on completion, even at the same number.

3. THE JOBS THAT DIDN'T HAPPEN

If you quote six jobs to win two, the cost of the four you lost belongs in the two you won. That
might be a full day of site visits and quoting. If it isn't in your pricing, you're funding your own
sales process out of margin.

━━━━━━━━━━━━━━━━━━━━━━━

THE TEST

Take the last job you finished. Everything in, including the above. What did it actually make?

Most people find the answer is 8–12% below what they thought, and that the difference is entirely in
these three.

🧮 THE TOOL: job margin calculator — put the last one through it
→ klyara.com/tools.html

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №7 — Thursday 3 December 2026
**Subject:** `The January hole`
**Preview:** `It arrives every year and it surprises everyone every year.`

```
📅 DATES

Mon 21 Dec — CIS return + payment, month to 5 Dec (19th falls on a Saturday)
Tue 5 Jan  — MTD quarter ends (6 Oct – 5 Jan)
Sun 31 Jan — Final declaration + tax payment + payment on account
Sun 7 Feb  — MTD quarterly update due

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: plan for January now, because January is where building firms die

Here's what happens every year.

You work through to about the 20th of December. Sites shut. Nobody's paying invoices between
Christmas and New Year because the accounts departments are off.

You come back on the 5th of January. Sites are slow to restart, weather's against you, and the first
two weeks are half-speed.

Then on 31 January, HMRC wants your tax bill AND your first payment on account for the following
year. Which, if you had a good year, can be roughly 150% of what you were expecting.

So: five to six weeks of reduced income, followed by the single largest payment of your year.

That's the January hole. It arrives at exactly the same time every year and it surprises almost
everybody.

WHAT TO DO, THIS MONTH

1. Work out what you owe on 31 January now. Not in January. Now. If you don't know, that number is
   the most important thing in this email.

2. Get every invoice out before the 18th of December. Anything invoiced after that sits until the
   second week of January regardless of your terms.

3. Chase everything outstanding this week and next. "Just tidying the books before the break" is the
   most socially acceptable chasing line of the entire year. Use it.

4. Don't spend December's cash on January's van. It looks like a good month. It is one month
   carrying two.

5. If the 31 January number is genuinely unaffordable — talk to HMRC BEFORE the deadline. A Time to
   Pay arrangement agreed in advance is routine. The same conversation in February, after a missed
   payment, is a different conversation with penalties attached.

━━━━━━━━━━━━━━━━━━━━━━━

🧮 THE TOOL: cash position forecaster
→ klyara.com/tools.html

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №8 — Thursday 17 December 2026
**Subject:** `Before you shut down`
**Preview:** `Nine things, one hour, and January is 40% easier.`

```
📅 DATES

Mon 21 Dec — CIS return + payment, month to 5 Dec
Tue 5 Jan  — MTD quarter ends (6 Oct – 5 Jan)
Sun 31 Jan — Final declaration + tax payment + payment on account
Sun 7 Feb  — MTD quarterly update due

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the shutdown checklist

One hour before you finish. It makes January materially easier.

☐ 1. Every invoice out. Everything you've done that isn't invoiced, invoice today. Anything after
     tomorrow sits until the second week of January anyway.

☐ 2. Chase everything outstanding. "Just tidying up before the break" — the most acceptable chasing
     line of the year, and it works.

☐ 3. CIS return for the month to 5 December — due Monday 21st. Don't leave it in the pile.

☐ 4. Receipts in. Three months of them, one sitting. You'll thank yourself in the first week of
     January when the quarter closes on the 5th.

☐ 5. Chase missing CIS deduction statements. Contractors are shutting down too — after Christmas
     they'll have forgotten which job you mean.

☐ 6. Know your 31 January number. If you don't know it, find out this week. There is no version of
     January where that number is better news than it is now.

☐ 7. Diary the January dates: quarter ends 5th, tax due 31st, quarterly update due 7 February.

☐ 8. Tell your customers when you're back. One text. It stops the "are you around?" messages on
     Boxing Day and it gets you first in the queue for January starts.

☐ 9. Book the first week of January lighter than you think. It always goes slower than planned and
     an over-booked first week is how the whole month gets behind.

━━━━━━━━━━━━━━━━━━━━━━━

Have a proper break. The paperwork will still be there and it will not have got worse.

Back on 7 January.

Craig
```

---

## №9 — Thursday 7 January 2027
**Subject:** `31 January: two payments, not one`
**Preview:** `The payment on account catches people out every year.`

```
📅 DATES

Tue 19 Jan — CIS return + payment, month to 5 Jan
Sun 31 Jan — Final declaration + balancing payment + payment on account
Sun 7 Feb  — MTD quarterly update due (6 Oct – 5 Jan)

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: what's actually due on 31 January

This catches people every single year, so:

On 31 January you may be paying TWO things.

1. THE BALANCING PAYMENT — what you owe for the tax year that ended 5 April 2026, less anything
   you've already paid on account and less any CIS already deducted from you.

2. THE FIRST PAYMENT ON ACCOUNT for the current year — normally 50% of last year's tax bill, paid in
   advance.

Then a second payment on account follows on 31 July.

So if your bill for the year was £6,000 and you had nothing on account, 31 January is £6,000 plus
£3,000 = £9,000. Not £6,000.

The first year this happens is brutal, because it's 150% of a number you were already dreading. After
that it settles into a rhythm — but the first one has ended more building firms than bad weather has.

IF YOU'RE A CIS SUBCONTRACTOR, READ THIS BIT

Every pound of CIS deducted from you during the year counts toward this bill. If 20% has been coming
off all year, there's a decent chance you're owed a refund rather than owing anything.

But — and this is the whole point — you can only claim the deductions you can evidence. If you're
missing payment and deduction statements, you can't claim them, and you'll pay that tax twice.

Chase the missing ones this week. It is the highest-value hour available to you in January.

YOU CAN REDUCE PAYMENTS ON ACCOUNT

If you know this year will be lower than last, you can apply to reduce them. Be careful: reduce them
too far and HMRC charges interest on the shortfall. Reduce on evidence, not on optimism.

IF YOU CAN'T PAY

Talk to HMRC before 31 January. Time to Pay arrangements are routine and they're set up online for
smaller amounts. The conversation before the deadline is administrative. The one after it involves
penalties.

━━━━━━━━━━━━━━━━━━━━━━━

🧮 THE TOOL: CIS calculator + deadline checker
→ klyara.com/tools.html

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №10 — Thursday 21 January 2027 ⚠️
**Subject:** `Ten days`
**Preview:** `31 January. And what to do if the number's wrong.`

```
📅 DATES

⚠️ Sun 31 Jan — Final declaration + balancing payment + payment on account — 10 DAYS
Sun 7 Feb  — MTD quarterly update due (6 Oct – 5 Jan)
Fri 19 Feb — CIS return + payment, month to 5 Feb

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: ten days, in order

☐ TODAY — file it if it isn't filed. Even if you can't pay. The late FILING penalty and the late
  PAYMENT penalty are separate things. Filing on time and paying late costs you far less than doing
  neither, and it takes the worst penalty off the table entirely.

☐ TODAY — if you can't pay, set up Time to Pay. It's online for smaller balances. Do it before the
  31st.

☐ THIS WEEK — chase every missing CIS deduction statement. Unevidenced deductions are tax you pay
  twice. This is the last useful week to chase them.

☐ THIS WEEK — check whether your payment on account should be reduced. Only on evidence. Reduce it
  on optimism and HMRC charges interest on the difference.

☐ BEFORE THE 31st — check the figures actually look right. The commonest errors I see: CIS
  deductions entered as income, materials included in the CIS deduction calculation, and the
  payment on account forgotten entirely.

☐ THE 31st — pay. Allow for clearing time if you're not paying by card or faster payment.

☐ 1 FEBRUARY — put 7 February in the diary. Your MTD quarterly update for 6 Oct to 5 Jan is due a
  week later, and every year people file on the 31st, exhale, and miss it.

━━━━━━━━━━━━━━━━━━━━━━━

AND THEN

When it's done, do one thing: work out what you'll owe next 31 January, and start putting it aside
monthly.

A separate account, a standing order, 25–30% of what lands. It is the single change that turns
January from an event into a date.

Everyone knows this. Almost nobody does it. The ones who do never have a bad January again.

━━━━━━━━━━━━━━━━━━━━━━━

Craig

If it's gone wrong and you want someone to look at it — reply. I'd rather help in January than hear
about it in June.
```

---

## №11 — Thursday 4 February 2027
**Subject:** `Buying a van before April?`
**Preview:** `The timing is worth more than the haggling.`

```
📅 DATES

Sun 7 Feb  — MTD quarterly update due (6 Oct – 5 Jan) — 3 days
Fri 19 Feb — CIS return + payment, month to 5 Feb
Mon 5 Apr  — Tax year ends · MTD quarter ends
Apr 2027   — MTD threshold drops to £30,000

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: capital allowances, and why the date on the invoice matters

Two months left in the tax year. If you're planning to buy anything substantial — van, plant,
machinery, a decent run of tools — the date it goes on the invoice decides which tax year it lands
in.

THE BASICS

Most plant, machinery, tools and commercial vehicles qualify for the Annual Investment Allowance,
which lets you deduct the full cost from your profits in the year you buy it, up to a generous
annual limit that most small firms will never reach.

Full deduction. In year one. Not spread over the life of the asset.

WHY THE TIMING MATTERS

Buy on 3 April and it comes off this year's profit. Buy on 8 April and it comes off next year's.

Same van. Same money. Different year, and possibly a different tax rate.

The right answer depends on which year has the higher profit. If this year was strong and next looks
quieter — buy before 5 April. If this year was quiet and you're booked solid from April — wait.

That is a genuine decision worth making deliberately, and it's worth more than anything you'll
achieve by haggling on the price.

THREE THINGS TO WATCH

1. CARS ARE DIFFERENT. Cars generally don't get the Annual Investment Allowance and are treated
   under separate rules based on emissions. A commercial vehicle — a van, a pickup that genuinely
   qualifies — is treated as plant and machinery. The line between "van" and "car" for tax has been
   litigated and it is not always obvious. Check before you buy, not after.

2. FINANCE MATTERS. Hire purchase usually gets the allowance on the full cost when the asset is
   brought into use. A lease usually doesn't work that way at all. The finance structure changes the
   tax treatment substantially.

3. IT HAS TO BE IN USE. Ordered isn't enough. It generally needs to be in use in the business by
   the year end.

DON'T BUY THINGS FOR TAX REASONS

Worth saying plainly: spending £30,000 to save tax at 20% leaves you £24,000 worse off in cash. If
you need the van, the timing is worth optimising. If you don't need the van, no amount of tax relief
makes it a good purchase.

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №12 — Thursday 18 February 2027
**Subject:** `£30,000 from April. That's most subbies.`
**Preview:** `Six weeks. And this wave is much bigger than the first.`

```
📅 DATES

Fri 19 Feb — CIS return + payment, month to 5 Feb
Mon 5 Apr  — Tax year ends · MTD quarter ends (6 Jan – 5 Apr)
Apr 2027   — ⚠️ MTD threshold drops to £30,000
Fri 7 May  — MTD quarterly update due

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the £30,000 wave

From April 2027, Making Tax Digital for Income Tax applies to anyone with qualifying income over
£30,000.

The first wave, at £50,000, caught established sole traders and larger subbies. This one is different.
£30,000 gross is a working subcontractor. It's most of the trade.

And qualifying income is still measured GROSS — before expenses, before CIS. So:

  £30,000 gross invoicing is roughly £24,000 in the bank after 20% CIS.
  £24,000 in the bank puts you in MTD.

If you're a subbie who assumed this didn't apply to you, check the number you invoiced, not the
number you banked.

WHAT TO DO IN THE NEXT SIX WEEKS

1. WORK OUT IF YOU'RE IN. Gross self-employment income plus gross property income for 2025/26. Over
   £30,000, you're in from April 2027.

2. START THE DIGITAL RECORDS NOW, NOT IN APRIL. The single biggest mistake the first wave made was
   waiting for the start date. Get the bank feed connected and the receipts flowing this month, and
   April is a non-event. Leave it to April and your first quarter is a panic.

3. GET COMPATIBLE SOFTWARE. Whatever you use has to be able to submit to HMRC.

4. PUT THE DATES IN. Quarters end 5 Jul, 5 Oct, 5 Jan, 5 Apr. Updates due 7 Aug, 7 Nov, 7 Feb, 7 May.

THE HONEST VERSION

If your books are already running monthly, MTD is about twenty minutes a quarter and this email is
nothing to worry about.

If they're a bag in the van, MTD doesn't create four times the work — it creates four times the
panic, and it does it forever. Which is why the sensible move is to fix the bookkeeping between now
and April rather than to fix the deadline in August.

━━━━━━━━━━━━━━━━━━━━━━━

🧮 THE TOOL: MTD scope checker + deadline reminders
→ klyara.com/tools.html

📄 FROM THE SITE: the 15-page MTD guide, updated for the £30,000 threshold
→ klyara.com/guide.html

━━━━━━━━━━━━━━━━━━━━━━━

That's six months of these. Thank you for reading them.

If the answer to all of this is "I need someone to just handle it" — that's what Klyara is.
Bookkeeping, CIS, reverse charge, payroll and the quarterly filing, for a fixed monthly fee from
£59 + VAT. Twenty-minute call, no pitch: klyara.com

Craig
```

---
---

# PART 9 — Transactional emails

## Discovery call booked — confirmation
**Subject:** `Booked: {{DATE}} at {{TIME}}`
```
Hi {{FIRSTNAME}},

You're booked in for {{DATE}} at {{TIME}}. I'll call you on {{PHONE}}.

It'll take about twenty minutes. Nothing to prepare, but if you can have these to hand it makes it
more useful:

  • Roughly what you invoiced last year, gross
  • Whether you're a sole trader or a limited company
  • Whether CIS is deducted from you, or you deduct from others, or both
  • What you currently use for the books, if anything

I'll tell you what your situation actually needs. If that's nothing, or if it's something we don't
do, I'll tell you that — it's a twenty-minute call, not a sales process.

Need to move it? Reschedule here: {{RESCHEDULE_LINK}}

Craig
020 8058 1496
```

## Reminder — 24 hours before
**Subject:** `Tomorrow at {{TIME}}`
```
Hi {{FIRSTNAME}},

Quick reminder — I'm calling you tomorrow at {{TIME}} on {{PHONE}}.

If you're on site and it's a bad time, just move it: {{RESCHEDULE_LINK}}. Genuinely no problem, it's
easier than trying to talk over a breaker.

Craig
```

## Guide download — the delivery email
**Subject:** `Your {{GUIDE_NAME}}`
```
Hi {{FIRSTNAME}},

Here you go: [DOWNLOAD →]

If the link doesn't work, reply and I'll send it as an attachment.

Craig
Klyara — 020 8058 1496
```

## Waitlist confirmation (pre-AML)
**Subject:** `You're on the list`
```
Hi {{FIRSTNAME}},

You're on the founding list.

What that means: when we open for clients, you get first call and the founding rate held for as long
as you stay with us. No payment now, nothing to sign, and you can tell me to get lost at any point.

I'll email you when we open — realistically {{TIMEFRAME}}. In the meantime you'll get the fortnightly
newsletter: every deadline before it bites, and one useful thing.

If anything urgent comes up before then, ring me. 020 8058 1496.

Craig
```

---

# PART 10 — Email signature

Two versions, both in the delivered files: `email/signature.html` (rich) and the plain-text fallback
below. Keep signatures **under 4 lines of actual content** — long signatures with social icons and
quotes read as amateur in B2B and add weight to every email in the thread.

**Plain text version:**
```
--
Craig {{SURNAME}}
Klyara — the back office for small construction firms

020 8058 1496  |  craig@klyara.com  |  klyara.com
Bookkeeping · CIS · VAT reverse charge · Payroll · Making Tax Digital
```

**Do not include:** a confidentiality disclaimer nobody reads, a "please consider the environment"
line, social media icon rows, or an image-only signature (it breaks in dark mode and triggers spam
filters).

**Do include, once supervised:** your professional body membership line and AML supervision
reference. For a bookkeeping firm that is a genuine trust signal and it belongs in the signature:
```
{{ICB/AAT}} member in practice · AML supervised by {{BODY}} · Practice licence {{NUMBER}}
```

---

# PART 11 — Metrics to actually watch

Ignore vanity metrics. Four numbers, monthly:

| Metric | Healthy for B2B trade audience | What it tells you |
|---|---|---|
| **Open rate** | 35–50% | Subject lines and list quality. Below 25% = list hygiene problem. |
| **Click rate** | 3–8% | Whether the content earns action |
| **Reply rate** | **Track this above everything** | The only metric that turns into revenue. Replies are leads. |
| **Unsubscribe** | Under 0.5% per send | Above 1% means wrong audience or wrong frequency |

**The one that matters is replies.** Every sequence above is written to invite one. A newsletter with
a 30% open rate and eight replies is worth more to Klyara than one with 60% opens and none.

---
---

# PART 12 — The recurring client emails

*Not marketing. These are the operational emails that run every month for every client, forever.
Automate them in Brevo against the client list, or send from the practice inbox — but write them once
and stop rewriting them.*

**These go to the Clients list, which never receives marketing sends. See §Suppression rules.**

---

## Records reminder — the 5th of each month
**Subject:** `Records for {{MONTH}} — by the 10th`
```
Hi {{FIRSTNAME}},

Quick nudge: anything for {{MONTH}} that isn't already in the app, we need by the 10th.

Most of it should be in already if you've been snapping receipts as you go. The ones that usually
aren't:
• Anything paid in cash
• Trade counter purchases on a personal card
• Invoices you raised but haven't put through

Nothing to send if it's all in — ignore this.

Craig
```

## Late records — the 11th, only if needed
**Subject:** `Still waiting on {{MONTH}}`
```
Hi {{FIRSTNAME}},

We're missing {{WHAT}} for {{MONTH}}.

Not chasing for the sake of it — the CIS return has to go in by the 19th and I'd rather not file it
on incomplete figures.

If it's easier, ring me and we'll go through what's outstanding in five minutes.

Craig
020 8058 1496
```
*The late-records surcharge is in the engagement letter. Warn once, apply it the second time. It
almost never needs applying twice.*

## CIS filed — the 19th
**Subject:** `CIS filed for {{MONTH}}`
```
Hi {{FIRSTNAME}},

CIS return for the month to {{DATE}} is filed.

Deducted this month: {{AMOUNT}}
Due to HMRC by: {{22nd or 19th}}
Subcontractors on the return: {{N}}

Payment and deduction statements have gone out to all of them.

{{ANY FLAG — an unverified subbie, a missing statement, something odd. If nothing, delete this line.}}

Craig
```

## Monthly reports — by the 10th
**Subject:** `{{MONTH}} figures`
```
Hi {{FIRSTNAME}},

{{MONTH}} is in the portal.

Turnover               {{X}}
Gross margin           {{X}}
Owed to you            {{X}}  (over 60 days: {{X}})
Retentions outstanding {{X}}
Bank vs next 30 days   {{X}}

{{ONE OBSERVATION. The single most useful thing in the numbers, in one sentence. Never more than
one — if there are three things worth saying, ring them instead.}}

Nothing needed from you.

Craig
```

## VAT return filed — quarterly
**Subject:** `VAT return filed — {{QUARTER}}`
```
Hi {{FIRSTNAME}},

VAT return for {{QUARTER}} is filed.

{{Payable / Repayable}}: {{AMOUNT}}
{{Due by / Expected}}: {{DATE}}

{{If repayable and it's a pattern: "That's the third quarter running you've been in repayment. Worth
moving to monthly returns — you'd get the money back twelve times a year instead of four. Say the
word and I'll apply."}}

Craig
```

## MTD quarterly update filed
**Subject:** `MTD update filed — {{QUARTER}}`
```
Hi {{FIRSTNAME}},

Your quarterly update for {{PERIOD}} has gone to HMRC.

Nothing to pay on it — it's a summary, not a calculation. The tax gets settled at the final
declaration on 31 January.

Next quarter ends {{DATE}}, due {{DATE}}.

Craig
```

## Deadline warning — 14 days before anything with a date
**Subject:** `{{DEADLINE}} — {{DATE}}`
```
Hi {{FIRSTNAME}},

{{DEADLINE}} falls on {{DATE}}, two weeks today.

{{What we need from you, or "nothing needed — it's handled".}}

{{If money is due: the amount, and where it goes.}}

Craig
```

## Year end pack
**Subject:** `Year end — everything your accountant needs`
```
Hi {{FIRSTNAME}},

Year end pack is ready and I've sent it to {{ACCOUNTANT}}.

What went over: trial balance, reconciled control accounts, CIS reconciled to your deduction
statements, aged debtors and creditors, retention schedule, fixed asset movements, and the bank
reconciliations.

They shouldn't need to come back to you for anything. If they do, send it to me rather than digging
it out yourself.

Craig
```

## The 90-day and six-monthly review invite
See `docs/12 §Part 2, Email 5`. Diarise it at onboarding — it is the most commonly skipped email in
this list and the one that produces the add-on revenue.

---

## Automating these

In Brevo, most of these are date-triggered rather than behaviour-triggered:

```
5th of month       Records reminder      → Clients list
11th of month      Late records          → manual, only where needed
19th of month      CIS filed             → per client, after filing
By the 10th        Monthly reports       → per client, after reports published
Quarterly          VAT filed             → per VAT client
Quarterly          MTD filed             → per Solo client
-14 days           Deadline warning      → per applicable deadline
Day 85             90-day review invite  → set at onboarding
```

**Do not fully automate the ones carrying figures.** A wrong number sent automatically is worse than
a late email. Automate the trigger and the template; type the numbers.

---
---

# PART 13 — Newsletters 13–24: the second six months

*Issues 1–12 cover September 2026 to February 2027. These carry it through to August 2027, so the
programme runs a full year without you writing anything.*

| # | Date | Theme |
|---|---|---|
| 13 | Thu 4 Mar 2027 | Five weeks to year end |
| 14 | Thu 18 Mar 2027 | Buying before 5 April |
| 15 | Thu 1 Apr 2027 | ⚠️ The £30,000 wave lands Monday |
| 16 | Thu 15 Apr 2027 | Your first quarter under MTD |
| 17 | Thu 29 Apr 2027 | The receipt habit |
| 18 | Thu 13 May 2027 | Verification, and the 30% trap |
| 19 | Thu 27 May 2027 | Why busy firms are skint |
| 20 | Thu 10 Jun 2027 | Quoting and winning work |
| 21 | Thu 24 Jun 2027 | Quarter end, 5 July |
| 22 | Thu 8 Jul 2027 | 31 July payment on account |
| 23 | Thu 22 Jul 2027 | Mid-year: gross payment status |
| 24 | Thu 5 Aug 2027 | ⚠️ MTD update due Saturday |

---

## №13 — Thu 4 March 2027
**Subject:** `Five weeks to year end`
**Preview:** `Five things worth doing before 5 April.`

```
📅 DATES

Fri 19 Mar — CIS return, month to 5 Mar
Mon 5 Apr  — Tax year ends. MTD quarter ends. £30,000 threshold begins.
Mon 19 Apr — CIS return, month to 5 Apr
Fri 7 May  — MTD quarterly update due

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: five things before 5 April

Nothing here is dramatic. All of it is harder in June.

1. GET EVERY INVOICE OUT. Anything you have done and not invoiced belongs in this tax year.
   Sitting on it does not defer the tax, it just makes the records wrong.

2. GET EVERY RECEIPT IN. The ones people lose money on are always the same: fuel, parking,
   tools under £100, trade counter on a personal card, PPE.

3. DECIDE ON ANY PURCHASE. The invoice date decides which tax year it lands in. If this year
   was strong and next looks quieter, buy before 5 April. If the reverse, wait. It has to be
   in use in the business by the year end, not just ordered.

4. CHECK GROSS PAYMENT STATUS. The compliance test looks at the last twelve months. If those
   twelve months are clean and your construction turnover clears the threshold, you would pass
   — and most firms who would pass have never applied.

5. CHASE MISSING CIS STATEMENTS. Every deduction you cannot evidence is tax you pay twice.

━━━━━━━━━━━━━━━━━━━━━━━

🧮 THE TOOL: CIS calculator and deadline checker → klyara.com/tools.html

Craig
```

---

## №14 — Thu 18 March 2027
**Subject:** `Buying a van before April?`
**Preview:** `The date on the invoice is worth more than the haggling.`

```
📅 DATES

Fri 19 Mar — CIS return, month to 5 Mar — tomorrow
Mon 5 Apr  — Tax year ends · MTD £30,000 threshold begins
Fri 7 May  — MTD quarterly update due

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: capital allowances, and the two-week decision

If you are buying a van, plant, or a serious run of tools, the date on the invoice decides
which tax year the deduction falls in.

THE BASICS

Most plant, machinery, tools and commercial vehicles qualify for the Annual Investment
Allowance — the full cost off your profits in the year of purchase, not spread over the life
of the asset.

WHY THE TIMING MATTERS

Buy on 3 April and it comes off this year. Buy on 8 April and it comes off next year. Same
van, same money, potentially a different rate of tax.

The right answer depends on which year has the higher profit. Strong year now and a quieter
one ahead — buy before 5 April. The other way round — wait. That decision is worth more than
anything you will achieve arguing about the price.

THREE THINGS TO WATCH

Cars are treated differently from commercial vehicles, and the line between them for tax has
been litigated more than once. Check before you buy, not after.

Hire purchase usually gets the allowance on the full cost when the asset is brought into use.
A lease usually does not work that way at all.

And it has to be in use in the business by the year end. Ordered is not enough.

DO NOT BUY THINGS FOR TAX REASONS

Spending £30,000 to save tax at 20% leaves you £24,000 down. If you need the van, optimise the
timing. If you do not, no amount of relief makes it a good purchase.

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №15 — Thu 1 April 2027 ⚠️
**Subject:** `£30,000 from Monday`
**Preview:** `Measured on what you invoiced, not what you banked.`

```
📅 DATES

⚠️ Mon 5 Apr — Tax year ends. MTD applies at £30,000 qualifying income.
Mon 19 Apr — CIS return, month to 5 Apr
Fri 7 May  — MTD quarterly update due (6 Jan – 5 Apr)

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the wave that catches most of the trade

From Monday, Making Tax Digital for Income Tax applies to anyone with qualifying income over
£30,000.

HMRC's wording is "the amount before expenses (also known as turnover), based on the tax
return you submitted in the previous tax year".

The bit that matters for anyone in CIS: deductions do not reduce your turnover. They sit in a
separate box on your return as tax you have already paid. So £30,000 of turnover is roughly
£24,000 in the bank after 20% comes off.

Which means a subbie who banked £24,000 is in. And their bank statement spent the whole year
suggesting otherwise.

Add property income too — it is combined, not assessed separately. Invoice £24,000 with a flat
bringing in £8,000 gross and you are at £32,000.

CHECK IT PROPERLY

Find your 2025–26 return. Look at the turnover box on the self-employment pages, not the
profit and not the bank. Add gross property income. That total is the number.

WHAT TO DO IF YOU ARE IN

Connect your business bank account to compatible software. That single step does most of the
work, takes about ten minutes, and everything else follows from it.

Then put four dates in your phone: quarters end 5 Jul, 5 Oct, 5 Jan, 5 Apr. Updates due on
the 7th of the following month.

━━━━━━━━━━━━━━━━━━━━━━━

📘 Free 15-page MTD guide, no email needed → klyara.com/guide.html

Craig
```

---

## №16 — Thu 15 April 2027
**Subject:** `Your first quarter`
**Preview:** `Less than the panic suggests.`

```
📅 DATES

Mon 19 Apr — CIS return, month to 5 Apr
Fri 7 May  — MTD quarterly update due (6 Jan – 5 Apr)
Mon 5 Jul  — Next MTD quarter ends

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: what a quarterly update actually involves

If April was your first month in MTD, here is the whole thing.

You keep digital records as you go. At the end of each quarter you send HMRC a summary of
income and expenses by category, from compatible software. Totals. That is the submission.

It is not a tax return. Nothing is calculated. Nothing is due. Nothing is final — you can
correct figures later. The tax is still settled once a year at the final declaration on
31 January, exactly as it always was.

So the change is the record keeping, not the return. Asking for four updates a year is simply
how HMRC makes sure the bookkeeping happens throughout the year rather than retrospectively.

IF YOUR BOOKS ARE CURRENT: about twenty minutes a quarter.
IF THEY ARE NOT: MTD does not create four times the work. It creates four times the panic,
permanently. Which is the real reason to fix it now rather than in July.

THE ONE HABIT

Photograph the receipt at the counter. Ten seconds, while you are standing there. Not
collected in the van, not sorted at the weekend. That single habit is the difference between
this being easy and this being a quarterly argument.

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №17 — Thu 29 April 2027
**Subject:** `Ten seconds at the counter`
**Preview:** `The habit that makes everything else easy.`

```
📅 DATES

Fri 7 May  — MTD quarterly update due
Wed 19 May — CIS return, month to 5 May
Mon 5 Jul  — MTD quarter ends

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the receipts you are about to hand HMRC for nothing

Every receipt photo sitting in your camera roll, and every crumpled thing in the van, is
either a deduction or it is money you did not need to give away.

The ones people consistently lose:

Fuel · parking and tolls · tools under £100 · trade counter purchases on a personal card ·
PPE and protective workwear · materials paid in cash · phone, at a defensible business share ·
use of home for the paperwork · subsistence when working away · the Sunday emergency run

None of those are aggressive claims. They are ordinary business costs that go unclaimed
because the paper vanished.

THE FIX IS NOT A SYSTEM. IT IS A MOMENT.

Photograph it at the counter, while you are still standing there. Ten seconds. Then forget it.

What does not work: collecting them, sorting them later, keeping them in the glovebox with
good intentions. Everyone has tried all three.

MIXED USE, BRIEFLY

Van, phone, home office, workwear. Pick a defensible split, apply it consistently every year,
and write down why you picked it. A consistent, defensible number has never been the thing
that caused anyone a problem.

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №18 — Thu 13 May 2027
**Subject:** `20% or 30%? It is not a choice`
**Preview:** `And if you get it wrong, HMRC comes to you.`

```
📅 DATES

Wed 19 May — CIS return, month to 5 May
Mon 21 Jun — CIS return, month to 5 Jun (the 19th is a Saturday)
Mon 5 Jul  — MTD quarter ends

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the two minutes that cost contractors the most

Verification. Before the first payment to any subcontractor, you ask HMRC how much to deduct.

HMRC comes back with one of three answers:
  Gross      → 0%   registered for gross payment status
  Net        → 20%  registered under CIS. The normal outcome.
  Unmatched  → 30%  they cannot match them, or they are not registered

THE EXPENSIVE MISTAKE

Paying someone 20% because you assume they are registered, without verifying.

If HMRC's answer would have been 30%, you have under-deducted. HMRC recovers the shortfall
from YOU, the contractor, with penalties. You have already paid the money out. There is no
mechanism that makes the subcontractor give it back.

Verify first. Every time. Keep the reference number.

IF YOU ARE THE SUBBIE ON 30%

It is not a punishment the contractor chose — if you are unverified they are obliged to deduct
30%. Two things to check: are you actually registered under CIS as a subcontractor (which is
not the same as being registered for self assessment), and do your details match exactly?
Failed verifications are usually a trading name given instead of the registered name.

The money is not lost either way. But 30% instead of 20% for a year is a lot of your cash
sitting with HMRC.

━━━━━━━━━━━━━━━━━━━━━━━

🧮 Free CIS calculator → klyara.com/tools.html

Craig
```

---

## №19 — Thu 27 May 2027
**Subject:** `Busy, and no money in the bank`
**Preview:** `Four things that drain cash while the P&L looks fine.`

```
📅 DATES

Mon 21 Jun — CIS return, month to 5 Jun
Mon 5 Jul  — MTD quarter ends
Sat 7 Aug  — MTD quarterly update due

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: it is almost never a pricing problem

"We are busier than we have ever been and there is no money in the bank." Four things cause
it, and none of them show up on a profit and loss.

1. YOUR REAL PAYMENT TERMS
Invoice dated the 30th, terms 30 days, paid on the 15th payment run following. That is 46
days, not 30. Add the eleven days you sat on the invoice and you funded that job for 57.

2. RETENTIONS
Three per cent of everything, held for twelve to twenty-four months. On £400,000 of turnover
that is £12,000 permanently out of the business, growing as you grow.

3. THE REVERSE CHARGE
Before 2021 you collected VAT on sales and held it until the quarter end. Never your money,
but it was in your account. That float is gone and nobody sent a letter explaining that your
working capital had structurally dropped.

4. CIS DEDUCTIONS
20% off every labour invoice, sitting with HMRC until you reconcile. On £120,000 of labour
invoicing that is £24,000 lent interest-free, sometimes for a year.

Add those four on a firm turning over £400,000 and you are looking at £50,000–£80,000 of
working capital that exists on paper and not in the bank.

You cannot price your way out of it. You can only shorten it: invoice faster, chase harder,
claim retentions, move to monthly VAT returns if you are in repayment, and apply for gross
payment status if you qualify.

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №20 — Thu 10 June 2027
**Subject:** `The quote that loses the job`
**Preview:** `Usually the fourth day, not the price.`

```
📅 DATES

Mon 21 Jun — CIS return, month to 5 Jun
Mon 5 Jul  — MTD quarter ends
Sat 7 Aug  — MTD quarterly update due

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: speed beats polish

Most lost jobs are not lost on price. They are lost on the fourth day.

A quote sent within 24 hours wins substantially more often than the identical quote sent four
days later — not because it is better, but because by day four they have two others and you
have become the one who seemed less bothered.

Research on how people choose local trades is fairly blunt about this: around three quarters
decide within thirty minutes of starting to look, and most evaluate three or fewer businesses.
You are not competing to be the best answer. You are competing to be an answer while they are
still deciding.

IF YOU CANNOT QUOTE SAME DAY

Send a holding message anyway: "Thanks for seeing me today — I'll have a full quote to you by
Thursday." That one text keeps you in it, and it costs nothing.

A NUMBER IS NOT A QUOTE

A figure in a text message gets compared to other figures, which is a competition decided
entirely on price. A quote should say what is included, what is not, how long it will take,
when you could start, the payment stages, and the number — on a document with your name on it.

The same price presented properly beats a cheaper number in a text more often than people
expect. You are not selling the price. You are selling the impression that you will turn up
and do what you said.

AND ASK WHY WHEN YOU LOSE

"No problem at all — do you mind me asking, was it price or timing?" Half will tell you. If
the answer is consistently timing rather than price, you have been dropping your prices to fix
a scheduling problem.

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №21 — Thu 24 June 2027
**Subject:** `Quarter ends 5 July`
**Preview:** `Seven jobs, one a day, and you are done by Sunday.`

```
📅 DATES

⚠️ Mon 5 Jul — MTD quarter ends (6 Apr – 5 Jul)
Mon 19 Jul — CIS return, month to 5 Jul
Sat 31 Jul — Second payment on account
Sat 7 Aug  — MTD quarterly update due

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the seven-job quarter end

Eleven days. One job a day, each under twenty minutes, and the order matters because each
makes the next easier.

1. BANK FEED — every business account connected and feeding, not exported and typed. Ten
   minutes, and it does about eighty per cent of the work on its own.

2. RECEIPTS — everything not already on the feed. One sitting.

3. MIXED USE — van, phone, home, workwear. Consistent, defensible, written down.

4. RECONCILE — zero unmatched. Watch for payments in you never matched to an invoice; that is
   usually money you already had and were about to chase for.

5. CIS — add up your deduction statements and compare to your records. Chase anything missing
   now, while the contractor still remembers the job.

6. REVERSE CHARGE — last ten sales invoices, four questions each. Two minutes, highest value
   on the list.

7. THE NUMBER — margin by job, owed by age, retentions outstanding, bank against thirty days.

Do one a day and you are closed off before the quarter even ends, five weeks ahead of the
deadline.

━━━━━━━━━━━━━━━━━━━━━━━

📄 Full checklist, free → klyara.com

Craig
```

---

## №22 — Thu 8 July 2027
**Subject:** `31 July, and the payment people forget`
**Preview:** `It lands in the quietest cash month of the year.`

```
📅 DATES

Mon 19 Jul — CIS return, month to 5 Jul
⚠️ Sat 31 Jul — Second payment on account
Sat 7 Aug  — MTD quarterly update due (6 Apr – 5 Jul)

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: the July payment on account

Your second payment on account is due 31 July. It is normally half of last year's tax bill,
paid in advance, and it arrives in one of the quietest cash months of the year for a lot of
building firms.

People remember January. Fewer diarise July, and it is the same size.

IF IT IS UNAFFORDABLE

Talk to HMRC before the deadline, not after. A Time to Pay arrangement agreed in advance is an
administrative conversation. The same conversation in August, after a missed payment, comes
with penalties attached.

CAN YOU REDUCE IT?

If you genuinely know this year will be lower than last, you can apply to reduce payments on
account. Reduce on evidence, not on optimism — HMRC charges interest on the shortfall if you
reduce too far.

AND WHEN IT IS PAID

Work out what next January looks like and start putting it aside monthly. A separate account,
a standing order, twenty-five to thirty per cent of what lands.

Everyone knows this. Almost nobody does it. The ones who do never have a bad January again.

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №23 — Thu 22 July 2027
**Subject:** `Would you pass the compliance test?`
**Preview:** `Mid-year is the right moment to check.`

```
📅 DATES

Sat 31 Jul — Second payment on account
Sat 7 Aug  — MTD quarterly update due
Thu 19 Aug — CIS return, month to 5 Aug

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: gross payment status, checked at the halfway point

One question: have you filed and paid everything on time for the last twelve months? CIS,
PAYE, VAT, corporation tax or self assessment.

If the answer is yes, and your construction turnover excluding VAT and materials clears the
minimum threshold, you would pass the compliance test for gross payment status.

WHY IT MATTERS

With gross status, contractors pay you in full and you settle your own tax. Without it, 20% of
every labour invoice sits with HMRC until you reconcile — up to a year after you earned it,
while you are borrowing to buy materials.

On £120,000 of labour invoicing that is £24,000.

THE THREE TESTS

Business — you do construction work in the UK through a bank account. Easy.
Turnover — above a minimum, excluding VAT and materials. Check the current figures.
Compliance — twelve clean months. This is the one that catches people.

IF YOU FAILED BEFORE

The compliance test only looks back twelve months. A great many firms tried once years ago,
failed on a couple of late returns, and would comfortably pass today. Count back twelve
months. If it is clean, apply.

AND IF YOU HAVE IT

Keep filing on time. It gets reviewed, and losing it mid-year hurts far more than never having
had it, because your cash flow has already adjusted to being paid in full.

━━━━━━━━━━━━━━━━━━━━━━━

Craig
```

---

## №24 — Thu 5 August 2027 ⚠️
**Subject:** `MTD update due Saturday`
**Preview:** `Ten minutes if your records are current.`

```
📅 DATES

⚠️ Sat 7 Aug — MTD quarterly update due (6 Apr – 5 Jul)
Thu 19 Aug — CIS return, month to 5 Aug
Tue 5 Oct  — Next MTD quarter ends

━━━━━━━━━━━━━━━━━━━━━━━

ONE THING: two days

Your quarterly update for 6 April to 5 July is due Saturday.

If you have been keeping records as you go, this is a ten-minute job: check the categories,
submit.

If you have not, here is the fastest legitimate route:

1. Connect the bank feed. It pulls three months of transactions in automatically and that is
   most of the job.
2. Categorise in bulk. Not transaction by transaction — sort by description, select all the
   fuel, categorise in one go. Then the merchants. Then the subbies.
3. Add the cash and personal-card purchases that are not on the feed. Do not hunt for
   perfection; get the significant ones in.
4. Submit.

REMEMBER WHAT THIS IS

A summary of totals. Not a return, nothing to pay, correctable later. Submitting something
reasonable on time beats submitting something perfect late.

IF YOU GENUINELY CANNOT

Submit what you have. The late-submission system works on points, so one late update is not a
disaster — a habit of them is. Then spend August setting it up properly so October is not the
same weekend.

━━━━━━━━━━━━━━━━━━━━━━━

That is a year of these. Thank you for reading them.

If the answer to all of this is "I need someone to just handle it" — that is what Klyara is.
Bookkeeping, CIS, reverse charge, payroll and the quarterly filing, for a fixed monthly fee
from £59 + VAT. Twenty-minute call, no pitch: klyara.com

Craig
```

---

## After issue 24

The four anchors repeat forever: the 19th of every month, the four MTD update dates, 31 January, and
5 April. Between them they carry roughly half the calendar.

**But rewrite these from real conversations.** By issue 24 you will have had well over a hundred. The
structure holds; the language should be theirs, not mine.
