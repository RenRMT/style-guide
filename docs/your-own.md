---
title: Make your own
nav_order: 8
---

# Make your own style guide

This guide is written to be copied. Most of it applies to any organisation as it is: the principles, chart limits, map rules and the brief. A few parts depend on your brand and tools. This page lists those parts and how to approach each one.

The source is on [GitHub](https://github.com/RenRMT/style_guide). Fork it, or take the structure and write your own.

## What to keep and what to change

| Part | Keep as is | Change |
|:--|:--|:--|
| [Principles](../principles/) | ✔ | |
| [Planning](../planning/) | ✔ | Swap the examples for your own domain, and rename the requester and maker roles to match your team. |
| [Colour](../colour/) | The rules | The palette itself. See [Build your own palette](../colour/build-your-own/). |
| [Typography](../typography/) | The criteria | The typeface, chosen to fit your brand and tools. |
| [Chart layout](../charts/layout/) | The element list | The positions, logo rules and template files. |
| Chart types and limits | ✔ | Tighten the limits if your audience is mostly 3-second readers. |
| [Map layout](../maps/layout/) | The element rules | The paper sizes, basemap choice and logo variants. |
| [Background](../background/) | ✔ | |

## Order of work

1. **Data palette.** Start from Okabe–Ito, shift it towards your brand, fix an order, derive ramps and test. This is the biggest job and affects everything else. See [Build your own palette](../colour/build-your-own/).
2. **Typeface.** Check your brand font against the [number criteria](../typography/#choosing-a-typeface). If it fails, pick a chart typeface that matches its character.
3. **Colour roles.** Decide which brand colour is used for titles, which grey for gridlines, and which for de-emphasised data. One table, like the one in [Colour](../colour/#which-colour-for-which-element).
4. **Templates.** Build chart and map templates in the tools your team actually uses: Excel or PowerPoint chart templates, a ggplot or matplotlib theme, a Datawrapper theme, a GIS layout. A guide without templates gets ignored.
5. **Examples.** Make one good example of each common chart type with your own data. Examples convince people more than rules do.
6. **Request process.** Publish [the brief](../planning/brief/), so requests arrive with a message, an audience and data.

## Make the rules stick

- **Keep the core short.** People read the rules but skip the theory, which is why this guide keeps the research on [separate pages](../background/).
- **Say why.** A rule with a one-line reason is followed. A rule without one gets argued about.
- **Make the right choice the default.** If your template has no chart border, nobody has to remember the "no borders" rule.
- **Review against the [principles](../principles/)** and the [checklist](../../#pre-publish-checklist), not against taste.
