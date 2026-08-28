# Klyara — Infrastructure Handover

*State as of 27 August 2026. Written to hand this off to a fresh session.*
*Updated 27 August 2026: admin panel AND document library moved behind Cloudflare Access.*
*Updated 28 August 2026: checkout location confirmed (see below); this file created on disk here — see `..\CLAUDE.md` for the whole project.*

---

## How the site ships now

```
<repo checkout — this folder>                ← working folder AND git checkout
        │                                       (one tree, no second copy)
        └── git push origin main
                  │
                  ▼
        github.com/keypascal/klyara-web (private)
                  │
                  ▼
        Cloudflare Workers Builds → npx wrangler deploy
                  │
                  ▼
        Worker "klyara-web"  →  klyara.com + www.klyara.com
```

Edit files in place, `git add -A && git commit && git push`. That's the whole loop.

- **Repo:** `keypascal/klyara-web` (private). The older `Klyara-WebSite` repo was **deleted** — it no longer exists and pushing there is not possible.
- **Worker:** `klyara-web`, account `KEYS Domains *moveall*` (`1e58cc0f3a14386313eb592ac5b9894f`).
- **Tooling installed on key-desk:** Git 2.55, GitHub CLI 2.98 (authenticated as `keypascal`).

> **Checkout location confirmed 28 August 2026:** this folder —
> `C:\Users\key\Clouds\onedrive\kieranpascal\OneDrive\Projects\WLDFIN\Companies\klyara.com\Klyara\05_Website\`.
> `C:\Users\key\klyara-web` is empty and unused — same pattern as the portal's
> old path (see `..\12_App\klyara-portal\HANDOVER.md`). `git status` and
> `git push` both work from here directly.

> **The `workers.dev` fallback URL is gone.** `klyara-web.keys-domains-moveall.workers.dev`
> and the preview URLs are both **disabled** — verified 27 August. This is deliberate: an
> enabled `workers.dev` hostname would serve the same content while bypassing the
> hostname-scoped Access policies below. Do not re-enable it without adding it to the Access
> applications first. Test against `klyara.com` instead.

### wrangler.jsonc

`assets.directory` is `"."` — the repo root is the public web root, matching the working folder layout. `html_handling: auto-trailing-slash` (so `/pricing` serves `pricing.html`), `not_found_handling: 404-page`.

Both `klyara.com` and `www.klyara.com` are attached as **Custom Domains**, so Cloudflare owns their DNS records and certificates. Do not hand-edit those rows.

> **Lesson learned:** a Custom Domain cannot be created on a hostname that already has a DNS record. Attaching apex and www together failed and rolled the apex back with it. www only worked after its old placeholder record was deleted.

---

## Access control — Cloudflare Access (added 27 August 2026)

Both the admin panel and the document library are behind **Cloudflare Access** on the Zero
Trust **Free** plan (£0, 50-seat cap). Enforcement happens at the edge, before the Worker
runs, so it covers every file under the protected paths — HTML, PDFs, everything — not just
pages that choose to check.

**Two applications, one shared policy.** The five-destinations-per-application limit is why
there are two; both point at the same `Klyara admins` policy, so access is managed in
exactly one place.

| | `Klyara Admin Panel` | `Klyara Documents` |
|---|---|---|
| Type | Self-hosted | Self-hosted |
| Destinations | `klyara.com/admin.html`, `/login.html`, `/admin` | `klyara.com/assets/docs/`, `/marketing/`, `/build/`, `/app/`, `/misc/` |
| Policy | `Klyara admins` | `Klyara admins` (the same policy) |
| Session | 24 hours | 24 hours |

| Setting | Value |
|---|---|
| Policy | `Klyara admins` — Allow, Include → Emails |
| Allowed | `key@kpascal.com`, `keyenc@proton.me`, `brewercraig627@gmail.com` |
| Team domain | `spring-pond-2578.cloudflareaccess.com` |
| Login methods | Cloudflare account sign-in, and One-time PIN by email |

Notes that will save a future session some time:

- `keyenc@proton.me` is **Key's Cloudflare account identity**, which is not the same as
  `key@kpascal.com`. The "Sign in with Cloudflare" button authenticates as the former; the
  one-time PIN box authenticates as whatever address is typed. Both are on the list, so
  either route works. This mismatch caused the first login to be refused.
- Craig uses the **Email / one-time PIN** box, not the Cloudflare button. Codes come from
  `noreply@notify.cloudflare.com`.
- **Destination paths carry a trailing slash on purpose.** `app/` not `app` — the site has a
  public `app.html` page, and a bare `app` destination risks gating it. Verified after the
  change: `/app.html` → `/app` still returns 200 to an anonymous visitor.
- `klyara.com/admin` and `/admin/` currently return the 404 page — the path is listed only
  so the gate already exists if the panel is later moved into an `/admin/` folder.
- Add or remove people at **Zero Trust → Access controls → Policies → `Klyara admins`**.
  One edit covers both applications. Removal is immediate.
- Authentication attempts are logged at **Insights & Logs → Access authentication logs**
  with email, decision and country.
- To test as an outsider without a second browser profile, visit
  `https://spring-pond-2578.cloudflareaccess.com/cdn-cgi/access/logout` first — that clears
  the Access session for the whole browser.

