# content4.py (v3): faq, regulations-2026, resources hub.
import parts as P

def faq(L):
    def sec(anchor, title, qas):
        return f'''<div id="{anchor}" style="scroll-margin-top:100px"><h2 class="h2 mb2 mt3">{title}</h2>{P.fx(qas)}</div>'''
    return f"""
<section class="hero" style="min-height:min(52dvh,440px)">
  <div class="wrap hero-in">
    <h1 class="hero-t"><span class="cs" data-chars>Fair questions.</span><br><span class="cs acc" data-chars>Straight answers.</span></h1>
    <p class="hero-sub">Everything builders actually ask us, grouped so you can find yours fast. If it is not here, ask on a free call and we will add it.</p>
    <div class="toc mt3" data-reveal>
      <a href="#mtd">Making Tax Digital</a><a href="#cis">CIS</a><a href="#vat">VAT &amp; reverse charge</a>
      <a href="#price">Pricing &amp; engagement</a><a href="#data">Portal, data &amp; security</a><a href="#working">Working with Klyara</a>
    </div>
  </div>
  <div class="hero-rule"></div>
</section>

<section class="sec" style="padding-top:24px">
  <div class="wrap" style="max-width:880px">
    {sec("mtd","Making Tax Digital",[
      ("When does MTD apply to me?",
       "Sole traders and landlords over &pound;50,000 qualifying income have been in since April 2026. Over &pound;30,000 joins in April 2027, over &pound;20,000 in April 2028. The <a class='a-line' href='"+L('making-tax-digital.html')+"#checker'>ten-second checker</a> gives you your exact date."),
      ("Does the threshold count money before or after CIS deductions?",
       "Before. It is your gross qualifying income. Invoice &pound;55k and bank &pound;44k after the 20 percent deduction? HMRC counts the &pound;55k. This single detail puts most full-time subbies in the April 2027 wave."),
      ("Is a quarterly update a full tax return?",
       "No. It is a summary of the quarter's income and expenses sent from recognised software. No tax is calculated or due at that point. The final declaration at year end settles the actual bill, fed by a year of live data."),
      ("Can I keep using my spreadsheet?",
       "Not on its own. Records must be digital and updates must travel from HMRC-recognised software. Every Klyara plan includes recognised software in the price, so it is one bill, not two."),
      ("What are the penalties if I ignore it?",
       "A points-based system. Each late submission earns a point; at the threshold, fixed fines start, with interest on late payment. Like licence points: forgiving of a one-off, expensive as a habit."),
    ])}
    {sec("cis","CIS",[
      ("What actually is the 20 percent that disappears from my invoices?",
       "It is your own income tax and National Insurance paid in advance. The contractor deducts it from the labour part of your invoice and sends it to HMRC against your name. It is not an extra tax, and if too much is taken across the year, it comes back as a refund."),
      ("Why is my deduction 30 percent instead of 20?",
       "You are either not registered for CIS or your details do not match HMRC's records. Fixing registration is free and drops you to 20 percent immediately. If you have been on 30 for months, you are owed the difference at year end; clean records get it back faster."),
      ("What is gross payment status?",
       "Zero deductions: HMRC trusts you to pay your own tax later. You need a clean compliance history and turnover above their thresholds. Brilliant for cash flow, and our quarterly figures become your early warning for the bill building up."),
      ("I have taken on my first subbie. What just changed?",
       "Everything. You are now a contractor: register with HMRC, verify each subbie before first payment, deduct at the rate HMRC gives you, file a return by the 19th every month, and issue deduction statements. Miss a return and penalties start at &pound;100. This is exactly what Trade and Pro exist for."),
      ("Why should materials be on a separate line?",
       "CIS deductions come off labour only. Split materials clearly and that money arrives untouched. Lump it all together and you invite over-deduction, an interest-free loan to HMRC until refund time."),
    ])}
    {sec("vat","VAT and the reverse charge",[
      ("What is the domestic reverse charge in one sentence?",
       "For most VAT-registered construction work between CIS-registered businesses, the supplier charges no VAT and the customer accounts for it on their own return instead."),
      ("When do I still charge VAT normally?",
       "Homeowners and anyone not VAT-registered: always normal VAT. End users, meaning customers not selling the construction service on, such as a business refurbishing its own premises: normal VAT, but get their end-user status in writing. No written confirmation and the other conditions met? Reverse charge applies."),
      ("The reverse charge killed my VAT cash-flow float. Any fix?",
       "Often, yes. If most of your sales are now reverse charge you probably reclaim more input VAT than you owe, and switching to monthly VAT returns turns that into a monthly refund. It is one of the first things we check on a new Trade or Pro client."),
      ("What does getting it wrong actually cost?",
       "Charge VAT to a contractor and the invoice bounces, or worse, gets paid and you sit on incorrectly charged VAT that has to be unwound. Reverse-charge an end user and you have undercharged HMRC's money. Either way: delays, corrections, and awkward phone calls we would rather you never have."),
    ])}
    {sec("price","Pricing and engagement",[
      ("Why are prices shown ex VAT?",
       "Because nearly every client is VAT-registered and reclaims it, so ex VAT is your real price. Not registered? Your invoice shows the VAT line clearly. No games either way."),
      ("What is the one-off onboarding fee for?",
       "The catch-up. Backlog entered and reconciled, software set up, HMRC authorisation submitted, the app demoed on your phone with a real crumpled receipt. It is sized to your backlog and quoted exactly before you commit, so the monthly fee only ever pays for the future."),
      ("Am I locked in?",
       "No. Monthly plans roll with 30 days notice. Annual plans pay for eleven months and get twelve. Prices are reviewed once a year with written notice, never mid-term."),
      ("What happens if my records go in late?",
       "Records in by the 10th are guaranteed into that month's cycle. Later records can still be done but carry a &pound;25 surcharge, which exists to keep the deadline real. The snap-a-receipt app means almost nobody ever pays it."),
      ("Do I still need a year-end accountant?",
       "Limited companies: yes, statutory accounts and Corporation Tax are filed by an accountant, ours through the partnership or yours, working from spotless books, which is why the year-end bill drops. Solo sole traders: your final declaration is included, no extra accountant needed."),
      ("Can I switch tiers mid-year?",
       "From the next month, no penalty, no re-onboarding. First subbie, VAT registration, crossing an MTD threshold: those moments are precisely what the tiers are shaped around."),
    ])}
    {sec("data","Portal, data and security",[
      ("Why do you need my passport or driving licence?",
       "Anti-money-laundering law. Every supervised bookkeeping firm must verify each client's identity before acting, and keep the record. It is a one-off check during onboarding, done in minutes from your phone, and it is a legal requirement, not curiosity."),
      ("What is this HMRC authorisation you keep mentioning?",
       "To file for you as your agent, VAT, CIS or MTD, HMRC requires your permission on record, the modern version of the old 64-8 form, usually a digital handshake. We send the request during onboarding; you approve it; HMRC's post takes about a week. It is the only part of setup we cannot speed up."),
      ("Where does my data live and who can see it?",
       "In an encrypted portal hosted in the UK and EU, with two-factor authentication on every system we run. Access is limited to the people doing your books. The privacy policy is in actual English and takes five minutes to read."),
      ("Do you ever hold my money?",
       "Never. Wages, taxes, supplier payments: everything moves through your own bank account with your approval. We prepare; you press pay."),
      ("What happens to my data if I leave?",
       "It is yours. Books export on the day you ask, statements and records hand over cleanly, and we keep only what tax and anti-money-laundering law requires us to retain."),
    ])}
    {sec("working","Working with Klyara",[
      ("I am months behind. Is that a problem?",
       "It is the normal starting point. The onboarding fee exists precisely because nearly everyone arrives with a backlog. We rebuild it, reconcile it, and then the monthly rhythm keeps it clean. Nobody here will make you feel bad about a carrier bag of receipts; it keeps us in business."),
      ("I am mid-year with another bookkeeper. Can I still move?",
       "Yes, and mid-year moves are routine. We request handover records professionally, rebuild anything missing, and time the switch so no filing falls in the gap. Your current bookkeeper never needs to hear a cross word from you."),
      ("Who actually does my books?",
       "A construction specialist, with Craig reviewing every client's books personally. Software does the heavy lifting; a human who speaks site does the judging."),
      ("What if Craig is on holiday, or worse?",
       "There is a written continuity arrangement with a partner accountancy practice, the same arrangement professional bodies and insurers expect. Your deadlines do not depend on one person's diary or one person's luck."),
      ("My directors got a letter about verifying identity with Companies House. Is that you?",
       "Not us, but it is real: under the new Companies House rules every director must verify their identity, with deadlines rolling through 2026 by confirmation-statement date. It is free and takes minutes. Details on the <a class='a-line' href='"+L('regulations-2026.html')+"'>regulation radar</a>, and we nudge our Ltd clients before their date."),
    ])}
    <div class="center mt3" data-reveal>
      <a class="btn btn-solid btn-lg" href="{L('contact.html')}"><span>Ask the one we missed</span><span class="ar">&rarr;</span></a>
    </div>
  </div>
</section>"""

