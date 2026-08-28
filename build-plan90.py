# -*- coding: utf-8 -*-
"""Klyara — plan90.json generator.

Source: docs/16 (day-by-day), docs/14 (90-day plan), docs/02 (account setup),
docs/06 (ops playbook), docs/12 (client onboarding), v3/SPEC.md.

Anchors (SPEC, non-negotiable):
  Setup  Tue 1 Sep 2026 - Sun 13 Sep 2026
  Day 1  Mon 14 Sep 2026
  Day 90 Sat 12 Dec 2026
Nothing is scheduled for Kieran or Craig before Tue 1 Sep 2026.

The day-by-day source had its DATES re-anchored a week later but its PROSE left
behind, so hard-deadline copy sat seven days after the deadline it described.
Every fixed date below is placed on the day it actually falls on, and a CIS
deadline landing on a weekend moves BACK, never forward.
"""
import datetime as dt, json, io, os, re

LAUNCH = dt.date(2026, 9, 14)
SETUP_START = dt.date(2026, 9, 1)
SETUP_END = dt.date(2026, 9, 13)
DAY90 = dt.date(2026, 12, 12)

WD = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
WDL = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MONL = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December']


def date_of(n):
    """Date of plan day n (1..90)."""
    return LAUNCH + dt.timedelta(days=n - 1)


def setup_date(n):
    """Date of setup day n (1..13)."""
    return SETUP_START + dt.timedelta(days=n - 1)


def label(d):
    return '%s %d %s' % (WD[d.weekday()], d.day, MON[d.month - 1])


def longlabel(d):
    return '%s %d %s %d' % (WDL[d.weekday()], d.day, MONL[d.month - 1], d.year)


# ── owners ────────────────────────────────────────────────────────────────
K, C, B = 'K', 'C', 'B'      # Kieran, Craig, both

# ── task helper ───────────────────────────────────────────────────────────
def T(title, owner, minutes, why, tips, wrong, fix, subs=(), deps=(), flags=()):
    return dict(title=title, owner=owner, minutes=minutes, why=why,
                tips=list(tips), wrong=wrong, fix=fix,
                subtasks=list(subs), deps=list(deps), flags=list(flags))


# ══════════════════════════════════════════════════════════════════════════
# The weekly rhythm — docs/16 "the printable week", docs/06 §2.
# Generated onto every one of the 90 days so no day is ever empty, each with
# its own reason, tips, failure mode and fix.
# ══════════════════════════════════════════════════════════════════════════
RHYTHM = {
    0: [  # Monday
        T('07:30 — Anchor post to LinkedIn, X, Facebook and Instagram', C, 15,
          'The anchor is the one post that carries the week. Everything else that week is a '
          'variation on it, and reach on LinkedIn is decided in the first sixty minutes.',
          ['Post to Craig’s personal profile first, then the Company Page — LinkedIn gives a '
           'personal post several times the reach of a page post.',
           'No outbound link in the post body. Put the link in the first comment.',
           'Write it the Friday before, in the production hour. Monday morning is for posting, '
           'not for writing.'],
          'It gets written on Monday morning, so it goes out at 09:40 instead of 07:30 and half '
          'the reach is already gone.',
          'Write next week’s anchor in Friday’s production hour. If Monday arrives and '
          'nothing is written, post last month’s best performer again rather than nothing.',
          subs=['Publish to Craig’s personal LinkedIn and pin it if it is a big one',
                'Company Page version',
                'X version — reformat, do not paste the LinkedIn copy',
                'Facebook Page version',
                'Instagram version with the matching asset']),
        T('07:45 — Google Business Profile post', C, 5,
          'GBP is the highest-return five minutes in the whole pack. Posts no longer expire, but '
          'only the newest shows prominently, so a stale profile reads as a firm that went bust.',
          ['The year of posts is already written and dated in docs/13 — copy, do not compose.',
           'Always set a button. "Learn more" pointed at the page the post is about.',
           'If the profile is not verified yet, write the post anyway and queue it.'],
          'It is the first thing dropped in a busy week, and it is the one thing that must never '
          'be dropped.',
          'Five minutes, in the same sitting as the anchor post. Never a separate task in the day.'),
        T('Reply to every comment left over the weekend', C, 10,
          'Not replying is worse than not posting. An unanswered comment is a public signal that '
          'nobody is home.',
          ['Reply properly — a sentence with something in it, not "thanks!".',
           'Answer in the thread, not by DM. The answer is the content.'],
          'Weekend comments get seen on the phone, mentally answered, and never actually answered.',
          'Do it before the anchor post goes out, so the profile is clean when the new traffic '
          'arrives.'),
    ],
    1: [  # Tuesday
        T('Short video, uploaded natively to TikTok, Reels and YouTube Shorts', C, 20,
          'Vertical video is the only channel here that reaches people who have never heard of '
          'Klyara. Everything else preaches to a list.',
          ['Upload the file separately to each platform. Never cross-post a watermarked export — '
           'every platform demotes a competitor’s watermark.',
           'Add a trending audio from the platform’s own commercial library at low volume. '
           'The kit videos are silent by design so you can.',
           'Caption in the first three words says who it is for: "Subbies —".'],
          'One file gets shared to all three from the TikTok share sheet, and Reels and Shorts '
          'both bury it.',
          'Download the render three times, upload three times. It costs four extra minutes.',
          subs=['TikTok', 'Instagram Reels', 'YouTube Shorts',
                'Add the caption and the pinned first comment']),
    ],
    2: [  # Wednesday
        T('Carousel to Instagram, and as a LinkedIn document post', C, 20,
          'Carousels are the format that gets saved, and saves are what LinkedIn and Instagram '
          'both weight most heavily.',
          ['For LinkedIn, export the slides as a single PDF so it renders as a document.',
           'Slide one is a claim, not a title. "Most subbies overpay CIS" beats "CIS explained".'],
          'The slides are uploaded as separate images on LinkedIn, which kills the swipe.',
          'PDF on LinkedIn, image set on Instagram. Two exports from the same folder.'),
        T('17:30 — The community slot. One real answer. No link.', C, 30,
          'This is the slot that builds the pipeline. It is slow precisely because it works, and '
          'it is the first slot that gets cancelled.',
          ['Answer one question properly rather than five badly. Use docs/15 for the substance '
           'and rewrite the opening line every time — copy-paste answers read as copy-paste.',
           'No link and no signature until you are past eight to ten genuine answers.',
           'Reddit stays read-only for the first three weeks. Doc 01 has the protocol.'],
          'It is dropped for two weeks running, the accounts go quiet, and forum credibility '
          'resets to zero — visibly, because the post history has a hole in it.',
          'Never drop it twice in a row. If the week is gone, spend ten minutes on one answer '
          'rather than skipping it.'),
    ],
    3: [  # Thursday
        T('The week’s big piece — a long video or the week’s main page', C, 120,
          'One substantial asset a week is what the shorts, the carousel and the newsletter all '
          'cut from. Without it you are producing seven things instead of one.',
          ['Phone on a tripod is fine. Audio matters more than video — a £15 lapel mic is the '
           'single best purchase in the kit.',
           'Scripts are written in docs/04. Read them aloud once before recording.',
           'Upload with the description and timestamps, and add it to the right playlist.'],
          'It slips to Friday, then to the weekend, then it does not happen and the week has no '
          'centre.',
          'Record badly rather than not at all. An unpolished seven-minute video that exists '
          'beats a perfect one that does not.'),
    ],
    4: [  # Friday
        T('Practical post — a tool, a template or a date', C, 20,
          'Friday is the day people are thinking about the week they have just had. A practical '
          'post lands better here than an opinion.',
          ['A free calculator is welcome in places a service link gets removed. That is the '
           'whole reason the tools exist.',
           'Give the thing away outright. No email wall on the Friday asset.'],
          'It turns into a sales post, and the engagement halves.',
          'If the post has a CTA in it, cut the CTA. The tool is the CTA.'),
        T('16:00 — Production hour', C, 60,
          'The hour that makes every other slot cheap. Next week gets written while this week is '
          'still fresh.',
          ['Write next week’s anchor post first, while you still remember what got replies.',
           'Record one short video on the phone.',
           'Schedule everything that can be scheduled.'],
          'It is the slot that gets eaten by client work, and then Monday is written on Monday.',
          'Diarise it as a recurring appointment now, not as a to-do. It survives as an '
          'appointment and it does not survive as a to-do.',
          subs=['Write next week’s anchor post',
                'Record one short video',
                'Schedule the week’s posts',
                'Check next week’s deadlines against the plan']),
        T('Log the four numbers', K, 10,
          'Four numbers, every Friday, even when they are all zero. The habit is the point — you '
          'cannot kill a channel you never measured.',
          ['Booked discovery calls · cost per booked call · guide downloads · GBP calls, '
           'directions and website clicks. Nothing else is a goal.',
           'Followers are not a business metric. Do not record them.',
           'The KPI workbook has the twenty-six week tracker built.'],
          'Weeks one to four are all zeros, it feels pointless, and the habit dies before the '
          'numbers become interesting.',
          'Log the zeros. The zeros are the baseline that makes month three legible.'),
    ],
    5: [  # Saturday
        T('One light human post', C, 15,
          'One post a week that is not about tax keeps the account looking like a person rather '
          'than a feed. It is also the post that most often gets the most comments.',
          ['A photo from a site, a van, a genuinely bad receipt. Nothing staged.',
           'Ask a real question. "What is the worst bit of admin in your week" outperforms '
           'everything else in the pack.'],
          'It gets skipped because it feels unimportant, and it is the cheapest reach in the week.',
          'Fifteen minutes on a Saturday morning. If it is missed, it is the first thing that may '
          'be dropped without consequence — nobody notices a missing Saturday post.'),
    ],
    6: [  # Sunday
        T('Week-ahead post — the deadlines coming up', C, 20,
          'The week-ahead post is the one that gets saved and screenshotted, because it is the '
          'only post in the feed that tells somebody what they have to do.',
          ['Flag deadlines that are still ahead. A post flagging a date that has already passed '
           'is the fastest way to look like you are not paying attention.',
           'Check the fixed-dates list in this panel before writing it.'],
          'It repeats last week’s deadline because the copy was written a month ago and not '
          're-read.',
          'Read the fixed dates for the coming seven days from this panel, then write the post.'),
    ],
}


