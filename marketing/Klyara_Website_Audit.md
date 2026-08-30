# Klyara — Website Audit
*klyara.com. First reviewed 26 August 2026. Re-checked against the live site 28 August 2026,
before launch on Monday 14 September 2026.*

The site is good. The copy is better than most firms ten times your size — "Three waves. Everyone
gets wet", "Twelve tools. Zero email walls", "Builders talk straight. So do reviews" — that's real
writing, and the MTD page is the best piece of MTD content I've seen aimed at trades.

So this audit is short on praise and long on the things that will cost you.

**Status of this document.** Every finding below was re-checked on the live site on 28 August 2026.
Nothing has been fixed yet. The five testimonials are still on the homepage, there is still no
JSON-LD anywhere, there is still no `rel=canonical` on any page, and the homepage still carries
nineteen calls to action. Two further findings have been added since the first pass: item 8 and
item 9 in the technical list. When a finding is fixed, strike it here rather than deleting it, so
you can see what has moved.

---

## CRITICAL — deal with this before a single visitor arrives

### The testimonials on the homepage

There are five named testimonials on your homepage:

> Marcus B. — roofing firm, 12 crew · Dean W. — groundworks, 8 on books · Sam O. — electrical
> contractor · Priya T. — sole-trader plasterer · Jodie F. — kitchen fitter

**Klyara has not traded yet.** It isn't AML supervised, so it cannot legally have taken on
bookkeeping clients by way of business. Those five people therefore cannot be Klyara clients.

If they're placeholder copy left in from the build, they have to come off the site before you drive
a single visitor to it. I'm assuming that's what happened — but I have to be direct about why it
matters, because this one isn't a marketing preference.

**Why this is the most serious item in this pack:**

1. **It's unlawful.** Under the Digital Markets, Competition and Consumers Act 2024, publishing fake
   consumer reviews or testimonials — or commissioning them — is a banned practice, directly
   enforceable by the CMA with penalties running to a percentage of global turnover. This isn't a
   grey area any more; it changed in 2025 specifically to catch this.

2. **It threatens your practice licence.** You apply to the ICB for AML supervision and a practice
   licence on Tuesday 1 September 2026, and it takes 28 days. The ICB has professional conduct
   requirements covering honesty and professional behaviour in how you market the practice, and it
   can look at the site. A firm whose website carried invented
   client testimonials before it had clients is a bad look in front of that application, and a worse
   one if a competitor points at it.

3. **It destroys the exact thing you're selling.** Your whole positioning is "a real construction
   specialist you can trust with your money, not a call centre". Five invented builders is the
   single most damaging thing that could sit on that page.

4. **It is genuinely discoverable.** Companies House shows your incorporation date. The reviews claim
   a service history you didn't have. Anyone doing due diligence — a prospect, a partner accountant,
   a journalist responding to the press release in this pack — can join those two dots in a minute.

#### What to do instead — today

Replace the testimonial section with things that are **true and still persuasive**. You have plenty:

**Option A — Craig's track record, correctly labelled.** Not "Klyara clients" but "Craig has been
doing this for eleven years." A short, honest paragraph about the work, plus — if any former clients
or employers will give one — a testimonial that says explicitly *"on Craig's previous work"*. That's
legitimate and it does most of the same job.

**Option B — the founding-client offer, which is stronger than fake reviews anyway.** Replace the
section with honesty as the pitch:

```
We're new. Here's what that's worth to you.

Klyara opened in 2026. We don't have a wall of reviews yet, and we're not going to
pretend otherwise.

What we do have: eleven years of construction bookkeeping behind the person doing your
work, a fixed price, and thirty days' notice with no lock-in.

And because we're building the review wall from scratch, the first ten firms get a
founding rate held for twelve months from the day they start, and considerably more of
our attention than client fifty will get.

[Join the founding list →]
```

That converts. "We're new and here's the honest deal" outperforms generic testimonials with this
audience, because builders are professionally suspicious of anyone who sounds too polished.

**Option C — proof that isn't a review.** Certifications (once held), the professional body
membership (once granted), the partner accountant's written endorsement, and the free tools
themselves. Twelve working calculators are a better credibility signal than five anonymous quotes.

#### Related: audit every other claim on the site the same way

