# Klyara client portal — where it stands

_Written 27 August 2026, at the end of an overnight build-and-audit session._

## The one-line version

`app.klyara.com` is live, deployed, tested and pushed. The database schema is
applied through migration 0016. Four write-side security holes that were
exploitable from a normal client login have been closed, the tax engine has
been corrected against current HMRC rates, and the app now works with no
signal at all.

---

## What it is

| Piece | Where | Notes |
| --- | --- | --- |
| Client portal | `app.klyara.com` | React 19 + Vite 8 + Tailwind v4, served as static files by Cloudflare Pages, project `klyara-portal` |
| Website | `klyara.com` | A Cloudflare Worker serving the repo root as assets. **Not** WordPress. |
| Database and auth | Supabase project `pfxlcxofbkexrqhplyul` | Region eu-west-2 (London) |
| Portal source | `github.com/keypascal/klyara-portal`, and `C:\Users\key\klyara-portal` | |
| Website source | `github.com/keypascal/klyara-web`, and the OneDrive `05_Website` folder | The OneDrive folder **is** the repo working copy |
| Handbook | `klyara.com/uni/`, behind Cloudflare Access | Five guides |

The browser holds the Supabase anon key and talks to Postgres directly. That
means **row-level security is the entire security model** — there is no server
in between to check anything. Every rule has to live in the database.

## Accounts

| Who | Email | Note |
| --- | --- | --- |
| Admin | `key@kpascal.com` | **Change this password.** It was set during the build and has been in a transcript. |
| Demo client | `demo@klyara.com` | Three seeded receipts, for showing people |

## What changed in this session

### Security — four exploitable holes, plus one found while verifying

Migration `0015_security_and_integrity.sql`:

1. **`clients` had no INSERT guard.** It had one on UPDATE, so nobody noticed.
   A signup could post its own row with `tier: 'pro'`, `status: 'active'`, a
   `platform_inbox_email` of its choosing, and the whole onboarding checklist
   ticked — including `id_check`, which is an anti-money-laundering record.
   Now forced to safe values on insert.
2. **`receipts.storage_path` was unvalidated free text**, and server-side code
   dereferences it later. A crafted path was a read primitive into another
   client's folder, and through the `route-receipt` function a mail relay on
   Klyara's own SPF and DKIM. Now constrained to the client's own folder, with
   `..` and absolute paths rejected.
3. **Add-on enquiries could be filed already marked `won`.**
4. **Invoice totals were computed by trigger but not pinned**, so a direct
   PATCH could leave a £12,000 invoice with `due_total` 0.

The guards also stopped trusting `auth.uid() is not null` to mean "our own
server sent this" — true only while `anon` holds no write grants, which is one
grant away from failing open. They test the Postgres role instead, which meant
moving them from SECURITY DEFINER to SECURITY INVOKER.

Migration `0016_revoke_stray_grants.sql`: Supabase's default privileges grant
`all` on new public tables, and `all` includes TRUNCATE. Every table added in
0011–0013 had handed TRUNCATE, REFERENCES and TRIGGER to **`anon`** — the role
whose key ships inside the JavaScript bundle. PostgREST cannot issue a TRUNCATE
today so it was not exploitable as things stood, but TRUNCATE ignores RLS
entirely. `anon` now holds nothing at all in `public`.

**Migration 0014 had never actually been applied** to the live database,
despite the schema being described as current. The deadline screen was
querying columns that did not exist. Applied.

### Tax and figures

- **HMRC raised the approved mileage rate to 55p on 6 April 2026.** The app was
  on 45p. Rates now carry the date they changed on, so a trip logged last March
  is still worth 45p, and the database prices the trip rather than the browser.
- The 10,000-mile step was dead code. 9,990 miles logged plus a 500-mile trip
  said £275; it is £128.
- The VAT deadline disappeared from the screen during the fortnight it was
  actually due.
- Corporation Tax "nine months and a day" overflowed: a 31 May year end said
  4 March instead of 1 March.
- Deadlines now fall back past bank holidays, computed rather than listed.
- Take-home applies the £100,000 allowance taper and the 45% band.
- Employer pension is 3% of qualifying earnings, not of salary.
- The £10,500 Employment Allowance is offered.
- CIS distinguishes plant hired in from plant the subcontractor owns
  (CISR15090) — the app previously excluded both.
