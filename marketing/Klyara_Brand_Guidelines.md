# Klyara — Brand Guidelines
### Extracted from klyara.com, not invented. Hand this to anyone who touches the brand.

*Revised 28 August 2026. Re-checked against the live site.*

*Every value below is taken directly from the site's own CSS custom properties and its embedded
font files. The palette is cream and deep green with a brass accent. An early written direction
in an earlier pack said navy and safety orange; that direction was never built, it does not match
the site, and it must not be reintroduced anywhere.*

---

## 1. Colour

These are the site's `:root` tokens, verbatim. Use the token name in conversation, not the hex.

```
--paper    #F4EFE4   Warm bone. The page ground. Also called --bone.
--paper2   #ECE5D4   Deeper cream. Alternate rows, subtle blocks.
--card     #FBF8F0   Warm white. Cards and surfaces sitting on paper.
--ink      #14231C   Green-black. Primary text on paper.
--ink2     #22392E   Secondary dark.
--mute     #57685C   Muted sage. Body text that steps back, on paper.
--dim      #87947F   Dimmer sage. Muted text on pine.
--pine     #16352A   Deep green. Dark sections, covers, video, van livery.
--pine2    #1D4534   Lighter pine. Cards on pine, ghost numerals.
--em       #196A48   Emerald. Positive, "done", data bars, row labels.
--em2      #135237   Deeper emerald.
--brass    #C08A2E   THE accent. Rules, kickers, CTAs, numerals.
--warn     #A6592E   Terracotta. Warnings and negative data only.
```

**Hairlines** — the site uses translucent ink/bone. Flattened equivalents for print and images:
```
On paper:  #D6D0C2 (16%)   #B4AE9E (32%)
On pine:   #2A4A3C (16%)   #3E5D4E (32%)
```

### How the colours actually behave

**There are two grounds, and you pick one per asset.** Paper (cream) or pine (deep green). Never a
gradient between them, never a third ground.

**Brass is the accent and it is used sparingly.** The top rule, the kicker text, the numerals, the
one thing you want clicked. It is not a background for body text and it is not a headline colour on
paper — brass on cream fails contrast at small sizes.

**Emerald is not a second accent.** It means *positive, correct, complete*. Row labels in tables,
"filed", data bars going the right way, the page number in the footer. If it is decorating rather
than meaning something, it is wrong.

**Terracotta is for bad news only.** Penalties, missed deadlines, the losing side of a comparison
chart. Never for emphasis.

### Contrast, checked

| Text | On | Verdict |
|---|---|---|
| `--paper` | `--pine` | Pass. The main dark combination. |
| `--dim` | `--pine` | Pass. Body text on pine. |
| `--ink` | `--paper` / `--card` | Pass. The main light combination. |
| `--mute` | `--paper` | Pass. Body text on paper. |
| `--brass` | `--pine` | Pass. Kickers, numerals, small bold. |
| `--em2` | `--paper` | Pass. Table row labels, section leads. |
| `--brass` | `--paper` | Care. Large and bold only. Never body text, never small caps. |
| `--pine2` | `--pine` | Ghost numerals only. Deliberately low contrast, decorative, never carries meaning. |
| `--em` | `--pine` | Fail. Too close. Use brass or paper on pine. |

---

## 2. Typography

Three faces, three jobs. All three are embedded in the site and included in this pack as static TTF
instances at `brand/fonts/`.

```
Bricolage Grotesque   Display. Headlines, the wordmark, big numerals.
                      Weights used: 800 (display), 700, 600 (headings).
                      Tracking: -1.2% on headings. Optical size axis matters — the
                      600 cut is set at opsz 18, the display 800 at opsz 40.

Instrument Sans       Body. Everything you read in sentences.
                      Weights: 400 body, 500 emphasis, 650/700 labels.
                      Line height 1.66 on the web, ~1.5 in print.

Spline Sans Mono      Utility. Kickers, eyebrows, tags, chips, footers, dates,
                      page numbers, data labels.
                      Weight 500. ALWAYS uppercase. Tracking +16% on kickers,
                      +8–10% on footers and tags.
```

### The kicker is the brand's signature

More than any colour, the thing that makes a piece of Klyara material recognisable is the
**small uppercase brass mono label** sitting above a large Bricolage headline.

```
CHAPTER 02  ––––
Are you a contractor?
```

Get that pairing right and almost everything else follows.

### Headline rules

**Headlines end with a full stop.** "Run the jobs. We run the rest." "Are you in?" "MTD readiness
checklist." "Verification." This is consistent across the whole site and all four PDFs. It is not
optional styling — it is the voice.