While you're in there, check each of these is true *today*, and remove or future-tense anything that
isn't:

| Claim on site | Check |
|---|---|
| "Qualified, not just confident" | Which qualifications are actually held right now? |
| Xero / QuickBooks / FreeAgent certified | The Build Manual has ProAdvisor certification as a week-1 task. Is it done? |
| "24/7 answering" | Is the Hey Jodie white-label actually live and wired to the number? |
| AI receptionist, chatbot, invoice chasing as live services | Manual Part 10 says month 1 sells core tiers + receptionist + website + phone only. Everything else should read "coming soon". |
| Client portal | Is the Lovable build live at app.klyara.com? |
| Review collection service | You're selling a review service. It has to be beyond reproach on your own site. |

**Nothing on that list is hard to fix.** Future-tense it ("from October", "coming soon") or take it
down. But a bookkeeping firm caught overstating its own credentials has a much shorter conversation
with a prospect than one that says "we're new".

---

## HIGH — the biggest free win available to you

### There is no structured data anywhere on the site

Not on the homepage, not on pricing, not on the MTD page. No Organization, no LocalBusiness, no
Service, no FAQPage, no Breadcrumb.

This is the cheapest significant SEO win you will ever get, and you're leaving it entirely.

**The MTD page alone has sixteen FAQ questions on it.** With FAQPage schema, those become eligible
for expanded results in Google — you occupy dramatically more vertical space on the results page for
exactly the queries you want. Without it, they're just text.

Every block of JSON-LD you need is written out and ready to paste in `docs/08-seo-schema-pack.md`.
It's about forty minutes of copy-paste for the whole site.

### Other technical items

| # | Issue | Fix | Effort |
|---|---|---|---|
| 1 | No JSON-LD | Paste the blocks from `docs/08` | 40 min |
| 2 | The twelve calculators are your best link asset and nothing points at them | Each already has its own URL — good. Now give each a proper title tag, meta description and `SoftwareApplication` schema. Details in `docs/08`. | 90 min |
| 3 | No visible town/area targeting | "Construction bookkeeping in [town]" needs to appear in the homepage H1 area or a dedicated local page. Local intent is where the money is and you're currently invisible to it. | 1 hr |
| 4 | Meta descriptions strip the £ sign | "from 59 pounds a month" reads as an escaping workaround. Use £ — it renders fine in SERPs and "£59" is far more scannable than "59 pounds". | 10 min |
| 5 | No Meta Pixel / LinkedIn Insight Tag | Install both now even with zero ad spend. The retargeting audience you don't collect today is gone forever. | 15 min |
| 6 | No `og:image` per page (only site-wide) | Every share of the MTD page uses the generic image. Use the rendered post graphics in `assets/posts/` as per-page OG images. | 30 min |
| 7 | Newsletter capture only on tools page footer | Put it on the guide page, the MTD page and every calculator result. See below. | 30 min |
| 8 | **No `rel=canonical` on any page** — all 98 pages are missing it | Add a self-referencing `<link rel="canonical">` to every page, pointing at the https apex URL you have chosen. Without it Google picks its own canonical, and with a duplicate hostname live (item 9) it has two identical candidates to choose between. | 60 min |
| 9 | **Apex and www both serve identical content** — klyara.com and www.klyara.com are two full copies of the site | Pick one as the real one, 301 the other to it at the host, and make every canonical, sitemap entry and internal link point at the winner. Do this before item 8, or you will canonicalise to the wrong host. | 20 min |

---

## CONVERSION — where you're losing people

### 1. The calculators have no capture at the point of pain

"Twelve tools. Zero email walls" is a great line and you should keep the promise. **But you can honour
it and still capture.**

The rule: never gate the tool. Offer after the result.

```
[Result displayed]

──────────────────────────────
Want the deadlines emailed to you before they bite?
[ your@email.com ]  [ Send them → ]
One email a fortnight. Unsubscribe any time. We'll never gate a calculator.
──────────────────────────────
```

Someone who has just calculated their CIS deduction is your exact buyer at their exact moment of
pain. This is the single highest-intent capture point on the entire site and it currently does
nothing.

### 2. Nineteen CTAs on the homepage