# ══════════════════════════════════════════════════════════════════════════
# SETUP PHASE — Tue 1 Sep to Sun 13 Sep 2026. Thirteen days, ~18 hours.
# Two waiting clocks start on day one because everything queues behind them.
# ══════════════════════════════════════════════════════════════════════════
SETUP = {
 1: dict(one='Start the two clocks. Nothing else in the ninety days matters as much as these two going in today.',
   tasks=[
    T('Apply for the ICB practice licence', C, 60,
      'It includes MLR supervision, and supervision is the thing that lets Klyara lawfully take '
      'bookkeeping clients. Every pound of revenue in the plan sits behind it.',
      ['£94 to apply, then £373–£406 a year — £206 licence plus £167–£200 membership.',
       'Stated processing is 28 days, so a 1 September application puts supervision around '
       '29 September, before the launch has had a month to produce anybody.',
       'Cheaper and faster than registering with HMRC directly: £300 plus £400 per premises, '
       'up to 45 days.',
       'Write the application date on a wall. It is the question you will be asked most.'],
      'It slips a fortnight "because there is no rush", and the 28-day wait lands in the middle '
      'of the launch month instead of before it.',
      'Apply on the first morning, before anything else on this list. Then chase weekly the '
      'moment it passes 28 days.',
      subs=['Confirm professional indemnity cover is in hand or quoted — ICB will not licence without it',
            'Complete the application and pay the £94',
            'Diarise the 28-day mark as a chase date',
            'Write the application date on the wall'],
      flags=['blocking', 'wait', 'cost']),
    T('Start the Google Business Profile claim', C, 30,
      'Verification takes 5 to 14 days and every local-search result in this plan sits behind it. '
      'It is the longest lead time in the pack after the licence.',
      ['Business name is exactly "Klyara". Do not add keywords — Google suspends listings for it '
       'and a suspension is a fortnight of pain to reverse.',
       'Set it up as a service-area business if home-based, 15-mile radius, and name the six to '
       'eight towns you actually want.',
       'docs/02 §1 has the description written to Google’s 750-character limit.'],
      'The claim is started and then abandoned half-finished waiting on the address decision, so '
      'the verification clock never actually starts.',
      'Start the claim today even if the address decision is not final. The clock matters more '
      'than the completeness.',
      subs=['Claim the listing', 'Choose primary category: Bookkeeping service',
            'Request verification and note the method and date'],
      flags=['blocking', 'wait']),
    T('Get professional indemnity insurance quotes', C, 20,
      'PII is a condition of the practice licence, so it sits in front of AML supervision rather '
      'than beside it.',
      ['ICB members have a discounted route — ask for it by name.',
       'Get three quotes. Decide the cover level with the other founder in decision block 2.'],
      'Quotes are requested and then nobody chases, so the licence application stalls on a '
      'condition that took ten minutes to satisfy.',
      'Chase on Thursday 3 September if nothing has come back.',
      deps=[], flags=['cost']),
    T('Sit down together and read docs/18 — the thirty decisions', B, 30,
      'Thirty decisions only the two of you can make. Until they are made, a large part of this '
      'plan is guesswork with a date on it.',
      ['One sitting, about 105 minutes across seven blocks. Craig is needed for two of them.',
       'Write the answers down. A decision that is not written down gets re-made differently '
       'next month.'],
      'It gets deferred to "when we have time", and the same five questions block work every week '
      'for a month.',
      'Book the sitting now, in the diary, for the first weekend. Then it happens.',
      flags=['both', 'blocking']),
   ]),
 2: dict(one='Kill the testimonials. Nothing else on the site matters until they are gone.',
   tasks=[
    T('Remove the five invented homepage testimonials', K, 45,
      'Fake reviews are a banned practice under the DMCC Act 2024 and a conduct issue in front of '
      'a licence application. Klyara has no clients — nothing on the site may imply otherwise.',
      ['The five are Marcus B., Dean W., Sam O., Priya T. and Jodie F.',
       'Replacement copy is already written: docs/07 §Option B, the honest-new-firm block.',
       'This is not a style note. It is a legal exposure and it is the highest-scoring item on '
       'the risk register.'],
      'It is left because the page "looks empty without them". It does not look empty with the '
      'replacement block in.',
      'Paste the replacement block in the same sitting you delete the testimonials, so the page '
      'is never in a half state.',
      subs=['Delete all five testimonial cards',
            'Paste the honest-new-firm block from docs/07 §Option B',
            'Search the whole site for any other named client or quote',
            'Re-check the homepage at 390px after the swap'],
      flags=['blocking']),
    T('Read docs/07 top to bottom', K, 15,
      'It is fifteen minutes and it is the only document in the pack that describes a legal '
      'exposure rather than a marketing opinion.',
      ['Read it before touching any other page, so the rest of the audit is done with the rules '
       'in your head.'],
      'It gets skimmed, and the claims audit then misses the ones that matter.',
      'Read it properly once. It does not need re-reading after that.'),
    T('Future-tense every site claim that is not true today', K, 60,
      'Certifications, "24/7 answering", the AI services and the client portal are all described '
      'in the present tense on a site where several of them are not live.',
      ['docs/07 has the checklist of every claim to check.',
       '"Coming soon" is a legitimate answer. "We do" when you do not is not.',
       'The compliance tab of this panel lists the seven claims to check.'],
      'The obvious ones get fixed and the ones inside service pages and meta descriptions get '
      'missed.',
      'Grep the site for the claim words, not just the pages. Check titles and meta descriptions '
      'as well as body copy.',
      subs=['"Qualified, not just confident" — which qualifications are held today?',
            'Xero / QuickBooks / FreeAgent certified — is certification actually done?',
            '"24/7 answering" — is the service live and wired to the number?',
            'AI receptionist, chatbot, invoice chasing — mark as coming soon',
            'Client portal — app.klyara.com is live; say what it does and nothing more',
            'Review collection — sell it only when your own house is in order'],
      flags=['blocking']),
    T('Create social@klyara.com, into Bitwarden, 2FA on', B, 20,
      'Every platform registration runs through one inbox. Using hello@ drowns the public inbox '
      'in verification codes and password resets.',
      ['Every account into Bitwarden as it is created, not afterwards.',
       '2FA on every single one. A hijacked social account for a firm that holds clients’ '
       'financial data is not a thing you talk your way out of.'],
      'Accounts get made on personal emails during the setup rush and there is no single place '
      'the recovery codes live.',
      'Create the inbox before the first signup, not after the fifth.',
      subs=['Create the mailbox', 'Add to Bitwarden', 'Turn on 2FA']),
    T('Buy tryklyara.com', K, 10,
      'Cold outreach must never run from the main domain. If a cold-send domain gets burned, it '
      'must not be the one your client email runs on.',
      ['About £10. Do not point it anywhere yet.'],
      'Cold email goes out from klyara.com, the domain reputation drops, and client email starts '
      'landing in spam.',
      'Buy it now, park it, and only warm it when there is actually cold outreach to send.',
      flags=['cost']),
   ]),
 3: dict(one='Finish the Google Business Profile, and get the compliance admin off the list.',
   tasks=[
    T('Finish the Google Business Profile listing', C, 45,
      'A half-finished listing verifies slower and ranks worse. The copy is already written to '
      'Google’s character limits.',
      ['docs/02 §1 has the description, the categories, the services and the attributes.',
       'Add the four tiers as Products with prices: Solo £59, Start £99, Trade £199, Pro £329.',
       'Real photos beat stock heavily here — Craig, a desk, a laptop, a site visit.'],
      'The description is written fresh and runs over 750 characters, or keywords get stuffed '
      'into the business name and the listing gets suspended.',
      'Paste the written copy. Do not improve it at the keyboard.',
      subs=['Description, categories and services',
            'Products: the four tiers with prices',
            'Photos: logo, cover, and five real ones',
            'Booking link: the Cal.com URL',
            'Attributes and opening hours'],
      deps=['setup-1-2']),
    T('Seed the first four Google Q&A entries', C, 10,
      'Ten minutes, and it stops a stranger answering "how much does it cost?" on your behalf.',
      ['The four are written out in docs/26 PART 4.',
       'Ask and answer them from your own account. That is the intended use, not a trick.'],
      'The panel is left empty on launch day and someone else fills it in wrongly.',
      'Four questions, four answers, ten minutes, today.'),
    T('Chase the PII quotes', C, 10,
      'The licence application is conditional on cover. A quote nobody chased is a licence nobody '
      'got.',
      ['One call beats three emails here.'],
      'It waits a week because it feels like admin rather than a blocker.',
      'Chase today if nothing came back from Tuesday.',
      deps=['setup-1-3']),
   ]),
 4: dict(one='Analytics and pixels, so you are collecting from day one.',
   tasks=[
    T('Install GA4 on klyara.com and set two conversions', K, 30,
      'The audience and the baseline you do not collect this month do not exist next month.',
      ['Two conversions only: book_call and download_guide. Everything else is diagnostic.',
       'Check it fires on a real page load before you call it done.'],
      'The tag is installed but no conversion is configured, so month one has traffic data and no '
      'outcome data.',
      'Set the two conversions in the same sitting as the tag.',
      subs=['Install the GA4 tag site-wide', 'Configure book_call', 'Configure download_guide',
            'Verify in DebugView']),
    T('Verify Search Console and submit the sitemap', K, 20,
      'Indexing is the slowest thing on the site and it starts when Search Console says it does.',
      ['Verify the domain property, not the URL prefix — it covers every subdomain and protocol.',
       'Submit sitemap.xml and check every calculator page is in it.'],
      'A URL-prefix property is verified instead, and half the site’s data is invisible.',
      'Domain property, DNS TXT verification. Ten minutes.'),
    T('Install the Meta Pixel and the LinkedIn Insight Tag', K, 20,
      'Yes, with zero ad budget. The retargeting audience you do not collect this month does not '
      'exist next month, and it cannot be backfilled.',
      ['Both are a single snippet each in the site head.',
       'Confirm each fires with the platform’s own browser extension.'],
      'They are deferred until "when we start advertising", which throws away three months of '
      'audience.',
      'Install them today. They cost nothing to run.'),
   ]),
 5: dict(one='Publish the schema, and validate every block.',
   tasks=[
    T('Paste the AccountingService block into the site-wide head', K, 30,
      'It is the block that tells Google what kind of business this is and where it operates.',
      ['docs/08 §1 has it written. Fill in the bracketed address and founding date.',
       'Also paste WebSite on the homepage (docs/08 §2).'],
      'The bracketed placeholders ship unfilled and the whole block is silently invalid.',
      'Search the page source for "[" after pasting. There should be none.',
      subs=['AccountingService site-wide', 'WebSite on the homepage',
            'Fill in address and founding date']),
    T('Validate every schema block at the Rich Results test', K, 30,
      'Ten seconds a page, and it catches the typo that silently kills a whole block.',
      ['search.google.com/test/rich-results.',
       'FAQPage and HowTo no longer produce rich results — FAQ stopped on 7 May 2026, HowTo was '
       'retired in September 2023. Keep the markup, but put the effort into AccountingService, '
       'Organization, BreadcrumbList and Service.'],
      'Blocks are pasted and never tested, and one trailing comma takes out a page’s entire '
      'structured data.',
      'Test each page as you paste it, not all of them at the end.'),
   ]),
 6: dict(one='Rest. Genuinely.', hours='rest',
   tasks=[
    T('Nothing', B, 0,
      'You have a ninety-day run starting in a week. Starting tired is a bad trade.',
      ['If you cannot leave it alone, read docs/09 — the sales pack. Reading is not working.'],
      'The rest day gets filled, and week three is where that gets paid for.',
      'Take the day. The plan has weekends deliberately empty for the same reason.'),
   ]),
 7: dict(one='Publish the Guildford page.',
   tasks=[
    T('Publish the Guildford landing page', K, 60,
      'It is the only page in the pack with buying intent behind it, and the local pack is built '
      'on top of it.',
      ['Paste the page body into the site template and delete the inline CSS — it is only there '
       'so the file stands alone for review.',
       'Replace [CAL_LINK] with the Cal.com URL, and [STREET]/[POSTCODE] in the schema.',
       'Link it from the homepage footer and the services page. An orphan page ranks for nothing.'],
      'It goes live unlinked, and three months later nobody can work out why it never ranked.',
      'Link it from two places before you submit it to Search Console.',
      subs=['Paste the body into the template, strip the inline CSS',
            'Replace [CAL_LINK], [STREET], [POSTCODE]',
            'Upload the two images the schema points at',
            'Link from the homepage footer and the services page',
            'Submit the URL in Search Console']),
   ]),
 8: dict(one='Brevo, and the DNS that has to propagate before you send anything.',
   tasks=[
    T('Create the Brevo account and add SPF, DKIM and DMARC', K, 45,
      'DNS propagation plus a 21-day warm-up ramp. Start it now or the first real send lands in '
      'spam.',
      ['DMARC at p=none to start. Do not go straight to reject.',
       'docs/05 §4 has the exact records.',
       'Sender is "Craig at Klyara <craig@klyara.com>". Never no-reply@.'],
      'DMARC is set to p=reject on day one, and legitimate mail starts bouncing invisibly.',
      'p=none, watch the reports for a fortnight, then tighten.',
      subs=['Create the account', 'SPF record', 'DKIM record', 'DMARC at p=none',
            'Set the sender name and address'],
      flags=['wait']),
    T('Create the six lists and the seven contact attributes', K, 20,
      'Ten minutes now. Retrofitting attributes onto a mixed list in November is a bad afternoon.',
      ['Lists: Newsletter, MTD Guide, Launch Kit, Solo Waitlist, Clients, Partners.',
       'docs/05 §2 has the attribute names — use them verbatim so the sequences work.'],
      'Everyone lands in one list, and by month three there is no way to send to guide downloaders '
      'without also mailing clients.',
      'Six lists before the first subscriber, not after the hundredth.'),
   ]),
 9: dict(one='Load the email sequences while you have quiet.',
   tasks=[
    T('Build the three email sequences', K, 90,
      'They are already written. Loading them now means every lead magnet works from launch day '
      'instead of collecting addresses nobody follows up.',
      ['Welcome, three emails (docs/05 §5). MTD guide, five emails (§6). Launch Kit, four (§7).',
       'Paste email/template.html in as a custom template and email/signature.html into Gmail.'],
      'The magnets go live before the sequences, so the first fifty subscribers get nothing.',
      'Sequences first, magnet second. Always that order.',
      subs=['Three-email welcome sequence', 'Five-email MTD guide sequence',
            'Four-email Launch Kit sequence', 'Custom template loaded',
            'Gmail signature loaded']),
    T('Start the domain warm-up', K, 20,
      'A cold domain that suddenly sends two thousand emails goes to spam and takes months to '
      'recover.',
      ['Days 1–3 is twenty sends: yourself, both founders, friends, the partner accountant.',
       'The ramp in docs/05 §4 is not optional.',
       'Open and reply to the warm-up sends. Engagement is what the ramp is actually building.'],
      'The ramp is skipped because twenty emails feels absurd, and newsletter #1 lands in spam '
      'for the whole list.',
      'Twenty sends today, and follow the ramp. It is three weeks and it cannot be compressed.',
      flags=['wait']),
   ]),
 10: dict(one='Set up the profiles that do not wait on anything.',
   tasks=[
    T('Decide the handle, then use it everywhere', B, 10,
      'Consistency beats perfection. @klyarahq everywhere is worth more than the perfect handle '
      'on three platforms and a mess on the rest.',
      ['Order of preference: klyara → klyarahq → klyara_uk → getklyara → klyaraback.',
       'Write it down. Use it even where a better one is free.'],
      'A better handle is free on platform four, it gets taken, and now there are two handles in '
      'circulation forever.',
      'First available in the list wins, and that is the end of the discussion.',
      flags=['both']),
    T('LinkedIn Company Page', C, 30,
      'The company page is the credibility check. It is not where the reach is.',
      ['Copy in docs/02 §2. Logo and cover are in the asset set.',
       'Set both founders as admins from day one — pages are owned by personal profiles.'],
      'One admin only, and the page becomes unrecoverable if that person is unavailable.',
      'Two admins, today, before anything is posted.'),
    T('Rebuild Craig’s personal LinkedIn profile', C, 60,
      'This profile does more work than the company page. LinkedIn gives personal posts several '
      'times the reach.',
      ['Headline, About, banner, Featured section, custom URL, creator mode on.',
       'Copy in docs/02 §3.',
       'Get a real headshot: on site, in a van, in hi-vis. Not a suit, not a logo, not AI.'],
      'It is treated as a CV rather than a shopfront, so the headline says a job title instead of '
      'who Klyara helps.',
      'Headline names the customer and the problem, not the role.',
      subs=['Headline', 'About section', 'Banner image', 'Featured section',
            'Custom URL', 'Creator mode on', 'Real headshot booked or taken']),
   ]),
 11: dict(one='The rest of the estate.',
   tasks=[
    T('Facebook Page, Instagram and Threads', B, 45,
      'Instagram converted to a Professional account auto-creates Threads, which is a free extra '
      'channel for one click.',
      ['Both founders as admins on the Facebook Page.',
       'Convert Instagram to Professional before posting anything.'],
      'The page is created on one personal profile with no second admin.',
      'Add the second admin in the same sitting.',
      subs=['Facebook Page + both founders as admins', 'Instagram Professional account',
            'Threads (auto-created)']),
    T('X, YouTube with five playlists, and TikTok Business', C, 45,
      'The playlists matter more than they look — YouTube treats a playlist as a topic signal.',
      ['Five playlists, named in docs/02.',
       'TikTok must be a Business account for the analytics and the commercial audio library.'],
      'Videos get uploaded with no playlist, and the channel reads as unstructured.',
      'Create the playlists before the first upload.',
      subs=['X', 'YouTube + five playlists', 'TikTok Business account']),
    T('Reddit ×2 — then stop and read only for three weeks', C, 20,
      'Reddit punishes new accounts that post. Three weeks of reading is the entry fee and it is '
      'not negotiable.',
      ['Craig’s human account and a brand account. docs/01 §Reddit Protocol.',
       'Read only. No comments, no posts, for three weeks.'],
      'A link gets posted in week one, the account is shadowbanned, and the channel is dead for '
      'the quarter.',
      'Read only. Start commenting in week four, first text post around day 40 if karma allows.'),
    T('Bluesky, Pinterest, Snapchat and Nextdoor', B, 30,
      'Bluesky’s DNS domain verification is free, takes ten minutes and is a real trust signal.',
      ['Verify the Bluesky domain via a DNS TXT record.',
       'Snapchat: claim the handle and leave it. It is a defensive registration, not a channel.'],
      'Time gets spent trying to make Snapchat and Pinterest work as channels.',
      'Claim, fill the profile, move on. These are name protection.',
      subs=['Bluesky + DNS domain verification', 'Pinterest', 'Snapchat (claim and leave)',
            'Nextdoor']),
   ]),
 12: dict(one='Directories. Boring, one-off, and they compound.',
   tasks=[
    T('Lock the NAP string and never vary it by a character', B, 10,
      'Name, address and phone have to match across every citation or the whole set works against '
      'you instead of for you.',
      ['docs/02 has the canonical strings. Copy them, do not retype them.',
       '"020 8058 1496" — one format, everywhere.'],
      'One directory gets "Klyara Ltd" and another gets "Klyara — Construction Back Office", and '
      'Google treats them as different businesses.',
      'Paste from one document every time. Never type it fresh.'),
    T('Tier 1 directories', B, 40,
      'Free placement, one-off effort, and they keep working.',
      ['Trustpilot, Yell, FreeIndex, Bing Places, Apple Business Connect.',
       'directory.getsurrey.co.uk is twenty minutes and in the August 2026 search it ranked third '
       'for "construction bookkeeper Surrey", above most of the actual firms.'],
      'The unglamorous local directory gets skipped, and it was the one ranking above the '
      'competition.',
      'Do getsurrey first, while you still have the enthusiasm.',
      subs=['Trustpilot', 'Yell', 'FreeIndex', 'Bing Places', 'Apple Business Connect',
            'directory.getsurrey.co.uk']),
    T('Tier 2 directories and the Surrey citations', B, 30,
      'Diminishing returns, but they are permanent and they cost nothing but an evening.',
      ['Cylex, Scoot, Thomson Local, Hotfrog, 192.com.',
       'Surrey Chambers enquiry, Business Surrey, thebestof Guildford (docs/11 §6).'],
      'They get done with slightly different details each time because the NAP document is not '
      'open.',
      'Keep the NAP document open on the second screen for the whole sitting.',
      subs=['Cylex', 'Scoot', 'Thomson Local', 'Hotfrog', '192.com',
            'Surrey Chambers enquiry', 'Business Surrey', 'thebestof Guildford']),
   ]),
 13: dict(one='Load the week and then stop.',
   tasks=[
    T('Register on the six forums — profiles only, no signature', C, 25,
      'A signature on a brand new account with no post history reads as an advert and gets the '
      'account flagged.',
      ['Screwfix Community, UK Business Forums, BookaBuilderUK, ContractorsTalk, '
       'UKPlumbersForums, ElectriciansForums.',
       'Add the signature after eight to ten genuine answers, around week three.'],
      'Signatures go on at registration and the first three posts get deleted as spam.',
      'Profiles only today. The signature is a week-three task.'),
    T('Request to join 12–15 Facebook groups', C, 20,
      'Approval can take days, so the request has to go in before you need the groups.',
      ['docs/01 has the search strings and the vetting rule.',
       'Ask now — the approvals land during launch week.'],
      'Groups are joined in week two and the answers cannot start until week three.',
      'Request today. It is the last quiet day.',
      flags=['wait']),
    T('Read docs/09, docs/21 and docs/22 — then do three small things', B, 45,
      'Tomorrow the phone might ring. And three twenty-minute jobs here are very hard to add later.',
      ['Put "founding client rate, held for twelve months" on the pricing page.',
       'Put the £285 bought-separately comparison on the pricing page and in the proposal '
       'template — Trade is £199 against £285 bought separately, £86 a month less.',
       'Diarise the price review for 1 September 2027.'],
      'The founding-rate wording is left off, and every client who signs in the next twelve months '
      'has an implied permanent price.',
      'Twenty minutes today. The modelling puts the 2027 increase at £14,160 a year at twenty '
      'clients, and this wording is what makes it a scheduled event rather than a confrontation.',
      subs=['Read docs/09 — the sales pack',
            'Read docs/21 and docs/22',
            '"Founding client rate, held for twelve months" onto the pricing page',
            '£285 bought-separately comparison onto pricing and the proposal template',
            'Diarise the price review for 1 September 2027'],
      flags=['both']),
    T('Attach the schedule of services to the engagement letter template', K, 15,
      'It has to go out with client 1, not client 12. Retrofitting scope onto an existing client '
      'is the hardest conversation in this business.',
      ['assets/sales/Klyara-Schedule-of-Services.pdf.'],
      'The first three clients are engaged without a scope schedule and every one of them has a '
      'different idea of what is included.',
      'Attach it to the template today, so it cannot be forgotten later.'),
    T('Print the trade counter cards', K, 20,
      'Fifty sheets is two hundred cards and costs about £15. They go out on merchant counters in '
      'week 2.',
      ['assets/print/Klyara-Trade-Counter-Card-A4-4up.pdf — A4 at 100%, no scaling, trim to the '
       'crop marks.'],
      'It prints scaled-to-fit and the crop marks are wrong on all fifty sheets.',
      'Print one sheet, check it against a ruler, then print the other forty-nine.',
      flags=['cost']),
    T('Put the outbound blocks in the diary as recurring appointments', B, 15,
      'Roughly four hours a week, and it is the single highest-yield block in the whole ninety '
      'days. It is also the first thing to get skipped.',
      ['docs/23 §PART 7: two early-morning call blocks, two email blocks, one partner coffee, '
       'twenty minutes of group answering four days a week.',
       'Recurring appointments, not a to-do list. Appointments survive.'],
      'It stays a good intention, and the content channel that pays off in month four is the only '
      'thing running.',
      'Diarise it now, while it is quiet. Content works in month four; outbound produces clients '
      'in month one.',
      flags=['both']),
    T('Schedule tomorrow’s launch posts by hand', C, 20,
      'You are not buying a scheduler until month two. Posting by hand for a month teaches you '
      'what a scheduler hides.',
      ['Which platform mangles line breaks, where hashtags go, what time the audience is awake.',
       'Metricool comes on day 30, once you know which channels earn their slot.'],
      'A scheduler is bought in week one and three channels get automated before they are proved.',
      'By hand for thirty days. Then buy.'),
   ]),
}


