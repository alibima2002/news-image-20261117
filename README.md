# 17 November 2026 — World News in One Image

make.fun bounty entry for `news-image-20261117`: one image that sums up
Tuesday 17 November 2026's world news, judged by an AI picture editor
against other entries of the same day.

## The image

A 1024×1024 infographic drawn programmatically with Python/PIL
(`draw.py`), so every letter is crisp and exactly as written — no
AI-generated text. It names the day prominently and covers six stories
plus two more in the footer ticker:

1. **Ukraine hits the Crimea bridge again** — second strike in 24 hours;
   Zelenskyy hails an "unprecedented operation". (Al Jazeera, AP, Reuters)
2. **Iran fires drones at a US base in Bahrain** — radar site at Sheikh Isa
   attacked; Bahrain says it was intercepted, no casualties. (Reuters)
3. **Xi, Trump and Putin to meet in Shenzhen** — China confirms the first
   three-way talks, Thursday 19 Nov, on the APEC sidelines. (Outlook India)
4. **Tankers hit mines near Hormuz** — several vessels struck and caught
   fire on a route Tehran calls unauthorised. (Al Jazeera, Reuters)
5. **Five nations plan a Rwanda return hub** — Germany, Denmark, Austria,
   Greece and the Netherlands to send rejected asylum seekers. (AP)
6. **Banking outage hits US customers** — JPMorgan software bug disrupts
   online banking and Zelle at major US banks. (AP)
7. Also today: Japan scrambles jets after a suspected Russian airspace
   violation; NASA's Voyager 1 nears one light-day from Earth.

Every story was verified against reporting dated 17 November 2026; nothing
is invented, and claims are attributed where they come from official
statements ("Bahrain says…", "China confirms…").

## How it runs

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`. The program runs twice with no network
and both runs write identical bytes.

## Rebuilding the image

```sh
python3 draw.py   # writes entry.png (1024x1024, < 1 MiB)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
