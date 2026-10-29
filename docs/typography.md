---
title: Typography
nav_order: 5
---

# Typography

## House typefaces

| Where | Typeface | Notes |
|:--|:--|:--|
| Office (Excel, PowerPoint, Word) | **Calibri**, or **Aptos** to match the Office default | Both are installed on every Windows machine and have the right figures for numbers (see below). Calibri is narrower, so more text fits without shrinking it. |
| Web and code (D3, Plotly, ggplot, matplotlib) | **IBM Plex Sans** | Open source, with many weights. Turn on tabular figures (`font-variant-numeric: tabular-nums` in CSS). |

Use one typeface per visual. Create hierarchy with weight and size, not with a second font.

## Sizes and weights

| Element | Weight | Relative size | Minimum in print |
|:--|:--|:--|:--|
| Title | Bold or semibold | Largest, about 1.5× body | 12 pt |
| Subtitle | Regular | About 1.15× body | 10 pt |
| Labels, axis values, legend | Regular | Body | 9 pt |
| Source, notes | Regular | About 0.85× body | 7 pt |
| Big number value | Bold | As large as the space allows | |

{: .rule }
Use sentence case and left alignment for the title, subtitle, source and note. Don't use all caps except for short labels, and don't use italics for emphasis.

{: .rule }
Text is horizontal. Rotated text is a last resort, after you've tried a horizontal bar chart, fewer labels, and abbreviations.

## Choosing a typeface

A typeface for your own guide needs three properties:

1. **Available:** installed on, or easy to install on, every device and tool your team uses.
2. **Legible:** clear at small sizes, on screen and in print. Sans-serif is the safe choice.
3. **Several weights:** at least regular and bold, ideally light and semibold too, so you can emphasise the message and de-emphasise supporting text.

And it needs these properties for numbers:

| Property | What it means | Why it matters |
|:--|:--|:--|
| Lining figures | All digits sit on the baseline at the same height. | Numbers in labels look even. |
| Tabular figures | All digits are the same width. | Columns of numbers line up. |
| Multiplexed weights | Digits stay the same width across weights. | Bolding a highlighted label doesn't shift the layout. |

Of the common Windows sans-serifs (Aptos, Arial, Calibri, Segoe UI and Verdana), only Aptos and Calibri meet all three number criteria.

{: .adapt }
If your brand already has a typeface, check it against these criteria before adopting it for charts. Many display typefaces have old-style or proportional figures, which make tables and axis labels look ragged.

{: .why }
Sans-serif is the safe choice: it is generally more legible at small sizes and on screen, and there is little evidence that serifs read better in print. See [Typography research](../background/typography-research/).
