---
title: Data and colour
parent: Dashboards
nav_order: 2
---

# Data and colour

How to give every number context, use status colours, keep colour and scales consistent across tiles and filters, and design for data you haven't seen yet.

## KPIs and status

{: .rule }
Every number on the page carries a comparison. "€42.6 million" says nothing; "€42.6 million, 61% of budget" does. Four comparisons work:

- **Against a target:** is it on course?
- **Against the previous period:** is it moving the right way?
- **Against the baseline:** have we achieved anything since we started?
- **Against the rest:** is this a lot or a little, compared with the other programmes, regions or teams?

Which one to use is a decision about content, not formatting. Say what a percentage is measured against. Progress against this quarter's target and progress against the final goal give different answers, and mixing them up makes a programme that's ahead of schedule look behind.

- Show the comparison as a number with a sign (+6%) or as a short phrase ("On target (85)"), not with an arrow alone.
- Add a sparkline when the trend matters as much as the value.
- Use a **bullet chart** or a progress bar to show progress towards a target. Fix its ends at zero and the target. A bar that scales automatically always ends up somewhere between empty and full, and says nothing.

{: .avoid }
Don't use gauges, speedometers or dials. They take a lot of room to show one number, and readers judge angles poorly. Use a big number with a comparison, or a bullet chart.

### Status colours

Status colours are kept for one job: showing where a measure stands. Never use them for decoration.

| Status | Colour | Sign | Word, for example |
|:--|:--|:-:|:--|
| On track | Baltic `#2B5B9B` | ✓ | "On track", "On target (85)" |
| Watch | Jasmine `#FFDD77` | ! | "Watch", "Close to target" |
| Off track | Cherry `#BC3C4C` | ✕ | "Off track", "Above target (20%)" |
| Completed | Sky `#88CCFF` | ◍ | "Completed", "Closed" |
| No data, or no target | Steel `#B8B8B8` | – | "No data" |

{: .rule }
Every status has a colour, a sign and a word. Show it as a small square in the status colour with the sign inside, followed by the word. Draw the sign in white on Baltic and Cherry, and in black on the light colours, so it stays readable.

- In a table, the status can also be a light tint of its colour behind the cell. Use the tint or the square, not both.
- Show statuses in this order everywhere: on track, watch, off track, completed, no data. If a chart's legend can't follow that order, turn it off and write the statuses beside the chart in order.
- The status colours are also [data colours](../../colour/categorical/). A chart shows status or categories, never both. On a page with status, draw category charts in colours that aren't status colours: Teal and its ramp, Coral, Violet or Blush, with Steel for context.

{: .why }
"On track" uses blue rather than green. Teal and Cherry are hard to tell apart for many colour-blind readers, while Baltic and Cherry stay distinct for all common types of colour-vision deficiency. "Completed" is Sky rather than a second dark blue for the same reason. Even so, the sign and the word carry the meaning, and the colour only reinforces it.

## Consistency across tiles

Readers compare tiles to each other, so differences between tiles read as differences in the data.

- **Colour:** a category keeps the same colour on every tile. If "Denied or delayed" is Coral in the trend, it is Coral in the breakdown too.
- **Scales:** tiles that readers will compare share the same axis range.
- **Numbers:** use the same units, rounding and number format everywhere.
- **Periods:** every tile covers the period shown in the header, unless its subtitle says otherwise.
- **Order:** sort categories by value, not alphabetically. Alphabetical order chooses to give no information. When the categories have their own order, such as periods, levels or statuses, follow it.
- **Labels or axis:** label the data or show a value axis, not both. Labels suit a few points; an axis suits many.

## Colour that survives filtering

