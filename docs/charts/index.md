---
title: Charts
nav_order: 7
---
Charts are the appropriate data visualisation type when you need to visualise the relationship between two or more variables. The type of chart depends on the type of pattern you wish to display: comparison, composition, relationship (correlation) or distribution. The different types of charts are further explained below. Regardless of the chart type chosen, there are a number of elements that should be present in any chart. Manadatory chart layout elements are outlined below.

# Choosing a chart type

If you want to visualise...

- A change over time or trend, which is:
  - Continuous (daily, weekly, etc.) -> line chart
    - and emphasizes volume or totals -> area chart
    - and shows changing composition over time -> stacked area chart
  - Discrete (years, quarters, categories) -> column chart
    - and shows changing composition over time -> stacked column chart

- A comparison between categories, which are:
  - Ordered -> column chart
    - and across 2 dimensions -> grouped (clustered) column chart
    - with many series that would overlap -> small multiples column chart
  - Not ordered -> horizontal bar chart
    - and across 2 dimensions -> grouped (clustered) bar chart
    - with many series that would overlap -> small multiples bar chart

- A composition or part-to-whole, with:
  - 2–5 segments -> pie chart or donut chart
  - More than 5 segments -> stacked bar chart
  - Hierarchical or multi-level data -> treemap

- A distribution of values, focusing on:
  - Frequency distribution -> histogram
  - Spread, median, outliers -> box plot
  - Shape or density -> KDE plot or violin plot

- A relationships or correlation, between:
  - Two variables -> scatterplot
  - Three variables -> bubble chart
  - Mixed categorical + numerical -> heatmap

- Flows or movement:
  - Flow of quantities between stages -> Sankey diagram

# References
Atlassian (n.d.) How to choose the right data visualization. Available at: https://www.atlassian.com/data/charts/how-to-choose-data-visualization 
Datawrapper (2025) A friendly guide to choosing a chart type. Available at: https://www.datawrapper.de/blog/chart-types-guide
GeeksforGeeks (2025) Choosing the Right Chart Type: A Technical Guide. Available at: https://www.geeksforgeeks.org/data-visualization/choosing-the-right-chart-type-a-technical-guide/
Highcharts (n.d.) Chartchooser. Available at: https://www.highcharts.com/chartchooser/ 
The Data Visualisation Catalogue (n.d.) The Data Visualisation Catalogue. Available at: https://datavizcatalogue.com/
