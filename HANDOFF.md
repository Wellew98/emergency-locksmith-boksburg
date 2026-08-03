# HANDOFF — Emergency Locksmith Boksburg microsite

**Owner:** Wellew Phiri (Wellew98)
**Date of this handoff:** 3 August 2026
**Status:** Site built (1 day old), not indexed, SEO pass 1 in open PR awaiting merge

---

## 1. What this project is

A **GBP-less lead-generation microsite**. Built following a YouTube/Rank Expand Academy
course ("How I Built 50 Microsites That Took Over a State" — the STAR method) using the
course's own microsite builder tool plus a custom GPT for content, then Hermes agent.

**Business model:** rank organically for `locksmith boksburg`, capture calls, resell the
leads to a real locksmith. Wellew is the middleman. He does NOT operate a locksmith business.

**Important distinction:** This is deliberately NOT the Clarity Clicks model. Clarity Clicks
is his agency where the *client* owns the GBP and the site. This microsite is an asset
**he** owns. Do not collapse the two — a previous session made that mistake and it was
correctly rejected. Do not suggest converting this into a client-owned site unless he raises it.

- **Live URL:** https://emergencylocksmithboksburg.co.za
- **Repo:** `Wellew98/emergency-locksmith-boksburg` (default branch is **`master`**, not `main`)
- **Hosting:** Cloudflare Pages, auto-deploys from GitHub
- **Phone on site:** 079 106 5911
- **Stack:** static HTML, one CSS file, one JS file. No build step.

---

## 2. VERIFIED DATA (all measured via DataForSEO / live SERP — do not re-guess these)

### Keyword demand — Boksburg
| Keyword | Volume/mo | KD | CPC |
|---|---|---|---|
| locksmith boksburg | **720** | **0** | $4.00 |
| emergency locksmith boksburg | 10 | – | $4.53 |
| car key replacement boksburg | 10 | – | $1.66 |
| auto locksmith boksburg | 10 | – | $2.05 |
| 24 hour locksmith boksburg | 10 | – | – |
| key cutting boksburg | 70 | – | $0.92 |

**Critical finding: there is no subniche tail in South Africa.** The US course's advice to
avoid head terms and target subniches DOES NOT TRANSFER. SA volumes are too small. The city
head term is the only term worth targeting. A previous session wrongly advised pivoting to
subniches — this was corrected.

### Suburb-level demand (Boksburg)
Only three suburbs register measurable volume:
- Vosloorus **90/mo** (CPC $1.97)
- Boksburg North **50/mo** (CPC $2.37)
- Sunward Park **20/mo**

All other suburbs (Beyers Park, Parkrand, Atlasville, Dawn Park, Cason, Jet Park, Bartlett,
Boksburg South/East/West/Central) are **below measurement threshold**. The site has 11 area
pages; 8 of them target near-zero demand. They are topical-depth assets, not traffic assets.

### Service-keyword layer — DOES NOT EXIST
Out of 521 SA locksmith-related keywords above 100/mo, essentially every commercially
relevant one is `[city] + locksmith`. No national service terms (emergency lockout,
transponder programming, rekeying) clear 100 searches. **The vertical is purely geographic.**
The site's 6 service pages are conversion/topical assets, not ranking assets.

### Expansion candidates (all KD 0)
| City | Volume/mo | CPC | Notes |
|---|---|---|---|
| locksmith pretoria | 2400 | $4.86 | |
| **locksmith midrand** | **1900** | **$7.01** | **LOW ad competition — best next domain** |
| locksmith durban | 1600 | $1.20 | high volume, low click value |
| locksmith cape town | 1300 | $3.18 | |
| locksmith centurion | 1000 | $7.86 | highest CPC |
| locksmith pinetown | 1000 | $0.69 | very low value |
| locksmith germiston / kempton park / edenvale / sandton | 720 each | $3.19–$4.80 | |
| locksmith benoni / alberton | 590 each | ~$4.40 | |

**Sort future domains by CPC, not volume.** Coastal cities have high volume and low click
value. Gauteng (Midrand, Centurion, Pretoria) is where advertisers pay.