The [colour order](../../colour/categorical/#colour-order) works because someone checks the finished chart. On a dashboard, a filter can remove the first category, and every colour after it shifts along. "North" is Teal in one view and Jasmine in the next, and readers take a change of colour as a change of category.

{: .rule }
Tie each colour to a category, not to its position. Keep a fixed table that gives every category value a colour, and apply it on every tile, under every filter.

- Assign colours in the colour order, by importance or by the usual sort order, then freeze the table. A new category gets the next free colour and leaves the existing ones alone.
- Keep Steel for "Other", "Unknown" and context, as on any chart.
- The limits don't change: no more than eight colours. If a filter can show twenty regions, use the [highlight pattern](../../colour/categorical/#how-many-colours) or top five plus "Other", not twenty colours.
- Set the colours in one place, not by hand on each chart. Tableau keeps a field's colour assignment across every sheet that uses it. In Power BI, theme colours follow position, so store each category's colour in a column and apply it with conditional formatting.

## Data you haven't seen

You check a chart before you publish it. Nobody checks every filter combination on a dashboard, or next month's data. Design each tile for the data it might get, not only the data it has today.

### Data states

Decide in advance what each tile shows in each state, and use the same wording on every tile. The tile keeps its title, and a sentence replaces the chart. Never leave the tool's own message: it's generic, often in the wrong language, and says nothing about why.

There are three kinds of empty, and they mean different things. A reader who can't tell them apart draws the wrong conclusion.

| State | Means | Show |
|:--|:--|:--|
| **No data** | Nothing was measured | "No data", and why: "This programme reports twice a year. Next report due 15 January." |
| **No results** | There is data, but the filters exclude it | "No results for these filters", and the way out: "Clear the region filter to see all regions." |
| **Error** | Something broke | What failed and the last good refresh: "The incidents data didn't load. Last refreshed 27 October." |

The other states:

| State | Show | For example |
|:--|:--|:--|
| Loading | The tile's title and an empty chart area | |
| No access | Empty, with an explanation. Never an error, and never all the data | "You don't have access to programme data for this region." |
| Zero | The chart, with the zero shown and labelled | A bar at 0, labelled "0" |
| Missing values | A gap in the line, a dash in a table, or a Steel "No data" category | "No data" in the legend or a note |
| Partial period | The value, with a dashed line or lighter fill | "Partial week" |
| Stale | The last good data, with a warning next to the update time | "Not updated since 21 October: source delayed." |
| Too few to show | Nothing, and the reason | "Fewer than 5 cases. Hidden to protect privacy." |

{: .rule }
Never show missing data as zero. A zero says nothing happened. A gap says nobody knows. A dashboard about 17 of 31 programmes that doesn't say so is wrong.

Show a refresh warning in one place: one line under the header, or in the affected tile. The same warning twice on one screen reads as two problems.

### Labels and scales that hold up

- A title that includes a filter value ("Incidents in {region}") must still read well with the longest value, and with "All".
- Wrap or abbreviate long category names consistently. Don't cut them off mid-word.
- A filter that removes the largest value rescales a floating axis. Fix the axis where readers compare selections, and let it float only where the shape matters more than the size.
- Show the top categories plus "Other", so a filter can't produce a chart with thirty bars.
- Bars still start at zero, whatever the data. If a value axis doesn't start at zero, the subtitle says why.
- Fix the zoom and frame of a map, so it doesn't move with every filter. Colour areas with no data Steel on purpose: left white, they look like zero.
- Give table columns fixed widths. Automatic widths jump with every filter change, and two screenshots of the same table can't be compared.

### Test the states, not the picture

You check a static chart by looking at it. You check a dashboard by going through the states a reader can reach and you haven't seen. Before you publish, check:

- [ ] **The opening view,** with no selection. Is every number right, and does it say which period?
- [ ] **One selection at the deepest level.** Are the totals still right?
- [ ] **A selection with no results.** Does the no-results message appear, with a way out?
- [ ] **The first period in the data.** A comparison with "the previous period" mustn't fall back to zero.
- [ ] **The latest period, still running.** Does it say it's incomplete?
- [ ] **An item that reports late.** Does it show as No data, or carry over its last value? Is that what you intended?
- [ ] **A reader without access.** Empty with an explanation, not an error, and certainly not everything.
- [ ] **The longest names and an outlier.** Do labels and scales hold up?
- [ ] **A screenshot,** without the filters around it. Does it still say what it shows, for when and for whom?

If one of these fails, it's rarely a formatting problem. It's a calculation that's wrong at one level, or text that was typed where it should come from the data.

{: .adapt }
Swap the status colours for your own palette's blue (or other colour-blind-safe "good"), yellow, red and a light colour for "completed", and test all five together with a colour-blindness simulator. Keep the signs and words as they are.