# ══════════════════════════════════════════════════════════════════════════
# THE NINETY DAYS. Day 1 = Mon 14 Sep 2026. Day 90 = Sat 12 Dec 2026.
# Rhythm tasks are generated per weekday; `extra` below is what makes the day
# itself. Every hard date sits on the day it actually falls on.
# ══════════════════════════════════════════════════════════════════════════
def CIS_RETURN(period, moved=None):
    tips = ['Nil returns still have to be filed. A month with no payments to subcontractors is '
            'still a return, and forgetting it is the single most common £100 penalty.',
            'Penalties run £100 at one day late, £200 at two months, then £300 or 5% of the '
            'deductions at six months and again at twelve.',
            'Deduction rates are 0% gross, 20% verified, 30% unverified. If a subbie cannot '
            'evidence a verification, treat them as unverified.']
    if moved:
        tips.insert(0, moved)
    return T('CIS monthly return filed — %s' % period, C, 45,
             'The return is due on the 19th of the month. When the 19th is a weekend or a bank '
             'holiday the deadline moves BACK to the last working day before it, never forward.',
             tips,
             'Everybody works to "the 19th" as a habit and files on the Monday after a weekend '
             '19th, which is one day late and a £100 penalty each.',
             'Diarise the moved date, not the 19th. Say the real date out loud in the post and '
             'to every client.',
             subs=['Reconcile the month’s subcontractor payments',
                   'Check every subcontractor’s verification status',
                   'Split materials from labour on every payment',
                   'File the return (nil return if there were no payments)',
                   'Issue deduction statements to every subcontractor'],
             flags=['deadline'])


def CIS_PAYMENT(period, moved=None):
    tips = ['Electronic payment is due by the 22nd. Post is the 19th, and nobody should be '
            'paying CIS by post.',
            'Use the correct 13-character accounts office reference or the payment sits '
            'unallocated and the reminder letters start.']
    if moved:
        tips.insert(0, moved)
    return T('CIS and PAYE electronic payment — %s' % period, C, 20,
             'Filing the return and paying the deductions are two separate deadlines. Filing on '
             'time and paying late still costs money.',
             tips,
             'The return is filed and everyone relaxes, and the payment goes out on the 25th.',
             'Set the payment up on the same day you file the return, dated for the 22nd.',
             flags=['deadline'])