This is a **stopgap**. When the portal at app.klyara.com ships, the admin section moves
there behind Supabase auth and both Access applications should be deleted.

---

## ⚠️ Security — what is fixed and what is still open

### Fixed — the fake login

`login.html` compared username and password against string literals in the page source of a
static site, and `admin.html` was fetchable directly by URL with no check at all. Both are
now behind Cloudflare Access (above).

The old `klyara-admin` credential is **burned**: it sat in the page source of a public
website, and it is in the repo's git history, so deleting the file does not erase it. It
gates nothing any more — but it must never be reused for anything else, and the same goes
for any variation of it.

### Fixed — the document library

`assets/docs/` (148 files) plus `marketing/`, `build/`, `app/` and `misc/` were downloadable
by anyone with the URL, including the business plan, financial model, financial summary,
pricing-and-scope strategy, competitor benchmark, risk register and the staff offer letter.
Measured before the fix: `GET /marketing/Klyara_Sales_Pack.md` and
`GET /app/Klyara_App_Build_Plan.md` both returned **HTTP 200** to an anonymous client.

Closed 27 August by the `Klyara Documents` Access application. Verified afterwards from a
logged-out browser: all five prefixes redirect to the Access sign-in with
`auth_status: NONE`, while `/`, `/pricing`, `/about`, `/contact`, `/tools`, `/guide`,
`/app` and `/DOCS-INDEX.md` still return 200.

**Assume the documents already leaked.** They were publicly reachable from first deploy
until 27 August, and 226 of those paths were linked from an `admin.html` that anyone could
open. Access stops future downloads; it does not un-publish what was already fetched or
indexed. If anything in that set is genuinely sensitive — the staff offer letter names a
person and a salary — treat it as disclosed rather than protected.

### Still open — everything in the repo is published by default

`.assetsignore` is the only thing keeping files off the web. Its `.git` line is
load-bearing: Workers, unlike Pages, does not exclude `.git` automatically, and publishing
it publishes the entire commit history. Verified returning 404: `/.git/config`,
`/.gitignore`, `/wrangler.jsonc`, `/.htaccess`, `/build-admin.py`.

Wrangler's `Read N files from the assets directory` line counts **before** `.assetsignore`
is applied, so it is not a safety check. The only real test is requesting the path on the
deployed site.

Access now gates the known-sensitive directories, but the default is still "publish
everything". Anything new dropped into the repo is live on the web the moment it is pushed.

---

## Repo layout

| Path | Contents |
|---|---|
| `index.html`, `pricing.html`, … | Site pages, served from root |
| `assets/`, `blog/`, `services/`, `tools/`, `fonts/` | Site content |
| `marketing/` | 23 launch, SEO, pricing, sales and ops documents (markdown) — Access-gated |
| `build/` | Build Manual & Business Plan v3.3 — Access-gated |
| `app/` | Portal platform decision, app build plan, Lovable prompt — Access-gated |
| `misc/` | Content generator, Craig intake notes — Access-gated |
| `assets/docs/` | 148 published PDFs/DOCXs — Access-gated |
| `archive/` | Superseded revisions only — see `archive/README.md` |
| `DOCS-INDEX.md` | Document-by-document index — still public |

**To be removed:** `login.html` and `README-admin.txt`, along with the credential literals
in `admin.html`. Not yet done — now that the checkout path is confirmed (above), this has no
remaining blocker. Do not restore them from history once removed.

**Overlap that is NOT a duplicate:** 23 of the 24 markdown documents have a PDF/DOCX twin in `assets/docs/` (e.g. `marketing/Klyara_Sales_Pack.md` ↔ `assets/docs/08_Marketing_and_Ops/09_sales_pack.pdf`). These are source and published form of the same current documents, not old vs new. Do not "deduplicate" them.

**Genuinely archived:** `Klyara_Day_By_Day_90_Day_Plan.md` (earlier revision of `Klyara_Day_By_Day_90_Days.md`) and `Klyara_Build_Manual_v3_2.md` (byte-identical to v3.3 — the same content was saved twice under two version names; "v3.3" is not a newer revision).

---

## Email — all 14 domains

Audited 26 August 2026. **Eleven are correctly on Fastmail** (MX `in1/in2-smtp.messagingengine.com`, SPF `include:spf.messagingengine.com ?all`, all three `fm1-3._domainkey` CNAMEs):