### Competitive landscape — `locksmith boksburg` (live SERP, measured)
Local pack fires with three established businesses:
- Unique Locksmith — 4.5 (115 reviews)
- Safe T Locksmiths — 4.4 (175 reviews)
- Exec-Q-Locksmith — 4.4 (41 reviews)

Organic:
| Pos | Domain | Referring domains |
|---|---|---|
| 1 | boksburglocksmith.co.za | 11 |
| 2 | execqlocksmith.co.za | **0** |
| 5 | waze.com (Lockwell listing) | – |
| 6 | uniquelocksmith.co.za | 57 |
| 8 | gplocksmiths.co.za | 31 |
| 9 | safe-t-locksmiths.co.za | 21 |
| 12 | autoadaptlocksmiths.co.za | 1 |
| 13 | locksmithboksburg.com | 49 |
| 17 | locksmithinboksburg.co.za | 11 |
| — | **emergencylocksmithboksburg.co.za (ours)** | **0** |

**Key reads:**
- Links are NOT the barrier. A site with 0 backlinks ranks #2. A site with 49 ranks #13.
- **A GBP-less lead-gen microsite holds #1** (boksburglocksmith.co.za). The model works here.
  A previous session claimed the missing GBP would cap us — that was wrong and was corrected.
- The #1 site's homepage is ~200 words, free WordPress theme, phone number repeated 4×.
  **The content bar is extremely low.**

### Traffic reality check (important correction)
A previous session reported the #1 competitor gets ~6,225 monthly visits (DataForSEO ETV).
**This was wrong.** The figure was inflated by malformed keyword-planner artifacts
("locksmith locksmith near me", "locksmith in near me", "locksmith close by me" — all
reporting exactly 33,100, all the same underlying query, each getting a CTR multiplier).

**Measured check:** boksburglocksmith.co.za does **NOT** appear in the top 20 for the real
`locksmith near me` in SA. Realistic traffic for the #1 site is **150–300 visits/month**,
producing maybe 10–30 calls. One site is a rounding error; the model requires a network.

**Rule for future sessions: never report ETV as traffic. Label modelled vs measured.**

### Search intent — all four People Also Ask questions are about PRICE
- How much is the cheapest locksmith?
- How much does a locksmith cost in South Africa?
- How much does it usually cost to change a lock?
- What locks can locksmiths not open?

Related searches: *locksmith boksburg prices*, *cheapest locksmith boksburg*,
*mobile locksmith boksburg*, *24 hour locksmith boksburg*, *locksmith boksburg commissioner
street*, *locksmith boksburg east rand mall*.

**Nobody on page one publishes Boksburg-specific pricing.** This is the content gap and the
main strategic bet of SEO pass 1.

### Published SA locksmith price ranges (compiled from public sources)
| Job | Typical range |
|---|---|
| Call-out / base fee | R350–R750 |
| House lockout, daytime | R400–R1 500 |
| House lockout, after hours | R1 900–R3 300 |
| Car lockout | R350–R900 |
| Rekey a lock | R250–R1 200 |
| Standard lock replacement | R550–R1 500 |
| Car key cut + programmed | R550–R2 500 |
| Smart/remote/transponder key | R2 000–R4 950 |
| High-security lock installed | R1 200–R3 500 each |

Sources: ProConnectSA, localpros.co.za, progeeks.co.za, locksmithscapetown.com,
gplocksmiths.co.za, thirtyone.co.za.
Note: several sites publish an identical "R500–R3 500" band — it is a recycled figure across
lead-gen sites, not measured pricing. These are NOT Wellew's prices; the site frames them as
market ranges compiled from published sources (CPA-safe).

---

## 3. WORK COMPLETED — PR #1, branch `seo-pass-1`

https://github.com/Wellew98/emergency-locksmith-boksburg/pull/1

**Not yet merged as of this handoff.**

### Bugs found and fixed
1. **Canonicals had no scheme** — `href="emergencylocksmithboksburg.co.za/about"` is a
   *relative* URL. Every one of 35 pages told Google its canonical was a non-existent path.
   Combined with Cloudflare returning 200 for any URL, this pointed all pages at a phantom
   duplicate. **This was the actual indexing blocker.** Now absolute `https://...`.
2. **No sitemap.xml** — `/sitemap.xml` was returning homepage HTML. Now a real 33-URL sitemap.
3. **No robots.txt** — Cloudflare was serving a default content-signals boilerplate. Now a
   real robots.txt with a `Sitemap:` directive.
