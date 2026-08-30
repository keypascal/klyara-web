# Klyara — SEO & Schema Pack
### Copy-paste JSON-LD, title tags and the calculator SEO plan

---

## How to use this

Every block below goes in the `<head>` of the named page, inside `<script type="application/ld+json">`
tags. Replace anything in `[SQUARE BRACKETS]` with your real values before publishing. Four things are
still bracketed: the street address, the postcode, the five social handles and the FAQ answers.
Everything else — phone, town, county, opening hours, all four plan prices — is filled in and matches
the pricing page. Schema with invented data is worse than no schema.

**Upload these two images to your site first**, from the pack — the schema references them:
`assets/logo/klyara-mark-disc-512.png` → `/assets/klyara-mark-disc-512.png`, and any 1200×630 crop of
`assets/banners/x-header-1500x500.png` → `/assets/og/klyara-og.png`.

Validate every page after pasting at `search.google.com/test/rich-results`. It takes ten seconds per
page and it catches typos that silently kill the whole block.

**Do not add the `AggregateRating` or `Review` schema types** until you have real reviews. Marking up
reviews you don't have is the machine-readable version of the testimonial problem in `docs/07`, and
Google issues manual actions for it.

---

# 1. Organization + LocalBusiness — goes on EVERY page

This is the foundation. It tells Google what Klyara is, where it operates and how to contact you.
Put it site-wide in the template head.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AccountingService",
  "@id": "https://klyara.com/#organization",
  "name": "Klyara",
  "alternateName": "Klyara — Construction Back Office",
  "description": "Bookkeeping, CIS returns, VAT reverse charge coding, payroll and Making Tax Digital quarterly filing for UK construction firms and subcontractors.",
  "url": "https://klyara.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://klyara.com/assets/klyara-mark-disc-512.png",
    "width": 512,
    "height": 512
  },
  "image": "https://klyara.com/assets/og/klyara-og.png",
  "telephone": "+44 20 8058 1496",
  "email": "hello@klyara.com",
  "foundingDate": "2026",
  "priceRange": "££",
  "currenciesAccepted": "GBP",
  "paymentAccepted": "Direct Debit, Bank Transfer",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[STREET]",
    "addressLocality": "Guildford",
    "addressRegion": "Surrey",
    "postalCode": "[POSTCODE]",
    "addressCountry": "GB"
  },
  "areaServed": [
    { "@type": "Country", "name": "United Kingdom" },
    { "@type": "City", "name": "Guildford" },
    { "@type": "City", "name": "Woking" },
    { "@type": "City", "name": "Godalming" },
    { "@type": "City", "name": "Farnham" }
  ],
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }],
  "knowsAbout": [
    "Construction Industry Scheme",
    "CIS returns",
    "Making Tax Digital for Income Tax",
    "VAT domestic reverse charge",
    "Construction payroll",
    "Subcontractor verification",
    "Gross payment status",
    "Construction bookkeeping"
  ],
  "sameAs": [
    "https://www.linkedin.com/company/[HANDLE]",
    "https://www.facebook.com/[HANDLE]",
    "https://x.com/[HANDLE]",
    "https://www.instagram.com/[HANDLE]",
    "https://www.youtube.com/@[HANDLE]"
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Klyara plans",
    "itemListElement": [
      { "@type": "Offer", "name": "Klyara Solo", "price": "59", "priceCurrency": "GBP",
        "description": "MTD quarterly filing, receipt app and CIS tracking for sole-trader subcontractors. £59 per month ex VAT.",
        "priceSpecification": { "@type": "UnitPriceSpecification", "price": "59", "priceCurrency": "GBP",
          "unitCode": "MON", "valueAddedTaxIncluded": false } },
      { "@type": "Offer", "name": "Klyara Start", "price": "99", "priceCurrency": "GBP",
        "description": "Monthly bookkeeping and P&L for micro limited companies. £99 per month ex VAT.",
        "priceSpecification": { "@type": "UnitPriceSpecification", "price": "99", "priceCurrency": "GBP",
          "unitCode": "MON", "valueAddedTaxIncluded": false } },
      { "@type": "Offer", "name": "Klyara Trade", "price": "199", "priceCurrency": "GBP",
        "description": "Bookkeeping, VAT, CIS, payroll and invoice chasing for 5–15 person firms. £199 per month ex VAT.",
        "priceSpecification": { "@type": "UnitPriceSpecification", "price": "199", "priceCurrency": "GBP",
          "unitCode": "MON", "valueAddedTaxIncluded": false } },
      { "@type": "Offer", "name": "Klyara Pro", "price": "329", "priceCurrency": "GBP",
        "description": "Full management pack, self assessment, CT600 and business phone. £329 per month ex VAT.",
        "priceSpecification": { "@type": "UnitPriceSpecification", "price": "329", "priceCurrency": "GBP",
          "unitCode": "MON", "valueAddedTaxIncluded": false } }
    ]
  }
}
</script>
```

**Two things to settle before this goes live.** `[STREET]` and `[POSTCODE]` are the only placeholders
left. If Google Business Profile is set up as a service-area business because Craig works from home,
do not publish the home address here either — delete the `streetAddress` and `postalCode` lines and
leave `addressLocality`, `addressRegion` and `addressCountry`. That is valid schema and it keeps the
address off the open web. All four plan prices are per month, ex VAT, and match the pricing page.

**Note on `AccountingService`:** it's a subtype of `LocalBusiness` and `ProfessionalService`, so you
inherit all the local-business properties. It's more specific than `LocalBusiness` and more accurate
than `FinancialService`, which implies regulated activity you deliberately don't do.

---

# 2. WebSite — homepage only

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://klyara.com/#website",
  "url": "https://klyara.com",
  "name": "Klyara",
  "publisher": { "@id": "https://klyara.com/#organization" },
  "inLanguage": "en-GB"
}
</script>
```