def regulations(L):
    return f"""
<section class="hero" style="min-height:min(60dvh,540px)">
  <div class="wrap hero-in">
    <p class="kicker" data-reveal>Regulation radar</p>
    <h1 class="hero-t mt1"><span class="cs" data-chars>What is hitting</span><br><span class="cs acc" data-chars>construction in 2026.</span></h1>
    <p class="hero-sub">The rule changes rolling through this year and next, in date order, in plain English, with what to actually do about each one. Bookmark it; we keep it current.</p>
  </div>
  <div class="hero-rule"></div>
</section>

<section class="sec" style="padding-top:28px">
  <div class="wrap" style="max-width:920px">
    <div class="tl" data-stagger>
      <div class="tlx now"><span class="d">April 2026, in force now</span>
        <h3 class="h3">MTD for Income Tax goes live at &pound;50,000</h3>
        <p>Sole traders and landlords over &pound;50k qualifying income must keep digital records and file quarterly updates from recognised software, with a final declaration at year end. Gross income counts, before CIS deductions. Penalty points are already accruing for late filers.</p>
        <p class="mt1"><strong>Do this:</strong> over &pound;50k and not filing quarterly? Sort it this month. <a class="a-line" href="{L('making-tax-digital.html')}">Klyara Solo</a> takes the whole job for &pound;59 a month.</p></div>
      <div class="tlx"><span class="d">Rolling through 2026</span>
        <h3 class="h3">Companies House identity verification, every director</h3>
        <p>Under the new Companies House rules, new directors have needed verified identity since November 2025, and existing directors must verify by their next confirmation statement, with deadlines rolling through autumn 2026. It is free, takes minutes, and ignoring it blocks your filings.</p>
        <p class="mt1"><strong>Do this:</strong> every director verifies now rather than at the deadline. We nudge our Ltd clients ahead of their confirmation-statement date.</p></div>
      <div class="tlx"><span class="d">April 2027</span>
        <h3 class="h3">MTD threshold drops to &pound;30,000</h3>
        <p>The big one for the trade: most full-time subbies clear &pound;30k gross without trying. Digital records and four quarterly updates a year become mandatory for the bulk of self-employed construction.</p>
        <p class="mt1"><strong>Do this:</strong> spend the 2026-27 tax year getting records digital so day one is a non-event. The <a class="a-line" href="{L('making-tax-digital.html')}#waitlist">Solo waitlist</a> locks a &pound;59 founding rate.</p></div>
      <div class="tlx"><span class="d">April 2028</span>
        <h3 class="h3">MTD threshold drops again, to &pound;20,000</h3>
        <p>By this point it is essentially every self-employed tradesperson bar part-timers. The direction of travel is one way; the only choice left is whether you join calmly or in a panic.</p>
        <p class="mt1"><strong>Do this:</strong> nothing urgent if you are only in this wave, but snapping receipts into an app from now costs ten seconds a day and removes the cliff entirely.</p></div>
    </div>

    <hr class="hr">

    <h2 class="h1 mb2" data-reveal>The standing rules<br><span class="underline-mark">that never sleep.</span></h2>
    <p class="lede mb3" data-reveal>Not new, still catching firms out every single month. The permanent fixtures on the compliance calendar.</p>
    <div class="grid g2" data-stagger>
      <div class="card">{P.icon('shield-check')}<h3 class="h3 mt1">CIS returns, the 19th, monthly</h3><p class="mute mt1">Contractors file every month, even a nil return. Subbies verified before first payment, statements issued after. Penalties start at &pound;100 per late return and climb.</p></div>
      <div class="card">{P.icon('chart-line-up')}<h3 class="h3 mt1">VAT domestic reverse charge</h3><p class="mute mt1">In force since March 2021 and still wrecking invoices. Most B2B construction work between VAT and CIS registered firms: no VAT on the invoice, customer accounts for it. <a class="a-line" href="{L('blog/vat-domestic-reverse-charge-plain-english.html')}">The plain-English guide</a>.</p></div>
      <div class="card">{P.icon('users-three')}<h3 class="h3 mt1">Payroll RTI, on or before payday</h3><p class="mute mt1">Every pay run reports to HMRC in real time, plus pension auto-enrolment duties for the PAYE crew. Weekly-paid crews mean fifty-two deadlines a year, which is why ours run on rails.</p></div>
      <div class="card">{P.icon('clock-countdown')}<h3 class="h3 mt1">MTD penalty points</h3><p class="mute mt1">The points-based regime behind every MTD deadline: each late submission is a point, points become fixed fines, interest rides on late payment. Zero points is a habit, not luck.</p></div>
    </div>

    <div class="center mt3" data-reveal>
      <p class="small mb2">Dates correct at August 2026. Rules move; before acting, check gov.uk or ask us. The check is free.</p>
      <a class="btn btn-solid btn-lg" href="{L('contact.html')}"><span>Get your compliance position checked, free</span><span class="ar">&rarr;</span></a>
    </div>
  </div>
</section>"""