4. **No 404 page** — every junk URL returned 200 with the homepage (soft-404, infinite
   duplicate URLs). Added `404.html`.
5. **No structured data anywhere.** Added Organization sitewide, Service on the 6 service
   pages, FAQPage on `/faq` and `/locksmith-prices-boksburg`. All JSON-LD validated.
   **Deliberately NO LocalBusiness schema** — no verifiable address, and fake address markup
   is a real penalty risk. Do not add it unless a partner with a real premises signs on.
6. Added OG/Twitter meta across all pages.

### Content added
- **`locksmith-prices-boksburg.html`** — the main new asset. 9-row price table, a
  "what moves the price" section, 6 FAQ answers targeting the PAA questions, CTA.
  This is the single biggest differentiator vs page one.
- **`faq.html`** — was a "Content coming soon" stub. Now answers all 4 PAA questions + 2 more.
- Homepage: replaced the vague FAQ cost answer with actual rand figures; added a 3-card
  pricing summary block above the final CTA.
- Changed "our team of **licensed** locksmiths" → "experienced". Licensing is PSIRA-regulated
  in SA; unverifiable regulated claims are a CPA risk. **Revert only if he insists.**

### Internal linking (second commit)
Price guide now has **20 inbound internal links**: 3 in homepage body content, 6 from service
pages, 11 from area pages — each with a relevant figure rather than a bare link. Plus nav
and footer. It is now the most-linked page on the site, which is correct.

---

## 4. OUTSTANDING WORK (priority order)

### Immediate
1. **Merge PR #1.**
2. **Verify Cloudflare production branch is `master`** — the repo default is NOT `main`.
   If Pages is watching `main`, nothing will ever deploy.
3. **Confirm the fix landed:** `https://emergencylocksmithboksburg.co.za/sitemap.xml` must
   return XML, not HTML. This is the single test that proves it worked.
4. **Google Search Console** — add domain property, verify, submit sitemap, request indexing
   on `/` and `/locksmith-prices-boksburg`.
5. **Citations for crawl path + referral:** Snupit and Infoisinfo both rank page one for the
   target term. Listing there gives Google a discovery route in (site currently has 0
   referring domains) and sends referral traffic.

### 11 pages still say "Content coming soon"
`about.html`, `contact.html`, `accessibility.html`, `careers.html`, `complaints-policy.html`,
`disclaimer.html`, `meet-the-team.html`, `privacy-policy.html`, `referral-marketing-disclosure.html`,
`terms-conditions.html`, `thank-you.html`

**`contact.html` is the urgent one** — it's a conversion page and currently looks broken.
The legal pages matter because a lead-gen site with no privacy policy or referral disclosure
is exposed under POPIA and the CPA. `referral-marketing-disclosure.html` is especially
important given the lead-resale model.

### Strategic decisions pending
- **Lead buyer.** No buyer is lined up. Ranking without one produces nothing. Candidates
  researched (see §5). This is the real bottleneck, not SEO.
- **Second domain.** Midrand is the data-backed pick (1900/mo, KD 0, CPC $7.01, LOW ad
  competition). Wellew has committed to running the Boksburg site for a year.
- Consider retargeting: the domain is an EMD for `emergency locksmith boksburg` (10/mo)
  while the money term is `locksmith boksburg` (720/mo). Title tags already target the
  right term, so this is not urgent, but worth noting.

---

## 5. LEAD BUYER CANDIDATES (researched via Google Places)