There is no `potentialAction` / `SearchAction` in this block on purpose. Google retired the sitelinks
search box in November 2024, so the markup no longer does anything, and Klyara has no site search to
point it at. Leave it out.

---

# 3. FAQPage — the MTD page

Your MTD page has sixteen questions and no markup. Add it, but know what it buys you. Google stopped
showing FAQ rich results for ordinary commercial sites in 2023 — they now run for government and
health sites only. So this will not put an expanded result in the search listing.

It is still worth ten minutes. The markup is how the page states, in machine-readable form, that
these are questions and these are the answers, and that is what AI search and assistant answers read.
Answers must match the on-page text — mismatched answers get the whole block ignored.

I've written the first six out in full using your actual questions. Replicate the pattern for the
remaining ten, pasting your real on-page answers in.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://klyara.com/making-tax-digital.html#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does CIS money count towards the MTD threshold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Qualifying income for Making Tax Digital is measured gross — before expenses and before CIS deductions. If you invoice £55,000 and 20% CIS is deducted, you bank £44,000 but HMRC counts £55,000. That puts you over the £50,000 threshold even though your bank balance says otherwise."
      }
    },
    {
      "@type": "Question",
      "name": "I run a limited company. Does MTD for Income Tax apply to me?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[PASTE YOUR ON-PAGE ANSWER VERBATIM]"
      }
    },
    {
      "@type": "Question",
      "name": "What happens if I just ignore Making Tax Digital?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[PASTE YOUR ON-PAGE ANSWER VERBATIM]"
      }
    },
    {
      "@type": "Question",
      "name": "Can I just use a spreadsheet like always?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[PASTE YOUR ON-PAGE ANSWER VERBATIM]"
      }
    },
    {
      "@type": "Question",
      "name": "I have property income too. Does that count towards the threshold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[PASTE YOUR ON-PAGE ANSWER VERBATIM]"
      }
    },
    {
      "@type": "Question",
      "name": "When should I actually start preparing for MTD?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[PASTE YOUR ON-PAGE ANSWER VERBATIM]"
      }
    }
  ]
}
</script>
```

**Rules that stop this backfiring:**
- Every question in the markup must be visibly on the page
- Every answer must match the visible text (paraphrasing is fine, contradicting is not)
- No promotional links inside answer text
- One `FAQPage` block per page, never two

---

# 4. Service schema — one per service page

Template. Duplicate and adjust for Bookkeeping & CIS, MTD, Payroll, Invoice Chasing, AI Receptionist,
Websites, Local Search.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "CIS returns and construction bookkeeping",
  "name": "Bookkeeping and CIS for construction firms",
  "description": "Monthly bookkeeping, CIS returns filed by the 19th, subcontractor verification, VAT reverse charge coding and management reports for UK building firms.",
  "provider": { "@id": "https://klyara.com/#organization" },
  "areaServed": { "@type": "Country", "name": "United Kingdom" },
  "audience": {
    "@type": "BusinessAudience",
    "name": "UK construction firms and subcontractors"
  },
  "offers": {
    "@type": "Offer",
    "price": "199",
    "priceCurrency": "GBP",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "price": "199",
      "priceCurrency": "GBP",
      "unitCode": "MON",
      "valueAddedTaxIncluded": false
    }
  }
}
</script>
```

