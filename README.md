# klyara-web

The Klyara website, deployed as a Cloudflare Worker, plus the business documentation set.

This repo's working copy **is** the live working folder:

```
...\OneDrive\Projects\WLDFIN\Companies\klyara.com\Klyara\05_Website
```

Edit in place, then `git add -A && git commit -m "..." && git push`. There is no second copy.
Pushing to `main` triggers the Cloudflare build, which runs `npx wrangler deploy`.

## Layout

| Path | What it is |
|---|---|
| `public/` | **The site.** Everything here is served. `public/index.html` is the homepage. |
| `_internal/` | Business documentation. Not served — see below. |
| `wrangler.jsonc` | Worker config. `assets.directory` is `./public`. |
| `README.md`, `.gitignore`, `.gitattributes` | Repo housekeeping, not served. |

Site URLs are unchanged by the `public/` folder: `public/` *is* the web root, so
`public/pricing.html` is still `https://klyara.com/pricing`.

## Why the site sits in `public/`

`_internal/` holds the business plan, pricing strategy, competitor benchmark, market intelligence
and risk register. If the assets directory were the repo root, a single wrong line in an ignore file
would publish all of it — along with `.git`, which would expose the entire history.

Putting the site in `public/` makes that structurally impossible: `_internal/` and `.git` are
siblings of the assets directory, not inside it, so Wrangler never sees them.
`public/.assetsignore` is a second layer, not the only one.

**Do not change `assets.directory` to `"."`.**

## Deploying

Cloudflare Workers Builds is connected to this repo:

- **Deploy command:** `npx wrangler deploy`
- **Build command:** none — the site is plain HTML, nothing to compile
- **Root directory:** repo root (where `wrangler.jsonc` lives)

Locally: `npx wrangler dev` to preview, `npx wrangler deploy` to ship.

`404.html` is wired up via `not_found_handling`, and `html_handling` is set to
`auto-trailing-slash` so `/about` serves `about.html`.

## `_internal/`

| Path | Contents |
|---|---|
| `_internal/marketing/` | 24 launch, SEO, pricing, sales and ops documents |
| `_internal/build/` | Klyara Build Manual & Business Plan |
| `_internal/app/` | Portal platform decision, app build plan, Lovable prompt |
| `_internal/misc/` | Content generator script, Craig intake notes |
| `_internal/admin-tooling/` | `build-admin.py` and its README |
| `_internal/legacy/` | Old Apache `.htaccess`, kept for reference only — Cloudflare ignores it |

See `_internal/README.md` for the document-by-document index.

**Note on `build-admin.py`:** it resolves paths relative to its own location and reads from a Linux
path (`/root/klyara/v2/out/`) that does not exist on this machine, so it cannot run as-is. Moving it
out of the site root does not make it any more broken, but if you revive it, its output paths now
need to point at `public/`.

## Related

- [`keypascal/Klyara-WebSite`](https://github.com/keypascal/Klyara-WebSite) — earlier backup of the
  same site, superseded by this repo. Archive it rather than pushing to both.
- Source of truth for `_internal/` documents is the **klyara.com Claude project**; edits here do not
  flow back to it automatically.