**Sentence case, never title case, never all caps.** The only all-caps in the system are mono
kickers and the KLYARA wordmark in print headers.

**Scale** — pick from the site's own clamps:
```
hero  2.7 → 5.6rem      h1  2.0 → 3.5rem      h2  1.45 → 2.05rem
h3    1.06 → 1.26rem    body 1.0 → 1.08rem    lede 1.1 → 1.3rem
```

**Measure:** the site sets `.lede { max-width: 58ch }`. Keep running text at 58–65 characters.

### Money and numbers

Every price carries the £ sign. Never "59 pounds", never a bare "59". Ranges take an en dash and
repeat the sign: £29–£59, £149–£399. Where a price is being quoted to a prospect, say **ex VAT**
next to it, because the site does and the engagement letter does. A monthly price is written
£59/mo in a table and "£59 a month" in a sentence.

### The font subset constraint — read this before making anything

The fonts embedded in the site are **subsets of 108 glyphs**. These characters do **not** exist and
will render as blank gaps:

```
—  (em dash)     ✓ ✔  (ticks)      ✗ ✘  (crosses)     ⚠  (warning)     ₤
→  (arrow — absent from Spline Mono; present in the others)
```

**Use instead:** en dash `–`, the mid dot `·`, drawn tick marks, and the word "and". Every generator
in this pack routes text through a `safe()` function that substitutes automatically — if you write
copy by hand into a design tool, do the substitution yourself.

The `·` mid dot is the brand's natural separator and it is present in all three faces. Use it.

---

## 3. The mark

An angular **K** drawn as a single polygon, not a typeset letter. The exact coordinates, in an
88 × 88 box:

```
20,16  35,16  35,40  57,16  76,16  47.5,46  76,72  56,72  35,52  35,72  20,72
```

That polygon is the mark. Do not substitute a K from any typeface, including Bricolage.

### Two containers

**Disc** — a brass circle with the K in pine, sitting inside at 60% of the disc width.
Used in print headers, avatars, and anywhere the mark needs to hold its own.

**Plain** — the bare K in bone, no container. Used in the site header, where it sits on pine.

### The wordmark

Two forms, both correct in their place:

- **`Klyara`** — sentence case, Bricolage 600. The web header, and anywhere the brand appears
  conversationally.
- **`KLYARA`** — all caps, Bricolage 800. Print headers and document covers only.

Mark-to-wordmark gap: 42% of the mark's height.

### Never
- Retype the K in another font
- Recolour the disc away from brass
- Add a gradient, shadow, glow or outline
- Rotate, skew or stretch it
- Put it on a photograph without a solid ground behind it
- Write "KLYARA" in sentence-case contexts, or "Klyara" on a print cover

**Minimum size:** 24px on screen, 8mm in print. Below that, drop the disc and use the bare K.
**Clear space:** 30% of the mark's width on all four sides.

---

## 4. Layout

### The two page architectures

**Cover / full-bleed (pine).**
Brass rule across the very top. Wordmark and mono strapline top-left. A large amount of empty pine.
Headline low on the page, roughly two-thirds down. Sub-headline in brass. Body in paper. Mono fine
print at the bottom.

**Interior (paper).**
A pine header band across the top, roughly 40mm on A4 or 17% of a social graphic. Inside the band: a
mono brass kicker with a short brass dash rule, then the heading in paper, and a very large ghosted
numeral in `--pine2` bleeding off the right edge. A brass rule closes the band. Body sits on paper
below. Mono footer, with the page number in emerald.

That ghosted numeral is doing a lot of work. Keep it.

### Radii
```
--r     16px   cards, callouts, tables
--r-lg  24px   large panels
99px           pills, tags, chips
```

### Shadow
One only: `0 26px 70px rgba(20,35,28,.14)`. Soft, large, low opacity, green-tinted. Never a hard
drop shadow, never black.

### Components
- **Pine callout** — deep green box, brass mono label, brass bullet dots, paper text. For the
  "one-minute version" style summary block.
- **Quote box** — card ground, emerald left bar 3px, brass mono label. For the aside that matters.
- **Brass box** — solid brass, ink text, for the single call to action at the end of a document.
- **Section head** — a 2.6px brass vertical bar to the left of a Bricolage 600 heading.
- **Table** — mono brass column headers, hairline under the header, hairlines between rows, emerald
  row labels in the first column. No vertical rules, no filled header block.

