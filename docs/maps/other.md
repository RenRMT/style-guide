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
- Scale flow lines to the volume, and include a width key. Classifying the widths into three or four sizes makes them easier to compare and remember.
- Start and end every flow at a labelled place, so readers can tell where it comes from and where it goes.
- The main risk is clutter. When lines cross too often, simplify the routes, merge flows to a higher admin level or show only the largest ones. If that's still too many, use a Sankey diagram or a table instead.
- Movement data can be sensitive. Check that showing where people go doesn't put them at risk. See [Sensitive data](../../planning/data/#sensitive-data).

### Drawing flows

Readability matters more than geometric accuracy on a flow map. Simplify the geography if that makes the flows clearer.

- Curve flows gently, rather than drawing straight lines, to reduce overlaps. Curve long flows more than short ones, but avoid sharp bends.
- Keep crossings few, and cross at wide angles.
- Don't let a flow pass under a place it doesn't connect to.
- Spread flows that leave the same place at different angles, rather than bundling them.
- Draw thin flows on top of thick ones.
- Show direction with an arrowhead scaled to the line width, enlarged a little for very thin lines. Don't use tapered lines: they make widths hard to compare.
- If every flow goes to the same place, leave out the arrows. Mark the origins with dots, and label the destination.

{: .why }
These rules come from an analysis of 97 published flow maps and a user study. See Jenny et al. (2018) in the [references](../../background/references/).

## Isoline map

An isoline map draws lines of equal value across a continuous surface, such as travel time to the nearest clinic, temperature or interpolated survey results.

<div class="figure">
<img src="{{ '/assets/examples/map-isoline.svg' | relative_url }}" alt="Isolines of travel time to the nearest clinic at 30, 60 and 90 minutes, with the 90-minute line in the north-east">
</div>

- Use it only when the phenomenon really changes smoothly across space, and when there are enough measurement points.
- With sparse or sharply varying data, an isoline map looks precise when it isn't. Use points or areas instead.

## Change over time

To show how something changed, such as the growth of a settlement or the spread of damage:

- Use a sequential ramp for the dates, from light (oldest) to dark (newest).
- Choose dates far enough apart that the change is visible: decades rather than years if change is slow. Keep the intervals equal when readers need to see when change was fastest.
- Don't stack layers from different dates on one map. The top layer hides what is underneath, so the overlap may not show the real change. Map the change itself, such as areas that were added or lost, or show each date as a small multiple with the same extent and style.

## Charts on maps

Bar charts and pie charts placed on a map are hard to read. They aren't aligned, so they can't be compared, and they cover the geography.

- Don't put bar charts on maps.
- Use pie charts only with two to four slices of very different size, and size them like [proportional circles](../point/#proportional-circles).
- Never use 3D charts or shadows.

Instead, use [small multiples](../layout/#several-maps-together): one map per measure, side by side. Or use symbols on the map and put the chart beside it, linked by place names.

## Overlapping areas

When layers overlap, such as flooded areas over land use, readers can't tell what they are looking at.

- Best: combine the layers into joint classes, such as "high exposure, often flooded", and name each one in the key.
- Otherwise, show one layer as a fill and the other as a hatch. With two hatched layers, set them 90° apart (vertical and horizontal, or 45° and 135°), so they still read where they cross. Use two textures at most.
- Use hatches only for categories. Readers can't judge amounts from hatch density.
