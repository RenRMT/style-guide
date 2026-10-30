---
title: Point maps
parent: Maps
nav_order: 5
---

# Point maps

Use point maps when the exact position of discrete events or values matters, not for continuous surfaces. Draw them on the [data-led basemap](../basemap/#basemap-colours), with the [point symbols](../basemap/#point-symbols).

## Choosing a visual variable

| To show… | Use |
|:--|:--|
| Quantities | **Size** |
| Categories | **Colour**, or up to three shapes |
| Intensity or density | Merging nearby points, clustering or binning |

{: .rule }
Use one primary variable. Use colour *or* size for meaning, and use other variables only to make the map legible. Combine size and colour only when both are equally important.

## Event map

**Up to about 50 dots.** Each dot is one event, or several events merged at one location. Use it when the precise location matters, such as distance to a town, border or route.

<div class="figure">
<img src="{{ '/assets/examples/map-events.svg' | relative_url }}" alt="Teal dots for protests across the Netherlands, one larger coral dot at the port, and one annotation">
</div>

- Draw each dot as a 7 px circle with a 0.75 px white stroke.
- Use one category, in Teal, where possible. Split into categories only when the split is the story.
- Mark the one event to read first in Coral, and annotate one or two events, not every cluster.
- **Avoid** with too many points, or when you need to show amounts (use proportional circles).
- Leave out the key when the title explains what a dot is. Avoid insets on event maps.
- If events at nearby locations share a dot, say so in a note: "Events within 2 km share a dot."
- For *dot density* maps, where each dot is a fixed amount placed at random within an area, state clearly that dots aren't exact locations.

## Proportional circles

**No fixed maximum.** Circle size shows an amount at a location. This is how to show counts where points overlap: group them into one circle.

<div class="figure">
<img src="{{ '/assets/examples/map-proportional.svg' | relative_url }}" alt="Teal circles sized by displaced people in Dutch towns, with a size key above the map">
</div>

- **Avoid** when the range of values is too small, such as only 1 and 2.
- **Scale by area, not radius.** Make the smallest circle at least 4 px.
- Always include a size key with round values, because readers judge sizes poorly.
- Draw the larger circles first, so that smaller ones sit on top, and separate them with a 1 px white stroke.

## Annotated map

**Up to 7 annotations, of at most two lines each.** Short text gives context for selected points. Use it when readers need to know why particular points matter.

<div class="figure">
<img src="{{ '/assets/examples/map-annotated.svg' | relative_url }}" alt="Four events on the Netherlands, each a dot with a two-line annotation on a thin leader line, with the port closure as a larger coral dot">
</div>

- **Avoid** with many annotations or a complicated key.
- Write in headline style: short, and with the most important words first. Longer text goes beside the map.
- Set annotations in [label style](../labels/): regular 11 px Ink with a halo, and a short straight leader line of 0.75 px. Don't put them in boxes.

## Overplotting

When points pile up, try these in order:

1. A white stroke around each point
2. Merging events at nearby locations into one dot, and saying so in a note
3. Jittering, if exact positions aren't critical
4. Cluster markers, for interactive maps
5. Switching to [proportional circles](#proportional-circles) or a [hexbin map](../area/#hexbin-map)

Test interactive maps at several zoom levels, and check that the symbols stay clear and meaningful at each one.