`unitCode: "MON"` is the UN/CEFACT code for one month, and `valueAddedTaxIncluded: false` is what
makes £199 read as £199 ex VAT rather than inclusive. Change the price on every duplicate of this
block to the plan the page actually sells: Solo £59, Start £99, Trade £199, Pro £329, all ex VAT.

---

# 5. BreadcrumbList — every page below the homepage

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home",     "item": "https://klyara.com" },
    { "@type": "ListItem", "position": 2, "name": "Services", "item": "https://klyara.com/services/" },
    { "@type": "ListItem", "position": 3, "name": "Bookkeeping and CIS" }
  ]
}
</script>
```
*The last item has no `item` URL — that's correct, it's the current page.*

---

# 6. SoftwareApplication — every calculator

**This is the most under-exploited asset you own.** Twelve working, ungated calculators on their own
URLs. Marked up properly, each becomes independently discoverable, independently linkable, and
independently rankable for its own long-tail query.

Paste one of these on each calculator page:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "CIS Deduction Calculator",
  "description": "Work out CIS deductions at 20% or 30%, in both directions, with the materials split excluded. Free, no signup.",
  "url": "https://klyara.com/tools/cis-deduction-calculator.html",
  "applicationCategory": "FinanceApplication",
  "operatingSystem": "Any",
  "browserRequirements": "Requires JavaScript",
  "inLanguage": "en-GB",
  "isAccessibleForFree": true,
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "GBP" },
  "publisher": { "@id": "https://klyara.com/#organization" }
}
</script>
```

## Title tags and meta descriptions for all twelve

Each calculator needs its own. These are written to the query, not to the brand.

**Every title below is finished with ` | Klyara`** — a space, a pipe, a space, then the brand. The
suffix is left off the table cells on purpose: a pipe inside a Markdown table cell splits the row and
breaks the table. The "Chars" column counts the finished title *including* the suffix, so paste the
cell, add ` | Klyara`, and you are on the number shown. Everything is inside Google's ~60-character
title and 150–160-character description windows.

