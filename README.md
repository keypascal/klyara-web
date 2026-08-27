# klyara-web

The Klyara website, deployed as a Cloudflare Worker, plus the documentation set.

The working copy **is** the live working folder — one tree, no second copy:

```
...\OneDrive\Projects\WLDFIN\Companies\klyara.com\Klyara\05_Website
```

Edit in place, then `git add -A && git commit -m "..." && git push`. Pushing to
`main` triggers the Cloudflare build, which runs `npx wrangler deploy`.

## ⚠️ Everything in this repo is publicly served

`assets.directory` is `"."` — the repo root. Every file here is on the public
internet at `https://klyara.com/<path>` unless `.assetsignore` excludes it.

`.assetsignore` currently keeps out `.git`, `wrangler.jsonc`, `.gitignore`,
`.gitattributes`, `.htaccess`, `build-admin.py` and `README-admin.txt`.
**Do not remove the `.git` line** — Workers, unlike Pages, does not exclude it
automatically, and publishing `.git` publishes the entire commit history.

Before adding a file to this repo, decide whether the world should be able to
read it. If not, it needs an `.assetsignore` entry in the same commit.

### Known: the document library is public

`assets/docs/` (148 files) and `marketing/`, `build/`, `app/`, `misc/` are all
publicly downloadable. That includes the business plan, financial model, pricing
and scope strategy, competitor benchmark, risk register and the offer letter.

`login.html` is **not** access control — it compares credentials against string
literals in the page source on a static site, so anyone can read them with View
Source. Access control is a known outstanding task, not an oversight.

## Layout

| Path | What it is |
|---|---|
| `index.html`, `pricing.html`, … | Site pages, served from the root |
| `services/`, `blog/`, `tools/` | Site sections |
| `assets/` | Images, fonts, CSS/JS, and the `assets/docs/` library |
| `fonts/` | Web fonts |
| `marketing/` | 23 launch, SEO, pricing, sales and ops documents (markdown) |
| `build/` | Build Manual & Business Plan |
| `app/` | Portal platform decision, app build plan, Lovable prompt |
| `misc/` | Content generator, Craig intake notes |
| `uni/` | **Klyara Uni** — the internal handbook. See below. |
| `archive/` | Superseded revisions — see `archive/README.md` |
| `DOCS-INDEX.md` | Document-by-document index of the above |
| `worker/` | Cloudflare Worker code — to be added |

## Klyara Uni

`uni/` is the internal handbook — how things work here, written for Key, Craig and whoever
joins next. Reached from the control panel (`admin.html` → **Uni** tab) and directly at
`klyara.com/uni`.

**This folder is the only copy.** Add a guide here, add a card to `index.html`, then
commit and push. There used to be a second copy at `...\Klyara\11_Uni\` kept in step by a
`sync-to-website.cmd` script; it was removed on 27 August 2026 because that script copied
`index.html` across too, overwriting this folder's site-integrated version. See
`uni/README.txt`.

Guides are self-contained single HTML files: no build step, they open by double-click from
OneDrive, and they still work in ten years.

**Uni pages now require a sign-in.** Since 27 August 2026 `klyara.com/uni/` is behind
Cloudflare Access on the `Klyara admins` policy — the same policy as `admin.html` and the
document library. Before that date they were readable by anyone who guessed the filename,
so treat anything written earlier as having been public.

Access protects the `/uni/` path, not the repository: everything else here is still
published by default. No passwords, no client data, no identity documents, no bank details.

## Deploying

Cloudflare Workers Builds is connected to this repo:

- **Deploy command:** `npx wrangler deploy`
- **Build command:** none — plain HTML, nothing to compile
- **Root directory:** repo root

Locally: `npx wrangler dev` to preview, `npx wrangler deploy` to ship.

`404.html` is wired via `not_found_handling`; `html_handling` is
`auto-trailing-slash`, so `/pricing` serves `pricing.html`.

### Domain

`klyara.com` is attached as a Custom Domain — Cloudflare manages its DNS record
and certificate, so do not hand-edit that record.

`www.klyara.com` is **not** attached. It still has an old proxied placeholder
record serving `webserver is functioning normally`. A Custom Domain cannot be
created on a hostname that already has a DNS record, so delete that record
first, then add to `wrangler.jsonc`:

```jsonc
{ "pattern": "www.klyara.com", "custom_domain": true }
```

Fallback URL, always available: `klyara-web.keys-domains-moveall.workers.dev`

## Related

- Source of truth for the markdown documents is the **klyara.com Claude
  project**; edits here do not flow back to it.
- `keypascal/Klyara-WebSite` is the earlier backup of this site and is
  superseded. Delete or archive it — pushing there deploys nothing.
