# Changelog

All notable changes to the Dance by Nolan website (formerly First Dance by Nolan).

## 2026-06-09

### Rebrand & restructure
- Rebranded from **First Dance by Nolan** to **Dance by Nolan** (dancebynolan.com), broadening focus beyond weddings to dance lessons for beginners and the dance-curious.
- Restructured the single-page site into a **multi-page site** with shared nav, footer, and styles:
  - `index.html` — new split-path landing page (Wedding First Dance vs. Dance Lessons), leading with approachability and DWTS Austin credibility.
  - `wedding-services.html` — wedding first-dance page (reuses the prior single-page wedding content: how-it-works, testimonials, gallery, FAQ, pricing, contact). `firstdancebynolan.com` forwards here.
  - `lessons.html` — new general lessons page for beginners across genres; country-western framed for both beginners and experienced/social dancers (Nolan competed at top levels in country).
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
- `firstdancebynolan.com` now URL-forwards to `dancebynolan.com`, configured at the **domain registrar** (not in code — GitHub Pages can't do a true cross-domain redirect).

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
- [ ] Set up Formspree form ID
- [ ] Get Google Voice number for contact
- [ ] Replace gallery images with real photos
- [ ] Update testimonials with real reviews
- [ ] Swap hero video for original footage