- Reverse-charge invoices show the rate the customer must account for, as HMRC
  requires, and warn about the end-user exception.
- VAT extract rounds once, so net, VAT and gross always agree.
- Every calendar date is derived locally — nothing shifts a day under BST.
- A negative unit price survives the input; credit lines used to flip sign.

### New

- **The offline outbox.** A receipt no longer depends on the network at the
  moment it is taken. It goes into IndexedDB and uploads itself when a
  connection comes back — after the phone is locked, the app closed, or days
  later. This is the single most important reliability change in the app.
- **An error boundary.** A render error used to leave a white screen.
- **Get it out.** FreeAgent bank CSV, Xero and QuickBooks invoice imports, the
  nine VAT return boxes for a period, and plain spreadsheets of everything.
- **Search over everything.** Ctrl-K, or the magnifier in the header.
- **A Content-Security-Policy**, generated at build time from the same Supabase
  URL the bundle was compiled against so the two cannot drift.
- **Self-hosted typefaces.** A page load now makes zero requests outside our own
  origin and Supabase.

## The tests, and how to run them

From `C:\Users\key\klyara-portal`:

```
node scripts/test-tax.ts             61 assertions — rates, dates, bank holidays
node scripts/test-exports.ts         31 assertions — every export format, every VAT box
node scripts/verify-db.mjs           the live schema: tables, policies, triggers, grants, views
node scripts/rls-test.mjs            37 real attacks against the live database
node scripts/test-invoice-maths.mjs  CIS and VAT against hand-worked figures, live
node scripts/smoke-live.mjs https://app.klyara.com
```

And against a local build (`npm run build`, then `npx vite preview`):

```
node uitest2.mjs     134 checks, including driven calculators and an offline receipt
node a11y.mjs        axe over 23 screens as client and admin
node cspall.mjs      21 screens under the real Content-Security-Policy
```

Everything above passes as of this writing. `rls-test.mjs` is the one that
matters most: **every line must read PASS before a real client is added.**

## Two things waiting on you

1. **Rotate the Cloudflare API token.** It was echoed into a transcript during
   the build by a `.cmd` file missing `@echo off`. Nothing has been done with
   it, but rotate it.
2. **A Brevo API key** for `route-receipt`, so approved receipts can be emailed
   to the client's platform inbox.

Neither blocks anything else.

## What I would do next, in order

1. **A direct API connection to QuickBooks, Xero and FreeAgent.** The CSV
   exports get the figures across; OAuth and a refresh-token store would remove
   the step entirely. This needs a small server — a Supabase Edge Function is
   enough.
2. **Customers as records rather than free text.** `customer_name` is typed
   fresh onto every invoice. A contacts table would give repeat customers, a
   statement per customer, and chasing that knows who to chase.
3. **Recurring invoices** for retainer work.
4. **Site photographs against a job**, not only receipts. The storage and the
   policies already exist.
5. **A focus trap in the search and sheet overlays.** Escape and arrows work;
   Tab can still reach the page behind. Minor, but worth doing.
6. **Push notifications** for a published document or a message, once the PWA
   is installed on enough phones to be worth it.

## Things worth knowing before you touch it

- **The OneDrive `05_Website` folder is the website's git working copy.** Editing
  a file there and committing is the whole deploy process, plus
  `npx wrangler deploy`.
- **Everything in the website repo is served publicly** — `assets.directory` is
  the repo root. `.assetsignore` is what stops `.git` being published. Do not
  remove that line.
- **The Uni and the control panel are behind Cloudflare Access.** That is real
  access control. It is still not a safe deposit box: nothing sensitive goes in
  the repo.
- **Never let a build ship without its environment variables.** `import.meta.env`
  is replaced with a literal at build time, so a module-level `throw` becomes
  provably unconditional and the minifier deletes the entire application behind
  it — a green build, a normal-sized bundle, and a blank white screen. There is
  a prebuild guard for this now. Leave it there.
- **When HMRC moves a rate, add a band with the date it changed.** Do not edit
  the old one, or every historic figure in the app silently changes.