DAYS = {
 1: dict(one='Launch. Post the anchor, then answer every reply for the rest of the day.', minutes=180,
   extra=[
    T('Publish the Day 1 anchor post and pin it', C, 30,
      'The single most important post of the month. Reach on day one is decided by how fast the '
      'first replies come.',
      ['Full copy in docs/03 Day 1. Craig’s personal LinkedIn first, then everything else.',
       'Pin it to the profile.',
       'Block the day out. Replying within the hour for a whole day is the job today.'],
      'It goes out and then nobody is available to reply for six hours, and the algorithm reads '
      'that as a dead post.',
      'Clear the diary. Day one is a posting day and a replying day, not a working day.',
      flags=['blocking']),
    T('First Google Business Profile post', C, 10,
      'The profile has been sitting there through verification. Day one is when it starts working.',
      ['docs/13 W1. Button: Learn more.'],
      'The profile is still unverified and the post cannot go out.',
      'If verification has not landed, chase it today — it is now over a fortnight.',
      deps=['setup-1-2']),
    T('Send Newsletter #0 to the warm-up list — "we’re live"', K, 20,
      'Twenty people, and it keeps the domain warm-up ramp going on the day the volume starts to '
      'matter.',
      ['Keep the ramp going. Do not jump the volume because it is launch day.'],
      'Launch excitement blows the warm-up ramp and the domain reputation drops in week one.',
      'Stick to the ramp in docs/05 §4 regardless of what day it is.'),
    T('Chase the Google Business Profile verification if it has not landed', C, 10,
      'Verification is 5 to 14 days from 1 September, so it is due about now. Nothing local works '
      'until it is done.',
      ['This is the single most common launch failure and it is the cause about nine times in ten '
       'when month-1 local numbers are flat.'],
      'It is assumed to be fine because the listing looks complete in the dashboard.',
      'Check the verification status explicitly, not the listing completeness.',
      flags=['wait']),
   ]),
 2: dict(one='Short video out, and start the accountant list.',
   extra=[
    T('Build the accountant target list — 20 firms', C, 45,
      'Accountant partnerships are the fastest route to clients 1–5. Twenty emails is a small '
      'sample and it is still the best channel in the pack.',
      ['Search accountants in Guildford, Woking, Godalming and Farnham. Take the first two pages '
       'of each.',
       'Prioritise two-to-six partner firms — big enough to have construction clients, small '
       'enough that the partner reads their own email.',
       'docs/11 §8 has the approach and the email.'],
      'The list is built from the biggest firms, who have an in-house bookkeeping team and no '
      'reason to refer anything out.',
      'Two to six partners. Skip the sole practitioners and skip the top twenty.',
      subs=['Guildford', 'Woking', 'Godalming', 'Farnham',
            'Filter to two-to-six partner firms', 'Find a named partner for each']),
   ]),
 3: dict(one='Carousel, and your first community contribution.',
   extra=[]),
 4: dict(one='Record the first long video. It is the asset everything else cuts from.', minutes=150,
   extra=[
    T('Record "Making Tax Digital for Builders: Are You In?"', C, 90,
      'Seven minutes, and it is the spine of the month. The shorts, the carousel and the '
      'newsletter all cut from it.',
      ['Full script in docs/04. Read it aloud once before you record.',
       'Upload with the description and timestamps. Add it to the "Making Tax Digital" playlist.',
       'LinkedIn announce post with the link in the first comment, not the post body.'],
      'It is recorded and uploaded with no description, no timestamps and no playlist, and it '
      'ranks for nothing.',
      'The description is written before you press record. It takes ten minutes and it is most of '
      'the SEO.',
      subs=['Record — seven minutes', 'Upload with description and timestamps',
            'Add to the MTD playlist', 'LinkedIn announce, link in the first comment']),
    T('Newsletter #1 goes out at 07:00', K, 20,
      'First real send. Check the warm-up ramp allows the volume before you press it.',
      ['docs/05 §8 №1.',
       'If the ramp does not allow the full list yet, send to the segment it does allow.'],
      'The full list gets mailed on day four of a twenty-one day ramp and the domain takes the hit.',
      'Check the ramp, then send. The ramp is not a suggestion.'),
   ]),
 5: dict(one='⚠ CIS deadline day. The 19th is a Saturday, so the return is due today, Friday the 18th.',
   minutes=140,
   extra=[
    CIS_RETURN('month to 5 September 2026',
               moved='19 September 2026 is a Saturday. The deadline moves BACK to Friday '
                     '18 September. It does not move forward to Monday the 21st.'),
    T('Deadline post — say Friday, not Saturday', C, 30,
      'This is the format that gets saved and shared, and it is the one post that saves a stranger '
      '£100 today.',
      ['X thread: every MTD and CIS date, seven tweets (docs/03 Day 5).',
       'Facebook plus the deadline graphic assets/posts/post-deadline-calendar.png.',
       'Lead with the nil-return point. That is the one that saves people money.',
       'Say "Friday the 18th" explicitly. Anyone working to "the 19th" files a day late.'],
      'The post says "the 19th" out of habit, and it is the post that caused the penalty.',
      'Write the actual date. Never the rule.',
      flags=['deadline']),
   ]),
 6: dict(one='Light. One human post.'),
 7: dict(one='Week-ahead post. Next up is the electronic payment on Tuesday the 22nd.',
   extra=[
    T('Week-ahead post — flag Tue 22 Sep', C, 15,
      'The CIS return went in on Friday. The payment is a separate deadline three days from now '
      'and it is the one people forget.',
      ['Filing and paying are two deadlines. Say so.',
       'Do not re-flag the 18th. It has gone.'],
      'The week-ahead post recycles last week’s deadline and flags a date that has already passed.',
      'Read the fixed dates for the coming seven days before writing it.'),
   ]),
 8: dict(one='Week 2 anchor: CIS in real numbers.',
   extra=[
    T('Send the first ten accountant partnership emails', C, 45,
      'Ten today, ten on Thursday. The first ten will teach you something about the second ten, '
      'and blasting twenty at once throws that away.',
      ['Attach assets/sales/Klyara-For-Accountants-Partnership.pdf.',
       'Named partner, not info@. docs/11 §8 has the email.',
       'Log every send. You are following these up on day 18.'],
      'Twenty go out at once, the subject line turns out to be wrong, and the whole sample is '
      'burned.',
      'Ten, learn, adjust, ten more.',
      subs=['Emails 1–10 sent', 'Each one logged with the date and the named partner'],
      deps=['d2-3']),
   ]),
 9: dict(one='⚠ CIS and PAYE electronic payment is due today.',
   extra=[
    CIS_PAYMENT('month to 5 September 2026'),
    T('Order 250 A5 merchant cards — with a QR code added first', K, 30,
      'The QR with a UTM on it is the only way you will ever know whether £40 of print worked.',
      ['QR points at the Guildford page with '
       '?utm_source=merchant&utm_medium=qr&utm_campaign=slyfield.',
       'assets/print/merchant-card-A5-300dpi.png. About £30–45 for 250.',
       'Without the UTM you will either stop doing the thing that is working or keep doing the '
       'thing that is not.'],
      'The cards are ordered without the QR because it is one more step, and the channel becomes '
      'unmeasurable forever.',
      'Add the QR before you upload the artwork. Ten minutes.',
      flags=['cost']),
    T('Plan the Slyfield merchant route for Thursday', C, 20,
      'Four counters in one industrial estate. The route is the difference between a morning and '
      'a whole day.',
      ['Selco (Slyfield Industrial Estate), Travis Perkins, Jewson, Howdens.',
       'Go before 08:00 or after 15:00. Mid-morning is when the counter is busiest and the '
       'manager has no time.'],
      'It is done ad hoc, one branch at a time over three weeks, and the momentum never builds.',
      'One route, one morning, four counters.'),
   ]),
 10: dict(one='CIS carousel and the community slot.',
   extra=[]),
 11: dict(one='Record the reverse charge video, send the second ten emails.', minutes=180,
   extra=[
    T('Record "The VAT Domestic Reverse Charge, Explained Once and Properly"', C, 90,
      'Nine minutes. The reverse charge is the thing most often got wrong on a construction sales '
      'invoice, and almost nobody explains it properly.',
      ['docs/04 has the script. The six tests and the end-user rule are the whole video.',
       'It is wrong for zero-rated new build — that was a defect found in the pack’s own tool and '
       'it is worth saying out loud in the video.'],
      'It gets simplified down to "20% becomes reverse charge", which is wrong often enough to '
      'cause real damage.',
      'Cover the end-user declaration. That is the part that decides most real invoices.'),
    T('Send accountant emails 11–20', C, 30,
      'The second ten, adjusted for whatever the first ten taught you.',
      ['If nothing came back from the first ten, change the subject line before sending these.'],
      'The same email goes out again unchanged, and now twenty firms have ignored the same email.',
      'Change one variable. Subject line first.',
      deps=['d8-1']),
    T('Chase the GBP verification — it is now over two weeks', C, 10,
      'Five to fourteen days from 1 September. If it has not landed it has gone wrong and it needs '
      'escalating, not waiting on.',
      ['Google’s support chat is the fastest route once you are past fourteen days.'],
      'It gets waited on for another fortnight, and the whole local channel is dark for a month.',
      'Escalate at day fourteen, not day thirty.',
      flags=['wait']),
   ]),
 12: dict(one='Practical post, production hour, and the week-1 numbers.',
   extra=[]),
 13: dict(one='Light, and the question post.',
   extra=[
    T('Post "what’s the worst bit of admin in your week?"', C, 20,
      'A genuine question with genuine replies. This one usually gets the most comments of the '
      'month, and every reply is a piece of market research.',
      ['Reply to every single answer. The replies are the post.',
       'Write down the answers. They are next month’s content themes.'],
      'It gets posted and then not monitored, so twenty comments sit unanswered.',
      'Post it in the morning and check it four times during the day.'),
   ]),
 14: dict(one='Week ahead. Quarter-end countdown week starts tomorrow.',
   extra=[
    T('Week-ahead post — flag Mon 5 Oct', C, 15,
      'The MTD quarter (6 July – 5 October) ends eleven days from now, and next week is the '
      'seven-job checklist that gets people ready for it.',
      ['Do not re-flag the 22nd. It has gone.',
       'Set up the checklist week: one job a day, every day, starting Monday.'],
      'It flags a date that has already passed, which is the fastest way to look like nobody is '
      'reading their own calendar.',
      'Check the fixed dates in this panel before writing.'),
   ]),
 15: dict(one='Quarter-end countdown starts. One checklist job a day for seven days, into 5 October.',
   minutes=120,
   extra=[
    T('Anchor: seven days to quarter end', C, 30,
      'The MTD quarter ends Monday 5 October. This is the conversion week — it produces more '
      'replies than the other three combined.',
      ['assets/posts/post-quarter-end.png.',
       'From today, one checklist job a day for seven days. Each is a post and each is genuinely '
       'useful on its own.',
       'docs/03 Day 22 has the copy — it is written for this week.'],
      'The countdown starts after the quarter has already ended, which is the mistake the source '
      'plan made. Seven days before 5 October is Monday 28 September.',
      'Count backwards from the deadline, not forwards from the week you happen to be in.',
      subs=['Anchor post, all channels', 'GBP post W3',
            'Checklist job 1 published']),
   ]),
 16: dict(one='Checklist 2 — receipts. Plus the Slyfield merchant round.',
   extra=[
    T('The Slyfield merchant round', C, 120,
      'Cards on four counters, and one conversation with each counter manager that is worth more '
      'than the cards.',
      ['Selco, Travis Perkins, Jewson, Howdens.',
       'Ask each counter manager which local firms are busy. They see the account volumes and '
       'they will tell you.',
       'Write down every firm name they mention. That is your prospect list.'],
      'The cards get left on the counter and nobody has the conversation, which was the whole '
      'point of going.',
      'Ask the question before you hand over the cards, not as you leave.',
      subs=['Selco — Slyfield Industrial Estate', 'Travis Perkins', 'Jewson', 'Howdens',
            'Write down every firm name mentioned']),
   ]),
 17: dict(one='Checklist 3 — mixed-use costs. Plus the big carousel.',
   extra=[
    T('Publish the quarter-end carousel — 8 slides', C, 30,
      'The strongest slide set in the pack, and it lands in the week people are actually thinking '
      'about it.',
      ['assets/carousel/quarterend-8slides/. LinkedIn as a PDF, Instagram as images.'],
      'It goes out the week after the quarter ends, when nobody needs it.',
      'This week or not at all.'),
   ]),
 18: dict(one='Checklist 4 — reconcile. Record the quarter-end video, and follow up the accountants.',
   minutes=180,
   extra=[
    T('Record "Quarter-End in Under an Hour"', C, 90,
      'The most practical video in the set, published in the week it is needed.',
      ['docs/04 has the script.',
       'Publish the checklist as its own page too — it earns links every quarter, forever.'],
      'It is recorded but the page version is never built, so it only works once.',
      'Page and video in the same sitting.'),
    T('Follow up every accountant who has not replied. Once.', C, 30,
      'One line, once. A second chase reads as desperation and a first chase doubles the reply '
      'rate.',
      ['"Just checking this reached you — happy to leave it if the timing’s wrong."',
       'Once. Not twice.'],
      'Either nobody is chased, or everybody is chased three times.',
      'One chase, logged, then leave it until the second round on day 73.',
      deps=['d8-1', 'd11-2']),
    T('Newsletter #2', K, 20,
      'Fortnightly. docs/05 §8 №2.',
      ['Check the open rate on #1 before you send #2. Under 35% and the list needs looking at.'],
      'The fortnightly rhythm slips to monthly and the list goes cold.',
      'Diarise every newsletter date now, for the whole ninety days.'),
   ]),
 19: dict(one='Checklist 5 — the CIS reconciliation. The highest-value post of the month for subbies.',
   extra=[
    T('Publish the CIS reconciliation checklist post', C, 30,
      'The single highest-value post in the whole thirty days for subcontractors, and it lands '
      'the week before quarter end.',
      ['docs/03 Day 26 has the copy.',
       'The point is that most subbies never reconcile deduction statements against what the '
       'contractor actually filed.'],
      'It gets written as an explainer rather than a checklist, and nobody does anything with it.',
      'Numbered steps. Something to actually do tonight.'),
   ]),
 20: dict(one='Checklist 6 — the two-minute reverse charge check.'),
 21: dict(one='Checklist 7 — the ask. Quarter end is tomorrow.',
   minutes=90,
   extra=[
    T('The conversion post — use the HOLD version unless supervision is confirmed', C, 45,
      'This is the post the whole month has been building to. It is also the post that is illegal '
      'to run in its live form before AML supervision lands.',
      ['docs/03 Day 28 has both versions.',
       'HOLD version: waitlist and founding rate. Live version: "book a call to engage".',
       'Reply to every single response personally, today.'],
      'The live version goes out before supervision is confirmed, which is soliciting bookkeeping '
      'work you are not permitted to carry on.',
      'Check the compliance tab of this panel before posting. If AML says anything other than '
      'Done, use the HOLD version.',
      flags=['blocking']),
    T('Week-ahead post — quarter end is tomorrow', C, 15,
      'Monday 5 October is the end of the MTD quarter that started 6 July.',
      ['Flag it as tomorrow, not as "next week".'],
      'It says "next week" because the copy was written a fortnight ago.',
      'Re-read the date before posting.'),
   ]),
 22: dict(one='⚠ Quarter end. The MTD quarter 6 July – 5 October closes today.',
   extra=[
    T('Quarter-end day post', C, 30,
      'The MTD quarter (6 July – 5 October) ends today. Everything the last seven days built '
      'points at this date.',
      ['The quarterly update itself is due Saturday 7 November — that is a separate deadline, '
       'thirty-three days away. Say both dates.',
       'docs/03 Day 29 has the quarter-closed copy.'],
      'Quarter end and the filing deadline get treated as the same date, and people either panic '
      'today or relax until the 7th.',
      'Two dates, said separately, every time: the quarter ENDS 5 October, the update is DUE '
      '7 November.',
      flags=['deadline']),
   ]),
 23: dict(one='Video, and the first of the post-quarter-end evergreen week.'),
 24: dict(one='Carousel and community. Publish the CIS accountant page.',
   extra=[
    T('Publish web/cis-accountant-surrey.html', K, 45,
      'A second intent page. Link it from the Guildford page and the services page or it ranks for '
      'nothing.',
      ['Internal links first, Search Console second.'],
      'It goes live orphaned.',
      'Two inbound internal links before you submit it.'),
   ]),
 25: dict(one='Long video, and the late payment anchor — you are not a bank.', minutes=180,
   extra=[
    T('The late payment anchor post', C, 45,
      'The quarter has closed and everybody is looking at what they are owed. This is the right '
      'week for it, not the week before quarter end.',
      ['assets/posts/post-late-payment.png and post-retentions.png.',
       'The Facebook version has comment bait — "comment RETENTION and I’ll send the tracker". '
       'Actually send it, within the hour, to everyone who comments.',
       'Statutory interest is 8% over base. The Bank of England base rate was 3.75% as at '
       '30 July 2026 and the 17 September decision has already happened — check the current rate '
       'before you quote a number publicly.'],
      'A stale base rate gets quoted publicly. The source plan still said "next BoE decision '
      '17 September" a fortnight after that decision had been made.',
      'Look the rate up on the Bank of England site the morning you post it. Never quote a rate '
      'from a document.',
      flags=['deadline']),
   ]),
 26: dict(one='Give the retention tracker away.',
   extra=[
    T('Post the free retention tracker and two calculator cards', C, 30,
      'A free tool is welcome in forums where a service link gets removed. That is the whole '
      'reason the calculators exist.',
      ['assets/tools/ has the cards.',
       'Post the tool, not the page it lives on.'],
      'It is posted with a "book a call" line attached and gets removed as promotion.',
      'No CTA. The tool is the CTA.'),
   ]),
 27: dict(one='Light. The "best builders aren’t the ones who do well" post.'),
 28: dict(one='Week ahead, and publish the Woking page.',
   extra=[
    T('Publish web/construction-bookkeeping-woking.html', K, 45,
      'Second of the five local pages.',
      ['Swap the town everywhere including the schema, the title and the meta description.',
       'Link it from the Guildford page and the services page.'],
      'A "Guildford" is left in the schema or the meta description of the Woking page.',
      'Search the file for the old town name after the swap. Every time.'),
   ]),
 29: dict(one='Month 1 review. Thirty days of numbers, honestly.',
   extra=[
    T('Month 1 review against target', K, 60,
      'Booked calls, cost per call, guide downloads, GBP calls, directions and clicks. Target is '
      'four or more Guildford-postcode calls.',
      ['If it is under four, check GBP verification is actually live before you change anything '
       'else. It is the cause about nine times in ten.',
       'Write down the three things that worked and the three that did not.'],
      'The content gets changed before the plumbing is checked, and a verification problem gets '
      'treated as a messaging problem for another month.',
      'Check verification first. Always first.',
      subs=['Booked discovery calls', 'Cost per booked call', 'Guide downloads',
            'GBP calls, directions and website clicks',
            'Is GBP verification actually live?',
            'Three things that worked, three that did not']),
   ]),
 30: dict(one='Thirty-day recap, and now buy the scheduler.',
   extra=[
    T('Post the 30-day recap', C, 30,
      'Everything in one place. It gets saved, and it is the post you link to for the next six '
      'months.',
      ['docs/03 Day 30.'],
      'It reads as a victory lap. It should read as a resource.',
      'Lead with what somebody can use, not with what you did.'),
    T('Buy Metricool — Starter tier', K, 30,
      'You have posted by hand for a month and you now know which channels earn their slot. That '
      'is the whole reason it was not bought in week one.',
      ['About £20–28/month all in. X is a paid add-on; the free tier excludes LinkedIn and X.',
       'It is the only mainstream scheduler that natively posts to Google Business Profile, which '
       'is the whole reason it wins here.',
       'Verify the pricing at signup — every tool in this category repriced in the last two years.',
       'Do not buy Hootsuite.'],
      'A scheduler is bought that cannot post to GBP, leaving the single best channel as a '
      'permanent manual chore — which is exactly the chore that stops happening in a busy month.',
      'GBP support is the only requirement that matters. Check it before paying.',
      flags=['cost']),
    T('Load weeks 5–8 of GBP posts into the scheduler', C, 30,
      'The year of GBP posts is already written. Loading a month at a time is the difference '
      'between a habit and a chore.',
      ['docs/13 has fifty-two dated posts.'],
      'One week gets loaded and the rest never do.',
      'Load four weeks every time you open it.'),
   ]),
}

