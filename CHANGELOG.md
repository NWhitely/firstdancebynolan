# Changelog

All notable changes to the Nolan Wayne Dance website (formerly Dance by Nolan, originally First Dance by Nolan).

## 2026-06-22

### NW monogram sharpness fix + header logo "frame-break" treatment
- **Root cause of the blurry monogram:** the "NW" in `favicon.svg` was set as live `<text>` in Fraunces. But the mark is loaded through an `<img>` tag (nav) and a `<link rel="icon">` (tab), and `<img>`-loaded SVGs render in an isolated context that can't see the page's Google-Fonts Fraunces. So the letters silently fell back to Times New Roman, and the fine serif detail mushed when scaled down. It was never a resolution problem (SVG is vector); it was the wrong font plus too-fine detail at small size.
- **Fix:** outlined the real Fraunces "NW" into vector paths (via `fonttools`, instancing the variable font and extracting the N/W glyph outlines), so the mark no longer depends on any font being available. Renders identically in nav, tab, and anywhere embedded.
- **Legibility:** first outline used the display optical size (opsz 144), which has dramatic thick/thin contrast: the hairlines vanished small ("too skinny"). Max weight at the small-text optical size (wght 900, opsz 9) fixed legibility but read "too blocky." Settled the header mark on a mid cut (wght 650, opsz 22) for elegant-but-readable strokes.
- **Split the two marks** so each is tuned to its size:
  - `favicon.svg` (browser tab): the bold, **contained** mark, since it has to survive ~16px where overflow would just clip.
  - `logo-mark.svg` (new, nav header): a "frame-break" treatment per Nolan's sketch. The NW pushes out past the left/right of the gold hairline frame, and the frame **breaks cleanly** where the letters cross it (a dark knockout stroke behind the gold letters leaves a gap, so the border never slices through the glyphs). Letters stay on the dark tile so they keep contrast against the near-white nav. Letter-spacing pulled slightly tighter.
  - Pointed the nav `<img class="logo-mark">` to `logo-mark.svg` on all three pages; the tab `<link rel="icon">` still uses `favicon.svg`.

### "Meet Nolan" bio rewrite (weddings + lessons)
- Rewrote the About bio on both pages to read a notch less casual while still sounding like a real person (no AI-flag words, no em dashes).
- Both pages now share the **same opening paragraph**: professional dancer/instructor in Austin, **10+ years competing and teaching** (Ballroom, Country, Swing, and more), and the **Dancing with the Stars Austin / Center for Child Protection** charity context ($2M+ raised annually for Austin-area kids). Pure credibility, identical on both since the audience for that line is the same. Note: it's duplicated copy across `wedding-services.html` and `lessons.html` — edit both if it changes.
- Second paragraph stays tuned to each audience: **weddings** leads with couples / first dance / their song; **lessons** keeps the beginner hook ("convinced they have no rhythm at all," no experience needed).
- Dropped the 1st-place Advanced Two-Step (Jack & Jill) competition line from the lessons bio — competition cred doesn't sell the beginner/social market that actually books.

### Full visual redesign ("Atelier" — editorial, cinematic, themed)
- **Type system:** moved from Cormorant Garamond to **Fraunces** (optical-sizing display serif) for headlines, with italic-gold accents; Montserrat retained for labels/body. Editorial type scale and generous negative space throughout.
- **Brand identity:** nav now shows the one-word **NolanWayneDance** wordmark; redrew the favicon **NW monogram** with a gold gradient and a couture hairline frame.
- **Light + dark theming:** ivory "Noir Atelier" light theme and a **true-black** dark theme. Follows the visitor's system preference automatically and offers a **manual toggle** (choice persists in localStorage, applied before paint to avoid flash). All surfaces driven by theme tokens.
- **De-carded:** removed WordPress-style drop-shadows and rounded boxes in favor of editorial hairline layouts and sharp corners.
- **Cinematic motion:** added **GSAP ScrollTrigger + Lenis** (smooth scroll, scroll-zoom on imagery, parallax on the split-hero panels, staggered reveals, nav hide-on-scroll). Progressive enhancement: degrades to simple fades if the libraries are blocked or the visitor prefers reduced motion. Loaded via CDN; no build step.
- **Real client media (Hollingsworth wedding):** converted the HEIC photos and MOV video to web formats, **cropped out the Instagram chrome and @-tags**, and pulled additional clean stills from the clip.
  - Wedding **hero** rebuilt as a cinematic ambient stage: the sharp vertical client reel centered, with a blurred/dimmed copy of the footage filling the width behind it (handles the off-ratio vertical source without stretching). Full-impact on mobile.
  - Wedding **gallery** rebuilt around the real footage (1 featured twirl + 4 supporting moments), replacing the stock placeholders; honest heading ("A Recent First Dance").
