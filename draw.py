#!/usr/bin/env python3
"""Draw the 17 November 2026 world-news infographic (1024x1024 PNG).

All facts were verified against news reported on 17 Nov 2026
(Algenom daily brief, Just Security Early Edition, AP, Reuters,
Al Jazeera, CNN, BBC, FeedCast). No invented events.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (244, 241, 234)      # paper
NAVY = (20, 33, 61)       # header/footer
GOLD = (233, 196, 106)
CARD = (255, 255, 255)
INK = (24, 24, 24)
GREY = (90, 90, 90)
RED = (178, 34, 34)

def font(name, size):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}.ttf", size)

F_DATE = font("DejaVuSans-Bold", 76)
F_SUB = font("DejaVuSans-Bold", 27)
F_TAG = font("DejaVuSans-Bold", 20)
F_HEAD = font("DejaVuSans-Bold", 29)
F_BODY = font("DejaVuSans", 23)
F_TICK = font("DejaVuSans-Bold", 21)
F_SRC = font("DejaVuSans", 19)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- header ----
d.rectangle([0, 0, W, 148], fill=NAVY)
d.rectangle([0, 148, W, 154], fill=GOLD)
# small globe mark
cx, cy, r = 78, 74, 42
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=4)
d.ellipse([cx - r, cy - 8, cx + r, cy + 8], outline=GOLD, width=3)
d.line([cx, cy - r, cx, cy + r], fill=GOLD, width=3)
d.line([cx - r, cy, cx + r, cy], fill=GOLD, width=3)
d.text((140, 22), "17 NOVEMBER 2026", font=F_DATE, fill=(255, 255, 255))
d.text((142, 106), "TUESDAY  ·  THE WORLD IN ONE DAY", font=F_SUB, fill=GOLD)

# ---- stories: (tag, colour, headline, body, icon) ----
stories = [
    ("EUROPE · WAR", (178, 34, 34),
     "Ukraine hits the Crimea bridge again",
     "Second strike in 24 hours; Zelenskyy hails an \u201cunprecedented operation\u201d.",
     "bridge"),
    ("MIDDLE EAST · CONFLICT", (178, 34, 34),
     "Iran fires drones at a US base in Bahrain",
     "Radar site at Sheikh Isa attacked; Bahrain says it was intercepted, no casualties.",
     "radar"),
    ("ASIA · DIPLOMACY", (31, 93, 140),
     "Xi, Trump and Putin to meet in Shenzhen",
     "China confirms first three-way talks, Thursday 19 Nov, on the APEC sidelines.",
     "summit"),
    ("MIDDLE EAST · SHIPPING", (178, 34, 34),
     "Tankers hit mines near Hormuz",
     "Several vessels struck and caught fire on a route Tehran calls unauthorised.",
     "ship"),
    ("EUROPE · MIGRATION", (31, 93, 140),
     "Five nations plan a Rwanda return hub",
     "Germany, Denmark, Austria, Greece and the Netherlands to send rejected asylum seekers.",
     "pin"),
    ("AMERICAS · FINANCE", (31, 93, 140),
     "Banking outage hits US customers",
     "JPMorgan software bug disrupts online banking and Zelle at major US banks.",
     "bank"),
]

def icon(kind, x, y, s, col):
    if kind == "bridge":
        d.arc([x, y + s * 0.3, x + s, y + s], 180, 360, fill=col, width=5)
        d.line([x, y + s * 0.75, x + s, y + s * 0.75], fill=col, width=5)
        d.line([x + s * 0.15, y + s * 0.45, x + s * 0.15, y + s * 0.75], fill=col, width=4)
        d.line([x + s * 0.85, y + s * 0.45, x + s * 0.85, y + s * 0.75], fill=col, width=4)
        d.line([x + s * 0.5, y + s * 0.3, x + s * 0.5, y + s * 0.75], fill=col, width=4)
    elif kind == "radar":
        d.ellipse([x + s * 0.2, y + s * 0.2, x + s * 0.8, y + s * 0.8], outline=col, width=4)
        d.arc([x, y, x + s, y + s], 300, 60, fill=col, width=4)
        d.line([x + s * 0.5, y + s * 0.5, x + s * 0.9, y + s * 0.15], fill=col, width=4)
        d.point([x + s * 0.5, y + s * 0.5], fill=col)
    elif kind == "summit":
        for i, dx in enumerate([0.12, 0.42, 0.72]):
            d.ellipse([x + s * dx, y + s * 0.25, x + s * (dx + 0.16), y + s * 0.41],
                      fill=col)
        d.line([x + s * 0.2, y + s * 0.6, x + s * 0.8, y + s * 0.6], fill=col, width=5)
        d.line([x + s * 0.2, y + s * 0.72, x + s * 0.8, y + s * 0.72], fill=col, width=5)
    elif kind == "ship":
        d.polygon([(x, y + s * 0.55), (x + s, y + s * 0.55), (x + s * 0.85, y + s * 0.85),
                   (x + s * 0.15, y + s * 0.85)], fill=col)
        d.rectangle([x + s * 0.4, y + s * 0.3, x + s * 0.6, y + s * 0.55], fill=col)
        d.line([x + s * 0.5, y + s * 0.1, x + s * 0.5, y + s * 0.3], fill=col, width=4)
    elif kind == "pin":
        d.ellipse([x + s * 0.2, y + s * 0.1, x + s * 0.8, y + s * 0.6], fill=col)
        d.polygon([(x + s * 0.28, y + s * 0.45), (x + s * 0.72, y + s * 0.45),
                   (x + s * 0.5, y + s * 0.9)], fill=col)
        d.ellipse([x + s * 0.38, y + s * 0.22, x + s * 0.62, y + s * 0.46], fill=(255, 255, 255))
    elif kind == "bank":
        d.polygon([(x, y + s * 0.35), (x + s * 0.5, y + s * 0.05),
                   (x + s, y + s * 0.35)], fill=col)
        for dx in [0.08, 0.32, 0.56, 0.8]:
            d.rectangle([x + s * dx, y + s * 0.42, x + s * (dx + 0.12), y + s * 0.78], fill=col)
        d.rectangle([x, y + s * 0.82, x + s, y + s * 0.92], fill=col)

# ---- grid of cards: 2 cols x 3 rows ----
mx, my = 28, 178
gap = 18
cw = (W - 2 * mx - gap) // 2
ch = 234
for i, (tag, col, head, body, kind) in enumerate(stories):
    r, c = divmod(i, 2)
    x0 = mx + c * (cw + gap)
    y0 = my + r * (ch + gap)
    d.rounded_rectangle([x0, y0, x0 + cw, y0 + ch], radius=14, fill=CARD,
                        outline=(210, 205, 195), width=2)
    d.rectangle([x0, y0 + 14, x0 + 9, y0 + ch - 14], fill=col)
    icon(kind, x0 + cw - 56, y0 + 14, 40, col)
    d.text((x0 + 24, y0 + 16), tag, font=F_TAG, fill=col)
    hl = wrap(d, head, F_HEAD, cw - 112)
    yy = y0 + 48
    for line in hl[:2]:
        d.text((x0 + 24, yy), line, font=F_HEAD, fill=INK)
        yy += 38
    bl = wrap(d, body, F_BODY, cw - 48)
    yy += 6
    for line in bl[:3]:
        d.text((x0 + 24, yy), line, font=F_BODY, fill=GREY)
        yy += 30

# ---- footer ----
fy = H - 100
d.rectangle([0, fy, W, H], fill=NAVY)
d.text((28, fy + 10),
       "ALSO TODAY:  Japan scrambles jets after suspected Russian airspace violation  ·  ",
       font=F_TICK, fill=(255, 255, 255))
d.text((28, fy + 38),
       "NASA\u2019s Voyager 1 nears one light-day from Earth.",
       font=F_TICK, fill=(255, 255, 255))
d.text((28, fy + 66),
       "Sources: Reuters · AP · Al Jazeera · CNN · BBC — events of 17 Nov 2026, as reported.",
       font=F_SRC, fill=(180, 185, 200))

img.save("/home/hatch/workspace/makefun/entries/news-image-20261117/entry.png",
         optimize=True)
print("saved")
