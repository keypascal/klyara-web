# Klyara Portal — Platform Decision Record

*Companion to Klyara_App_Build_Plan.md. Researched and written 26 August 2026; hosting corrected 27 August 2026.*
*Interactive version: https://claude.ai/code/artifact/f9447eaa-1281-482c-89da-a9fa13d172ef*

---

## Decision

**Build the portal in Claude Code against our own Supabase project, hosted on Cloudflare Pages. Do not use Lovable.**

Same stack, same output, same five-day M0–M3 timeline as the existing build plan. The only line that changes is who writes the code, and that line goes from $25–100/month to £0 because the subscription already exists.

Reasons, in order of weight:

1. **The metered tool is metered on the wrong thing.** Lovable credits are burned by *fixing*, not building. Documented: a single auth bug at 15 credits (15% of a Pro month); one developer's entire monthly allowance spent in an afternoon on a Stripe integration. Auth and payments are two of the three hard items on our list.
2. **Zero lock-in**, which is the stated standing preference. The repo is the product from minute one — no Cloud instance, no export step, no perpetual data licence over customer data.
3. **The design is already fixed.** Colours, fonts, radii and tone are extracted from the live klyara.com and written into Lovable_Prompt_1.md. There is no visual exploration to do — which is the one thing Lovable is genuinely better at.
4. **Craig was never going to prompt it.** The non-technical-handover argument for Lovable does not apply here.

The decision is reversible: Lovable syncs two-way with a GitHub repo, so it can be pointed at this repo later for a visual polish pass.

---

## The trap, if we ever do use Lovable

**Lovable Cloud enables itself the moment you ask for a login or a database.** It is a Supabase instance held inside Lovable's account — invisible in the Supabase dashboard, no service-role key, no direct database URL, billed through credits, and with no migration path off it.

Non-negotiable order if that route is taken:

1. Create the Supabase project first, EU (London) region.
2. Connect GitHub before the first prompt (and never disconnect — reconnecting creates a *new* repo and orphans the old one).
3. Connect our own Supabase **before** any prompt mentioning auth or tables.
4. Turn off model training (free on any plan).
5. One small feature per prompt.

Cost of using our own Supabase with Lovable: built-in Stripe/Paddle payments, chat-configured logins, custom-domain email and in-editor database views all stop working. All replaced by the Supabase dashboard, and we were hand-rolling Stripe regardless.

Migrating off Lovable Cloud after the fact loses every user password, changes every user ID (so every foreign key needs hand-patching), and requires bucket-by-bucket storage re-upload. Community guides run to 33 steps.

---

## Corrections to the existing build plan

**1. The budget line is light.** Manual 9.1 has "Lovable + Supabase £25–45/mo". Receipt photos push us past Supabase's 1 GB free storage tier in month 2–3 at 30 clients (~4.5 GB/year), so **Supabase Pro at ~£20/mo is a permanent line regardless of route**. On the Lovable route add £20–80/mo on top during the build weeks.

**2. Two payment systems are being conflated.** GoCardless Direct Debit for monthly retainers (manual 7.4) and "Stripe checkout in the add-on store" (weeks 6–12) are separate integrations for separate jobs. Fees at 30 clients × £150: GoCardless ~£612/yr vs UK *business* card ~£1,584/yr. Note the business-card rate is 2.8% + 20p, not the 1.5% consumer rate usually quoted.

**3. Ship the payment version with no payment code.** At 10–50 clients, raise the invoice in QuickBooks and let its native GoCardless integration collect it. The portal displays status only. Zero lines of code until the add-on store actually needs checkout.

**4. Add a security acceptance test to M3.** Two test client accounts; client A must not be able to read client B's receipts by ID; grep the built bundle for `service_role`. Row-level security is the entire security model and is the single most common failure in AI-built apps. This gates the first real client, not the first release.

**5. Compress receipt images in the browser** to ~300 KB before upload. Materially affects both mobile experience and the storage bill.

**6. The build manual's hosting section is out of date.** klyara.com is not WordPress on Fasthosts — it is a static site served by a Cloudflare Worker out of `keypascal/klyara-web`, deployed with `npx wrangler deploy` on every push to `main`. Delete the £5–10/mo Fasthosts line from the financial model; it is £0. Host the portal on **Cloudflare Pages** rather than Netlify — same account, same DNS, one dashboard. Netlify is an equivalent alternative with no reason to prefer it here.

