KLYARA — HIDDEN ADMIN PANEL
===========================

WHAT IT IS
  A read-only control panel for the Klyara delivery pack, built into the existing static site.
  Reached at /admin.html, gated by the form on /login.html.

  This is a convenience gate for a static site, not authentication — anyone who views source can
  read the credential, and the panel must never hold anything that would matter if it leaked.

  Everything is view-and-download. Nothing on the panel edits, uploads, saves or posts.

HOW TO GET IN
  /login.html  →  username  klyara-admin
                  password  *P0k31t1029!
  Any other credentials show the existing preview message and do not navigate anywhere.

WHAT IS IN IT
  90-day plan      The whole day-by-day plan as a dated timeline, with a live "you are here"
                   marker computed from the browser's clock, a progress ring, four phase bands,
                   seven milestones and every day expandable to its tasks.
  Business plan    All fourteen sections readable in the browser with every chart inline, plus
                   the Word, PDF and PowerPoint downloads.
  Documents        The whole delivery pack grouped by the same folders as the ZIP, with search,
                   folder filters, page previews and a download per format.
  Compliance       AML/MLR supervision, the ICO data protection fee, professional indemnity
                   insurance and ASA/CAP compliance of the site's claims, as a status board.
                   Every item reads at the state Klyara is genuinely at: nothing is claimed.
  Quick links      OneDrive (placeholder), Brevo, Cal.com, QuickBooks, HMRC ASA, Google Business
                   Profile, ICB, ICO, ASA.
  Launch control   Where the project stands, illustrated: animated counters, the decision blocks,
                   the phase timeline, a live bar chart of the pack, and the defect list.

FILES
  admin.html                 the panel (one page, no page loads between views)
  assets/css/admin.css       panel styles — additive, nothing existing is touched
  assets/js/admin.js         panel behaviour
  assets/data/plan.json      the 90-day plan, generated
  assets/data/library.json   the document index, generated
  assets/data/bplan.json     the business plan, generated
  assets/data/*.js           identical payloads on a window.KLY_* global, so the panel also
                             works from a file:// URL where fetch() is blocked
  assets/docs/<folder>/      the staged deliverables — the same files that go in the ZIP
  assets/docs/_prev/         first-page PNG previews
  build-admin.py             regenerates all of the above
  login.html                 the only existing page that was changed, and only to add routing

REBUILDING
  python3 site/build-admin.py

  It copies /root/klyara/v2/out/** into site/assets/docs/, renders a first-page preview for
  every PDF, parses docs/16-day-by-day-plan.md into plan.json, extracts the business plan
  DOCX into bplan.json, and walks the staged folders to rebuild library.json. Nothing in
  those three files is hand-typed, so adding or removing a deliverable and re-running is
  the whole update procedure.

BEFORE IT GOES ANYWHERE PUBLIC
  - Paste the real OneDrive folder URL into admin.html (the link with id "q-onedrive").
  - admin.html carries noindex/nofollow, and it is not in sitemap.xml. Keep it that way.
  - Serve /admin.html and /assets/docs/ behind real server-side auth if the pack ever holds
    anything confidential. The gate on login.html will not stop anyone who looks.
