# Klyara — SEO & Schema Pack
### Copy-paste JSON-LD, title tags and the calculator SEO plan

---

## How to use this

Every block below goes in the `<head>` of the named page, inside `<script type="application/ld+json">`
tags. Replace anything in `[SQUARE BRACKETS]` with your real values before publishing — **especially
the address and the founding date.** Schema with invented data is worse than no schema.

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
  "telephone": "+442080581496",
  "email": "hello@klyara.com",
  "foundingDate": "[YYYY-MM-DD]",
  "priceRange": "££",
  "currenciesAccepted": "GBP",
  "paymentAccepted": "Direct Debit, Bank Transfer",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[STREET]",
    "addressLocality": "[TOWN]",
    "addressRegion": "[COUNTY]",
    "postalCode": "[POSTCODE]",
    "addressCountry": "GB"
  },
  "areaServed": [
    { "@type": "Country", "name": "United Kingdom" },
    { "@type": "City", "name": "[TOWN 1]" },
    { "@type": "City", "name": "[TOWN 2]" },
    { "@type": "City", "name": "[TOWN 3]" }
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
      { "@type": "Offer", "name": "Klyara Solo",  "price": "59",  "priceCurrency": "GBP",
        "description": "MTD quarterly filing, receipt app, CIS tracking for sole-trader subcontractors",
        "eligibleCustomerType": "Business" },
      { "@type": "Offer", "name": "Klyara Start", "price": "99",  "priceCurrency": "GBP",
        "description": "Monthly bookkeeping and P&L for micro limited companies" },
      { "@type": "Offer", "name": "Klyara Trade", "price": "199", "priceCurrency": "GBP",
        "description": "Bookkeeping, VAT, CIS, payroll and invoice chasing for 5-15 person firms" },
      { "@type": "Offer", "name": "Klyara Pro",   "price": "329", "priceCurrency": "GBP",
        "description": "Full management pack, self assessment, CT600 and business phone" }
    ]
  }
}
</script>
```

**Note on `AccountingService`:** it's a subtype of `LocalBusiness` and `ProfessionalService`, so you
inherit all the local-business properties. It's more specific than `LocalBusiness` and more accurate
than `FinancialService`, which implies regulated activity you deliberately don't do.

---

# 2. WebSite + Sitelinks Search — homepage only

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

---

# 3. FAQPage — the MTD page ⭐ biggest single win

Your MTD page has sixteen questions and no markup. This block makes them eligible for expanded
results. Answers must match the on-page text — Google checks, and mismatched answers get the markup
ignored.

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

# 6. SoftwareApplication — every calculator ⭐ the sleeper win

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

| Calculator | Title tag | Meta description |
|---|---|---|
| CIS deduction | `CIS Deduction Calculator — 20% and 30% \| Klyara` | Work out CIS deductions both ways, with materials excluded. Free, no signup, no email wall. Built for UK builders and subcontractors. |
| VAT + reverse charge | `VAT Reverse Charge Calculator for Construction \| Klyara` | Add or extract VAT, and check whether the domestic reverse charge applies to your job. Free tool for UK construction. |
| Job margin | `Job Margin Calculator for Builders \| Klyara` | Put price, costs and days in — get your true margin and real day rate. Free, no email required. |
| Day rate builder | `Day Rate Calculator — What Should You Charge? \| Klyara` | Work out what you actually need to charge per day once overheads, downtime and unpaid admin are in. Free. |
| Late payment interest | `Late Payment Interest Calculator — UK B2B \| Klyara` | Calculate statutory interest at 8% over base plus the fixed compensation sum you're legally owed on overdue invoices. |
| Retention tracker | `Construction Retention Tracker — Free Template \| Klyara` | Track every retention with its release date, both halves. Most firms find £4,000–£15,000 they'd written off. |
| VAT threshold tracker | `VAT Registration Threshold Tracker \| Klyara` | See how close your rolling turnover is to the VAT registration threshold, before it catches you. |
| Flat rate vs standard | `Flat Rate vs Standard VAT Calculator \| Klyara` | Compare the flat rate scheme against standard VAT for your figures and see which one actually wins. |
| Deadline calendar | `UK Tax Deadline Calendar — CIS, VAT, MTD \| Klyara` | Every CIS, VAT, MTD and self assessment date, counted down. Free, no signup. |
| Subbie take-home | `Subcontractor Take-Home Calculator — After CIS \| Klyara` | Turn your day rate into real money after CIS, tax and expenses. Built for UK subcontractors. |
| True employee cost | `True Cost of an Employee Calculator — UK \| Klyara` | Salary isn't the cost. Add NI, pension, holiday, sick and downtime to see what a hire really costs. |
| Name + domain finder | `Construction Business Name and Domain Generator \| Klyara` | Find a name for your building firm and check the domain in one go. Free. |

**Why this matters more than it looks:** a *tool* is welcome in places a *service* gets removed.
You can post "here's a free CIS calculator, no signup" in a subreddit or a trade forum where "here's
my bookkeeping firm" would be deleted on sight. Twelve tools is twelve legitimate, rule-compliant
reasons to participate in communities. That is the entire Reddit and forum strategy in `docs/01`,
and the calculators are what makes it work.

---

# 7. HowTo — for the quarter-end and verification guides

When you publish the quarter-end checklist as a page:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Quarter-end checklist for builders under Making Tax Digital",
  "description": "Seven jobs, each under twenty minutes, to close an MTD quarter properly.",
  "totalTime": "PT1H",
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
bookkeeper for builders [town] · cis accountant [town] · construction accountant [town]
bookkeeper near me construction · accountant for subcontractors [town]
```
**Gap:** you currently rank for none of these because there's no town on the site. This is where the
£199–£329 clients come from. One local page plus the Google Business Profile does most of it.

## Cluster 6 — Running the firm
```
true cost of an employee uk · day rate calculator construction · job margin construction
first employee builder · construction cash flow
```

---

# 9. Ten pages to build next, in priority order

| # | Page | Cluster | Why |
|---|---|---|---|
| 1 | Construction bookkeeping in [town] | Local | The only cluster with buying intent. Nothing else beats it. |
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
☐ Google Search Console — verify domain, submit sitemap
☐ Google Analytics 4 — install, set "book a call" and "download guide" as conversions
☐ Bing Webmaster Tools — import from GSC, two minutes
☐ Meta Pixel — install now, zero spend
☐ LinkedIn Insight Tag — install now
☐ robots.txt — confirm nothing important is blocked
☐ XML sitemap — confirm every calculator URL is in it
☐ Canonical tags on every page
☐ Per-page og:image (use assets/posts/*.png)
☐ Every image has alt text — currently unchecked
☐ Core Web Vitals — run PageSpeed Insights on homepage, MTD page and one calculator
☐ Mobile check — most of this audience is on a phone, on site, in daylight
☐ HTTPS + HSTS
☐ 404 page that routes to the tools and the guide rather than dead-ending
```