Ruled out (already rank, don't need leads): Unique Locksmith, Safe-T Locksmiths,
Exec-Q Locksmith, AutoAdapt Locksmiths.

| Business | Rating | Hours | Website | Notes |
|---|---|---|---|---|
| **Power Locksmith** (Vosloorus) | 5.0 (25) | 24h | `turtle-art.github.io/power-locksmith` | **Top pick.** Free GitHub Pages site = wants web presence, nobody has sold them one. Based in the only suburb with real volume. +27 76 817 5531 |
| **Ultimate Auto Lock** (Windmill Park) | 5.0 (11) | 24h | ultimateautolock.co.za | Strong auto-key work (BMW/Merc/VW). Owns a domain already. +27 60 380 0128 |
| Lockwell Key Coding (Cason Rd) | 4.3 (22) | Business hrs | none | Genuinely no website, but not 24h — clashes with site positioning. +27 82 221 3228 |

A WhatsApp outreach script was drafted (three variants: low-friction price enquiry,
straight ask, lead-partner opener). Recommended sequence: use the low-friction variant first
to get honest price data as a customer, then switch to the partner opener once he knows who's
worth working with.

---

## 6. TOOLS & ACCESS NEEDED

### DataForSEO (essential)
- Account: `hello@saremotejobs.co.za`
- Auth: HTTP Basic, base64 of `email:password`. **Wellew must supply fresh credentials** —
  the previous ones were used in an earlier session and should be rotated.
- Account required verification at app.dataforseo.com before paid endpoints worked
  (error 40104). This is now done.
- **Balance was ~$0.83 (R15) at handoff.** Roughly: live SERP $0.004/call,
  Labs keyword_overview ~$0.013, backlinks bulk ~$0.024.
- Endpoints used and known-good:
  - `POST /v3/serp/google/organic/live/advanced` (location_code 2710 = South Africa,
    se_domain google.co.za)
  - `POST /v3/dataforseo_labs/google/keyword_overview/live`
  - `POST /v3/dataforseo_labs/google/ranked_keywords/live`
  - `POST /v3/dataforseo_labs/google/keyword_ideas/live`
  - `POST /v3/backlinks/bulk_referring_domains/live`
  - `GET /v3/appendix/user_data` (balance check, free)
- **Gotcha:** writing curl output to a file with `-o` intermittently failed with
  "DNS resolution failure". Piping directly to python worked. Pipe, don't redirect.

### GitHub
- Repo `Wellew98/emergency-locksmith-boksburg`
- Needs a **fine-grained PAT** with **Contents: Read and write**.
- **Common failure:** selecting "Public repositories" under Repository access makes the token
  read-only and hides the Repository permissions box entirely. Must select
  "Only select repositories" → pick the repo → then set Contents to Read and write.
- The token used in this session expires **10 August 2026** and was exposed in chat —
  Wellew should revoke it and issue a fresh one per session.

### Other
- `bash_tool` with network access (git, curl, python3)
- `web_search` / `web_fetch` for competitor and pricing research
- Google Places search for local business/partner research
- Container resets between sessions — always re-clone.

---

## 7. HOW WELLEW WANTS TO BE WORKED WITH

- **Blunt, logic-first. No compliments, no padding, no engagement bait.**
- Push back hard on weak reasoning. He responds well to it and explicitly asks for it.
- **Verify factual and time-sensitive claims with tools. Do not answer from memory with
  false confidence.** He gave API access specifically so decisions are data-based.
- **Label measured vs modelled.** Never present an estimate as a measurement.
- When wrong, say so plainly and move on. Do not grovel.
- He will challenge conclusions — usually correctly. Check before defending.

### Corrections made during this session (do not repeat these errors)
1. Assumed he hadn't validated competition. He had, via DataForSEO.
2. Advised pivoting to subniches. Wrong — no subniche volume exists in SA.
3. Claimed the missing GBP would cap rankings. Wrong — a GBP-less microsite holds #1.
4. Reported ETV 6,225 as traffic. Wrong — inflated by keyword-planner artifacts.
5. Collapsed this project into the Clarity Clicks client model. He rejected it correctly.
6. Over-alarmed about the site not being indexed — it was one day old with zero backlinks.
   That's the null result, not a problem.

---

## 8. CREDENTIALS

Not stored here — this repository is **public**, and GitHub secret scanning auto-revokes
personal access tokens pushed to public repos.

Wellew holds the live DataForSEO and GitHub credentials in the downloadable copy of this
handoff (`HANDOFF-locksmith-boksburg.md`). He supplies them at the start of each session.

Setup notes that are safe to record:
- DataForSEO account `hello@saremotejobs.co.za`, verified, HTTP Basic auth.
- GitHub PAT must be **fine-grained**, Repository access = "Only select repositories"
  (NOT "Public repositories", which is read-only), Repository permissions → Contents →
  **Read and write**.
- Pipe curl output to python; `-o` file writes fail intermittently in the container.