DAYS.update({
 31: dict(one='Month 2 starts. Gross payment status week.',
   extra=[
    T('Publish the gross payment status page', K, 60,
      'The text is already written in the CIS Compliance Pack. Copy and reformat — do not rewrite '
      'it.',
      ['The angle is the three tests, and why most firms who would pass never apply.',
       'Business test, turnover test, compliance test. Turnover is £30,000 per director or partner.'],
      'It gets rewritten from scratch and takes a day instead of an hour, and the rewritten '
      'version is worse.',
      'Copy the pack text. Reformat only.'),
   ]),
 32: dict(one='Video, and the second merchant lap.',
   extra=[
    T('Second merchant lap — Woking, Godalming, Farnham', C, 120,
      'Restock the counters that emptied, and find out which ones did not.',
      ['A counter whose cards have not moved is a counter to stop restocking.',
       'Ask the same question again: who is busy?'],
      'Every branch gets restocked equally regardless of whether the cards moved.',
      'Count what is left before you top up. That is the measurement.'),
   ]),
 33: dict(one='Community and tools. Check the contribution count.',
   extra=[
    T('Count your genuine community contributions — target 25+', C, 15,
      'The slowest channel in the pack, and the only way to know you are behind is to count.',
      ['If you are under 25 by now, you have dropped the Wednesday slot more than twice.'],
      'Nobody counts, so nobody knows the channel is dying until it is dead.',
      'Count on the same day every month. Write the number down.'),
   ]),
 34: dict(one='Long video, and the contractor lead magnet goes live.', minutes=120,
   extra=[
    T('Publish /cis-pack.html with the contractor magnet behind a one-field form', K, 60,
      'This magnet targets the £199–£329 tier, which the other two magnets do not reach at all.',
      ['assets/lead-magnets/Klyara-Contractors-CIS-Compliance-Pack.pdf.',
       'One field. Email only. Every extra field costs conversions.',
       'Wire it to a Brevo list and a short nurture sequence before it goes live.'],
      'The magnet goes live before the sequence exists, and the first fifty downloads get nothing.',
      'Sequence first, form second, page third.',
      subs=['Build the page', 'One-field form', 'Wire to the Brevo list',
            'Nurture sequence loaded', 'Test the whole flow with a real address']),
   ]),
 35: dict(one='Practical post, production hour, numbers.'),
 36: dict(one='⚠ CIS deadline day. The return for the month to 5 October is due today, Monday the 19th.',
   minutes=105,
   extra=[
    CIS_RETURN('month to 5 October 2026',
               moved='19 October 2026 is a Monday, so the deadline is the 19th itself. No move.'),
    T('CIS deadline post, all channels', C, 25,
      'The monthly return post. It is the most reliably useful post in the calendar because it is '
      'the same deadline every month and people still miss it.',
      ['If you have clients, their returns go in today, not tomorrow.',
       'Nil returns still count.'],
      'The post goes out and the client work does not, because the post felt like the task.',
      'Client returns first, post second.',
      flags=['deadline']),
   ]),
 37: dict(one='Week ahead — the electronic payment falls on Thursday the 22nd.',
   extra=[
    T('Week-ahead post — flag Thu 22 Oct', C, 15,
      'The return went in yesterday. The payment is Thursday, and it is a separate deadline.',
      ['Do not re-flag the 19th. It has gone.'],
      'The week-ahead post flags the return deadline that passed yesterday.',
      'Read the fixed dates before writing.'),
   ]),
 38: dict(one='Pricing week, and the "which tier am I?" helper.',
   extra=[
    T('Build the "which tier am I?" helper on the pricing page', K, 180,
      'Half a day of development, and it will move more revenue than any other single change on '
      'the site.',
      ['Three questions, recommends a tier, pre-fills the booking.',
       'docs/07 §Conversion 3 has the logic.'],
      'It gets built as a five-question quiz. Every extra question loses people.',
      'Three questions. No more.',
      subs=['Three questions', 'Tier recommendation logic', 'Pre-fill the booking link',
            'Test at 390px']),
   ]),
 39: dict(one='⚠ CIS and PAYE electronic payment is due today.',
   extra=[
    CIS_PAYMENT('month to 5 October 2026'),
    T('Review engine — ask every client for a Google review', C, 20,
      'Twenty reviews needs about eighty asks, so the asking has to start immediately and be '
      'systematic. Reviews are the single missing input for the whole AI-discovery channel.',
      ['Ask at the report handover, and text the link on the spot. Not later, not by email.',
       'Target two a month, forever. Google first, Trustpilot second, nothing else.',
       'docs/26 is the review engine; docs/06 §9 is the ask.'],
      'The ask is made by email a week later, and the conversion rate collapses.',
      'On the spot, by text, with the link. Every time.'),
   ]),
 40: dict(one='Community, and the Reddit escalation.',
   extra=[
    T('First Reddit text post, if you are past 30 comments and the rules allow', C, 45,
      'Six weeks of reading and commenting is the entry fee. This is where it pays.',
      ['Long-form, useful, no link in the body.',
       'docs/01 §Reddit Protocol. Check the sub’s self-promotion rules first, every time.'],
      'A link goes in the body and the post is removed, taking the account’s standing with it.',
      'No link. If somebody asks, answer in a comment.'),
   ]),
 41: dict(one='Long video, and cut the homepage to one CTA per section.',
   extra=[
    T('Cut the homepage to one primary CTA per section', K, 90,
      'Nineteen competing calls to action is a menu, not a conversion path.',
      ['docs/07 §Conversion 2.',
       'One primary per section. Secondary links are fine; second buttons are not.'],
      'CTAs get removed from the sections nobody uses and left in the ones that matter.',
      'Count them before and after. Nineteen to seven is the job.'),
   ]),
 42: dict(one='Practical post, and per-page OG images.',
   extra=[
    T('Set a per-page og:image on every page', K, 60,
      'Every share this month has used the generic card. The images already exist.',
      ['assets/posts/*.png.',
       'Check with the LinkedIn Post Inspector and Facebook’s sharing debugger — both cache '
       'aggressively and need a manual re-scrape.'],
      'The tags are set and the platforms keep serving the cached old card, so it looks like it '
      'did not work.',
      'Re-scrape each URL in both debuggers after the change.'),
   ]),
 43: dict(one='Pricing and margin — the evergreen anchor.',
   extra=[
    T('Anchor: the three costs that never make it into a quote', C, 45,
      'Post-deadline weeks are the right place for evergreen. The urgency audience has just been '
      'served and the next hard date is a fortnight out.',
      ['docs/05 §8 №6 has the full text — reuse it as a post.',
       'The source plan put a CIS deadline post here. That deadline was the 19th, a week ago. '
       'This week has no hard date in it, which is exactly why it suits evergreen.'],
      'A deadline post goes out for a deadline that has passed, which reads as automated.',
      'Check this panel’s fixed dates before writing any post with a date in it.'),
   ]),
 44: dict(one='Week ahead.'),
 45: dict(one='First employee week, and the calculator page SEO.',
   extra=[
    T('Calculator page SEO — titles, metas and schema for all twelve', K, 120,
      'This is the long-tail engine and it is a two-hour job that pays for years.',
      ['docs/08 §6. SoftwareApplication schema on each.',
       'Twelve individual calculator pages, plus the consolidated tools.html — docs/08 §12 '
       'explains which schema goes where.'],
      'The same title template is used on all twelve and they compete with each other.',
      'One distinct primary phrase per calculator. Write them out in a list first.',
      subs=['Twelve titles', 'Twelve meta descriptions', 'SoftwareApplication schema on each',
            'Validate each in the Rich Results test']),
   ]),
 46: dict(one='Video, and pitch twenty podcasts.',
   extra=[
    T('Pitch 20 podcasts', C, 90,
      'Expect three replies and one booking. That is a normal, good result, and one episode beats '
      'a month of posting.',
      ['The 40-word template is in docs/06 §6.',
       'Trade and small-business podcasts, not accounting ones. The audience is builders.'],
      'The pitch describes Klyara instead of describing an episode.',
      'Pitch a topic with a title, not a guest.'),
   ]),
 47: dict(one='Community slot.'),
 48: dict(one='Long video, and go to one Chambers event.',
   extra=[
    T('Surrey Chambers event, or Guildford & Waverley Business Question Time', B, 180,
      'Go to one. Local business rooms are where referral relationships actually start.',
      ['docs/11 §7.',
       'Take the trade counter cards, not a brochure.'],
      'It gets deferred every month because there is always a reason not to go.',
      'Book one, pay for it, and it happens.',
      flags=['both', 'cost']),
   ]),
 49: dict(one='Practical post, numbers, and Newsletter #3.',
   extra=[
    T('Newsletter #3', K, 30,
      'Fortnightly, on the same day, forever.',
      ['Check the open rate. Above 35% is the target.'],
      'It slips a week and then a fortnight becomes a month.',
      'Same day, every fortnight, diarised.'),
   ]),
 50: dict(one='Light.'),
 51: dict(one='Week ahead — the MTD quarterly update is due Saturday, four days from now.',
   extra=[
    T('Week-ahead post — the 7 November deadline is four days away', C, 20,
      'This is the highest-urgency content window in the whole ninety days. It is four days out, '
      'not two weeks.',
      ['The source plan said "two weeks out" here, because its prose was written against a launch '
       'a week earlier. It is four days.',
       'Start the countdown now and run it every day to Saturday.'],
      'The countdown says two weeks, then five days, then suddenly the deadline is yesterday.',
      'Count the actual days from the actual date. Every time.',
      flags=['deadline']),
   ]),
 52: dict(one='MTD countdown: three days. Anchor for people who are behind.',
   extra=[
    T('Anchor: what to do if you are behind, with three days to go', C, 45,
      'The highest-urgency content window of the ninety days. Use it.',
      ['docs/05 §8 №5 has the 40-minute version for people who have not started.',
       'MTD for Income Tax is sole traders and landlords only — never limited companies. Say so, '
       'because half the panic comes from people who are not in scope.',
       'Thresholds: more than £50k from April 2026, £30k April 2027, £20k April 2028.'],
      'The post implies limited companies are in scope, which is wrong and generates the wrong '
      'enquiries.',
      'Sole traders and landlords. Every post. No exceptions.',
      flags=['deadline']),
   ]),
 53: dict(one='Newsletter #5 — "MTD update due Saturday". Two days out, which is deliberate.',
   extra=[
    T('Newsletter #5 — MTD update due Saturday', K, 30,
      'Two days before the deadline. That timing is deliberate: far enough to act, close enough '
      'to matter.',
      ['docs/05 §8 №5.',
       'One action, at the top, above everything else.'],
      'It goes out after the deadline. In the source plan it was scheduled for 12 November, five '
      'days after the deadline it was announcing.',
      'Two days before. Check the date against the deadline before you schedule the send.',
      flags=['deadline']),
    T('Short video: the MTD deadline', C, 20,
      'Two days out is when the short video does its most work.',
      ['Sixty seconds. One date, one action.'],
      'It explains MTD instead of stating the deadline.',
      'Date first, explanation second.'),
   ]),
 54: dict(one='The day before the deadline. The fastest legitimate route, for anyone who has not filed.',
   extra=[
    T('The "if it isn’t done, here’s the fastest legitimate route" post', C, 45,
      'Panic drives engagement, and this is the day people ask. It is also the day a genuinely '
      'useful answer earns the most trust.',
      ['All channels. Reply to everything.',
       'File something reasonable on time rather than something perfect late. It is a summary of '
       'totals, not a return.'],
      'The post is a warning rather than a route. A warning on the day before helps nobody.',
      'Give the steps. Somebody should be able to follow the post and file.',
      flags=['deadline']),
    T('If you have MTD clients, everything is filed before today ends', C, 60,
      'Client filings do not go on the deadline day. They go before it.',
      ['If it is not filed by tonight, today is not the day to discover that.'],
      'Client work is left to deadline day and one submission fails at 23:40.',
      'Client updates go in on the Thursday. The Friday is for the ones that broke.',
      flags=['deadline']),
   ]),
 55: dict(one='⚠ 7 November. The MTD quarterly update is due today.', minutes=90,
   extra=[
    T('MTD quarterly update — deadline day', C, 45,
      'The biggest date in the ninety-day window. The quarter ended 5 October and the update is '
      'due today.',
      ['File something reasonable on time rather than something perfect late. It is a summary of '
       'totals, not a return.',
       'If you have MTD clients, everything is already filed. Today is for the exceptions.',
       'Deadline-day post plus a GBP post.'],
      'The date drifts in people’s heads because quarter end and filing deadline are a month '
      'apart. In the source plan this entry sat on 14 November — a week after the deadline it '
      'described.',
      'Both dates, said separately, in every post from day 22 onwards.',
      flags=['deadline']),
   ]),
 56: dict(one='Practical post, numbers, and the Month 2 review.',
   extra=[
    T('Month 2 review against target', K, 60,
      'Booked calls, cost per call, list growth, GBP actions, clients onboarded. Target is six to '
      'eight calls.',
      ['Decision gate: are any accountant partnership conversations live? If not, send twenty '
       'more. Twenty emails is a small sample.',
       'Decision gate: if ads are running, is cost per booked call under £40? If not, pause them.'],
      'The review is done but no decision comes out of it.',
      'Every gate has an "if no" written next to it. Do the "if no".',
      subs=['Booked calls', 'Cost per booked call', 'List growth', 'GBP actions',
            'Clients onboarded', 'Accountant conversations live?',
            'Cost per call under £40?']),
   ]),
 57: dict(one='Post-deadline week. Evergreen lands well now.',
   extra=[
    T('Anchor: something evergreen, now the urgency audience has been served', C, 45,
      'The deadline was Saturday. This week is the wrong week for urgency and the right week for '
      'the piece that keeps working.',
      ['The source plan had "five days to the MTD deadline" on this day, two days after the '
       'deadline had passed.'],
      'A countdown post goes out for a deadline that has gone.',
      'Check the fixed dates. Always before writing anything with a date in it.'),
   ]),
 58: dict(one='Video, and the post-deadline follow-up with clients.'),
 59: dict(one='Community. Post-deadline questions are everywhere this week.',
   extra=[
    T('Community slot — the post-deadline questions', C, 45,
      'The week after a deadline is the best community opportunity of the quarter. Everybody who '
      'struggled is asking about it now.',
      ['Answer the "I filed it wrong, what now" questions. Nobody else answers those.'],
      'The slot is skipped because the deadline is over and it feels like the moment has passed. '
      'The moment is now.',
      'Double the slot this week.'),
   ]),
 60: dict(one='Long video, and the end of Month 2.'),
 61: dict(one='Practical post, production hour, numbers.'),
 62: dict(one='Light. One human post.'),
 63: dict(one='Week ahead. Next up: Thursday 19 November, the CIS return.',
   extra=[
    T('Week-ahead post — flag Thu 19 Nov', C, 15,
      'The CIS return for the month to 5 November is due Thursday. It is the 19th and the 19th is '
      'a Thursday, so there is no move.',
      ['Also flag Friday 20 November for the electronic payment — the 22nd is a Sunday, so the '
       'payment moves back to Friday the 20th.'],
      'Only the return is flagged and the payment date is missed entirely.',
      'Both dates in the same post. They are always two deadlines.'),
   ]),
 64: dict(one='Pricing and margin week — what that job actually cost you.',
   extra=[
    T('Anchor: what that job actually cost you', C, 45,
      'docs/05 §8 №6. It converts because it is arithmetic, not opinion.',
      ['Mileage is 55p from April 2026. Use the real figure.',
       'Show the calculation. The post is the working, not the conclusion.'],
      'A rounded rate gets quoted and somebody in the comments corrects it, which costs more than '
      'the post earns.',
      'Every figure checked against gov.uk the morning you post it.'),
   ]),
 65: dict(one='Video, and the monthly review asks.'),
 66: dict(one='Community. You should be at 40+ contributions.',
   extra=[
    T('Count contributions — target 40+, and links now allowed where rules permit', C, 20,
      'Forty genuine contributions is where the accounts have enough standing to link '
      'occasionally.',
      ['Occasionally. Not in every answer.',
       'Check each forum’s rules again — several change them.'],
      'Standing gets spent all at once by linking in five answers in a week.',
      'One link in five answers, at most.'),
   ]),
 67: dict(one='⚠ CIS deadline day. The return for the month to 5 November is due today, Thursday the 19th.',
   minutes=105,
   extra=[
    CIS_RETURN('month to 5 November 2026',
               moved='19 November 2026 is a Thursday, so the deadline is the 19th itself. '
                     'No move — but the payment on the 22nd does move, because that is a Sunday.'),
    T('Anchor: chase your CIS deduction statements now, not in February', C, 45,
      'Genuinely the right week for it — contractors still remember October’s jobs, and in '
      'February they will not.',
      ['The statement is the evidence for the refund. No statement, no refund.',
       'A contractor who has gone quiet in February is a contractor who has gone quiet forever.'],
      'It gets left until the self-assessment rush, when the contractor cannot remember and the '
      'bookkeeper cannot chase.',
      'Chase in the month the work happened. Every month.',
      flags=['deadline']),
   ]),
 68: dict(one='⚠ CIS and PAYE electronic payment. The 22nd is a Sunday, so it is due today, Friday the 20th.',
   extra=[
    CIS_PAYMENT('month to 5 November 2026',
                moved='22 November 2026 is a Sunday. The payment deadline moves BACK to Friday '
                      '20 November. It does not move forward to Monday the 23rd.'),
    T('Newsletter #6', K, 30,
      'Fortnightly. docs/05 §8.',
      ['Lead with the December dates. People are already thinking about the shutdown.'],
      'It leads with a look back at the year, which nobody reads in November.',
      'Lead with what is coming, not what happened.'),
   ]),
 69: dict(one='Light.'),
 70: dict(one='Week ahead. December, and the January hole content starts next week.',
   extra=[
    T('Week-ahead post — into December', C, 15,
      'The CIS return went in on the 19th and the payment on the 20th. Both have gone. Next up is '
      'the December run and the January hole.',
      ['The source plan flagged the 19 November return here, three days after it had passed.'],
      'It re-flags a deadline that has gone.',
      'Read the fixed dates for the coming seven days, not the last seven.'),
   ]),
 71: dict(one='Deduction statements week — the substance behind Thursday’s anchor.'),
 72: dict(one='Video on deduction statements.'),
 73: dict(one='Community, and the second round of accountant outreach.',
   extra=[
    T('Second round of accountant outreach — another 20 firms', C, 90,
      'Twenty emails is a small sample and this is your best channel. Either another twenty firms '
      'or a second contact to the first twenty.',
      ['If the first twenty produced nothing, change the offer, not the volume.',
       'The partner one-pager goes with every one.'],
      'The same email goes to the same twenty firms a second time, unchanged.',
      'New firms, or a genuinely different angle to the old ones. Not the same email again.',
      deps=['d18-2']),
   ]),
 74: dict(one='Practical post. No hard date this week — the CIS deadlines went on the 19th and 20th.',
   extra=[]),
 75: dict(one='Practical post, production hour, numbers.'),
 76: dict(one='Light.'),
 77: dict(one='Week ahead. The January hole content starts Monday.'),
 78: dict(one='The January hole. The best seasonal content of the year.',
   extra=[
    T('Anchor: plan for January now', C, 60,
      'This post lands harder than anything else in the quarter because it is genuinely '
      'frightening and genuinely fixable.',
      ['docs/05 §8 №7 has the full text.',
       'All channels, plus a video.',
       'Self-employed record retention is five years after the 31 January deadline — worth saying '
       'here, because it is the thing people get wrong when they are clearing out in December.'],
      'It is written as a warning with no fix attached, which produces anxiety and no enquiries.',
      'Warning, then the arithmetic, then the fix. In that order.'),
   ]),
 79: dict(one='Video on the January hole, plus capital allowances.',
   extra=[
    T('Second post: buying a van before 5 April, and why the invoice date decides the tax year', C, 25,
      'docs/05 §8 №11. It is the most-asked December question in the trade.',
      ['The invoice date, not the payment date and not the delivery date.',
       'Mileage is 55p from April 2026 — the alternative to claiming the van.'],
      'It says "before April" without saying 5 April, and somebody buys on the 6th.',
      'The date is 5 April. Say the date.'),
   ]),
 80: dict(one='Community slot.'),
 81: dict(one='Long video, and the year-end content page.',
   extra=[
    T('Record "What to do before the tax year ends", and publish it as a page', C, 120,
      'It will get search traffic every February, forever.',
      ['Page and video together. The page is the asset that keeps working.'],
      'Only the video gets made, so it works for a week instead of every year.',
      'Page in the same sitting. Always.'),
   ]),
 82: dict(one='Practical post, numbers, and Newsletter #7.',
   extra=[
    T('Newsletter #7 — the January hole', K, 30,
      'The strongest newsletter of the quarter, sent in the month it matters.',
      ['docs/05 §8 №7 is the source text for both the post and the newsletter.'],
      'It duplicates the post word for word and the list has already read it.',
      'Same idea, different opening. The list saw the post.'),
   ]),
 83: dict(one='Light.'),
 84: dict(one='Week ahead.'),
 85: dict(one='The shutdown checklist week.',
   extra=[
    T('Anchor: the nine-item shutdown checklist', C, 45,
      'Highly practical, highly shared, and it positions you for the January enquiries.',
      ['docs/05 §8 №8.',
       'Get every invoice out before Friday 18 December — the last useful invoicing day before '
       'the shutdown.',
       'The next CIS return after day 90 is for the month to 5 December, due Saturday '
       '19 December, which moves BACK to Friday 18 December.'],
      'The checklist is published in the week of the shutdown, when it is too late to act on it.',
      'Two weeks before the shutdown. This week.'),
   ]),
 86: dict(one='Video: get every invoice out before the 18th.'),
 87: dict(one='Community, and the 90-day client reviews.',
   extra=[
    T('Run the 90-day review with every client onboarded in September', C, 60,
      'Twenty minutes each, and it is where the £199 client becomes the £366 client.',
      ['docs/12 Email 5 has the structure.',
       'The retention register almost always finds money. Lead with that.',
       'This is the single most commonly skipped step in the whole onboarding runbook.'],
      'It gets diarised at onboarding and then quietly dropped, because there is no client asking '
      'for it.',
      'It is in the diary from day 5 of onboarding. Treat it as a client appointment, not an '
      'internal task.',
      subs=['Retention register reviewed', 'Add-ons discussed', 'Price review flagged',
            'Google review asked for, on the spot, by text']),
   ]),
 88: dict(one='Write the first case study, and plan months 4–6.',
   extra=[
    T('Write up the first case study properly', C, 90,
      'The only tangible proof the firm will have, and it has to be agreed with the client before '
      'it is written.',
      ['docs/06 §10 has the structure.',
       'No client name without written permission. No numbers without written permission.'],
      'It gets written first and permission asked afterwards.',
      'Permission first, in writing, then write it.'),
    T('Draft the month 4–6 content themes', K, 60,
      'Off the back of what actually got engagement, not what you assumed would.',
      ['Cut the bottom half of the channel map. You now have real data.'],
      'The plan gets extended rather than re-cut, and the channels that produced nothing get '
      'another quarter.',
      'Cut first, then plan.'),
   ]),
 89: dict(one='The ninety-day review of the business. Be honest about every line.',
   minutes=120,
   extra=[
    T('Full review against "what good looks like at day 90"', B, 90,
      'docs/14 has the list. Be honest about every line — the point of the review is the lines '
      'that are not met.',
      ['GBP verified with 12 weekly posts and 5+ real reviews · 5 local pages indexed · '
       '150–400 subscribers and 6 newsletters · 12 anchor posts · 40+ community contributions · '
       '20+ accountants contacted · 250 cards out · 3–5 clients onboarded · 8–12 calls a month · '
       '1 case study agreed.',
       'If the only things achieved are GBP verified, the Guildford page live with schema, twenty '
       'accountant emails sent and the weekly rhythm actually running — that is a successful '
       'ninety days.'],
      'The review scores the things that went well and skips the ones that did not.',
      'Score every line, including the zeros. The zeros are the plan for month four.',
      flags=['both'],
      subs=['Score every line of "what good looks like"',
            'Cut the bottom half of the channel map',
            'Decide the month 4–6 plan']),
   ]),
 90: dict(one='Day 90. Write down what you learned.',
   extra=[
    T('Final numbers, and a one-page honest note', B, 45,
      'Booked calls a month, cost per call, clients, list size, reviews, community contributions. '
      'Then a page on what worked, what did not, and what you would not do again.',
      ['Write it the same day. A week later it becomes a story instead of a record.',
       'Then book the session. docs/18 is the list of what is needed from you.'],
      'The note gets written as a summary for somebody else, so the uncomfortable parts get '
      'smoothed out.',
      'Write it for yourselves. Nobody else has to read it.',
      flags=['both'],
      subs=['Final four numbers', 'Clients onboarded', 'Reviews collected',
            'Community contributions', 'The one-page honest note',
            'Book the month 4–6 session']),
   ]),
})