| Calculator | Title tag, brand suffix not shown | Chars | Meta description |
|---|---|---|---|
| CIS deduction | CIS Deduction Calculator — 20% and 30% | 47 | Work out CIS deductions both ways at 20% or 30%, with the materials split taken out first. Free, no signup, no email wall. For UK builders and subcontractors. |
| VAT + reverse charge | VAT Reverse Charge Calculator for Construction | 55 | Add or extract VAT, then run the five tests to see whether the domestic reverse charge applies to the job. Free, no signup. Built for UK construction firms. |
| Job margin | Job Margin Calculator for Builders | 43 | Put the price, the costs and the days in and get your true margin and your real day rate back out. Free, no email required. Built for UK building firms. |
| Day rate builder | Day Rate Calculator — What Should You Charge? | 54 | Work out what you need to charge a day once overheads, downtime, holiday and unpaid admin are counted. Most trades undercharge. Free, no signup needed. |
| Late payment interest | Late Payment Interest Calculator — UK B2B | 50 | Work out statutory interest at 8% over the Bank of England base rate, plus the fixed compensation sum you are owed on every late invoice. Free, no signup. |
| Retention tracker | Construction Retention Tracker — Free Template | 55 | Track every retention on every job, both halves, with the release date beside it. Ask on the day it falls due, not months later. Free, no signup needed. |
| VAT threshold tracker | VAT Registration Threshold Tracker | 43 | See how close your rolling twelve-month turnover is to the VAT registration threshold, month by month, before it catches you out. Free, no signup, no email. |
| Flat rate vs standard | Flat Rate vs Standard VAT Calculator | 45 | Compare the VAT flat rate scheme against standard VAT on your own figures and see which one actually leaves you better off. Free, no signup, no email wall. |
| Deadline calendar | UK Tax Deadline Calendar — CIS, VAT, MTD | 49 | Every CIS, VAT, MTD, PAYE and self assessment date for UK builders, counted down from today so nothing lands as a surprise. Free, no signup, no email wall. |
| Subbie take-home | Subcontractor Take-Home Calculator — After CIS | 55 | Turn your day rate into the money that actually reaches the bank once CIS, tax, National Insurance and expenses are out. Free, no signup, for UK subcontractors. |
| True employee cost | True Cost of an Employee Calculator — UK | 49 | Salary is not the cost. Add employer NI, pension, holiday, sick pay and unbilled downtime to see what your first hire really costs. Free, no email wall. |
| Name + domain finder | Construction Business Name and Domain Generator | 56 | Find a name for your building firm and check whether the .co.uk domain is still free, in one go. Free, no signup, no email wall. For UK trades starting out. |

**Why this matters more than it looks:** a *tool* is welcome in places a *service* gets removed.
You can post "here's a free CIS calculator, no signup" in a subreddit or a trade forum where "here's
my bookkeeping firm" would be deleted on sight. Twelve tools is twelve legitimate, rule-compliant
reasons to participate in communities. That is the entire Reddit and forum strategy in `docs/01`,
and the calculators are what makes it work.

---

# 7. HowTo — for the quarter-end and verification guides

Same caveat as the FAQ block: Google removed HowTo rich results in 2023, so this will not draw a
carousel. It is still the cleanest way to tell a machine what the seven steps are, and AI answers
read it. Add it, do not expect a listing change.

