---
title: Charts
nav_order: 7
has_children: true
---

# Charts

Use a chart to show a comparison, trend, composition, distribution or relationship. Pick the simplest chart type that supports your point, and lay it out with the [chart template](layout/).

## Choosing a chart type

Find what you want to show, then answer the questions about your data.

<details markdown="1">
<summary>Showing change over time? Usually a <a href="time/#line-chart">line chart</a></summary>

- Is the data continuous (daily, weekly)? → [Line chart](time/#line-chart)
  - Do the totals matter? → [Area chart](time/#area-chart-and-stacked-area-chart)
  - Is the composition changing? → [Stacked area chart](time/#area-chart-and-stacked-area-chart)
- Is the data discrete (years, quarters)? → [Column chart](comparison/#column-chart)
  - Is the composition changing? → [Stacked column chart](composition/#stacked-bar-and-column-chart)
- Only two points in time, several categories? → [Slope chart](relationship/#slope-chart)

</details>

<details markdown="1">
<summary>Comparing categories? Usually a <a href="comparison/#horizontal-bar-chart">horizontal bar chart</a></summary>

- Are the categories unordered? → [Horizontal bar chart](comparison/#horizontal-bar-chart) (the default)
- Do they have a natural order (age groups, months)? → [Column chart](comparison/#column-chart)
- Are you comparing across two dimensions? → [Clustered bar or column chart](comparison/#clustered-bar-chart)
- Are the values close together? → [Lollipop or dot chart](comparison/#lollipop-and-dot-chart)
- Are there many series that would overlap? → Small multiples

</details>

<details markdown="1">
<summary>Showing parts of a whole? A <a href="composition/#pie-and-donut-chart">pie</a> for a few parts, otherwise a <a href="composition/#stacked-bar-and-column-chart">stacked bar</a></summary>

- Are there only 2–5 parts? → [Pie or donut chart](composition/#pie-and-donut-chart)
- Are there more parts, or are you comparing across categories? → [Stacked bar chart](composition/#stacked-bar-and-column-chart)
- Are the parts hierarchical? → [Treemap](composition/#treemap)

</details>

<details markdown="1">
<summary>Showing a distribution? Depends on what matters most</summary>

- Is it the frequency of values? → [Histogram](distribution/)
- Is it the spread, median and outliers? → [Box plot](distribution/)
- Is it the overall shape? → [Density or violin plot](distribution/)

</details>

<details markdown="1">
<summary>Showing a relationship? Usually a <a href="relationship/">scatter plot</a></summary>

- Two numeric variables? → [Scatter plot](relationship/)
- Three numeric variables? → [Bubble chart](relationship/)
- A categorical and a numeric variable? → Heatmap

</details>

{: .rule }
When in doubt, use a horizontal bar chart. It handles long labels, reads naturally from top to bottom, and shows values as position along a common baseline, which people read most accurately.

## Limits at a glance

| Chart | Maximum |
|:--|:--|
| Horizontal bar | 15 bars |
| Column | 24 columns |
| Clustered bar or column | 18 bars in total |
| Stacked bar or column | 7 bars, each with at most 5 segments |
| Lollipop or dot | 15 categories |
| Line, area | 4 lines or series |
| Slope | 10 lines, at most 4 highlighted |
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
Highlight with grey. See [the highlight pattern](../colour/categorical/#how-many-colours).

{: .rule }
One value axis per chart. Dual y-axes let the maker set the apparent relationship by choosing the scales. Use two panels side by side, or index both series to a common start.

{: .rule }
Show uncertainty where it changes the message: error bars or ranges on estimates, and a dashed or shaded line for forecasts. Explain the measure in a note, such as "95% confidence interval".

---

Chart chooser sources: Atlassian, Datawrapper (2025), Highcharts Chartchooser and the Data Visualisation Catalogue. See [references](../background/references/).
