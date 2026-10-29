---
title: Colour
nav_order: 4
has_children: true
---

# Colour

The guide uses two separate sets of colours:

- **Brand colours** for text, titles and page elements. They tie a visual to the product it sits in.
- **Data colours** for the data itself: bars, lines, areas, points and map fills. They come in three forms:
  - [Categorical](categorical/), for categories without an order
  - [Sequential](sequential/), for ordered values
  - [Diverging](diverging/), for values on either side of a meaningful midpoint

Brand colours are too few and too similar to encode data, so the data colours were built separately to meet those needs.

All colours are also in the [interactive colour picker](https://rendata.nl/color-picker/), which lets you copy hex codes, build ramps and export CSS variables.

## Brand colours

{% include swatches.html group="corporate-brand" %}

## Neutral shades

{% include swatches.html group="neutral-shades" %}

## Which colour for which element

| Element | Colour |
|:--|:--|
| Title | Black, or Dark Teal for a branded header |
| Subtitle, labels, axis values, source and notes | Black |
| Background | White, or Light Grey for panels and cards |
| Gridlines | Platinum |
| Axis lines and tick marks, where used | Steel |
| Data that isn't the focus ("other", context, "no data") | Steel |
| Data | [Data colours](categorical/), starting with Teal |
| Text on a coloured fill | Black or white, whichever the swatch shows |

## Rules for every visual

{: .rule }
Use as few colours as possible. Start with one colour, plus Steel for everything that isn't the story. Add colours only for real categories.

{: .rule }
Never rely on colour alone. Label directly, or add position, shape or line style, so that the visual still works in greyscale, in black-and-white print and for colour-blind readers. Roughly 1 in 12 men has some form of colour-vision deficiency.

{: .rule }
Be consistent within a product. The same category always gets the same colour, and colours are always added in the [colour order](categorical/#colour-order).

{: .avoid }
Don't use red and green as the only positive/negative signal. If you have to, use them sparingly (an up or down arrow on a [big number](../big-numbers/), say) and always pair them with a + or − sign.

{: .adapt }
Building your own palette? See [Build your own palette](build-your-own/). It starts from the colour-blind-safe Okabe–Ito palette, which you then shift towards your brand.