`alicecore.com` · `alicecore.co.uk` · `axorva.com` · `fairxc.com` · `faixc.com` · `glbfi.com` · `klyara.com` · `kpascal.com` · `kpascalinc.com` · `wldfin.com` · `wldfin.co.uk`

**Two on Cloudflare Email Routing — leave alone:**

| Domain | Forwards to |
|---|---|
| `silverkid.co.uk` | catch-all + `contact@` → `kpascal@sent.com` (a Fastmail address) |
| `glbfi.co.uk` | catch-all → `k-pascal@outlook.com` |

**One on Namecheap forwarding, left as-is by decision:** `bornbroke448.com` (MX `eforward1-5.registrar-servers.com`).

### Notes

- `?all` in the SPF records is **correct** — it is exactly what Fastmail's own setup documentation specifies. Do not "harden" it to `-all` without checking Fastmail's current guidance.
- `fairxc.com` and `kpascal.com` also send through **GetResponse** (`include:_spf.getresponse.com`). Those two need GetResponse DKIM signing in place before DMARC is ever tightened past `p=none`, or their marketing mail starts failing.
- **DMARC approach: Cloudflare DMARC Management**, not `rua=mailto:` records. Email → DMARC Management → Enable, per zone. Cloudflare creates the record and parses reports into a dashboard. Per-zone, dashboard only, no API. **No `dmarc@` alias is needed on any domain.**
- `_dmarc.klyara.com` is set to `v=DMARC1; p=none;` — monitoring only, no `rua`. When DMARC Management is enabled on that zone, Cloudflare appends its own `rua` alongside.
- Existing DMARC records elsewhere: `fairxc.com` and `kpascal.com` both have a bare `v=DMARC1;p=none` with no reporting address, so they currently report nothing. Enabling DMARC Management on those zones fixes it.
- `C:\Users\key\cf-dmarc.ps1` is a PowerShell script that bulk-sets `rua=mailto:` DMARC records across all zones via the API. **Not needed** given the dashboard approach — kept only if a raw copy of reports is ever wanted. Holds no secrets; safe to delete.

---

## Open items

| Item | Owner | Notes |
|---|---|---|
| Delete `login.html` / `README-admin.txt` from the repo | Key | The credential is already dead — Access gates the panel — so this is tidying, not a fix. No longer blocked (checkout path confirmed above). |
| Decide whether the leaked documents need any action | Key | They were public from first deploy until 27 August. The staff offer letter is the one with a named person's pay in it. |
| Enable DMARC Management on the remaining 13 zones | Key | ~1 min per zone in the dashboard. |
| Canonical tags | Not started | **0 of 98 pages** have `rel="canonical"`. Apex and www serve identical content, and `auto-trailing-slash` means `/pricing` and `/pricing.html` both resolve — three URLs per page with nothing declaring which counts. Worth fixing before the site starts earning links. |
| GetResponse DKIM | Key | Prerequisite for tightening DMARC on `fairxc.com` / `kpascal.com`. |

**Closed 27 August:** access control for the admin panel *and* for the document library,
both via Cloudflare Access. Verified from a logged-out browser, not assumed.

**Closed 28 August:** the checkout location. See the note at the top.

---

## Gotchas worth remembering

- **Git may live inside OneDrive.** If it does, sync can touch `.git` mid-commit and corrupt the index — a stale `index.lock` file blocking a commit is the usual symptom. Fix: delete the lock file (`Remove-Item .git\index.lock -Force`) and retry; nothing else is usually wrong. Push after every session so GitHub always holds a good copy.
- **The Cloudflare *Add record* modal is hostile to automation.** Its type dropdown drops clicks mid-animation and silently selected `SVCB` once during this work. The inline **Edit** row on an existing record is reliable; the Add modal is not. Prefer the API for bulk DNS work.
- **Wrangler's asset count is not a safety check.** See the security section above.
- **The Zero Trust dashboard moved.** Access lives under `dash.cloudflare.com/<account>/one/access-controls/…` now, not `/one/access/…`; identity providers are under `/one/integrations/identity-providers`; the create-app form is at `/one/access-controls/apps/self-hosted/add`. Old bookmarks 404.
- **Zero Trust Free still requires a checkout.** Activating the £0 plan asks for a billing address, a payment method and an authorisation to charge for usage beyond free limits. It is genuinely free at this scale; the card is just on file.
- **`.html` URLs redirect.** `auto-trailing-slash` means `/pricing.html` 302s to `/pricing`. When probing whether a path is Access-gated, a redirect alone proves nothing — follow it and check whether it lands on `cloudflareaccess.com`.
- **`npx wrangler deploy` from a fresh shell needs `CLOUDFLARE_API_TOKEN` set**, or an interactive login (`npx wrangler login`). A fresh shell started here has neither by default — check before assuming a deploy will work, or expect the "non-interactive environment" error.