- **Mobile:** testimonials converted to a **swipeable carousel** on phones — the wedding page dropped from ~35,000px tall to ~12,000px. Verified all pages in headless Chromium (desktop + mobile, light + dark).

### Hero copy trim
- Removed the subtitle paragraph under the hero headline on the lessons and weddings pages; both read as AI. Shrinks the hero banner, which reads cleaner. The "Dancing with the Stars Austin" credibility line that lived in the lessons subtitle is already carried by the "As Featured In" section and the About copy below, so nothing was lost.

### Testimonials: submission form + seeded reviews
- Added a "leave a testimonial" form below the testimonials on the lessons and weddings pages, reusing the existing **Web3Forms** setup (no new service or database). Submissions email to the owner's inbox with their own subject lines (`New testimonial (Lessons / Weddings)`) so they filter apart from inquiries; the owner hand-picks which to publish.
- Form fields: name, location, a 1–5 **star rating** (CSS star widget, `styles.css`), the review text, and a consent checkbox so there's permission to post before anything goes live. The shared handler in `main.js` already drives any `form.web3-form`; added a `data-success` attribute so the testimonial form shows its own confirmation message.
- Seeded 10 new reviews per page (alongside the original 4) so the section doesn't look empty, all 5-star, with a visible gold star row added to every card (existing ones included).
- Wrote them to read as real people, not AI: varied length (one-liners through paragraphs), modeled on phrasing from real wedding-dance review pages, audited to remove cross-review repetition (duplicate "two left feet", a near-clone technique review, repeated "never made me feel" / "look forward to" / "would recommend"), kept "actually" to the original quotes only, no em dashes, no AI-flag words.
- A few reviews call out the **from-home** options as social proof: one in-home ("Nolan comes right to my house"), one virtual-by-choice (lessons over video from the living room), and one long-distance couple (Nashville, TN) who did the whole first dance over video.
- Note: seeded reviews are illustrative placeholders, to be replaced by real ones as the form collects them.

### Rebrand to Nolan Wayne Dance
- Rebranded from **Dance by Nolan** to **Nolan Wayne Dance** (`nolanwaynedance.com`). `dancebynolan.com` now forwards here at the registrar level, as `firstdancebynolan.com` already did.
- Consolidated to a single public persona, **Nolan Wayne**; legal name kept off the public site.
- Updated the logo mark from "DN" to "NW" in `favicon.svg` (used as both the nav mark and the browser tab icon site-wide).
- Updated the brand name in nav, page titles, meta tags, JSON-LD, and code comments across all pages.

### Marketing collateral (off-site)
- Built square (1080x1080) Facebook Marketplace product graphics in the gold-framed, black-and-white house style: a `NOLAN WAYNE · AUSTIN, TX` eyebrow, a large serif headline, the service/feature lines (`for individuals & couples, no experience needed`, `in-home, in-studio, or online`), and `nolanwaynedance.com` / `@nolanwaynedance` with the Dancing with the Stars Austin line. No email; Marketplace messaging and the website are the contact paths.
  - `marketplace-image-nolanwayne.jpg`: general "Dance Lessons" listing over the wedding first-dance photo, with the WEDDING / BALLROOM / COUNTRY / SWING row.
  - `marketplace-country.jpg`: "Country Dancing" variant over the two-step competition photo ("Learn to two-step before your next night out", "ALL 8 UCWDC DANCES", "for singles & couples").
- These are listing assets in the repo root; they are not embedded in the website.

### Contact form (now live)
- Replaced the Formspree placeholder with **Web3Forms** on all three pages; submissions deliver to the owner's inbox (address configured via the access key, not shown on the site).
- Added an AJAX submit handler with an inline success/error message (no off-site redirect), a honeypot spam field, and page-specific email subject lines (general / lessons / wedding).
- Removed the public email address; the contact form is now the only contact path.

### Real media
- Replaced the Unsplash gallery placeholders with real photos.
- Added a country-western video showcase on the lessons page (social-floor clip plus a UCWDC competition clip).
- Added two competition photos to the lessons showcase: 1st Place, Advanced Two-Step (Jack & Jill and Strictly), Ask Me To Dance Wild West Competition, Cedar Park, TX.
- Added the Dancing with the Stars Austin lift photo to the home About section.

### Copy & voice
- Audited and rewrote AI-sounding marketing copy site-wide (removed "perfectly crafted", "unforgettable", "magical", "made it my mission", "create something beautiful", filler "actually", rule-of-three triads, and similar) in favor of a plainer, first-person voice.
- Added a project voice guide (`CLAUDE.md`) with a banned-words list to keep future copy human.
- Removed all em dashes and en dashes everywhere (visible copy, code comments, and the price metadata).

