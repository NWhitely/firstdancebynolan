#!/usr/bin/env python3
"""
Marketplace-safe branded card.

A stripped-down version of the promo wedding card for Facebook Marketplace.
Keeps brand identity (name, service, location, credential) but REMOVES the three
things that trip Marketplace's off-platform-ad detector:
  - website URL
  - @handle / social redirect
  - "Book now" CTA button

Use as a SECONDARY photo on a listing (photo 2 or 3), never the lead image.
The lead image should be a plain real photo (assets/hollingsworth-2.jpg).

Run:  python3 make_marketplace_safe_card.py
Out:  marketplace-wedding-safe.jpg  (1080x1080)
"""
from PIL import Image, ImageDraw, ImageFont

SRC = "assets/hollingsworth-2.jpg"
OUT = "marketplace-wedding-safe.jpg"
SIZE = 1080

GOLD = (198, 165, 108)
GOLD_LIGHT = (220, 192, 146)
WHITE = (245, 242, 236)

FRAUNCES = "fonts/Fraunces.ttf"   # variable: opsz, wght, soft, wonk
MONTSERRAT = "fonts/Montserrat.ttf"  # variable: wght


def fraunces(size, wght=470, opsz=144, soft=0, wonk=0):
    f = ImageFont.truetype(FRAUNCES, size)
    f.set_variation_by_axes([opsz, wght, soft, wonk])
    return f


def mont(size, wght=500):
    f = ImageFont.truetype(MONTSERRAT, size)
    f.set_variation_by_axes([wght])
    return f


def cover(im, size):
    """Scale to cover a square, crop keeping the couple in the lower third."""
    w, h = im.size
    scale = max(size / w, size / h)
    nw, nh = round(w * scale), round(h * scale)
    im = im.resize((nw, nh), Image.LANCZOS)
    left = (nw - size) // 2
    top = min(nh - size, max(0, nh - size))  # bias toward bottom (keep couple)
    return im.crop((left, top, left + size, top + size))


def tracked(draw, xy, text, fnt, fill, tracking, anchor_center_x=None):
    """Draw letterspaced text. If anchor_center_x given, center the whole run."""
    widths = [draw.textlength(c, font=fnt) for c in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x, y = xy
    if anchor_center_x is not None:
        x = anchor_center_x - total / 2
    for c, cw in zip(text, widths):
        draw.text((x, y), c, font=fnt, fill=fill)
        x += cw + tracking
    return total


def main():
    base = cover(Image.open(SRC).convert("RGB"), SIZE)

    # Darken for legibility: overall + stronger top/bottom gradient.
    overlay = Image.new("L", (1, SIZE), 0)
    for y in range(SIZE):
        t = y / SIZE
        # darker at very top (eyebrow/headline) and bottom (footer)
        edge = max(0.0, 1 - y / 360) ** 1.5 + max(0.0, (y - (SIZE - 320)) / 320) ** 1.5
        val = int(150 * min(1.0, 0.45 + 0.55 * edge))
        overlay.putpixel((0, y), val)
    grad = overlay.resize((SIZE, SIZE))
    dark = Image.new("RGB", (SIZE, SIZE), (8, 7, 6))
    base = Image.composite(dark, base, grad)
    # gentle global dim
    base = Image.blend(base, Image.new("RGB", (SIZE, SIZE), (10, 9, 8)), 0.18)

    d = ImageDraw.Draw(base)
    cx = SIZE // 2

    # gold frame
    m = 30
    d.rectangle([m, m, SIZE - m - 1, SIZE - m - 1], outline=GOLD, width=2)

    # top eyebrow
    eb = mont(27, 600)
    tracked(d, (0, 96), "NOLAN WAYNE   ·   AUSTIN, TX", eb, GOLD_LIGHT, 6,
            anchor_center_x=cx)

    # headline (Fraunces display, two lines)
    head = fraunces(104, wght=470, opsz=144)
    d.text((cx, 168), "Wedding Dance", font=head, fill=WHITE, anchor="ma")
    d.text((cx, 290), "Lessons", font=head, fill=WHITE, anchor="ma")

    # subhead
    sub = mont(30, 450)
    d.text((cx, 432), "Custom choreography, built around your song",
           font=sub, fill=GOLD_LIGHT, anchor="ma")

    # bottom: divider + styles + credential (no url, no handle, no button)
    d.line([cx - 26, SIZE - 250, cx + 26, SIZE - 250], fill=GOLD, width=2)
    styles = mont(34, 600)
    tracked(d, (0, SIZE - 212), "WALTZ · COUNTRY · SWING · SLOW DANCE",
            styles, GOLD_LIGHT, 2, anchor_center_x=cx)
    where = mont(27, 450)
    d.text((cx, SIZE - 158), "in-home, in-studio, or online",
           font=where, fill=WHITE, anchor="ma")
    cred = mont(24, 600)
    tracked(d, (0, SIZE - 96), "10+ YEARS TEACHING & COMPETING",
            cred, GOLD, 3, anchor_center_x=cx)

    base.save(OUT, quality=92)
    print("wrote", OUT, base.size)


if __name__ == "__main__":
    main()
