---
title: Categorical
parent: Colour
nav_order: 1
---

# Categorical colours

Use categorical colours for categories with no inherent order, such as actor type, incident type or region. Use [sequential](../sequential/) or [diverging](../diverging/) colours when the categories *are* ordered, for example "low – medium – high".

## Two orders

There are eight data colours. Add them in one of two fixed orders: take as many as you need, from left to right, and stick to one order per product.

**Contrasting order.** The default. Each new colour contrasts as much as possible with the colours before it.

{% include swatches.html group="contrasting-order" numbered="yes" %}

**Rainbow order.** Neighbouring colours blend into a smooth gradient, which some designs find calmer. Use it when that look matters more than maximum contrast.

{% include swatches.html group="rainbow-order" numbered="yes" %}

Steel (`#B8B8B8`) can be added to either order, for "Other", "Unknown" or context data.

## How many colours

| Categories | What to do |
|:--|:--|
| 1 | Teal. Use Steel for anything that is context. |
| 2–5 | The first colours of the contrasting order. All five stay distinguishable for the common forms of colour blindness. |
| 6–8 | Possible, but label directly or add shapes. From the sixth colour on, some pairs become hard to tell apart for colour-blind readers: Teal and Cherry (protanopia), and Baltic and Violet (deuteranopia). |
| More than 8 | Don't. Group the smallest categories into "Other", split into small multiples, or highlight one category against Steel. |

{: .rule }
Use the highlight pattern. To make one category the story, colour it Teal and everything else Steel. This is the most effective use of colour in this guide.

## Lines and small marks

Jasmine, Coral, Sky and Blush are light. They work well as fills for bars, areas and map polygons, but lines, small dots and text in these colours almost disappear on a white background. Their contrast with white is between 1.3:1 and 2.1:1.

{: .rule }
For lines, small points and coloured text, use the dark colours first: Teal, Baltic and Cherry. Use Violet only when Baltic isn't also on the chart.

{: .why }
For how the palette was derived and tested, see [Colour research](../../background/colour-research/).