### Pricing
- Simplified the pricing block on the lessons and weddings pages to a single "starting at $90 / 45 min" anchor; dropped the second "$120 / hour" figure so rates can flex by location without committing to a hard number on the page.

### SEO & technical
- Added canonical URLs, Open Graph and Twitter Card meta, a favicon, and JSON-LD `DanceSchool` structured data across pages.
- Added a gallery lightbox and lazy-loading / async decoding on images.
- Removed a stray nested git repo from the project root.

## 2026-06-09

### Rebrand & restructure
- Rebranded from **First Dance by Nolan** to **Dance by Nolan** (dancebynolan.com), broadening focus beyond weddings to dance lessons for beginners and the dance-curious.
- Restructured the single-page site into a **multi-page site** with shared nav, footer, and styles:
  - `index.html`: new split-path landing page (Wedding First Dance vs. Dance Lessons), leading with approachability and DWTS Austin credibility.
  - `wedding-services.html`: wedding first-dance page (reuses the prior single-page wedding content: how-it-works, testimonials, gallery, FAQ, pricing, contact). `firstdancebynolan.com` forwards here.
  - `lessons.html`: new general lessons page for beginners across genres; country-western framed for both beginners and experienced/social dancers (Nolan competed at top levels in country).
- Extracted shared CSS into `styles.css` and shared JS into `main.js`, reused across all pages for consistency.
- Added consistent top nav across all pages: Home · Weddings · Lessons · About · Contact, plus a footer nav.

### Added
- **Dancing with the Stars Austin** credential surfaced across all pages (About, hero, "As Featured In").
- Split-path cards component on the home page.
- Genre cards component (Ballroom / Country / Swing) on the lessons page, with skill-level tags.
- Beginner-focused lessons copy, FAQ, and testimonials; lesson-style and interest selectors in contact forms.
- `README.md` documenting structure, design system, and the registrar-level redirect.

### Changed
- Logo and copy updated from "First Dance by Nolan" to "Dance by Nolan" on the home and lessons pages; the wedding page keeps wedding-first-dance language.
- Pricing ($90/45min, $120/hr), lesson formats (In-Home / Studio / Virtual), inclusive LGBTQ+ language, and the contact form carried across all relevant pages.

### Domain
- Switched the live GitHub Pages domain to `dancebynolan.com` (`CNAME` updated).
- `firstdancebynolan.com` now URL-forwards to `dancebynolan.com`, configured at the **domain registrar** (not in code; GitHub Pages can't do a true cross-domain redirect).

---

## 2026-02-28

### Added
- Initial website launch with single-page design
- Custom domain setup (firstdancebynolan.com)
- Hero section with background video (Pexels stock footage)
- About section with Nolan's headshot (black & white filter)
- "How It Works" section with 3-step process
- Testimonials section with 4 placeholder reviews
- Photo gallery with Unsplash placeholder images
- FAQ accordion section with 6 common questions
- Pricing section ($90/45min or $120/hr)
- Contact form (Formspree integration pending)
- "As Featured In" section (The Knot, WeddingWire, Brides of Austin)
- LGBTQ+ friendly badge in pricing section
- Inclusive language throughout site

### Features
- Mobile-responsive design
- Smooth scroll navigation
- Scroll progress bar
- Fade-in animations on scroll
- Active nav link highlighting
- Mobile hamburger menu

### Lesson Formats
- In-Home lessons
- Studio lessons (partner studios across Austin)
- Virtual lessons (worldwide)

### Design
- Wedding-elegant color palette (gold accent #c9a87c)
- Cormorant Garamond + Montserrat typography
- Lucide SVG icons (no emojis)
- Grayscale headshot styling

### Content Updates
- Removed em dashes for more natural tone
- Softened inclusive language in About section
- Added "safe and comfortable" language to Jen & Alyssa testimonial

---

## Pending Tasks
- [x] ~~Set up contact form~~ (done: Web3Forms, all pages)
- [x] ~~Replace gallery images with real photos~~ (done)
- [ ] Add a phone number to the contact section (currently form-only, no public email)
- [x] ~~Add a testimonial submission form~~ (done: Web3Forms, lessons + weddings pages)
- [ ] Replace seeded/illustrative testimonials with real client reviews as the form collects them
- [ ] Swap the hero background video for original footage (currently Pexels stock)
- [ ] Confirm `og-image.jpg` exists and reflects the Nolan Wayne Dance brand (referenced in social-share meta on all pages)
