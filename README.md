[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/brianchang0215-ai/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/brianchang0215-ai/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

# The World in One Page — Tuesday 24 November 2026

A make.fun entry for [Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124).

One front-page image summarising the news cycle reported on 23–24 November 2026:
36 stories across 7 regions, led by Jensen Huang's return as Nvidia CEO and the
market rebound, and Zelenskyy's call for four-way Ukraine peace talks. Claims
that were unverified at the time of writing are labelled as claims on the image.

## Run

```sh
python3 main.py
```

`main.py` uses only the Python standard library, uses no network, and decodes
the bundled `entry.png.b64` (the base64 form of the PNG) to write
`/output/entry.png` (falling back to `output/entry.png` beside the script if
`/output` cannot be created). Running it twice writes identical bytes both
times.

## Files

- `main.py` — the entry program (Python 3.13, at the repository root).
- `entry.png.b64` — the image in base64 form: a 1024 × 1024 PNG, under 1 MiB
  once decoded. Stored as text so the repository holds only UTF-8 files.
- `build_image.py` — the local build script that drew the PNG (Pillow +
  DejaVu fonts, run locally on 24 November 2026) before it was stored as
  base64. It is documentation of how the image was made; the entry program
  does not run it.
- `LICENSE` — MIT.

## Sources checked

Reuters, AP, Bloomberg (via Swissinfo), AFP, Al Jazeera, German media reports
(NDR/WDR/Süddeutsche Zeitung), and IRNA via The Jerusalem Post. Each story on
the image was checked against reporting dated 23–24 November 2026; figures
that differed between sources are either given with attribution or omitted.
