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
| Quantities | Size |
| Categories | Colour, or up to three shapes |
| Intensity or density | Merging nearby points, clustering or binning |

{: .rule }
Use one primary variable. Use colour *or* size for meaning, and use other variables only to make the map legible. Combine size and colour only when both are equally important.

{: .avoid }
Don't vary size for categories, and don't colour categories with a sequential ramp. Both suggest an order that isn't there.

## Event map

{: .meta }
Up to about 50 dots

Each dot is one event, or several events merged at one location. Use it when the precise location matters, such as distance to a town, border or route.

<div class="figure">
<img src="{{ '/assets/examples/map-events.svg' | relative_url }}" alt="Teal dots for protests across the Netherlands, one larger coral dot at the port, and one annotation">
</div>

- Draw each dot as a 7 px circle with a 0.75 px white stroke.
- Use one category, in Teal, where possible. Split into categories only when the split is the story.
- Mark the one event to read first in Coral, and annotate one or two events, not every cluster.
- With more than one category, draw the one that matters most, such as the most severe, on top.
- Avoid it with too many points, or when you need to show amounts (use proportional circles).
- Leave out the key when the title explains what a dot is. Avoid insets on event maps.
- If events at nearby locations share a dot, say so in a note: "Events within 2 km share a dot."
- For *dot density* maps, where each dot is a fixed amount placed at random within an area, state clearly that dots aren't exact locations.

## Proportional circles

{: .meta }
No fixed maximum

Circle size shows an amount at a location. This is how to show counts where points overlap: group them into one circle.

<div class="figure">
<img src="{{ '/assets/examples/map-proportional.svg' | relative_url }}" alt="Teal circles sized by displaced people in Dutch towns, with a size key above the map">
</div>

- Avoid them when the range of values is too small, such as only 1 and 2.
- Scale by area, not radius. Make the smallest circle at least 4 px.
- Always include a size key with round values, because readers judge sizes poorly.
- Draw the larger circles first, so that smaller ones sit on top, and separate them with a 1 px white stroke.
- Size the circles for the map scale. If the largest circles cover whole areas or hide the borders beneath them, shrink the scale or classify.
- Readers can't judge exact amounts from circle sizes. Print the value inside the larger circles, or label the ones the title mentions.

### Extreme values

When one value dwarfs the rest, a proportional scale either shrinks everything else to dots or lets the largest circle bury its neighbours. Either:

- Use graduated circles: classify the values and give each class one fixed size, with each size at least double the area of the one below. Show every size in the key.
- Or keep the proportional scale for most values, and draw the outlier as a separate symbol with its own entry in the key.

In both cases, explain the outlier in a note or annotation.

## Annotated map

{: .meta }
Up to 7 annotations · at most two lines each

Short text gives context for selected points. Use it when readers need to know why particular points matter.

<div class="figure">
<img src="{{ '/assets/examples/map-annotated.svg' | relative_url }}" alt="Four events on the Netherlands, each a dot with a two-line annotation on a thin leader line, with the port closure as a larger coral dot">
</div>

- Avoid it with many annotations or a complicated key.
- Write in headline style: short, and with the most important words first. Longer text goes beside the map.
- Set annotations in [label style](../labels/): regular 11 px Ink with a halo, and a short straight leader line of 0.75 px. Don't put them in boxes.

## Overplotting

When points pile up, try these in order:

1. A white stroke around each point
2. Merging events at nearby locations into one dot, and saying so in a note
3. Jittering or nudging symbols apart, if exact positions aren't critical. Move the symbols, never the data.
4. An [inset](../layout/#inset-zoomed-area) for one dense area, or cluster markers on interactive maps
5. Switching to [proportional circles](#proportional-circles) or a [hexbin map](../area/#hexbin-map)

Test interactive maps at several zoom levels, and check that the symbols stay clear and meaningful at each one.
