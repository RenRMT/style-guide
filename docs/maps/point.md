---
title: Point maps
parent: Maps
nav_order: 4
---

# Point maps

Use point maps when the exact position of discrete events or values matters, not for continuous surfaces.

## Choosing a visual variable

| To show… | Use |
|:--|:--|
| Quantities | **Size** |
| Categories | **Colour** (or a small number of shapes) |
| Intensity or density | Transparency, clustering or binning |

{: .rule }
Use one primary variable. Use colour *or* size for meaning, and use other variables only to make the map legible. Combine size and colour only when both are equally important.

## Dot map

**Up to about 50 dots.** Each dot is one event. Use it when the precise location matters, such as distance to a town, border or route.

- **Avoid** with too many points, or when you need to show amounts or types (use proportional circles or colour).
- Choose a dot size that stays visible without merging.
- Don't use a legend, because the title explains what a dot is.
- Avoid insets on dot maps.
- For *dot density* maps, where each dot is a fixed amount placed at random within an area, state clearly that dots aren't exact locations.

## Circles by colour

**Up to 4 classes, plus "Other".** Each circle is one event, coloured by type: actor, kind of incident.

- **Avoid** with too many points, or when amount matters more than type.
- Follow the [contrasting order](../../colour/categorical/#two-orders), with Steel for "Other".
- Use transparency where points overlap.

## Proportional circles

**No fixed maximum.** Circle size shows an amount at a location. This is how to show counts where points overlap: group them into one circle.

- **Avoid** when the range of values is too small, such as only 1 and 2.
- **Scale by area, not radius.**
- Always include a size legend, because readers judge sizes poorly.
- Use transparency, or draw the larger circles first, so that smaller ones stay visible.

## Circles by size and colour

**At most 6 legend entries.** Use it when type and amount are equally important, and no simpler map (or pair of maps) works.

- Works best when comparing two classes, such as two actors.
- **Avoid** if the legend would need more than about 6–8 entries, or if the map also needs roads, lakes and areas of control.
- Make sure the size steps are clearly different.

## Annotated map

**Up to 7 callouts, of at most 40 words each.** Text boxes give context for selected points. Use it when readers need to know why particular points matter.

- **Avoid** with many callouts or a complicated legend.
- Write in headline style: short, and with the most important words first.
- Give the boxes slight transparency, and keep their leader lines short.

## Overplotting

When points pile up, try these in order:

1. Transparency
2. Jittering, if exact positions aren't critical
3. Cluster markers, for interactive maps
4. Switching to a [hexbin map](../area/#hexbin-map)

Test interactive maps at several zoom levels, and check that the symbols stay clear and meaningful at each one.
