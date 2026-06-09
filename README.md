# Dance by Nolan

Marketing website for **Dance by Nolan** — beginner-friendly dance instruction in
Austin, TX by Nolan Wayne (of *Dancing with the Stars Austin*). The site serves two
audiences: wedding couples planning a first dance, and beginners / dance-curious folks
who want private lessons in Ballroom, Country, Swing, and more.

Static HTML/CSS/JS, hosted on GitHub Pages. No build step.

## Structure

This is a multi-page site sharing one stylesheet and one script for a consistent look.

| File                    | Purpose |
|-------------------------|---------|
| `index.html`            | **Home / landing.** Split-path hero sending visitors to either Weddings or Lessons. Leads with approachability + DWTS Austin credibility. |
| `wedding-services.html` | **Weddings.** The wedding first-dance page (how-it-works, testimonials, gallery, wedding FAQ, pricing, contact). `firstdancebynolan.com` forwards here. |
| `lessons.html`          | **Lessons.** General, beginner-focused lessons across genres. Country also serves experienced/social dancers (Nolan competed at top levels in country-western). |
| `styles.css`            | Shared styles for all pages (palette, typography, components). |
| `main.js`               | Shared interactions (mobile menu, scroll progress, fade-ins, FAQ accordion, smooth scroll). |
| `assets/`               | Images (e.g. `nolan-headshot.jpg`). |
| `CNAME`                 | GitHub Pages custom domain. |

### Shared design system
- **Palette:** gold accent `#c9a87c` on a warm off-white (`#fffcf8`).
- **Type:** Cormorant Garamond (headings) + Montserrat (body).
- **Components:** hero, cards, testimonials, pricing, lesson formats, inclusive
  (LGBTQ+ friendly) badge, "As Featured In", FAQ accordion, contact form.
- **Nav (every page):** Home · Weddings · Lessons · About · Contact.

## Domains & redirect

- **Primary brand domain:** `dancebynolan.com` (the rebrand). This is the live GitHub
  Pages domain — see `CNAME`.
- **Legacy domain:** `firstdancebynolan.com` → **URL-forwards to `dancebynolan.com`**
  (configured at the registrar). ✅ Live.

> ⚠️ **The legacy redirect is configured at the domain registrar (URL forwarding),
> NOT in this repo.** GitHub Pages can't do a true cross-domain redirect, so there is
> intentionally no redirect code here.

## Local preview

Open any page directly in a browser, or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Pending tasks
- [x] Point `dancebynolan.com` DNS at GitHub Pages and update `CNAME`.
- [x] Configure `firstdancebynolan.com` → `dancebynolan.com` forward at registrar.
- [ ] Replace `YOUR_FORM_ID` in the contact forms with the real Formspree endpoint.
- [ ] Add Google Voice number to contact sections (placeholder comment in each form).
- [ ] Replace gallery / placeholder images and stock hero video with original footage.
- [ ] Swap placeholder testimonials for real reviews.