# ══════════════════════════════════════════════════════════════════════════
# Fixed dates inside the window — every day number recomputed against
# Day 1 = Mon 14 Sep 2026. The source table had all six exactly seven days
# too high, which is the same one-week drift as the prose.
# ══════════════════════════════════════════════════════════════════════════
FIXED = [
 ('2026-09-18', 5,  'CIS monthly return, month to 5 Sep',
  'The 19th is a Saturday, so the deadline moves BACK to Friday the 18th.', 'cis'),
 ('2026-09-22', 9,  'CIS and PAYE electronic payment, month to 5 Sep',
  'Electronic payment is due by the 22nd. A Tuesday — no move.', 'cis'),
 ('2026-10-05', 22, 'MTD quarter ends (6 Jul – 5 Oct)',
  'The quarter ENDS today. The update itself is due 7 November — two different dates.', 'mtd'),
 ('2026-10-19', 36, 'CIS monthly return, month to 5 Oct',
  'The 19th is a Monday — no move.', 'cis'),
 ('2026-10-22', 39, 'CIS and PAYE electronic payment, month to 5 Oct',
  'A Thursday — no move.', 'cis'),
 ('2026-11-07', 55, 'MTD quarterly update due',
  'The biggest date in the window. A Saturday: file by Friday the 6th rather than trusting the '
  'weekend.', 'mtd'),
 ('2026-11-19', 67, 'CIS monthly return, month to 5 Nov',
  'The 19th is a Thursday — no move.', 'cis'),
 ('2026-11-20', 68, 'CIS and PAYE electronic payment, month to 5 Nov',
  'The 22nd is a Sunday, so the payment moves BACK to Friday the 20th.', 'cis'),
 ('2026-12-18', None, 'Last useful invoicing day before the Christmas shutdown — and the CIS '
  'return for the month to 5 Dec',
  'After day 90. The 19th is a Saturday, so that return moves BACK to Friday the 18th too.', 'after'),
]

