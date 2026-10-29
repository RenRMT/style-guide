---
title: Typography research
parent: Background
nav_order: 5
---

# Typography research

## Serif or sans-serif?

Sans-serif typefaces are generally considered more legible at small sizes and on screens. There is a long-standing belief that serif typefaces read better in print, but little evidence supports it. Choosing a sans-serif for screen use therefore doesn't make printed visuals less legible.

## Comparing the Windows sans-serifs

Of the five sans-serifs on most Windows machines, all meet the availability and legibility criteria, but only Aptos and Calibri also meet the [number criteria](../../typography/#choosing-a-typeface).

| | Aptos | Calibri |
|:--|:--|:--|
| Weights | Light, regular, semibold, bold and more | Light, regular and bold |
| Width | Wider | Narrower, so more text fits without shrinking it |
| Office default | Current default | Default until 2023 |

Calibri wins when space is tight, and when consistency with an existing brand that uses it matters. Aptos wins on its range of weights.

## Figures for numbers

Charts display numbers more than ordinary text does. Three properties matter:

- **Lining figures** sit on the baseline and share one height, so labels look even.
- **Tabular figures** all have the same width, so columns of numbers line up.
- **Multiplexed** typefaces keep digits the same width across weights, so bolding a label doesn't reflow the layout.

In CSS, `font-variant-numeric: tabular-nums lining-nums;` turns on the first two in fonts that support them.

---

Sources: Datawrapper, *Fonts for data visualization*; data.europa.eu, *Serif vs sans serif*. See [references](../references/).
