---
title: Distribution
parent: Charts
nav_order: 7
---

# Distribution charts

Distribution charts show how values are spread, grouped and distributed, rather than just totals or averages.

| Chart | Shows | Best for |
|:--|:--|:--|
| Histogram | Counts per value range (bin) | The overall shape of one continuous variable |
| Density plot | A smoothed histogram | Comparing the shapes of two or three groups |
| Box plot | Median, quartiles and outliers | Comparing many groups compactly |
| Violin plot | A box plot with density shape | Many groups, when shape matters |

<div class="figure">
<img src="{{ '/assets/examples/histogram.svg' | relative_url }}" alt="Histogram of households by distance to the nearest health facility, in 2 km bins">
</div>

<div class="figure">
<img src="{{ '/assets/examples/box-plot.svg' | relative_url }}" alt="Box plots of clinic waiting times for four regions, sorted by median">
</div>

- **Avoid** for audiences unfamiliar with statistical charts (for them, describe the distribution in words or use a simple histogram), for very small datasets, and when exact values matter more than patterns.
- **Bin sizes:** with too many bins, a histogram shows noise. With too few, it hides patterns. Try several sizes, and pick round-number bin edges.
- **Outliers:** decide deliberately whether to explain, transform or show them separately. Don't just let the axis stretch.
- These charts work only with continuous numeric data.
- A histogram is also the quickest way to choose [map classes](../../maps/area/#choosing-classes).
