---
title: Choropleth maps
parent: Maps
nav_order: 3
---
# Choropleth maps

Choropleth maps are used to show relative quantities, such as percentages, rates, or densities, by changing the lightness or hue of colours across geographic areas. They are appropriate when the values represent meaningful comparisons between areas and when the phenomenon is spatially continuous. Because shading reflects the value in each unit, the data must be normalised; using absolute counts would make large areas look more important than they really are.

When designing a choropleth map, colour choice and class breaks are key decisions. Sequential colour schemes work well for ordered values, while diverging schemes help show differences from a central point, such as an average. Classifying the data also affects interpretation. Quantile breaks often work best because they spread areas evenly across classes, but other methods can be used when they highlight important patterns. Avoid changing class breaks simply to influence the message. In cases where administrative boundaries vary greatly in size or do not match the spatial pattern, a hexbin choropleth can offer a more consistent view.

## Examples:

- Incident rates per 100,000 inhabitants to compare levels of violence across regions with different population sizes.
- Using hexagonal cells to map the density of recorded conflict events, reducing bias from uneven administrative units.

## Choosing a data classification type

A quick way to determine what data classification type to use, is to check the histogram:

- Uniform / evenly distributed (rectangular histogram) -> equal interval
- Normal / Poisson distribution (“bell curve” histogram) -> standard deviation
- Skewed (heavy-tailed histogram) -> quantiles (equal count)
- Clustered / gaps (irregular histogram) -> natural breaks

Special considerations:

- Outliers: if the histogram shows extreme outliers, choose natural breaks or quantiles over equal interval
- Comparison: for comparison across multiple maps, choose quantiles or manual breaks
- Classes: use at most 7 classes, preferably fewer.
