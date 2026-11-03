---
title: Area maps
parent: Maps
nav_order: 4
---

# Area maps

## Choropleth map

{: .meta }
At most 25 areas · 4–5 classes, plus "no data"

Use it to colour areas by a *relative* value, such as a rate, percentage, density or change.

<div class="figure">
<img src="{{ '/assets/examples/map-choropleth.svg' | relative_url }}" alt="Dutch provinces shaded in four teal classes by share of people in need, with Groningen labelled 46%">
</div>

- The data must be normalised. Show incidents per 100,000 people, not incident counts. Counts make large areas look important regardless of the actual values.
- Avoid it for raw counts of events (use a [point map](../point/)), when there are very few or very many areas, and when you'd need to put other data on top.
- Draw the borders between filled areas in white, so the fills stay clean. Neighbouring countries keep the context land tone.
- Label the area the title talks about with its value.
- When admin areas vary greatly in size, or don't match the pattern, use a [hexbin map](#hexbin-map).
- Map at the level the data represents. If a survey is representative by province, don't shade districts.
- Use one representation per measure. Don't show the same measure as fills for rural areas and dots for towns on one map: make two maps with the same style.

### Colour scales

Use the Teal ramp for ordered values. Maps use their own fixed step sets instead of the [chart steps](../../colour/sequential/#which-steps). They start at Teal 3, so the lightest class never reads as sea or empty land, and run to Teal 10, so neighbouring areas still differ: 3, 6, 8, 10 for four classes and 3, 5, 6, 8, 10 for five.

{% include ramp.html colour="Teal" steps="3,5,6,8,10" %}

Use a diverging ramp only when the data has a meaningful midpoint, such as change from last year. On maps, use the Baltic–Cherry pair from step 3, for the same reason.

{% include diverging.html left="Baltic" right="Cherry" steps="3,7" %}

For areas with no data, use a hatch of `#EAE6DD` on `#F8F5EF` at 135°, the same pattern used everywhere else. Never use the lightest ramp step.

<div class="swatches"><div class="swatch" style="background:repeating-linear-gradient(135deg,#EAE6DD 0 2px,#F8F5EF 2px 6px);color:#191919"><span class="swatch__name">No data</span><code class="swatch__hex">#EAE6DD on #F8F5EF</code></div></div>

See [Sequential](../../colour/sequential/) and [Diverging](../../colour/diverging/) for how the ramps are built.

### Choosing classes

Look at the histogram of your values first.

| Histogram shape | Classification | Why |
|:--|:--|:--|
| Clusters and gaps | Natural breaks (Jenks) | Puts the breaks in the gaps. A good default. |
| Skewed, with a long tail | Quantiles | An equal number of areas per class, so no classes are empty. |
| Evenly spread, or a fixed scale such as 0–100% | Equal interval | Intuitive, round class ranges. |
| Bell-shaped | Standard deviation | Shows deviation from the average, and outliers. |

Quantiles fill every class, but they can put very different values in one class and split near-identical values across two. Check the class ranges in the key before you publish. They remain a good choice for maps compared in a series, where readers found them the easiest to read (Brewer & Pickle 2002).

- Comparing several maps? Use the same breaks on all of them: set them by hand, or calculate them once from all the maps' values together.
- Extreme outliers? Avoid equal interval. Use natural breaks or quantiles.
- Round the class boundaries to readable numbers.
- Don't tune the breaks to make the map say what you want. Very narrow classes, such as 83–85% and 86–88%, suggest differences the data may not support.
- Make every class a closed range that doesn't overlap the next: "1–20%, 21–40%", not "0–30%, 30–60%" or "≤20%, ≤40%". Only the top class may be open: "More than 80%".
- When zero is meaningful, such as "no incidents", give it its own class.
- When there is a real gap in the values, show it: leave an empty class in the key, or split the range so that one class doesn't stretch across the gap.
- Comparing several maps? Use the same colours for the same ranges, as well as the same breaks.
- Classify by default. An unclassed ramp hides the differences between areas, so keep it for truly continuous fields, such as rainfall or elevation.

{: .rule }
Use 4–5 classes by default, never more than 7 and never fewer than 3. Beyond 7, readers can't match shades to the key. With 2, random patterns start to look meaningful.

## Hexbin map

A choropleth on a grid of equal hexagons instead of admin areas. Use it when the whole area is evenly relevant, there are many overlapping points, and the exact locations don't matter. It's a good replacement for a smoothed density heatmap.

<div class="figure">
<img src="{{ '/assets/examples/map-hexbin.svg' | relative_url }}" alt="Hexagon grid over the Netherlands shaded in four teal classes by number of incidents, darkest around Amsterdam and Rotterdam, with empty hexagons outlined in grey">
</div>

- Choose a hexagon size that suits the map scale and the density of the data, and state it in the subtitle or a note: "Hexagons of 50 km²".
- Follow the choropleth rules: at most 4–5 classes plus "no data", and a distinct "no data" or "no incidents" style.
- Hexagons work well for counts, such as the number of camps, because every cell has the same area.
- Be careful with rates. A cell that holds only two or three settlements, or a small sample, swings between classes on tiny differences. Use larger hexagons, or show counts instead.
- Keep borders, towns and main roads on top, so readers can still tell where they are.
- Make sure no cell reveals a single site or household. See [Sensitive data](../../planning/data/#sensitive-data).
- Use hexagons, not squares. They are closer to circles, so every neighbour is about equally far away, and patterns read more clearly.
- If admin areas tell the story, use a choropleth instead.

## Chorochromatic and areas of control maps

Use these to colour areas by *type*, not amount: who controls an area, access conditions, land use. Use the [map colour order](../basemap/#colour-on-maps), which carries no order of value. Never use a ramp.

<div class="figure">
<img src="{{ '/assets/examples/map-control.svg' | relative_url }}" alt="Areas of control: Group A in light teal across the north, Group B in light blue across the south, and a contested band hatched in both colours, with borders and rivers drawn on top">
</div>

- Keep the number of categories small, at most four, and make sure they don't overlap. If they do overlap, show it with a hatch or a separate colour.
- For areas of control, use custom polygons drawn to the real extent, not admin areas, unless control really follows admin boundaries. Fill them with a light step (2 or 3) of each category's ramp, rather than a transparent fill, so the colours stay exact and the basemap lines still show through on top.
- You may use colours already associated with specific actors, as long as they stay distinguishable.
- Avoid putting other data on top.

To point out an area without classifying it, use a [highlight area](../other/#highlight-areas) instead.

## Bivariate maps

A bivariate choropleth colours each area by two measures at once, on a grid of colours. It is hard to read, and it suggests a relationship between the two measures whether or not there is one.

{: .rule }
Show two measures as two maps side by side, with the same breaks and style. Use a bivariate map only when the relationship between the measures is the message and the data clearly supports it.

If you do use one:

- Use a 3 × 3 grid at most: three classes per measure.
- Give each measure a clearly different hue, so the grid mixes from light grey to two distinct colours. Two similar ramps, such as two reds, can't be told apart.
- Put the grid key next to the map, with each axis named.
- Remember that two measures rarely tell the whole story. Food insecurity, for example, depends on more than prices and access.

Simpler ways to combine two measures on one map:

| Combine | How |
|:--|:--|
| Size and colour | Proportional circles for one measure, coloured by class for the other |
| Size and shape | Proportional symbols in two shapes, such as circles and squares |

Even these need a careful key. When in doubt, use two maps.

{: .why }
In user tests, readers answered questions about two measures more accurately with combined symbols than with a colour grid. See Elmer (2013) in the [references](../../background/references/).

