# klyara-web

The Klyara website, its documentation set, and (to follow) the Cloudflare Worker.

This repo's working copy **is** the live working folder:

```
...\OneDrive\Projects\WLDFIN\Companies\klyara.com\Klyara\05_Website
```

Edit files there as normal, then `git add -A && git commit && git push`. There is no second copy.

## Layout

| Path | What it is |
|---|---|
| `index.html`, `about.html`, `pricing.html`, … | Site pages, served from the repo root |
| `services/`, `blog/`, `tools/` | Site sections |
| `assets/` | Images, fonts, CSS/JS, and the public `assets/docs/` download library |
| `fonts/` | Web fonts |
| `worker/` | Cloudflare Worker — to be added |
| `_internal/` | **Not part of the site.** Business documentation — see `_internal/README.md` |

## `_internal/` — do not deploy

`_internal/` holds the marketing pack, build manual, app plans and intake notes as markdown. It is
source material, not site content, and several documents (pricing strategy, competitor benchmark,
risk register, market intelligence) are not for publication.

**Make sure your deploy excludes it.** Whatever serves this repo — Cloudflare Pages, a Worker, or
rsync — must not publish `_internal/`. If the whole repo root is the deploy output, this folder goes
public with it.

## Related

- [`keypascal/Klyara-WebSite`](https://github.com/keypascal/Klyara-WebSite) — the earlier backup of
  the same site. Now redundant: this repo supersedes it. Archive it rather than pushing to both.
- Source of truth for `_internal/` documents is the **klyara.com Claude project**; edits here do not
  flow back to it automatically.
