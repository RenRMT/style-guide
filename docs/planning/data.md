---
title: Check the data
parent: Planning
nav_order: 4
---

# Check the data

A visual can only be as good as the data that goes into it. Check the data before you design anything, because a polished visual makes weak data look trustworthy.

## Your own data

- Use only data and analyses that have been checked. If you recode, aggregate or combine fields for the visual, have that step checked too.
- Don't break the data down further than the sample allows. If a survey represents regions, don't show districts.
- Look at the distribution before you choose a format or class breaks. A histogram shows outliers, gaps and clusters that a summary hides.
- Keep datasets close in time. If layers or series come from different dates, say so in a note.

## Data from others

Before you use someone else's data, check that:

- The source is reputable and independent of the outcome it reports.
- The method is documented and sound.
- You're allowed to use it. Prefer openly licensed data, and ask the owner when it isn't.
- It comes with metadata. Without metadata you can't judge the data, so don't use it.
- Its resolution and coverage match the rest of your data. If not, say so in a note.
- It's recent enough for your message.

Credit every source on the visual. Some licences prescribe the wording: OpenStreetMap, for example, requires "© OpenStreetMap contributors".

## Sensitive data

{: .rule }
Do no harm. A visual can travel much further than you intended, and showing who is where, or who has what, can put people at risk.

Never show personal data. That includes indirect identifiers such as origin, ethnicity, religion or profession, which can identify people when combined with a location. Before you publish, ask:

- Does the reader need this level of detail?
- Could individuals or vulnerable groups be identified?
- Could the visual put people at risk or stigmatise them?
- Will it be public, or shared with a restricted audience?

To reduce the risk:

- Aggregate to administrative areas, clusters or a [hexagon grid](../../maps/area/#hexbin-map), and make sure no area or cell holds a single household, site or person.
- Round coordinates, for example to one decimal place (roughly 10 km).
- Leave sensitive places unlabelled.
- In conflict settings, check with people who know the context before showing facilities, routes or groups.

Borders can be sensitive too. Use boundaries from a neutral, authoritative source, such as the United Nations, and draw contested borders in the [disputed border style](../../maps/basemap/#lines). Consider how the intended audience, such as a government, will read them.

## Checklist

- [ ] The data and any aggregation have been checked.
- [ ] The level of detail matches what the sample represents.
- [ ] External data is credible, documented, current and licensed for this use.
- [ ] Every source is credited, with its date.
- [ ] Differences in date, resolution or coverage are explained in a note.
- [ ] No person, household or small group can be identified, and nothing shown could put people at risk.
