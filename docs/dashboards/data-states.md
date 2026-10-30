---
title: Data states and testing
parent: Dashboards
nav_order: 4
---

# Data states and testing

How to design for data you haven't seen yet: empty, missing, partial and stale data, labels and scales that hold up, and the states to test before you publish.

You check a chart before you publish it. Nobody checks every filter combination on a dashboard, or next month's data. Design each tile for the data it might get, not only the data it has today.

## Data states

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

## Labels and scales that hold up

- A title that includes a filter value ("Incidents in {region}") must still read well with the longest value, and with "All".
- Wrap or abbreviate long category names consistently. Don't cut them off mid-word.
- A filter that removes the largest value rescales a floating axis. Fix the axis where readers compare selections, and let it float only where the shape matters more than the size.
- Show the top categories plus "Other", so a filter can't produce a chart with thirty bars.
- Bars still start at zero, whatever the data. If a value axis doesn't start at zero, the subtitle says why.
- Fix the zoom and frame of a map, so it doesn't move with every filter. Colour areas with no data Steel on purpose: left white, they look like zero.
- Give table columns fixed widths. Automatic widths jump with every filter change, and two screenshots of the same table can't be compared.

## Test the states, not the picture

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
