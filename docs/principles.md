---
title: Principles
nav_order: 2
---

# Principles

Match the effort a visual asks of the reader to how much its message is worth. Make every visual as easy to read as possible, but don't simplify it so far that it loses meaning. A complex message can justify a complex visual, as long as everything that doesn't help is removed. A simple message gets a simple visual.

Every published visual meets four principles. When a visual isn't working, they help you find out why.

| Principle | The question it answers |
|:--|:--|
| [Purpose](#purpose) | Does it make a clear, worthwhile point? |
| [Structure](#structure) | Does it show the data truthfully? |
| [Presentation](#presentation) | Can the reader understand it quickly? |
| [Style](#style) | Is it consistent and free of distractions? |

## Purpose

A visual must make a point that matters to the reader and that isn't obvious without it. It should help the reader reason, interpret or decide.

{: .rule }
State the main message in the title. Every other element supports that message.

<div class="rules" markdown="1">
<div markdown="1">
#### Do
- Write titles as a takeaway: "Access improved in all districts but one".
- Highlight the key trend or contrast with an annotation.
- Connect the visual to the surrounding text, so it answers the question the text raises.
- Map only when the spatial pattern is the message.
</div>
<div markdown="1">
#### Avoid
- Showing every metric "for completeness" and leaving no message.
- Adding a chart for decoration when one sentence would do.
- Mapping every region without saying why the regions matter.
- Legends with more categories than there are data points.
</div>
</div>

## Structure

The data is represented accurately. Axes, scales, transformations and values are truthful and precise, so the reader can trust that what they see reflects the data.

{: .rule }
Bars and areas start at zero. Keep units consistent, and base every trend line and error bar on real calculations.

<div class="rules" markdown="1">
<div markdown="1">
#### Do
- Choose conventional forms: bars for comparison, lines for trends, scatter plots for relationships.
- Normalise data on choropleth maps, using rates, not counts.
- Make sure legends, scale bars and symbols match the data and the geography.
</div>
<div markdown="1">
#### Avoid
- Truncated bar axes, misleading colour scales and cherry-picked timeframes.
- Effects that exaggerate differences, such as 3D, perspective or area scaled by radius.
- Inconsistent scales across panels meant for comparison.
- Wrong borders, mismatched layers or misplaced coordinates.
</div>
</div>

{: .why }
Whether a line chart's y-axis must start at zero is a real debate. See [Axes and baselines](../background/axes/).

## Presentation

The reader quickly understands the visual's structure, relationships and meaning. The visual is intuitive, readable and uncluttered.

{: .rule }
Remove everything that doesn't help understanding. Guide the eye to the point, and don't make the reader work it out.

<div class="rules" markdown="1">
<div markdown="1">
#### Do
- Label data directly, and keep legends close to the data when you need them.
- Order categories meaningfully: by value, by time, or with the key category first.
- Use visual hierarchy: the story in colour, context in grey.
- Split dense visuals into small multiples or several panels.
</div>
<div markdown="1">
#### Avoid
- Colour ramps that change hue unevenly. Perceptually, they lie.
- Pie charts with many similar-sized slices.
- Background features drawn stronger than the data.
- Making the reader go back and forth between legend and data.
</div>
</div>

{: .why }
These rules follow from how perception groups and ranks what we see, and from the limits of working memory. See [Perception](../background/perception/) and [Fluency and cognitive load](../background/fluency/).

## Style

Design choices help the reader understand the message instead of distracting from it. Colour, type, layout and spacing are intentional and consistent.

{: .rule }
Use the house [colours](../colour/) and [typeface](../typography/), and the [chart](../charts/layout/) and [map](../maps/layout/) templates.

<div class="rules" markdown="1">
<div markdown="1">
#### Do
- Use legible colours, strong contrast and one clean typeface.
- Match the tone to the message: a sombre topic gets a sober treatment.
- Use plain, pronounceable labels and terms.
</div>
<div markdown="1">
#### Avoid
- Clashing or oversaturated colours.
- Drop shadows, busy backgrounds and decorative fonts.
- Inconsistent font sizes and heavy gridlines.
</div>
</div>

{: .why }
Easy-to-read visuals are trusted more, whether or not they are correct. Polish is a responsibility, so only make something look finished once you know it is right. See [Fluency and cognitive load](../background/fluency/).

---

Adapted from Wilke (2019), *Fundamentals of Data Visualization*. See [references](../background/references/).
