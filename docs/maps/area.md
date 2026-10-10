---
title: Area maps
parent: Maps
nav_order: 3
---

# Area maps

## Choropleth map

**At most 25 areas. 4–5 classes, plus "no data".** Use it to colour areas by a *relative* value, such as a rate, percentage, density or change.

- **The data must be normalised.** Show incidents per 100,000 people, not incident counts. Counts make large areas look important regardless of the actual values.
- **Avoid** for raw counts of events (use a [point map](../point/)), when there are very few or very many areas, and when you'd need to put other data on top.
- Use a [sequential ramp](../../colour/sequential/) for ordered values, and a [diverging ramp](../../colour/diverging/) for values around a meaningful midpoint, such as an average or zero.
- Make "no data" clearly different from the lowest class. Use white or Platinum with a hatch, never the lightest ramp step.
- When admin areas vary greatly in size, or don't match the pattern, use a [hexbin map](#hexbin-map).

### Choosing classes

Look at the histogram of your values first.

| Histogram shape | Classification | Why |
|:--|:--|:--|
| Clusters and gaps | **Natural breaks** (Jenks) | Puts the breaks in the gaps. A good default. |
| Skewed, with a long tail | **Quantiles** | An equal number of areas per class, so no classes are empty. |
| Evenly spread, or a fixed scale such as 0–100% | **Equal interval** | Intuitive, round class ranges. |
| Bell-shaped | **Standard deviation** | Shows deviation from the average, and outliers. |

- **Comparing several maps?** Use the same breaks on all of them, either quantiles or manual breaks.
- **Extreme outliers?** Avoid equal interval. Use natural breaks or quantiles.
- Round the class boundaries to readable numbers.
- Don't tune the breaks to make the map say what you want.

{: .rule }
Use 4–5 classes by default and never more than 7. Beyond that, readers can't match shades to the legend.

## Hexbin map

A choropleth on a grid of equal hexagons instead of admin areas. Use it when the whole area is evenly relevant, there are many overlapping points, and the exact locations don't matter. It's a good replacement for a heatmap.

- Choose a hexagon size that suits the map scale and the density of the data, and state it in the subtitle or a note: "Hexagons of 50 km²".
- Follow the choropleth rules: at most 4–5 classes plus "no data", and a distinct "no data" or "no incidents" style.
- If admin areas tell the story, use a choropleth instead.

## Chorochromatic and areas of control maps

Use these to colour areas by **type**, not amount: who controls an area, access conditions, land use. Use [categorical colours](../../colour/categorical/), which carry no order. Never use a ramp.

- Keep the number of categories small, and make sure they don't overlap. If they do overlap, show it with a pattern or a separate colour.
- **Areas of control:** use custom polygons drawn to the real extent, not admin areas, unless control really follows admin boundaries. Use about 50% transparency so the basemap shows through.
- You may use colours already assigned to actors, as long as they stay distinguishable.
- Avoid putting other data on top.