I counted nineteen distinct calls to action on the homepage. That's not a conversion path, that's a
menu. Every extra choice reduces the odds of any of them being taken.

**Pick one primary action per section, and one primary action for the page.** The page's job is
"book a free discovery call" (or, pre-AML, "join the founding list"). Everything else should be
visually secondary — text links, not buttons.

Specifically: "Hear the receptionist", "See invoice chasing", "See websites and search", "See the AI
toolkit" are four buttons competing with your actual conversion goal in the same viewport.

### 3. Pricing page has no "which one am I?" helper

Four tiers, and the buyer has to self-diagnose. Most won't — they'll bounce or default to the
cheapest.

Add three questions above the table:

```
Not sure which? Answer three things.

Sole trader or limited company?     [Sole trader] [Limited]
Do you have anyone on payroll?      [No] [Yes]
Are you VAT registered?             [No] [Yes]

→ Recommends the tier and pre-fills the call booking.
```

This is a half-day of work and it will move more revenue than any other single change on the site.

### 4. No risk reversal above the fold

"30 day notice, no lock-in" is genuinely reassuring and it's buried on the pricing page. Put it under
the primary CTA everywhere it appears. It costs nothing to say and it removes the main objection this
audience has to a monthly commitment.

### 5. The onboarding fee appears with no cushioning on the tier cards

"£149", "£250", "from £350", "from £500" next to the monthly price is the biggest sticker-shock
moment on the site, and it appears before the explanation. All four are ex VAT and the page should
keep saying so next to the number, not only in the footer.

The explanation you already have — *"we clean up the past so the monthly fee only covers the future"*
— is good. It needs to be adjacent to the number, not in a separate section further down.

### 6. There is no exit from the MTD page for people who aren't in scope

Sixteen FAQs, three waves, a threshold checker — and if someone works out they're under £30,000,
there's nothing for them.

Give them somewhere to go: *"Under the threshold for now? Join the list and we'll tell you the year
before it catches you."* That's a free, zero-effort subscriber who becomes a client in 2028, and
right now they just leave.

---

## WHAT'S GOOD — don't let anyone talk you out of these

- **"Twelve tools. Zero email walls."** Keep this promise permanently. It is a genuine
  differentiator in a sector where everything is gated, and it will earn you links and Reddit
  goodwill that a gated PDF never will.
- **The MTD page.** Sixteen real FAQs answered plainly. This is the best asset you own. It should be
  the destination for every MTD ad, every Reddit answer, and every press mention.
- **"Three waves. Everyone gets wet."** Best line on the site.
- **The tier names.** Solo / Start / Trade / Pro is clear, ladder-shaped and lets people
  self-identify without jargon.
- **30 days notice, no lock-in.** Market it harder.
- **Straight answers / Jargon, translated / Regulation radar.** Excellent resource architecture. Most
  firms have "Blog". These are three distinct, genuinely useful content types with names that tell
  you what they are.

---

## Priority order

| When | What | Why |
|---|---|---|
| **Today** | Remove or correctly label the testimonials | Legal, regulatory and reputational. Nothing else matters until this is done. |
| **Today** | Audit every other claim for present-tense truth | Same reason |
| **This week** | 301 www to the apex, one host only | Two identical copies of the site competing with each other |
| **This week** | Self-referencing `rel=canonical` on all 98 pages | Do it after the redirect, not before |
| **Before Monday 14 September** | Paste the JSON-LD from `docs/08` | Biggest free SEO win; needs to be indexed before traffic arrives |
| **Before Monday 14 September** | Meta Pixel + LinkedIn Insight Tag | Audience you don't collect is gone |
| **Before Monday 14 September** | Newsletter capture after calculator results | Highest-intent capture on the site |
| **Week 1** | Cut homepage CTAs to one primary per section | Conversion |
| **Week 1** | Per-page og:image from `assets/posts/` | Every social share this month uses it |
| **Week 2** | "Which tier am I?" helper on pricing | Highest revenue impact of any single build |
| **Week 2** | Calculator page titles + SoftwareApplication schema | The long-tail SEO engine |
| **Week 3** | Town/area targeting | Local intent is the money |

Weeks are counted from launch on Monday 14 September 2026. "Today" and "this week" mean the setup
phase, Tuesday 1 September to Sunday 13 September.
