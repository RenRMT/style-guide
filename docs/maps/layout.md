---
title: Map layout
parent: Maps
nav_order: 1
---

# Map layout

## Two kinds of map product

<div class="rules" markdown="1">
<div markdown="1">
#### Integrated map
Placed in a report, slide or dashboard. Makes **one point, as simply as possible.**
- Simplest possible basemap and symbols
- Clear title and subtitle
- Direct labels in preference to a legend
- A4 size, portrait or landscape
</div>
<div markdown="1">
#### Standalone map
A map sheet in its own right. Treat it as an **infographic**, which can be more complex.
- One or several maps, plus charts, annotations and descriptive text
- Source credits, disclaimer, acronyms and partner logos
- A-series paper size (A4, A3), portrait or landscape
</div>
</div>

## Map elements

| # | Element | | Guidance |
|:-:|:--|:--|:--|
| 1 | Figure number | optional | Use when the text refers to the map. |
| 2 | **Title** | required | *Why* you're showing the map: the main point. |
| 3 | Subtitle | recommended | *What* the map shows: units, categories and period. Anything the subtitle can't hold goes in the legend. |
| 4 | **Map area** | required | |
| 5 | Legend | if needed | Only for symbols that the title and subtitle don't explain. |
| 6 | Location map | optional | Shows where the map area is. See [Location map](#location-map). |
| 7 | Inset (zoomed area) | optional | Shows a crowded or distant area at a larger scale. |
| 8 | North arrow | if needed | Only when north isn't at the top, or the area isn't recognisable. |
| 9 | Scale bar | if needed | Only when distances matter to the message. |
| 10 | **Source** | required | Bottom left. Credit both the data and the map layers. |
| 11 | **Logo** | required | Bottom right. Integrated maps use the symbol logo, and standalone maps use the full logo. |

### Elements by attention level

Use this table with the [3 / 30 / 300 rule](../../planning/audience/).

| Element | 3 s (locator) | 30 s (narrative) | 300 s (exploration) |
|:--|:-:|:-:|:-:|
| Title and subtitle | optional | ✔ | ✔ |
| Legend | ✘ | ✔ | ✔ |
| Location map or insets | ✘ | optional | optional |
| Scale bar, north arrow | ✘ | optional | optional |
| Source and credits | ✘ | optional | ✔ |
| Neatline (frame) | ✘ | optional | optional |
| Additional graphics (charts, photos) | ✘ | ✘ | optional |

## Placement

### Legend
- Place the legend inside the map area, at least 5 mm from the edge, on the opposite side from the location map.
- Don't title it "Legend".
- List only the elements that serve the map's purpose. Leave out static features such as admin boundaries, cities, lakes and rivers.
- For class ranges, see [Choosing classes](../area/#choosing-classes).

### Location map
A small map that shows where the main map is. Use either a **country location map** (where the country is in the world) or an **area location map** (which part of the country is shown), never both.

- Add a country location map only if most readers won't know where the country is *and* they need to know to understand the point.
- Add an area location map when the main map is so zoomed in that the country's outline isn't recognisable.
- It must not overlap the data or other elements, and it shows no unnecessary detail.
- Colours: Platinum or Steel for countries, and Primary Teal for the highlighted area.

### Inset (zoomed area)
- Use an inset for areas that are too dense to read, or that are far from the main map.
- Mark the zoomed area on the main map with a box or arrow.
- Never let it overlap data on the main map.
- Use at most two. If you need more, split the map.

### North arrow and scale bar
- **North arrow:** required when north isn't at the top, or the area isn't immediately recognisable. Leave it out when the projection has no single north. Otherwise, add one only if readers need it.
- **Scale bar:** only when exact distances matter to the message.
- Place them in a free corner, at least 5 mm from the edge.

{: .adapt }
Build your map template once in your GIS tool (an ArcGIS Pro layout or QGIS print layout) with every element in place. Delete what a map doesn't need, rather than adding elements one by one.
