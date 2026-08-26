# Lovable — Prompt 1 (Foundations)

**Before pasting: create the Supabase project in the EU (London/UK) region and turn GitHub sync ON. Non-negotiable.**

Paste everything below the line into Lovable as the first prompt.

---

I'm building the client portal for **Klyara** (klyara.com), a UK bookkeeping and back-office service for construction firms and CIS subcontractors. This portal will live at **app.klyara.com**. Clients use it to sign up, upload receipts, and see their bookkeeping; the owner (admin) manages clients and reviews receipts. It must feel like a native extension of the marketing site at klyara.com, and it must work beautifully on a phone — clients are builders on site, using one thumb.

**In this first prompt, build only the foundations. Do not build receipts, dashboards with fake data, or admin features yet.**

## Design system (match klyara.com exactly)

- Colours: background paper `#F4EFE4`; deep pine green `#16352A` for headers, nav and primary surfaces; ink text `#14231C`; primary/action green `#196A48`; light accent green `#7BC79A`; muted text `#57685C`; warning `#A6592E`; hairlines `rgba(20,35,28,0.16)` on light and `rgba(244,239,228,0.16)` on dark surfaces.
- Fonts (Google Fonts): **Bricolage Grotesque** for headings (bold, tight, confident), **Instrument Sans** for body/UI, **Spline Sans Mono** for small uppercase labels, numbers and status chips.
- Shape: 16px radius on cards and inputs, 24px on large containers; soft shadow `0 26px 70px rgba(20,35,28,0.14)`; generous padding; max content width 1240px.
- Tone: calm, solid, trustworthy — a well-organised site office, not a fintech toy. No gradients, no purple, no glassmorphism.
- Wordmark: "KLYARA" in Bricolage Grotesque bold, paper-white on pine green.

## Build now

1. **Supabase auth**: email + password sign up and sign in, email verification, password reset. Pages: `/login`, `/signup`, `/forgot-password`. Auth pages are centered cards on the paper background with the KLYARA wordmark above.
2. **`profiles` table**: id (references auth user), full_name, company_name, phone, role (text, `client` or `admin`, default `client`), created_at. Auto-create a profile row on signup via trigger. Signup form collects full name, company name, phone.
3. **RLS on from the start**: users can read/update only their own profile; `admin` role can read all profiles. Never expose service keys client-side.
4. **App shell** for logged-in users: pine-green top bar with the wordmark and a profile menu (name, Sign out). Mobile: bottom tab bar with Home, Receipts, Documents, More (Receipts and Documents are placeholder pages saying "Coming soon" for now). Desktop: left sidebar, same items.
5. **Home page** after login: warm greeting ("Morning, Dave — Dave's Brickwork Ltd"), and one card: "Your Klyara portal is being set up. Receipt uploads are coming in the next few days." Nothing fake, no dummy charts.
6. **Admin placeholder**: if role is `admin`, show an extra "Admin" nav item leading to an empty `/admin` page ("Admin panel — coming soon"). Route-guard it by role.
7. **PWA basics**: manifest with name "Klyara", short_name "Klyara", theme colour `#16352A`, background `#F4EFE4`, standalone display, and a simple K-monogram icon (pine green background, paper "K" in Bricolage Grotesque) at 192px and 512px.

Keep the code clean and conventional — this project will grow into receipt capture, an admin review queue, and accounting integrations (Xero, FreeAgent, QuickBooks), so keep components small and the schema tidy.