# Every correction made to the source day-by-day plan while writing this file.
CORRECTIONS = [
 ('Hard-dates table', 'All six day numbers were seven too high (18 Sep listed as day 12, 22 Sep as '
  '16, 5 Oct as 29, 19 Oct as 43, 7 Nov as 62, 19 Nov as 74).',
  'Recomputed against Day 1 = Mon 14 Sep: days 5, 9, 22, 36, 55 and 67.'),
 ('Day 5 · Fri 18 Sep', 'Carried a generic "deadline thread" while the CIS return for the month to '
  '5 Sep was actually due this day.',
  'Made the CIS deadline day. The 19th is a Saturday so the return moves BACK to Friday the 18th.'),
 ('Day 7 · Sun 20 Sep', 'Week-ahead post flagged "the 19 September CIS deadline" — a date that had '
  'already passed, on a Saturday.',
  'Flags Tue 22 Sep, the electronic payment, which is the next deadline ahead of it.'),
 ('Day 9 · Tue 22 Sep', 'No deadline marked, although this is the CIS/PAYE electronic payment date.',
  'Marked as a hard deadline with the payment task on it.'),
 ('Day 12 · Fri 25 Sep', 'Headed "⚠ CIS deadline messaging — say Friday, not Saturday, the 19th '
  'falls on a weekend". The 19th had passed a week earlier.',
  'Returned to a normal Friday: practical post, production hour, week-1 numbers.'),
 ('Day 14 · Sun 27 Sep', 'Week-ahead flagged "Tue 22 Sep electronic CIS payment" — five days after '
  'it had passed.',
  'Flags Mon 5 Oct quarter end and the checklist week starting the next morning.'),
 ('Days 15–21 · 28 Sep – 4 Oct', 'The seven-job quarter-end checklist ran days 22–28 (5–11 Oct), '
  'entirely AFTER the quarter had ended.',
  'Moved to days 15–21 so the countdown runs into 5 October. The late-payment anchor that was '
  'here moved to day 25, which is a better week for it anyway.'),
 ('Day 22 · Mon 5 Oct', 'Said "seven days to quarter end". 5 October IS the quarter end.',
  'Made quarter-end day, with both dates stated separately: the quarter ends 5 Oct, the update is '
  'due 7 Nov.'),
 ('Day 25 · Mon 28 Sep in the old anchoring', 'Quoted "Base rate is 3.75% as at 30 July 2026 … next '
  'BoE decision 17 September" on a day that fell after 17 September.',
  'Rewritten to say the 17 September decision has already happened and the rate must be checked on '
  'the Bank of England site the morning it is quoted.'),
 ('Day 29 · Mon 12 Oct', 'Headed "⚠ Quarter end".',
  'Quarter end was day 22. This day is the month-1 review only.'),
 ('Day 36 · Mon 19 Oct', 'Headed "Light. One human post" on the day the CIS return for the month to '
  '5 Oct was due.',
  'Made the CIS deadline day.'),
 ('Day 37 · Tue 20 Oct', 'Week-ahead flagged "Mon 19 Oct CIS return" — the day before.',
  'Flags Thu 22 Oct, the electronic payment.'),
 ('Day 43 · Mon 26 Oct', 'Headed "⚠ CIS deadline day (month to 5 Oct)". That deadline was day 36.',
  'Made the pricing-and-margin evergreen anchor, which suits a week with no hard date in it.'),
 ('Day 51 · Tue 3 Nov', 'Said the 7 November deadline was "two weeks out". It was four days out.',
  'Corrected to four days, and the countdown now runs daily to the 7th.'),
 ('Day 52 · Wed 4 Nov', 'Said "two weeks to the MTD update". It was three days.',
  'Corrected to three days.'),
 ('Day 53 · Thu 5 Nov', 'Nothing scheduled. Newsletter #5, written to land "two days before the '
  'deadline", sat on day 60 (12 Nov) — five days after it.',
  'Newsletter #5 moved here, two days before the 7 November deadline, as it was designed to be.'),
 ('Day 54 · Fri 6 Nov', 'Nothing scheduled. The "day before the deadline" post sat on day 61 '
  '(13 Nov).',
  'Moved here — it is the day before the deadline.'),
 ('Day 55 · Sat 7 Nov', 'Headed "Long video + case study" on the biggest deadline day in the window.',
  'Made MTD quarterly update deadline day.'),
 ('Day 57 · Mon 9 Nov', 'Headed "⚠ Five days to the MTD deadline", two days after the deadline.',
  'Made the post-deadline evergreen week.'),
 ('Day 60 · Thu 12 Nov', 'Carried Newsletter #5, "MTD update due Saturday", five days after the '
  'update was due.',
  'Newsletter #5 moved to day 53.'),
 ('Day 61 · Fri 13 Nov', 'Headed "Day before the deadline".',
  'Moved to day 54. This is a normal Friday.'),
 ('Day 62 · Sat 14 Nov', 'Headed "⚠ 7 November. MTD quarterly update due" — on 14 November.',
  'Moved to day 55.'),
 ('Day 67 · Thu 19 Nov', 'Headed "Long video + internal linking" on the day the CIS return for the '
  'month to 5 Nov was due.',
  'Made the CIS deadline day.'),
 ('Day 68 · Fri 20 Nov', 'Not listed at all. 22 November 2026 is a Sunday, so the electronic '
  'payment moves back to Friday the 20th.',
  'Added as a hard deadline.'),
 ('Day 70 · Sun 22 Nov', 'Week-ahead flagged "Thu 19 Nov CIS" — three days after it had passed.',
  'Flags the December run instead.'),
 ('Day 74 · Thu 26 Nov', 'Headed "⚠ CIS deadline (month to 5 Nov)". That deadline was day 67.',
  'Returned to a normal Thursday.'),
 ('After day 90', 'Fri 18 Dec was listed only as the last invoicing day before the shutdown.',
  'Also noted as the CIS return for the month to 5 Dec: the 19th is a Saturday, so that return '
  'moves BACK to Friday the 18th as well.'),
]