---

## Live-site findings, checked 27 August 2026

- **`app.klyara.com` does not exist.** `klyara.com` and `www.klyara.com` both resolve to Cloudflare and serve the Worker. There is no DNS record of any kind on `app`. Nothing is broken — it has simply never been created. Attaching the custom domain to the portal's Cloudflare Pages project creates both the record and the certificate, because Cloudflare already runs the zone.
- **The "Client login" link in the site header points at `login.html`** — the hidden control-panel gate, which is for Key and Craig, not for clients. Anyone clicking it today lands on an internal login. Repoint it at `app.klyara.com` when the portal goes live; until then point it at the contact page or hide it.
- **Everything in the `klyara-web` repo is publicly served.** `assets.directory` is the repo root, so any file added is readable at `klyara.com/<path>` unless `.assetsignore` excludes it. That includes the new `uni/` handbook — it is `noindex` and excluded in `robots.txt`, which is not access control. Nothing sensitive goes in the repo.

---

## PWA vs app stores — confirmed, with nuance

The plan's PWA-first sequencing is correct. Refinement:

- **Android**: an installed PWA is functionally native — own install prompt, WebAPK, push without installing, background sync for offline uploads. Not a compromise.
- **iOS**: three real limits. Install is manual (Share → Add to Home Screen, no triggerable prompt); push notifications only work *after* installing; no background upload. Use `<input type="file" capture>` rather than a live camera stream — `getUserMedia` is unreliable in installed iOS web apps. At 10–50 clients we walk each one through the install during onboarding.
- **Google Play** via Trusted Web Activity: $25 one-off, ~1 day of work. Two traps — the `assetlinks.json` fingerprint must be Google's *Play signing* certificate, not the local upload key; and register as an **organisation** (needs a free D-U-N-S, days–weeks lead) to skip the 12-testers-for-14-days rule that applies to personal accounts. Annual rebuild for target-API changes.
- **Apple App Store**: $99/yr, a Mac, and 1–3 weeks first pass. Guideline 4.2 rejects "repackaged websites" — passing requires bundled assets (not a remote URL), native tab bar, APNs push, native camera, Face ID lock, offline screen. Every subsequent fix needs a review cycle. **Defer** until iOS push reach demonstrably blocks sales. Keep all pricing and payment out of any iOS binary.

Effort ratio, roughly: PWA 1× · Play 2–3× · App Store 10–20×.

---

## Compliance points that touch the build

- No FCA authorisation needed to collect Direct Debits through GoCardless or Stripe — they are the regulated institution, we are a merchant. This changes entirely if the portal ever holds or moves client money.
- AML supervision (Craig's ICB/AAT route, or HMRC at £300 + £400/premises/yr) is unrelated to payments and remains the critical path.
- The portal will hold client ID documents → UK GDPR. ICO registration, Supabase DPA signed, London region, and a retention/deletion schedule designed in from day one.
- Advance notice of amount and date before each Direct Debit collection; both providers send these automatically, but confirm the notice period before promising a client a date.
- Custom Direct Debit branding costs £50/mo at both providers. Skip at launch; add past ~10 clients, or expect "who is GOCARDLESS?" support calls.

---

## Platforms considered and rejected

| Platform | Verdict | Why |
|---|---|---|
| **Bolt.new** | Best alternative if a visual builder is wanted | $25/mo, first-class Netlify + Supabase, cleanest exit — never had a "Cloud" to trap you in |
| **v0 (Vercel)** | Good, wrong shape | Weakest lock-in of any, genuinely two-way GitHub — but Next.js-shaped, pulls toward Vercel, and is a UI generator more than an app builder |
| **Replit** | Avoid | Effort-based pricing shows no price before it runs; documented $20-for-one-prompt and $1,000-in-a-week outcomes; hosting billed separately |
| **Base44 (Wix)** | Avoid | Export is front-end only — auth, schema and payments stay behind. Payments run through *their* merchant account. No bring-your-own-database |
| **Bubble** | Avoid | No code export, ever. Data exports as CSVs with relationships stripped |
| **Firebase Studio** | Dead | Closed to new users June 2026, full shutdown March 2027 |

---

*Figures checked against vendor pricing pages, docs and terms in August 2026. Lovable credit-burn figures are practitioner reports, not vendor data — directional. Not legal, financial or tax advice; the AML and Direct Debit points are pointers to check with Craig's supervisory body.*