When you publish the quarter-end checklist as a page:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Quarter-end checklist for builders under Making Tax Digital",
  "description": "Seven jobs, none of them longer than twenty minutes, to close an MTD quarter properly.",
  "totalTime": "PT2H",
  "step": [
    { "@type": "HowToStep", "position": 1, "name": "Connect the bank feed",
      "text": "Connect every business bank account to your software so transactions feed automatically rather than being exported and typed in." },
    { "@type": "HowToStep", "position": 2, "name": "Get the receipts in",
      "text": "Enter every receipt not already covered by the bank feed — fuel, parking, tools, trade counter purchases on personal cards, PPE." },
    { "@type": "HowToStep", "position": 3, "name": "Handle mixed-use costs",
      "text": "Apply a consistent, defensible split for van, phone, home office and workwear, and record why you chose it." },
    { "@type": "HowToStep", "position": 4, "name": "Reconcile",
      "text": "Match every transaction. Zero unmatched is the standard. Watch for payments in you never matched to an invoice." },
    { "@type": "HowToStep", "position": 5, "name": "Reconcile CIS",
      "text": "Chase every missing payment and deduction statement while the contractor still remembers the job. Unevidenced deductions are tax paid twice." },
    { "@type": "HowToStep", "position": 6, "name": "Check the reverse charge",
      "text": "Take your last ten sales invoices and check the five reverse charge tests on each. Two minutes." },
    { "@type": "HowToStep", "position": 7, "name": "Look at the number",
      "text": "Gross margin by job, what you're owed by age, retentions outstanding, and bank balance against the next thirty days." }
  ]
}
</script>
```

---

# 8. Keyword clusters — what to build content against

Six clusters. Each maps to one pillar page plus supporting pieces. This is your next six months of
SEO.

## Cluster 1 — MTD *(pillar: `/making-tax-digital.html` — already your best page)*
```
mtd for income tax · making tax digital sole trader · mtd threshold 2027 · mtd for subcontractors
mtd quarterly update deadline · do i need to do making tax digital · mtd £30,000 threshold
making tax digital for builders · mtd income tax cis · qualifying income mtd
```
**Gap to fill:** a page on *"MTD for CIS subcontractors"* specifically. The gross-income trap is the
highest-intent query in this whole cluster and nobody else is answering it in plain English.

## Cluster 2 — CIS *(pillar: `/services/bookkeeping-cis`)*
```
cis deduction calculator · cis returns deadline · cis 20 or 30 percent · verify subcontractor cis
cis gross payment status · cis materials deduction · nil cis return · cis penalties
cis monthly return · deemed contractor cis · cis payment and deduction statement
```
**Gap:** gross payment status deserves its own page. High intent, high value, low competition in
plain English. The content is already written in `assets/lead-magnets/`.

## Cluster 3 — VAT reverse charge
```
domestic reverse charge construction · vat reverse charge calculator · reverse charge end user
reverse charge invoice wording · cis reverse charge · construction vat monthly returns
```
**Gap:** an *"end user declaration template"* page. People search for the wording. Give it away as a
copy-paste block and it earns links.

## Cluster 4 — Getting paid
```
late payment interest calculator uk · retention construction · statutory interest commercial debt
how to chase unpaid invoices builder · construction retention release
```

## Cluster 5 — Local *(the money cluster)*
```
bookkeeper for builders guildford · cis accountant guildford · construction accountant surrey
bookkeeper near me construction · accountant for subcontractors woking · cis accountant farnham
construction bookkeeper godalming
```
**Gap:** you rank for none of these because there is no town on the site. This is where the £199 and
£329 clients come from. One Guildford page plus the Google Business Profile does most of it.

## Cluster 6 — Running the firm
```
true cost of an employee uk · day rate calculator construction · job margin construction
first employee builder · construction cash flow
```

---

# 9. Ten pages to build next, in priority order

| # | Page | Cluster | Why |
|---|---|---|---|
| 1 | Construction bookkeeping in Guildford | Local | The only cluster with buying intent. Nothing else beats it. |
| 2 | MTD for CIS subcontractors | MTD | Highest-intent long tail; the gross-income trap |
| 3 | Gross payment status: the three tests | CIS | Content already written in the CIS pack |
| 4 | End user declaration — free template | VAT | Template pages earn links passively |
| 5 | CIS penalties explained | CIS | Fear-driven search, high urgency |
| 6 | Switching bookkeepers mid-year | Trust | Removes the biggest objection to changing |
| 7 | Nil CIS returns | CIS | Tiny query, near-zero competition, easy win |
| 8 | Quarter-end checklist | MTD | HowTo schema, already written in `docs/03` |
| 9 | Retentions: how to get them back | Getting paid | The post that got most engagement in the calendar |
| 10 | What a bookkeeper actually does | Trust | Top-of-funnel; catches people who don't know they need you |

**Every one of these is already written somewhere in this pack.** The calendar, the newsletters and
the CIS lead magnet contain the full text for numbers 2, 3, 5, 8 and 9. It's a copy-and-reformat job,
not a writing job.

---

# 10. The technical basics, in one list

```
[ ] Google Search Console — verify domain, submit sitemap
[ ] Google Analytics 4 — install, set "book a call" and "download guide" as conversions
[ ] Bing Webmaster Tools — import from GSC, two minutes
[ ] Meta Pixel — install now, zero spend
[ ] LinkedIn Insight Tag — install now
[ ] robots.txt — confirm nothing important is blocked
[ ] XML sitemap — confirm every calculator URL is in it
[ ] Canonical tags on every page
[ ] Per-page og:image (use assets/posts/*.png)
[ ] Every image has alt text — currently unchecked
[ ] Core Web Vitals — run PageSpeed Insights on homepage, MTD page and one calculator
[ ] Mobile check — most of this audience is on a phone, on site, in daylight
[ ] HTTPS + HSTS
[ ] 404 page that routes to the tools and the guide rather than dead-ending
```
