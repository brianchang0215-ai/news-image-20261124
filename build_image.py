#!/usr/bin/env python3
"""Build the 24 Nov 2026 front-page image. Local build tool only;
the entry program itself (main.py) only copies entry.png."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
DARKRED = (122, 20, 20)
BLUE = (24, 68, 128)
TEAL = (14, 90, 86)
GREY = (92, 92, 88)
LINE = (180, 172, 152)
CARD = (255, 253, 247)

FDIR = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FDIR + name, size)

serif_b = F("DejaVuSerif-Bold.ttf", 42)
serif = F("DejaVuSerif.ttf", 15)
sans_b = F("DejaVuSans-Bold.ttf", 14)
sans = F("DejaVuSans.ttf", 11)
sans_b13 = F("DejaVuSans-Bold.ttf", 13)
sans_b11 = F("DejaVuSans-Bold.ttf", 11)
sans10 = F("DejaVuSans.ttf", 10)
tag_f = F("DejaVuSans-Bold.ttf", 9)
hero_h = F("DejaVuSans-Bold.ttf", 27)
hero_d = F("DejaVuSans.ttf", 14)
hero_tag = F("DejaVuSans-Bold.ttf", 11)

def wrap(draw, text, font, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(draw, x, y, text, font, width, fill, lh, max_lines=None):
    lines = wrap(draw, text, font, width)
    if max_lines:
        lines = lines[:max_lines]
    for i, ln in enumerate(lines):
        draw.text((x, y + i * lh), ln, font=font, fill=fill)
    return len(lines)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 6], fill=RED)
d.text((24, 16), "THE WORLD IN ONE PAGE", font=serif_b, fill=INK)
d.text((24, 66), "TUESDAY 24 NOVEMBER 2026  •  36 STORIES  •  7 REGIONS", font=F("DejaVuSans-Bold.ttf", 13), fill=RED)
d.text((1000, 20), "REPORTED 23–24 NOV 2026", font=sans_b11, fill=GREY, anchor="ra")
d.text((1000, 38), "Claims are labelled as claims.", font=sans10, fill=GREY, anchor="ra")
d.line([24, 88, 1000, 88], fill=INK, width=2)

# ---- hero ----
hy, hh = 98, 164
hw = 482
# left hero
d.rectangle([24, hy, 24 + hw, hy + hh], fill=(253, 238, 232), outline=RED, width=2)
d.text((38, hy + 10), "MARKETS  •  TECH  —  LEAD STORY", font=hero_tag, fill=RED)
draw_wrapped(d, 38, hy + 30, "HUANG IS BACK —", hero_h, 300, INK, 30, 1)
draw_wrapped(d, 38, hy + 60, "MARKETS ROAR", hero_h, 300, INK, 30, 1)
draw_wrapped(d, 38, hy + 92, "Nvidia reinstates Jensen Huang as CEO after a Trump push; shares jump 31% in a day, restoring nearly $1 trillion.", hero_d, 300, INK, 17, 4)
# chart on right of left hero
cx, cy = 350, hy + 26
bars = [18, 26, 22, 34, 30, 52, 78]
for i, b in enumerate(bars):
    x0 = cx + i * 20
    d.rectangle([x0, cy + 84 - b, x0 + 14, cy + 84], fill=(46, 125, 50))
d.line([cx - 6, cy + 84, cx + 146, cy + 84], fill=INK, width=2)
d.polygon([(cx + 132, cy - 4), (cx + 152, cy + 8), (cx + 132, cy + 20)], fill=(46, 125, 50))
d.text((cx, cy + 92), "+31%  NVIDIA", font=sans_b11, fill=(46, 125, 50))
d.text((cx, cy + 108), "Kospi +7.5%  •  Taiwan +9.1%", font=sans10, fill=INK)
d.text((cx, cy + 122), "Nikkei +4.5%  •  Brent $89", font=sans10, fill=INK)

# right hero
rx = 518
d.rectangle([rx, hy, rx + hw, hy + hh], fill=(232, 240, 250), outline=BLUE, width=2)
d.text((rx + 14, hy + 10), "UKRAINE  •  PEACE TALKS", font=hero_tag, fill=BLUE)
draw_wrapped(d, rx + 14, hy + 30, "ZELENSKY: FOUR-WAY", F("DejaVuSans-Bold.ttf", 24), 454, INK, 28, 1)
draw_wrapped(d, rx + 14, hy + 58, "TALKS 'AS SOON AS POSSIBLE'", F("DejaVuSans-Bold.ttf", 24), 454, INK, 28, 1)
draw_wrapped(d, rx + 14, hy + 92, "Kyiv urges a Ukraine–Europe–US–Russia meeting, ready 'literally tomorrow'. Envoys head to Moscow; EU readies 22nd sanctions.", hero_d, 454, INK, 17, 3)
# chips
for i, lab in enumerate(["UA", "EU", "US", "RU"]):
    x0 = rx + 14 + i * 52
    d.rounded_rectangle([x0, hy + 142, x0 + 44, hy + 160], radius=9, fill=BLUE)
    tw = d.textlength(lab, font=sans_b11)
    d.text((x0 + (44 - tw) / 2, hy + 145), lab, font=sans_b11, fill=(255, 255, 255))

# ---- grid: 20 cards, 4 x 5 ----
GRID = [
 ("CLIMATE", "COP31 ENDS WITH NO DEAL", "Antalya summit collapses after ~44 hours overtime; no fossil-fuel mention, EU-led revolt kills draft."),
 ("SPACE", "NUCLEAR SATELLITE WARNING", "Reports say Russia built 'Sputnik-S' to carry a warhead; NATO vows space defence. Kremlin dismisses it."),
 ("EUROPE", "MOSCOW: ESTONIA RISKS OPEN WAR", "Russia summons Estonian envoy, accuses it of letting Ukraine use its airspace. Estonia denies it."),
 ("UKRAINE", "UKRAINE SINKS RUSSIAN CORVETTE OFF LIBYA", "Zelensky: seven sea drones hit the Merkury in Benghazi port; MV Angara also struck."),
 ("BALTIC", "RUSSIAN CARGO SHIP HIT NEAR FINLAND", "Sparta II catches fire in the Gulf of Finland after a drone strike; Moscow warns of Baltic escalation."),
 ("UKRAINE", "KYIV REGION STRIKES KILL AT LEAST 15", "Five-storey block in Dymer hit; 11 killed there, rescuers search rubble, Ukraine says."),
 ("EUROPE", "EU'S 22ND SANCTIONS PACKAGE DUE", "Targets banks, crypto platforms and the shadow fleet; deal sought before the Christmas break."),
 ("UKRAINE", "LEAKED DATA: RUSSIAN DEAD NEAR 500,000", "Hacked records put the toll near 500,000, reports say; an earlier leak put it over 400,000."),
 ("MIDDLE EAST", "IRAN CLAIMS 3 TANKERS HIT MINES", "IRGC says tankers caught fire in the Strait of Hormuz under US escort. Claim unverified."),
 ("US • IRAN", "US WIDENS IRAN SANCTIONS", "Treasury targets dozens over shadow banking networks moving billions, stepping up isolation."),
 ("MIDDLE EAST", "DRONE DOWNED, TALKS PUSHED", "Tehran says a US drone was downed near Hormuz; Qatar's PM meets Vance and Rubio on talks."),
 ("LEBANON", "BEIRUT STRIKE KILLS HEZBOLLAH COMMANDER", "Israeli strike kills Haytham Ali Tabtabai in southern suburbs, straining the ceasefire."),
 ("SYRIA", "HOMS UNREST AFTER KILLINGS", "Attack on a Sunni Bedouin couple sparks unrest; curfew imposed as forces deploy."),
 ("AFRICA", "SUDAN DRONES HIT HOMES, UN BUILDING", "Strikes hit Khartoum and Omdurman, killing children; 24 killed in South Sudan's Warrap."),
 ("HEALTH", "FIGHTING DISRUPTS EBOLA RESPONSE", "WHO pleads for peace in DR Congo's Ituri so an Ebola team can be evacuated safely."),
 ("GAZA", "DEATHS AT AID SITES REPORTED", "Six killed, 33 wounded in 24 hours, Gaza officials say; UNRWA worker among four killed."),
 ("AFRICA", "NIGERIA BOAT CAPSIZE: 24 DEAD", "Boat carrying mourners capsizes in Bayelsa; 24 rescued. Tinubu approves aid for families."),
 ("ASIA", "INDONESIA FACTORY FIRE: 24 DEAD", "Candy factory blaze in Banten kills 24; rescuers search for missing workers."),
 ("US", "DEMOCRATS: 258 SEATS, BIGGEST SINCE 1992", "Hubbard's North Carolina win seals the majority; Jeffries poised to be first Black Speaker."),
 ("US", "DEMOCRATS PLAN 12 DEBATES FOR 2028", "DNC sets a dozen primary debates, first in June, after sweeping midterms in House and Senate."),
]
gx, gy = 24, 268
cw, chh, gut = 236, 96, 8
for idx, (tag, head, deck) in enumerate(GRID):
    r, c = divmod(idx, 4)
    x0 = gx + c * (cw + gut)
    y0 = gy + r * (chh + gut)
    d.rectangle([x0, y0, x0 + cw, y0 + chh], fill=CARD, outline=LINE, width=1)
    d.text((x0 + 8, y0 + 6), tag, font=tag_f, fill=RED)
    draw_wrapped(d, x0 + 8, y0 + 19, head, sans_b13, cw - 16, INK, 15, 2)
    draw_wrapped(d, x0 + 8, y0 + 49, deck, sans10, cw - 16, (52, 52, 52), 12, 3)

# ---- also today: 14 one-liners, 7 x 2 ----
ay = 788
d.text((24, ay), "ALSO TODAY", font=F("DejaVuSans-Bold.ttf", 13), fill=INK)
d.line([130, ay + 8, 1000, ay + 8], fill=INK, width=1)
ALSO = [
 ("TRUMP", "Targets Newsom in DOJ speech; orders federal executions expedited."),
 ("GROK SUITS", "Virginia, Oregon sue SpaceX over sexualised images, incl. children."),
 ("AI RULES", "UN chief: AI risk framework within a year."),
 ("MEGASPEED", "US to blacklist Singapore firm in Nvidia chip scandal."),
 ("BRUSSELS", "Airport strike cancels 429 flights; 59,000 passengers hit."),
 ("GTA HACKER", "Arion Kurtaj gets 7 years; walks free on time served."),
 ("CONCERT", "Thousands evacuated in UK over 'unknown substance'."),
 ("ALCARAZ", "Beats Zverev 6–2, 7–6 for first ATP Finals title."),
 ("CHESS", "Gukesh begins world title defence v. Sindarov in Geneva."),
 ("CRICKET", "India–New Zealand first Test drawn at Wellington."),
 ("MOLLY MELDRUM", "Australian music icon dies aged 83."),
 ("FILM", "'Hunger Games: Sunrise on the Reaping' opens to $225m."),
 ("MERCURY", "BepiColombo probe enters orbit around Mercury."),
 ("NEPAL", "PM Shah in India for economy and energy talks."),
]
aw = 136
for idx, (lead, txt) in enumerate(ALSO):
    r, c = divmod(idx, 7)
    x0 = 24 + c * (aw + 4)
    y0 = ay + 20 + r * 74
    d.rectangle([x0, y0, x0 + aw, y0 + 68], fill=CARD, outline=LINE, width=1)
    d.text((x0 + 6, y0 + 5), lead, font=tag_f, fill=BLUE)
    draw_wrapped(d, x0 + 6, y0 + 18, txt, sans10, aw - 12, INK, 12, 4)

# ---- footer ----
fy = 958
d.line([24, fy, 1000, fy], fill=INK, width=1)
d.text((24, fy + 8), "Sources: Reuters, AP, Bloomberg, AFP, Al Jazeera, German media reports, IRNA via JPost.  Unverified claims are labelled.", font=sans10, fill=GREY)
d.text((24, fy + 24), "A front-page summary of the news cycle on 24 November 2026. Built in Taipei on 24 Nov 2026. Programme copies this image; no network.", font=sans10, fill=GREY)

img.save("/home/hatch/workspace/makefun-news-image-20261124/entry.png", optimize=True)
print("saved", img.size)
