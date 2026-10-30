---
title: Perception
parent: Background
nav_order: 1
---

# Perception

Perception isn't neutral: people actively build what they see. Gestalt psychology describes how people group visual elements into wholes, looking for order and simplicity. Each principle below comes with what it means for design.

## Gestalt principles

### Proximity: space signals structure
People group elements that are close together. Even small differences in spacing create strong perceived structure.
- Group related rows or columns in a table with tighter spacing, and separate groups with white space instead of lines.
- Cluster related KPIs on a [dashboard](../../dashboards/plan-and-layout/#layout).

*Example:* in a table of monthly figures, tighter spacing within quarters and more space between them shows the quarters without any borders.

### Similarity: shared attributes bind meaning
Objects with the same colour, shape, size or orientation look related.
- Use one highlight colour consistently for the "story" data.
- Colour is a strong channel that is easily overloaded, so don't overuse it.

*Example:* to feature one region out of twelve, make all bars grey and the featured region Teal.

### Enclosure: boundaries create groups
People treat everything inside a boundary as a group.
- Light shading can separate forecast from actual values.
- Use enclosure strategically, not as a box around every chart.

### Closure: readers complete shapes themselves
People complete shapes mentally, so frames and borders are unnecessary.
- Remove chart borders, heavy gridlines and background shading. A bar chart without a frame still reads as a whole.

### Continuity: the eye follows smooth paths
The eye follows the smoothest path, and sees continuity even where there is none.
- Align labels so the eye moves naturally.
- Drop the y-axis line: aligned tick labels or gridlines already imply it.

### Connection: the strongest grouping cue
Connected elements look like they belong together, and connection beats similarity.
- Use lines deliberately, as in a time series, and don't connect things that don't belong together.

### Figure and ground: contrast is relative
Perception depends on relative brightness and local contrast.
- Give the focal data the strongest contrast, and put secondary elements on soft backgrounds.
- A bright highlight on a busy background loses its effect.

## Pre-attentive attributes

People spot some features almost instantly, before conscious attention: colour, size, orientation and shape.

- Use **one** pre-attentive feature (colour *or* size) to highlight one insight.
- Combine channels only when the data structure really calls for it, which is rare.
- Shape stands out less than colour, especially among many points.

*Example:* show an outlier in a scatter plot in one vivid colour, with all other points neutral.

## What this means in practice

| Rule in the guide | Principle |
|:--|:--|
| No borders, light gridlines | Closure |
| Group with space, not lines | Proximity |
| One highlight colour, grey for the rest | Similarity, pre-attentive colour |
| Shade forecasts or periods | Enclosure |
| Align labels, drop axis lines | Continuity |
| Connect only related points | Connection |
| Annotate key insights | Prevents readers from seeing patterns that aren't there |

---

Sources: Healy (2026), *Data Visualization: A Practical Introduction*; Nussbaumer Knaflic (2015), *Storytelling with Data*.