PHASES = [
 ('setup', 'Setup', 'Tue 1 – Sun 13 September',
  'Thirteen days, about eighteen hours. Two waiting clocks start on the first morning because '
  'everything else queues behind them.'),
 ('m1', 'Month 1 — Launch', 'Days 1–30',
  'The heaviest month by design. Nine to eleven hours a week, and it ends with thirty days of '
  'real numbers to judge the next two months on.'),
 ('m2', 'Month 2 — Build', 'Days 31–60',
  'Supervision and the first clients usually land in this month, and both change the plan. '
  'Seven to eight hours a week.'),
 ('m3', 'Month 3 — Convert', 'Days 61–90',
  'The 7 November deadline, then the seasonal run into January — the strongest content of the '
  'year. Six to seven hours a week.'),
]

DEPMAP = {'setup-1-2': 's1x2', 'setup-1-3': 's1x3', 'd2-3': 'd2x1',
          'd8-1': 'd8x1', 'd11-2': 'd11x2', 'd18-2': 'd18x2'}


def phase_of(n):
    return 'm1' if n <= 30 else ('m2' if n <= 60 else 'm3')


def build():
    days = []
    week_defs = []

    # setup days
    for s in range(1, 14):
        d = setup_date(s)
        spec = SETUP.get(s, {})
        wk = 'S1' if s <= 6 else 'S2'
        tasks = []
        for i, t in enumerate(spec.get('tasks', []), 1):
            tasks.append(('s%dx%d' % (s, i), t))
        days.append((None, s, 'setup', wk, d, spec.get('one', ''), spec.get('hours'), tasks))

    # the ninety days
    for n in range(1, 91):
        d = date_of(n)
        spec = DAYS.get(n, {})
        wk = 'W%d' % ((n - 1) // 7 + 1)
        tasks = []
        for i, t in enumerate(spec.get('extra', []), 1):
            tasks.append(('d%dx%d' % (n, i), t))
        for i, t in enumerate(RHYTHM.get(d.weekday(), []), 1):
            tasks.append(('d%dr%d' % (n, i), dict(t)))
        days.append((n, None, phase_of(n), wk, d, spec.get('one', ''), spec.get('hours'), tasks))

    out_days = []
    for n, sn, phase, wk, d, one, hours, tasks in days:
        tl = []
        total = 0
        for tid, t in tasks:
            subs = [{'id': '%s-s%d' % (tid, j), 't': s}
                    for j, s in enumerate(t['subtasks'], 1)]
            deps = [DEPMAP.get(x, x) for x in t['deps']]
            total += t['minutes']
            tl.append({
                'id': tid, 'day': n, 'setupDay': sn, 'date': d.isoformat(),
                'weekday': WD[d.weekday()], 'phase': phase, 'week': wk,
                'title': t['title'], 'owner': t['owner'], 'minutes': t['minutes'],
                'deps': deps, 'flags': t['flags'],
                'why': t['why'], 'tips': t['tips'],
                'wrong': t['wrong'], 'fix': t['fix'],
                'subtasks': subs,
            })
        fixed = [f for f in FIXED if f[0] == d.isoformat()]
        out_days.append({
            'id': ('d%d' % n) if n else ('s%d' % sn),
            'n': n, 'setupDay': sn, 'phase': phase, 'week': wk,
            'date': d.isoformat(), 'weekday': WD[d.weekday()],
            'label': label(d), 'long': longlabel(d),
            'one': one, 'hours': hours or None,
            'minutes': total,
            'fixed': [{'what': f[2], 'note': f[3], 'kind': f[4]} for f in fixed],
            'tasks': tl,
        })

    # weeks
    for key in ['S1', 'S2'] + ['W%d' % i for i in range(1, 14)]:
        dd = [x for x in out_days if x['week'] == key]
        if not dd:
            continue
        a, b = dt.date.fromisoformat(dd[0]['date']), dt.date.fromisoformat(dd[-1]['date'])
        if key.startswith('S'):
            name = 'Setup week %s' % key[1]
        else:
            name = 'Week %s' % key[1:]
        week_defs.append({
            'key': key, 'name': name, 'from': a.isoformat(), 'to': b.isoformat(),
            'range': '%s – %s' % (label(a), label(b)),
            'phase': dd[0]['phase'],
            'days': [x['id'] for x in dd],
            'minutes': sum(x['minutes'] for x in dd),
            'tasks': sum(len(x['tasks']) for x in dd),
        })

    doc = {
        'schema': 'klyara.plan90/1',
        'version': 1,
        'generated': dt.date.today().isoformat(),
        'anchors': {'setupStart': SETUP_START.isoformat(), 'setupEnd': SETUP_END.isoformat(),
                    'launch': LAUNCH.isoformat(), 'day90': DAY90.isoformat()},
        'owners': {'K': 'Kieran', 'C': 'Craig', 'B': 'Both'},
        'flagLabels': {'blocking': 'Blocking', 'deadline': 'Hard deadline',
                       'cost': 'Costs money', 'both': 'Needs both founders',
                       'wait': 'Waiting period'},
        'phases': [{'key': k, 'name': nm, 'sub': sub, 'note': note}
                   for k, nm, sub, note in PHASES],
        'weeks': week_defs,
        'fixedDates': [{'date': f[0], 'day': f[1], 'label': label(dt.date.fromisoformat(f[0])),
                        'what': f[2], 'note': f[3], 'kind': f[4]} for f in FIXED],
        'corrections': [{'where': a, 'was': b, 'now': c} for a, b, c in CORRECTIONS],
        'days': out_days,
    }
    return doc


if __name__ == '__main__':
    doc = build()

    # ── self-check: nothing ships without these passing ────────────────────
    errs = []
    assert LAUNCH.weekday() == 0, 'Day 1 must be a Monday'
    assert date_of(90) == DAY90, 'Day 90 must be Sat 12 Dec 2026'
    ids = set()
    for d in doc['days']:
        dd = dt.date.fromisoformat(d['date'])
        if WD[dd.weekday()] != d['weekday']:
            errs.append('weekday mismatch on %s' % d['date'])
        if d['n'] and date_of(d['n']) != dd:
            errs.append('day number %s does not match %s' % (d['n'], d['date']))
        if dd < SETUP_START:
            errs.append('%s is before Tue 1 Sep 2026' % d['date'])
        for t in d['tasks']:
            if t['id'] in ids:
                errs.append('duplicate task id %s' % t['id'])
            ids.add(t['id'])
            for s in t['subtasks']:
                if s['id'] in ids:
                    errs.append('duplicate subtask id %s' % s['id'])
                ids.add(s['id'])
    for d in doc['days']:
        for t in d['tasks']:
            for dep in t['deps']:
                if dep not in ids:
                    errs.append('task %s depends on unknown %s' % (t['id'], dep))
    for f in doc['fixedDates']:
        fd = dt.date.fromisoformat(f['date'])
        if f['day'] is not None and date_of(f['day']) != fd:
            errs.append('fixed date %s says day %s, actually day %d'
                        % (f['date'], f['day'], (fd - LAUNCH).days + 1))
        if f['kind'] == 'cis' and fd.weekday() >= 5:
            errs.append('CIS deadline %s falls on a weekend and was not moved back' % f['date'])
    if errs:
        for e in errs:
            print('FAIL', e)
        raise SystemExit(1)

    here = os.path.dirname(os.path.abspath(__file__))
    data = os.path.join(here, 'assets', 'data')
    out = os.path.join(data, 'plan90.json')
    with io.open(out, 'w', encoding='utf-8') as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    # the file:// shim admin.js falls back to when fetch cannot be used
    shim = os.path.join(data, 'plan90.js')
    with io.open(shim, 'w', encoding='utf-8') as fh:
        fh.write('/* generated by build-plan90.py \u2014 file:// fallback for plan90.json */\n')
        fh.write('window.KLY_PLAN90=')
        json.dump(doc, fh, ensure_ascii=False, separators=(',', ':'))
        fh.write(';\n')
    nt = sum(len(d['tasks']) for d in doc['days'])
    ns = sum(len(t['subtasks']) for d in doc['days'] for t in d['tasks'])
    print('OK  days=%d  tasks=%d  subtasks=%d  ticks=%d  json=%d  js=%d'
          % (len(doc['days']), nt, ns, nt + ns, os.path.getsize(out), os.path.getsize(shim)))
