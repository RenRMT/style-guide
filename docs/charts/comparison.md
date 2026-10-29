---
title: Comparison
parent: Charts
nav_order: 3
---

# Comparison charts

## Horizontal bar chart

**Up to 15 bars.** The default chart. Use it to compare values across categories and to show rankings. It has room for long labels and reads from top to bottom.

<div class="figure">
<img src="{{ '/assets/examples/bar-horizontal.svg' | relative_url }}" alt="Horizontal bar chart of incidents by region, sorted high to low, with one bar highlighted">
</div>

- **Avoid** when categories have a fixed order such as dates (use a column chart), or when the values are continuous rather than categorical (use a histogram or line chart).
- Sort bars meaningfully: high to low, or with the key category on top.
- **Always start the value axis at zero.**
- Use one colour for all bars. To highlight one bar, make it Teal and the rest Steel.

## Column chart

**Up to 24 columns.** A vertical bar chart. Use it when categories have a natural order, especially time: months, years, age groups.

<div class="figure">
<img src="{{ '/assets/examples/column.svg' | relative_url }}" alt="Column chart of incidents per month, peaking in July">
</div>

- **Avoid** with long category labels or for rankings. Use horizontal bars instead.
- Always start the value axis at zero.
- If the labels don't fit, see [long category labels](../layout/#long-category-labels).

## Clustered bar chart

**Up to 18 bars in total.** Also called a grouped bar chart. Use it to compare subcategories within each category, when comparing the parts matters more than comparing the totals.

- **Avoid** when clusters get crowded, or when the totals matter more. Use a stacked bar or small multiples instead.
- Keep the same series order and colours in every cluster.
- In Excel, missing category–subcategory pairs leave empty gaps. Fill them with zeros or restructure the data.

## Lollipop and dot chart

**Up to 15 categories.** A lighter alternative to bars, for many categories or when values sit close together, such as when everything is between 80% and 90%. Because the dot marks the value rather than a bar's length, the axis may start above zero.

<div class="figure">
<img src="{{ '/assets/examples/lollipop.svg' | relative_url }}" alt="Dumbbell chart of access to clean water in five districts, 2024 and 2025, with an axis starting at 60%">
</div>

- **Avoid** when you can't label points directly, because dots make comparison less precise.
- Keep the stems thin and Steel, so the dots are the focus.
- A dumbbell chart (two dots joined by a line) shows before and after, or two groups, per category.

{: .why }
Bars must start at zero because readers judge bars by their length. Dots and lines encode position, which is why their axes may start elsewhere. See [Axes and baselines](../../background/axes/).
