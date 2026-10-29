---
title: Maps
nav_order: 8
has_children: true
---

# Maps

{: .rule }
Map only when geography matters. Ask whether location matters to the story, or whether it's just available. Differences between areas, trends over time and relationships between variables are often clearer as a [chart](../charts/). A good map takes a lot of effort, so make sure it's worth it.

A map answers one question about a place. Everything on it either helps answer that question or comes off. The house style starts from news-graphics cartography: light land, quiet water, few labels and one highlight colour.

## Choosing a map type

| You want to show… | Use | Page |
|:--|:--|:--|
| Where one place, area or route is, with no variable data | Reference or locator map | [Other maps](other/#reference-and-locator-maps) |
| An area to point out, such as where something changed | Highlight areas | [Other maps](other/#highlight-areas) |
| Rates, percentages or intensity per administrative area | Choropleth (coloured areas) | [Area maps](area/#choropleth-map) |
| The density of many points, when exact locations matter less | Hexbin map | [Area maps](area/#hexbin-map) |
| Types or categories per area, such as control or access | Chorochromatic / areas of control | [Area maps](area/#chorochromatic-and-areas-of-control-maps) |
| The exact location of individual events | Event (dot) map | [Point maps](point/#event-map) |
| Events by type | Circles by colour | [Point maps](point/#circles-by-colour) |
| Amounts at locations, including overlapping points | Proportional circles | [Point maps](point/#proportional-circles) |
| Both type and amount | Circles by size and colour | [Point maps](point/#circles-by-size-and-colour) |
| Context for a few selected points | Annotated map | [Point maps](point/#annotated-map) |
| Movement between places | Routes and flow map | [Other maps](other/#routes-and-flow-maps) |
| A continuous surface, such as travel time or temperature | Isoline map | [Other maps](other/#isoline-map) |

## Rules for every map

<div class="rules rules--do-avoid" markdown="1">
<div markdown="1">
#### Do
- Put the finding in the title
- Show only the places the story needs
- Label directly; use a key from three categories
- Use one data colour, plus Coral for the one thing to read first
- Keep neighbouring countries in the duller land tone
- Name the source and period on every map
</div>
<div markdown="1">
#### Avoid
- Pictogram icons where a shape will do
- More than four colours or three symbol shapes
- Filled boxes over the land
- Keys and insets placed on top of data
- Labelling every town
- Shadows, glows, relief shading and transparency
</div>
</div>

{: .rule }
Choose the simplest basemap that supports the message. The basemap is context, and must never compete with the data. See [Basemaps and symbols](basemap/).

{: .rule }
Show one message per map. If the map gets cluttered, split it into several maps or small multiples.

{: .rule }
Check legibility at the final size. A map that works full-screen may be unreadable at A4 or on a phone.

## The same story, twice

Both maps show the same fictional protests in the Netherlands. The first keeps what the title needs. The second gives every attribute its own colour, every place a label and every area a fill.

<div class="rules rules--do-avoid" markdown="1">
<div markdown="1">
#### Do
<img src="{{ '/assets/examples/map-events.svg' | relative_url }}" alt="The same protests as teal dots, with the capital, one coral highlight and one annotation">

One event colour, the capital and one annotation. The key sits in one row above the map, and the title states the finding.
</div>
<div markdown="1">
#### Avoid
<img src="{{ '/assets/examples/map-avoid.svg' | relative_url }}" alt="Protest map with seven colours, fifteen city labels, filled boxes over the land and a boxed key on the map">

Seven colours, fifteen labels, filled boxes hiding the land, and a key box sitting on the map. The title names the topic, not the finding.
</div>
</div>

Principles can bend: a skilled designer can break a convention for good reason, as long as the data is still shown truthfully.
