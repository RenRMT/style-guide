---
title: Gestalt Principles
layout: default
parent: Design principles
nav_order: 7
---
# Gestalt principles 

Human perception is not neutral; we actively construct what we see.

Gestalt principles are psychology-based principles explaining how humans organize visual elements into structured wholes rather than sum-of-parts, emphasizing that our minds seek order and simplicity. Below, each Gestalt principle or perceptual rule is paired with (1) what it means, (2) how it guides practical design decisions, and (3) concrete examples of good application.

## 1. Proximity: use space to signal structure 

We group elements that are physically close together. Even subtle spacing differences create strong perceived structure.
How to apply it:
- Group related values in tables by reducing row or column spacing.
- Separate unrelated groups with more white space instead of adding lines.
- In dashboards, cluster related KPIs spatially.
Example: A table with uniform spacing makes monthly metrics look equally related. Add tighter spacing within quarterly groups and more space between quarters to visually encode time periods without adding borders.

## 2. Similarity: use consistent visual attributes to bind meaning

Objects that share colour, shape, size, or orientation appear related.

How to apply it
- Use one highlight colour consistently for the “story” data point.
- Use a single shape for a category rather than mixing multiple.
- Colour is a very strong channel and easily overloaded, do not overuse it.
Example: You want to emphasize one region out of 12 on a bar chart. Make all bars grey and use a single contrasting colour (e.g., blue) for the featured region.
## 3. Enclosure: use minimal boundaries to group elements

We treat items inside a boundary as a group.

How to apply it
- Subtle shading can separate forecast from actual values (e.g., shading future months).
- Use soft background rectangles to group related filters or controls in dashboards.
- Avoid boxes around every chart; use enclosure strategically.
Example:  Shade the forecast section of a line chart lightly to separate historical from projected values without extra text.

## 4. Closure: remove non essential chart elements
We complete shapes mentally, so borders and heavy frames are unnecessary.

How to apply it
- Remove chart borders, gridlines, and background shading.
- Rely on natural alignment and whitespace.
Example: a bar chart without a frame still reads as a complete graphic. Removing clutter reduces cognitive load and highlights the data.

## 5. Continuity: use smooth visual paths to guide the eye

Our eyes follow the smoothest path and construct continuity even where it’s missing.

How to apply it
- Align labels so the eye moves naturally.
- Remove unnecessary axis lines, because viewers will perceive alignment anyway.
- Use consistent spacing to create implicit guides.
Example: removing the y axis line on a bar chart doesn’t break readability because equal spacing maintains the perceived baseline.

## 6. Connection: linking is the strongest grouping cue
Connected elements are perceived as belonging together—even stronger than similarity.

How to apply it
- Use lines sparingly but deliberately (e.g., connecting observations in time series).
- Use thin lines for subtle grouping, thick lines for strong emphasis.
- Avoid connecting too many things.
Example: A line chart showing two product lines: connecting dots helps the viewer track performance more quickly than individual points.

## 7. Figure/background & contrast: use contrast intentionally

Perception depends on relative luminance and local contrast, not absolute brightness.
How to apply it
- Ensure the focal data has the strongest contrast.
- Use soft backgrounds behind secondary elements.
- Choose colour palettes that are perceptually uniform.
Example: If you highlight a KPI in bright colour but place it over a busy or high-contrast background, the highlight loses effectiveness.

## 8. Pre-attentive attributes: make key messages "pop"

We detect certain features almost instantly, such as colour, size, orientation, shape.
How to apply it
- Use one preattentive feature (colour OR size) to highlight a single insight.
- Don’t use multiple channels unless the data structure supports it (rare).
- Use shape sparingly. Shape pop-out is weaker than colour, especially in large sets.

Example: Highlight one unusual outlier in a scatterplot by using a single vivid colour while keeping all other points neutral.

## Summary checklist

- Minimize clutter: remove borders, reduce gridlines. (Closure)
- Use space intentionally to group related items. (Proximity)
- Apply one consistent highlight colour for the main message. (Similarity)
- Use subtle shading to separate contexts such as past vs future. (Enclosure)
- Guide the eye with alignment, not heavy lines. (Continuity)
- Connect things only when they belong together. (Connection)
- Use pre-attentive attributes sparingly for emphasis.
- Choose perceptually uniform colour palettes and avoid misleading contrasts.
- Annotate key insights so viewers don’t construct incorrect patterns.

# References
* Healy, K. (2026) Data Visualization: A Practical Introduction. 2nd ed. Princeton: Princeton University Press.
* Nussbaumer Knaflic, C. (2015) Storytelling with Data: A Data Visualization Guide for Business Professionals. Hoboken, NJ: John Wiley & Sons.

