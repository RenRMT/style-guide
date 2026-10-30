---
title: Comparison
parent: Charts
nav_order: 3
---

# Comparison charts

## Horizontal bar chart

{: .meta }
Up to 15 bars

The default chart. Use it to compare values across categories and to show rankings. It has room for long labels and reads from top to bottom.

<div class="figure">
<img src="{{ '/assets/examples/bar-horizontal.svg' | relative_url }}" alt="Horizontal bar chart of incidents by region, sorted high to low, with one bar highlighted">
</div>

- Avoid it when categories have a fixed order such as dates (use a column chart), or when the values are continuous rather than categorical (use a histogram or line chart).
- Sort bars meaningfully: high to low, or with the key category on top.
- Use one colour for all bars, or [highlight one](../../colour/categorical/#how-many-colours).

{: .rule }
Always start the value axis at zero.

## Column chart

{: .meta }
Up to 24 columns

A vertical bar chart. Use it when categories have a natural order, especially time: months, years, age groups.

<div class="figure">
<img src="{{ '/assets/examples/column.svg' | relative_url }}" alt="Column chart of incidents per month, peaking in July">
</div>

- Avoid it with long category labels or for rankings. Use horizontal bars instead.
- Always start the value axis at zero.
- If the labels don't fit, see [long category labels](../layout/#long-category-labels).

## Clustered bar chart

{: .meta }
Up to 18 bars in total

Also called a grouped bar chart. Use it to compare subcategories within each category, when comparing the parts matters more than comparing the totals.

<div class="figure">
<img src="{{ '/assets/examples/bar-clustered.svg' | relative_url }}" alt="Clustered bar chart of acute malnutrition in five regions, with bars for children, adults and older people in each region">
</div>

- Avoid it when clusters get crowded, or when the totals matter more. Use a stacked bar or small multiples instead.
- Keep the same series order and colours in every cluster.
- In Excel, missing category–subcategory pairs leave empty gaps. Fill them with zeros or restructure the data.

## Small multiples

{: .meta }
Up to about 12 panels

A grid of small charts of the same type, one per category, all on the same scales. Use it when one chart would hold too many overlapping series, such as more than four lines.

<div class="figure">
<img src="{{ '/assets/examples/small-multiples.svg' | relative_url }}" alt="Six small line charts of displacement, one per region, on shared axes, each showing its region in Teal against the others in light grey">
</div>

- Avoid them when readers need to compare exact values between panels. Put those series in one chart instead.
- Use the same axes in every panel, and label the axes only on the outer panels.
- Sort the panels meaningfully, such as by the latest value, not alphabetically.
- Show the other categories in Platinum behind each panel's own line, so each panel can be read against the whole.

## Lollipop and dot chart

{: .meta }
Up to 15 categories

A lighter alternative to bars, for when values sit close together, such as when everything is between 80% and 90%. In a dot or dumbbell chart, the dot marks the value, so the axis may start above zero. A lollipop's stem encodes length like a bar, so its axis starts at zero.

<div class="figure">
<img src="{{ '/assets/examples/lollipop.svg' | relative_url }}" alt="Dumbbell chart of access to clean water in five districts, 2024 and 2025, with an axis starting at 60%">
</div>

- Avoid it when you can't label points directly: a dot far from its axis label is hard to read off.
- Keep the stems thin and Steel, so the dots are the focus.
- A dumbbell chart (two dots joined by a line) shows before and after, or two groups, per category.

{: .why }
Bars must start at zero because readers judge bars by their length. Dots and lines encode position, which is why their axes may start elsewhere. See [Axes and baselines](../../background/axes/).
