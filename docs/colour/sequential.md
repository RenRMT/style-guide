---
title: Sequential
parent: Colour
nav_order: 2
---

# Sequential ramps

Use a single-colour ramp for quantitative differences in one measure, such as rates or densities, and for ordered categories, such as "low – medium – high". To use one with continuous data, bin the data first. Light means low and dark means high.

Every data colour has a ten-step ramp. Step 6 is the base colour.

{% include ramp.html colour="Teal" %}

## Which steps

Don't pick shades by eye. Use these fixed step sets, which are the same ones the [colour picker](https://rendata.nl/color-picker/) uses:

| Steps needed | Use steps |
|:--|:--|
| 2 | 2, 6 |
| 3 | 2, 4, 6 |
| 4 | 2, 3, 4, 6 |
| 5 | 2, 3, 4, 5, 6 |
| 6 | 2, 3, 4, 5, 6, 7 |
| 7 | 2, 3, 4, 5, 6, 7, 8 |

For example, Teal with three and five steps:

{% include ramp.html colour="Teal" steps="2,4,6" %}
{% include ramp.html colour="Teal" steps="2,3,4,5,6" %}

{: .rule }
Use five or six steps at most. Seven is the practical ceiling: beyond that, readers can't reliably match a shade to its legend entry.

## Which ramps

Use the ramps of the four dark data colours: Teal (default), Baltic, Cherry and Violet. Their base colours sit in the middle of the lightness range, so their steps spread evenly from light to dark.

{% include ramp.html colour="Baltic" steps="2,3,4,5,6" %}
{% include ramp.html colour="Cherry" steps="2,3,4,5,6" %}
{% include ramp.html colour="Violet" steps="2,3,4,5,6" %}

{: .avoid }
Jasmine, Coral, Sky and Blush have light base colours, so steps 1–6 of their ramps all look pale and the standard step sets barely differ. If you use these ramps, shift the steps into the dark half (for example 4, 6, 7 and 8) and check that every class is distinguishable.

{: .avoid }
Don't put two ramps with similar hues in one visual: Teal and Sky, or Baltic and Violet.

{: .why }
For how many steps people can tell apart, see [Colour research](../../background/colour-research/).
