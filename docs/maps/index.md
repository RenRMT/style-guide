---
title: Maps
nav_order: 8
has_children: true
---

# Maps

{: .rule }
Map only when geography matters. Differences between areas, trends and relationships are often clearer as a chart. See [Before you make a map](../planning/format/#before-you-make-a-map).

A map answers one question about a place. Everything on it either helps answer that question or comes off. The house style starts from news-graphics cartography: light land, quiet water, few labels and one highlight colour.

## Choosing a map type

Find what you want to show, then answer the questions about your data.

<details markdown="1">
<summary>Pointing out a place, area or route? Usually a <a href="other/#reference-and-locator-maps">reference or locator map</a></summary>

- Is it just where something is, with no data attached? → [Reference or locator map](other/#reference-and-locator-maps)
- Do you need to draw attention to an area, such as where something changed? → [Highlight areas](other/#highlight-areas)
- Do a few selected points need context or explanation? → [Annotated map](point/#annotated-map)

</details>

<details markdown="1">
<summary>Showing data for areas? Usually a <a href="area/#choropleth-map">choropleth</a></summary>

- Is it a rate, percentage or intensity per administrative area? → [Choropleth (coloured areas)](area/#choropleth-map)
- Is it a type or category per area, such as control or access? → [Chorochromatic or areas of control map](area/#chorochromatic-and-areas-of-control-maps)

</details>

<details markdown="1">
<summary>Showing events or locations? Usually an <a href="point/#event-map">event (dot) map</a></summary>

- Does the exact location of each event matter? → [Event (dot) map](point/#event-map)
- Are there amounts at each location, or overlapping points? → [Proportional circles](point/#proportional-circles)
- Are there so many points that density matters more than exact location? → [Hexbin map](area/#hexbin-map)

</details>

<details markdown="1">
<summary>Showing movement or a continuous surface?</summary>

- Are things moving between places? → [Routes and flow map](other/#routes-and-flow-maps)
- Does a value vary smoothly across space, such as travel time or temperature? → [Isoline map](other/#isoline-map)

</details>

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
- Shadows, glows and transparency, and relief shading unless terrain is the message
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
