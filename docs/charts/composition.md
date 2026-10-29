---
title: Composition
parent: Charts
nav_order: 5
---

# Composition (part-to-whole)

## Stacked bar and column chart

**Up to 7 bars, each with at most 5 segments.** Use it to show how totals divide into parts across categories, for both the overall size and the contribution of each part. A 100% stacked bar compares proportions, and is the best choice when the data is already in percentages.

<div class="figure">
<img src="{{ '/assets/examples/stacked-bar.svg' | relative_url }}" alt="100% stacked bar chart of household water sources in five regions">
</div>

- Use horizontal bars for categories you can sort, and vertical columns for a time sequence.
- **Avoid** when readers need to compare a segment's exact value across bars. Only the first segment shares a baseline, so use a clustered bar or small multiples instead.
- Label segments directly, so readers don't have to go back and forth to a legend.
- Keep the segment order the same in every bar, with the most important segment at the baseline.

## Pie and donut chart

**2–5 slices, at most 6.** Use it for part-to-whole proportions of a few categories, especially data that is naturally expressed as percentages. A donut chart has room in the middle for a total or key figure.

<div class="figure">
<img src="{{ '/assets/examples/donut.svg' | relative_url }}" alt="Donut chart of spending by sector with the total in the centre">
</div>

- **Avoid** when slices are similar in size (differences under about 5 percentage points are hard to see), to compare values across categories (use bars), and for trends or distributions.
- Start the largest slice at 12 o'clock and go clockwise from largest to smallest.
- Group small slices into "Other", and place "Other" last.
- Label slices directly with the category and the percentage.
- Slices must add up to 100%.

## Treemap

**Up to 10 rectangles.** Use it for how a whole divides into parts within a hierarchy, and to show which categories dominate a complex dataset.

<div class="figure">
<img src="{{ '/assets/examples/treemap.svg' | relative_url }}" alt="Treemap of funding by sector, with the three largest sectors highlighted">
</div>

- **Avoid** when precise comparison matters, or when the data isn't hierarchical. Use a bar chart instead.
- Label rectangles directly, and keep the labels short, because long labels don't fit in small rectangles.
