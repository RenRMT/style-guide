---
title: Other maps
parent: Maps
nav_order: 6
---

# Other map types

## Reference and locator maps

A reference map shows no data, only geography: coverage area, admin areas, towns, borders, roads. A locator map is the simplest kind: it shows where one place is. Use them to orient readers, or to show a route or border crossing.

<div class="figure">
<img src="{{ '/assets/examples/map-locator.svg' | relative_url }}" alt="Location basemap of the Netherlands with Amsterdam and a coral dot on Groningen, and a small locator in the top-left corner">
</div>

- Use the [location basemap](../basemap/#basemap-colours).
- Show the minimum: the capital, the place in the story and nothing else, usually at one admin level.
- Mark the place in Coral. Add a [locator](../layout/#locator-map) to put the country in its region.
- Avoid them when you need to show variable data such as incidents. Use a thematic map instead.

## Highlight areas

An outlined box with a label tab names an area without hiding what is under it. Use it to point out where something happened or changed.

<div class="figure">
<img src="{{ '/assets/examples/map-highlight-areas.svg' | relative_url }}" alt="Location basemap with a solid outlined box labelled Patrols increased, and a dashed box labelled Possible new route">
</div>

- Draw the outline at 1.5 px in `#1F5247`. Use a solid line for confirmed and a dashed line for possible.
- Put the label in a tab on top of the box: white on `#1F5247` when confirmed, `#1F5247` on white when possible.
- Use two boxes per map at most, and no fills.

## Routes and flow maps

A routes map shows *where* things move: supply routes, migration paths, trafficking routes. A flow map also shows *how much*, with line width.

<div class="figure">
<img src="{{ '/assets/examples/map-routes.svg' | relative_url }}" alt="Freight routes from Rotterdam: solid blue sea routes, a dashed suspected sea route, and a teal land route, each with a small arrowhead">
</div>

- Draw routes at 2 px, with a small solid arrowhead.
- Use colour for the mode, such as maritime or land, and at most three modes. Use dashes for uncertainty: a dashed route is suspected.
- Draw smooth or straight lines. Don't trace every bend in the road.
- Give destinations off the map a short label at the arrow: "To Germany".
- Scale flow lines to the volume, and include a width key.
- The main risk is clutter. When lines cross too often, simplify the routes, merge flows or show only the largest ones.

## Isoline map

An isoline map draws lines of equal value across a continuous surface, such as travel time to the nearest clinic, temperature or interpolated survey results.

<div class="figure">
<img src="{{ '/assets/examples/map-isoline.svg' | relative_url }}" alt="Isolines of travel time to the nearest clinic at 30, 60 and 90 minutes, with the 90-minute line in the north-east">
</div>

- Use it only when the phenomenon really changes smoothly across space, and when there are enough measurement points.
- With sparse or sharply varying data, an isoline map looks precise when it isn't. Use points or areas instead.
