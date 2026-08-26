# Klyara App — Build Plan (Portal v1)

*Companion to Build Manual v3.3, Part 6.2. August 2026.*

---

## 1. What we're building, in one paragraph

The Klyara client portal at **app.klyara.com**, built in **Lovable + Supabase (EU/UK region — set at project creation, cannot be moved later)**. Clients sign up, pick their tier, snap/upload receipts, and see their bookkeeping status. Craig gets an admin panel with a receipt review queue and client management. Every client is tagged with their accounting platform — **Xero, FreeAgent, or QuickBooks** — chosen at signup, and approved receipts route to that platform. The "Login" button on klyara.com simply links to app.klyara.com; no deeper coupling needed.

Two facts to hold onto:

1. **It's a PWA, not an app-store app.** Lovable builds web apps. We make it installable ("Add to Home Screen" — icon on the phone, full-screen, camera access for receipt snaps). That is what "the app people download" means for v1, and it matches the manual's roadmap (PWA before any native-app talk). Native wrappers come later only if there's a proven reason.
2. **The portal is the front; the accounting back-end is swappable.** Clients only ever see Klyara. Whether a receipt lands in QBO, Xero, or FreeAgent is plumbing they never touch. That's the moat: switch back-ends without the client noticing.

## 2. Accounting-platform routing (the key design decision)

Each platform accepts receipts by **email forwarding** — QBO receipt forwarding address, Xero email-to-Files/Bills, FreeAgent's auto-extract email inbox. So the v1 pipeline needs **no OAuth integrations at all**:

```
Client snaps receipt in portal → Supabase Storage
→ Craig approves in admin queue
→ Edge function emails the file to that client's platform address
→ status flips to "In your books"
```

Per-client config is just two fields: `platform` (xero | freeagent | quickbooks) and `platform_inbox_email`. Craig sets the forwarding address once during onboarding (5 minutes per client, inside each platform's settings).

Full OAuth API integrations (push directly, pull P&L data back into the dashboard) are **Milestone 5** — do QBO first (day-1 standard per the manual), Xero second, FreeAgent third. Don't build them before there are paying clients on each platform; the email bridge carries the first 10–15 clients fine.

*Note: FreeAgent is new relative to the manual (which committed to QBO + Xero). It's the right add — dominant among sole traders via the NatWest/RBS/Mettle free deal, i.e. exactly the Solo/MTD segment. Treat it as inbound-only like Xero: support clients who arrive on it, standardise new ones on QBO.*

## 3. Data model (Supabase)

- **profiles** — id (=auth uid), full_name, company_name, phone, role (`client` | `admin`), created_at
- **clients** — id, owner_profile_id, tier (`solo` | `start` | `trade` | `pro`), platform (`xero` | `freeagent` | `quickbooks`), platform_inbox_email, status (`lead` | `onboarding` | `active` | `paused`), vat_registered, cis_status (`none` | `subcontractor` | `contractor` | `both`), onboarding JSONB (engagement-letter signed, ID check done, DD mandate, agent authorisation — mirrors the Part 6.5 checklist), created_at
- **receipts** — id, client_id, storage_path, uploaded_by, amount (optional), note, status (`new` | `approved` | `sent` | `rejected`), rejected_reason, sent_at, created_at
- **documents** — id, client_id, storage_path, title, category (`report` | `letter` | `vat` | `cis` | `other`), uploaded_by, created_at  *(Craig publishes P&Ls and packs here until API pull exists)*
- **addon_enquiries** — id, client_id, addon_key, message, status (`new` | `contacted` | `won` | `dismissed`), created_at

RLS from day 1: clients see only their own rows; `admin` role sees everything. Storage buckets (`receipts`, `documents`) private, path-scoped per client.

## 4. Milestones

**M0 — Foundations (Day 1).** Lovable project + Supabase in EU/UK region, GitHub sync ON before the first prompt, brand/design system lifted from klyara.com, auth (email+password, verification, reset), roles, app shell, PWA manifest. → *Prompt 1, ready now.*

**M1 — Signup & client records (Day 1–2).** Signup wizard: name/company → tier → platform (Xero/FreeAgent/QuickBooks) → VAT/CIS flags. Creates the `clients` row with status `onboarding`. Client dashboard shows onboarding progress. Goal: a stranger can sign up and land somewhere sensible.

**M2 — Receipt capture (Day 2–3).** Camera/file upload to Storage, receipt list with status chips (Received → Approved → In your books), optional amount/note. Mobile-first — this screen *is* the product for clients. Test with a real crumpled diesel receipt (manual 6.3).

**M3 — Admin panel + routing (Day 3–5).** Craig-only: client list with tier/platform/onboarding checklist, receipt review queue (approve/reject), edge function that emails approved receipts to the client's platform inbox via Brevo SMTP (SPF/DKIM already required by the manual), documents publishing. **This is launch: signed-to-live in 5 working days works end-to-end.**

**M4 — Polish & install (Week 2).** PWA install prompt, empty states, email notifications (receipt approved / document published), add-on store as enquiry cards (manual: month 1 sells core + receptionist + website + phone only; everything else "coming soon"), Cal.com embed, custom domain app.klyara.com live and linked from the site header.

**M5 — Direct API integrations (Weeks 6–12, after real clients).** QBO OAuth: push receipts as attachments/expenses, pull P&L for the dashboard. Then Xero, then FreeAgent. Kill the email bridge platform-by-platform as each goes live.

**M6+ — AI services layer (Months 2–3).** Invoice-chasing status feed, receptionist call log (Hey Jodie), Stripe checkout in the add-on store, quarterly MTD status tracker for Solo tier. Planned separately once M0–M4 is earning.

## 5. Goals & acceptance checks

- **G1 (end of week 1):** a new client can sign up, pick Xero/FreeAgent/QBO, upload a receipt from their phone, and Craig can approve it into their books — with zero WhatsApp/email juggling.
- **G2:** Craig's morning routine is one screen: review queue → approve → done. Under 2 minutes per client per day.
- **G3:** switching a client's back-end (e.g. QBO receipt snap → Dext at client 10–15) requires changing one email address in admin, nothing client-facing.
- **G4 (week 2):** portal installed on ≥3 real phones as an icon; receipt→books round trip verified on all three platforms with test accounts.

## 6. Working rules for Lovable (from the manual, they matter)

One small feature per prompt. GitHub sync on before anything. Never let Lovable touch RLS casually — review every schema change. Ship ugly by day 5; polish after clients exist. Supabase region is EU/UK **at creation** — if the project was already created in a US region, recreate it now, before there's data.

## 7. Prompt sequence (queue these after Prompt 1)

1. **Prompt 1 — Foundations** *(separate file, ready to paste)*
2. Signup wizard + `clients` table + RLS
3. Receipt upload + Storage + receipt list
4. Admin: client list + onboarding checklist
5. Admin: receipt review queue
6. Edge function: email approved receipt to `platform_inbox_email` (Brevo SMTP creds as secrets)
7. Documents: admin upload → client view/download
8. Add-on store (enquiry-only) + Cal.com embed
9. Email notifications + empty states + PWA install prompt
10. Custom domain + final QA pass
