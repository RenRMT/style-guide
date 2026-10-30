---
title: Navigation and interaction
parent: Dashboards
nav_order: 2
---

# Navigation and interaction

How readers move between pages and items, and how to keep filters and other interaction predictable.

## Pages and navigation

A dashboard with more than one page has two kinds of navigation. Keep them on separate controls, or the dashboard works in one direction and gets stuck in the other.

| | Which view | Which item |
|:--|:--|:--|
| **Example** | Overview, Finance, Results | One programme out of thirty |
| **Control** | Page tabs in the header | A subject bar at the top of each detail page, with a picker |
| **Behaviour** | Always visible | The chosen item stays when the reader changes page |

- **Overview pages** filter a *population*: which programmes, which period. They have the filter rail.
- **Detail pages** show *one item*. They have a subject bar instead of a rail, with the item's name, its status, its position ("4 of 12") and a picker. A detail page that doesn't say which item it shows can't be fixed once it's a screenshot.

The picker depends on how long the list is:

| Items | Picker |
|:--|:--|
| Up to about 25 | A dropdown, everything visible |
| 25 to 500 | A dropdown with search. Filter on the overview first |
| More than 500 | No dropdown. Show the name and position, and let readers click through from a filtered table |

## Interaction

{: .rule }
The default view is the report. Most readers never touch a filter: they open the page, look for ten seconds and move on. The page as it opens must answer the main question on its own, and filters are for the few who dig further.

{: .rule }
Interaction is a cost, not a feature. Each filter hands a decision to the reader. Three filters is a choice about what to hand over; ten is refusing to choose. Ask which question each interaction answers, and whether readers actually have that question.

- Put filters in one place and always show the current selection. Use at most three, with an Apply and a Clear button when there are more than one.
- Use tooltips for extra detail, such as exact values or definitions. Never put information a reader needs only in a tooltip, because it is invisible on touch screens and in screenshots.
- Decide for each pair of tiles whether clicking one filters the other. Most tools turn this on everywhere by default, which confuses more often than it helps. Make it work the same way everywhere, and give readers an obvious way to reset.
- Say which tiles a filter affects. If one tile ignores the region filter, its subtitle says so ("All regions").
- Where the tool allows it, keep the filter selection in the link, so readers can share exactly the view they're looking at.
