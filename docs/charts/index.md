---
title: Charts
nav_order: 7
has_children: true
---

# Charts

Use a chart when you need to show the relationship between two or more variables. Pick the simplest chart type that supports your point, and lay it out with the [chart template](layout/).

## Choosing a chart type

| You want to show… | And the data is… | Use |
|:--|:--|:--|
| **Change over time** | continuous (daily, weekly) | [Line chart](time/#line-chart) |
| | continuous, and the totals matter | [Area chart](time/#area-chart-and-stacked-area-chart) |
| | continuous, with changing composition | [Stacked area chart](time/#area-chart-and-stacked-area-chart) |
| | discrete (years, quarters) | [Column chart](comparison/#column-chart) |
| | discrete, with changing composition | [Stacked column chart](composition/#stacked-bar-and-column-chart) |
| **Comparison** between categories | unordered | [Horizontal bar chart](comparison/#horizontal-bar-chart) (the default) |
| | ordered (age groups, months) | [Column chart](comparison/#column-chart) |
| | across two dimensions | [Clustered bar or column chart](comparison/#clustered-bar-chart) |
| | many categories, or values close together | [Lollipop or dot chart](comparison/#lollipop-and-dot-chart) |
| | many series that would overlap | Small multiples |
| **Composition** (part-to-whole) | 2–5 parts | [Pie or donut chart](composition/#pie-and-donut-chart) |
| | more parts, or compared across categories | [Stacked bar chart](composition/#stacked-bar-and-column-chart) |
| | hierarchical | [Treemap](composition/#treemap) |
| **Distribution** | frequency | [Histogram](distribution/) |
| | spread, median, outliers | [Box plot](distribution/) |
| | shape | [Density or violin plot](distribution/) |
| **Relationship** | two numeric variables | [Scatter plot](relationship/) |
| | three numeric variables | [Bubble chart](relationship/) |
| | categorical × numeric | Heatmap |
| **Flow** | quantities moving between stages | Sankey diagram |
| **A single number** | | [Big number](../big-numbers/) |

{: .rule }
When in doubt, use a horizontal bar chart. It handles long labels, reads naturally from top to bottom, and is the chart type people misread least.

## Limits at a glance

| Chart | Maximum |
|:--|:--|
| Horizontal bar | 15 bars |
| Column | 24 columns |
| Clustered bar or column | 18 bars in total |
| Stacked bar or column | 7 bars, each with at most 5 segments |
| Lollipop or dot | 15 categories |
| Line, area | 4 lines or series |
| Pie, donut | 6 slices (2–5 is better) |
| Treemap | 10 rectangles |
| Scatter, bubble | 4 colour categories |

If you go over a limit, group categories into "Other", use small multiples, or switch to another chart type.

## Rules for every chart

{: .rule }
Remove the clutter. Charts have no outline, no borders around bars or slices, no 3D effects, no shadows and no background fill.

{: .rule }
Label directly. Put labels on or next to the data, and use a legend only when direct labels don't fit. Once every value is labelled, drop the value axis and gridlines.

{: .rule }
Order categories meaningfully: by value, in their natural order, or with the key category first. Never sort alphabetically unless readers need to look items up.

{: .rule }
Highlight with grey. To make one category the story, colour it Teal and everything else Steel.

---

Chart chooser sources: Atlassian, Datawrapper (2025), Highcharts Chartchooser and the Data Visualisation Catalogue. See [references](../background/references/).