def resources(L):
    return f"""
<section class="hero" style="min-height:min(56dvh,480px)">
  <div class="wrap hero-in">
    <h1 class="hero-t"><span class="cs" data-chars>The site office.</span></h1>
    <p class="hero-sub">Everything we know, written down for free: plain-English guides, the questions everyone asks, and a live radar of the rules rolling in. Read it in the cab, act on it by Friday.</p>
  </div>
  <div class="hero-rule"></div>
</section>

<section class="sec" style="padding-top:28px">
  <div class="wrap">
    <div class="grid g3" data-stagger>
      <a class="cell dark" href="{L('blog/index.html')}" style="text-decoration:none;min-height:300px">
        <div class="img"><img src="https://picsum.photos/seed/klyara-res-guides/800/620" alt="" loading="lazy"></div>
        {P.icon('article','icn onpine')}
        <h3 class="h3 mt1">Guides library</h3>
        <p class="mute">Six deep, honest reads: MTD, CIS, the reverse charge, getting paid, what bookkeeping should cost.</p>
      </a>
      <a class="cell dark" href="{L('faq.html')}" style="text-decoration:none;min-height:300px">
        <div class="img"><img src="https://picsum.photos/seed/klyara-res-faq/800/620" alt="" loading="lazy"></div>
        {P.icon('list-checks','icn onpine')}
        <h3 class="h3 mt1">Straight answers, FAQ</h3>
        <p class="mute">Thirty-odd real questions from real builders, grouped and answered without waffle.</p>
      </a>
      <a class="cell dark" href="{L('regulations-2026.html')}" style="text-decoration:none;min-height:300px">
        <div class="img"><img src="https://picsum.photos/seed/klyara-res-radar/800/620" alt="" loading="lazy"></div>
        {P.icon('clock-countdown','icn onpine')}
        <h3 class="h3 mt1">Regulation radar 2026</h3>
        <p class="mute">Every rule change hitting the trade this year and next, in date order, with what to do about each.</p>
      </a>
    </div>
  </div>
</section>

<section class="sec band">
  <div class="wrap split">
    <div>
      <h2 class="h1" data-reveal>Start with the<br>free MTD guide.</h2>
      <p class="mt2 mute" data-reveal style="font-size:1.08rem;max-width:50ch">Ten pages, zero waffle: when you are in, what quarterly filing means for a subbie, how CIS fits, and the checklist to get ready in one afternoon.</p>
    </div>
    <div data-reveal>
      <a class="btn btn-bone btn-lg" href="{L('guide.html')}"><span>Get the free guide</span><span class="ar">&rarr;</span></a>
      <p class="fine mt1">PDF, emailed instantly. One useful email a fortnight after that.</p>
    </div>
  </div>
</section>"""

PAGES4 = [
  dict(file="faq.html", route="faq", active="resources.html", title="FAQ: Straight Answers for Builders | Klyara",
       desc="MTD, CIS, the VAT reverse charge, pricing, data security and working with Klyara. Real questions from real builders, answered without waffle.", body=faq),
  dict(file="regulations-2026.html", route="regs", active="resources.html", title="Regulation Radar 2026: What Is Hitting UK Construction | Klyara",
       desc="MTD thresholds, Companies House identity verification, CIS deadlines, the reverse charge and penalty points. Every rule change in date order, in plain English.", body=regulations),
  dict(file="resources.html", route="resources", active="resources.html", title="Resources: Guides, FAQ and Regulation Radar | Klyara",
       desc="Plain-English guides for UK construction, a straight-answer FAQ, and a live radar of the rules rolling in through 2026 and 2027.", body=resources),
]
