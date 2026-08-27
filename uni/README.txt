KLYARA UNI
The internal handbook. How things work here, written down once.

WHAT THIS IS
  Guides for Key, Craig and anyone who joins later. Not client-facing, not marketing.
  Open index.html to browse. Every guide is one self-contained HTML file. It opens
  fine by double-click from this folder - the stylesheets, fonts and icons it uses are
  in ..\assets\ right next to it, so no internet is needed.

WHERE IT LIVES
  This folder is the ONLY copy. Edit here, commit, push.
  Live at klyara.com/uni  ->  reached from klyara.com/admin.html, the Uni tab.

  There used to be a second copy in ..\11_Uni with a sync-to-website.cmd script.
  That was removed on 27 August 2026: two copies drift, and the sync script copied
  index.html over the website's own version, which broke its styling. One folder now.

ADDING OR CHANGING A GUIDE
  1. Put the file in this folder.
  2. Add a card to index.html.
  3. In ..\ run:  git add -A  &&  git commit -m "uni: ..."  &&  git push
     Cloudflare rebuilds on push; live in about a minute.

ACCESS - THIS CHANGED ON 27 AUGUST 2026
  klyara.com/uni/ now requires a sign-in. It is behind Cloudflare Access, on the same
  "Klyara admins" policy as the admin panel and the document library. Only the email
  addresses on that policy get in; everyone else is refused and the attempt is logged.
  This is real access control, not the robots.txt obscurity it used to rely on.

  Manage who has access at:
    Cloudflare dashboard -> Zero Trust -> Access controls -> Policies -> "Klyara admins"

STILL BE CAREFUL WHAT GOES IN HERE
  Access protects the path, but this folder is inside the website repository, and the
  repository's default is to publish everything. A file that ends up outside the /uni/
  path is public. The guides were also readable by anyone before 27 August 2026, so
  treat anything written here before that date as having been public.

  No passwords. No client data. No identity documents. No bank details. No API keys.
  If it would be a problem in a competitor's hands, it does not go in the Uni.

CURRENT GUIDES
  01  portal-build-playbook.html      the client portal: stack, costs, platform choice,
                                      payments, app stores. Nine chapters, interactive.
  02  portal-platform-decision.md     the short written record of the decision.
  03  portal-user-guide.html          for clients. How to use the portal. Send this to
                                      them instead of explaining it down the phone.
  04  portal-admin-guide.html         for Craig. The morning routine, onboarding a client,
                                      the receipt inbox address, and what to do when it breaks.

Started 27 August 2026.
