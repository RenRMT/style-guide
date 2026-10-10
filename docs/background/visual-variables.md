---
title: Visual variables
parent: Background
nav_order: 2
---

# Visual variables

Visual variables are the basic ways a symbol can vary to carry information. Jacques Bertin introduced them, and cartographers and visualisation researchers have extended the idea since. Each variable suits some kinds of data better than others. Choosing the right variable for your data is the core of good chart and map design.

A variable can be:

- **selective:** it lets you tell categories apart
- **associative:** symbols that share it are seen as belonging together
- **ordered:** it shows a sequence, from low to high
- **quantitative:** it lets you estimate the size of a difference, not just its direction

| Variable | Selective | Associative | Ordered | Quantitative | Typical use |
|:--|:-:|:-:|:-:|:-:|:--|
| Position | ✔ | ✔ | ✔ | ✔ | Where things are, and values on an axis. The strongest variable. |
| Size | ✔ | | ✔ | ✔ | Proportional symbols. Readers misjudge area, so add a legend. |
| Colour lightness (value) | ✔ | | ✔ | ✔ | Sequential ramps, choropleths |
| Colour hue | ✔ | ✔ | | | Categories. Implies no order. |
| Shape | | ✔ | | | Point categories, but only a few shapes are easy to tell apart. |
| Orientation | ✔ | ✔ | | | Direction, special cases |
| Texture or pattern | ✔ | ✔ | ✔ | | When colour isn't available, or to show overlap |
| Saturation | | | (✔) | | Emphasis, uncertainty. Easily confused. |
| Transparency | | | (✔) | | Overlapping points, density, uncertainty |
| Arrangement or spacing | | | (✔) | | Dot density patterns |

## What this means in practice

- Use **position** for whatever matters most. That's why bar and dot charts beat pies and bubbles.
- Use **lightness**, not hue, for quantities. A rainbow ramp has no natural order.
- Use **hue** for categories, never for amounts.
- Use **size** for amounts at locations, and always with a size legend.

---

Sources: Axis Maps, *Cartography Guide: Visual Variables*; UCGIS GIS&T Body of Knowledge, *CV-03-008*; Penn State GEOG 486.
