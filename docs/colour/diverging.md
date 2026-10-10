---
title: Diverging
parent: Colour
nav_order: 3
---

# Diverging ramps

Use a diverging ramp for data on either side of a meaningful midpoint:

- good – bad
- decrease – increase
- below – above average
- more X – more Y

To build one, put two [sequential ramps](../sequential/) back to back, with a neutral centre (`#F9F9F9`) in between. Each side uses the same step set as a sequential ramp, mirrored.

## Recommended pairs

These pairs have similar lightness at each step, so neither side looks heavier. They also stay distinct for red-green colour blindness.

**Baltic – Cherry.** The default for good–bad and decrease–increase.

{% include diverging.html left="Baltic" right="Cherry" steps="2,4,6" %}

**Teal – Violet**

{% include diverging.html left="Teal" right="Violet" steps="2,4,6" %}

**Sky – Coral.** Softer, and suits fills on large areas. It uses steps 4, 6 and 8, because the standard steps are too pale for these ramps.

{% include diverging.html left="Sky" right="Coral" steps="4,6,8" %}

## Rules

{: .rule }
Use an odd number of classes when the midpoint is a class of its own, such as "no change". Use an even number when no value is truly neutral. Use at most nine classes: perception becomes unreliable beyond that.

{: .rule }
On a white background, use Light Grey or Neutral for the centre. If the centre needs to stand out from the page, use Platinum.

{: .avoid }
Don't use pairs that collapse for colour-blind readers: **Teal – Cherry** (the classic red–green) and **Baltic – Violet**. Also avoid pairs with very different lightness, such as Teal – Jasmine, where one side looks faded next to the other.

{: .adapt }
To test your own pair, simulate deuteranopia and protanopia in [Viz Palette](https://projects.susielu.com/viz-palette) or [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/), and check that the two ends stay clearly different and that equal steps look equally far from the centre.