### Margins
```
Social graphic   7.5% of width
A4 print         19mm
Web              --pad: clamp(20px, 4vw, 44px)
Max width        1240px
```

---

## 5. Voice

**Short sentences. Then a shorter one.**

**Headlines end with a full stop.**

**Specific over general.** Not "significant penalties" — "£100 the day you're late, £200 at two
months, £300 or 5% at six."

**Second person.** "You are in MTD." Not "clients in this position are within scope."

**Say the uncomfortable thing.** "You don't need the receptionist." "We're new and we're not going to
pretend otherwise." "It is not fixable on 6 November." This is the most distinctive thing about how
Klyara sounds and it is why it is trusted.

**Lead with the reader's problem, never with Klyara.**

### Words to use
```
straight · sorted · handled · filed · on time · what it actually costs
the bit that catches people · gross means gross · plain English
```

### Words never to use
```
solution · synergy · leverage (verb) · best-in-class · seamless · world-class
revolutionise · empower · "we're passionate about" · "unlock your potential"
```

Also banned: exclamation marks in marketing copy, emoji in email subject lines, and any sentence
beginning "In today's fast-paced business environment".

### Emoji
Don't. Not in headlines, not in subject lines, not as bullets, not as section markers. The site
uses none and the audience does not want them from a bookkeeper. They also fall outside the font
subsets, so in anything the generators render they come out as a gap.

### The disclaimer — non-negotiable
Every piece of public tax content carries a version of the site's own line:

> General guidance, not tax advice. Rules move — check gov.uk or ask us before acting.

Keep it. You are publishing tax guidance under a bookkeeping firm's name.

---

## 6. Photography

**Real over stock, always.** The site's own imagery is real construction. A slightly badly-lit photo
of an actual Guildford site beats a perfect stock image of models in clean hi-vis, and this audience
can tell instantly.

**Shoot:** Craig at a desk with real paperwork. A phone photographing a crumpled receipt on a van
dashboard. An actual site. Hands, tools, muddy boots, a laptop on a workbench.

**Never:** handshakes in front of glass buildings, diverse teams laughing at a whiteboard, rising-graph
stock, immaculate unworn PPE.

**Treatment:** if a photo carries text, put a pine overlay at 70–85% behind the text block rather
than dropping text onto the image.

---

## 7. Making new assets

Everything in this pack is generated from Python, and the generators ship with it. Use them rather
than rebuilding by hand — it guarantees the tokens and the fonts are right.

```
brand/klyara_brand.py    Tokens, fonts, the K polygon, layout helpers, safe().
                         Change a colour here and every image rebuilds consistently.
brand/klyara_pdf.py      The print system for ReportLab — pine boxes, quote boxes,
                         brass boxes, tables, section heads, the mark.
brand/gen_identity.py    Logos, avatars, banners.
brand/gen_posts.py       Social posts, carousels, story covers, the deadline card.
brand/gen_video.py       Kinetic typography videos.
brand/gen_leadmagnet.py  The multi-page branded A4 guide.
brand/gen_proposal.py    Client proposals — edit the CLIENT dict, re-run.
brand/fonts/             The site's own fonts, converted to static TTF.
```

**New social post:** open `gen_posts.py`, copy a `post(...)` line, change the text, re-run.
**New client proposal:** open `gen_proposal.py`, edit `CLIENT`, re-run. It names the file itself.

---

## 8. Asset sizes

| Where | Size | Folder |
|---|---|---|
| X header | 1500×500 | `banners/` |
| LinkedIn company | 1128×191 | `banners/` |
| LinkedIn personal | 1584×396 | `banners/` |
| Facebook cover | 1640×856 | `banners/` |
| YouTube channel | 2560×1440 | `banners/` |
| Reddit banner | 1920×384 | `banners/` |
| Google Business cover | 1200×900 | `banners/klyara-banner-gbp.png` |
| Email header | 1200×260 | `banners/` |
| Avatars | 400 / 512 / 1024 | `avatars/` |
| Square post | 1080×1080 | `posts/` |
| Carousel slide | 1080×1350 | `carousel/` |
| Story / highlight | 1080×1920 | `stories/` |
| Vertical video | 1080×1920 | `video/` |
| A5 print | 1748×2480 @300dpi | `print/` |

---

## 9. The test

Before anything goes out:

1. **Is the ground paper or pine?** Not both, not something else.
2. **Is brass used once, on the thing that matters?**
3. **Is there a mono kicker above the headline?**
4. **Does the headline end with a full stop?**
5. **Would a builder read it and think "that's straight"?**

If all five are yes, it's Klyara.
