---
title: Dashboards
nav_order: 9
has_children: true
---

# Dashboards

A dashboard brings several big numbers, charts and sometimes a map together on one screen, so that people can check the same measures again and again. It answers "how are we doing?" at a glance and shows where to look next.

Everything else in this guide still applies to each tile. This section covers what changes when the visuals share a screen and the data keeps updating.

| Use a dashboard when… | Don't use one when… |
|:--|:--|
| The same people check the same measures regularly | The message is a one-off finding. Write it up as a chart in a report |
| The data refreshes daily, weekly or monthly | The data changes once a year |
| Readers need to monitor several related measures side by side | One or two numbers would do. Use [big numbers](../big-numbers/) |
| Readers need to filter to their own region, team or period | Nobody has said which decisions it supports |

## Between a style guide and a design system

A dashboard sits between two kinds of guidance. This guide covers each visual: what it shows, and how it shows the data honestly and clearly. A design system, such as the [REN Data design system](https://rendata.nl/design-system/site/), covers the interface around the visuals: cards, filters, buttons, type, spacing and colour tokens for a website or app. A dashboard needs both, and a few things that neither covers.

| | Style guide | Design system | What a dashboard adds |
|:--|:--|:--|:--|
| **Governs** | One visual with a fixed message | Components that work for any content | Many visuals on data that keeps changing |
| **Who checks the result** | The author, before publishing | The developer, component by component | Nobody sees every filter combination |
| **Colour** | Data colours, in a fixed order | Brand and interface colours | Colours tied to categories, and status colours |
| **Built in** | Chart tools, Excel, R, Python | HTML, CSS, components | Power BI, Tableau, Looker Studio, or a web page |

Which one to follow depends on where you build the dashboard:

- **For a client:** follow this guide for the visuals and the client's brand for everything else. The grid, the parts of the page and the status rules in this section still apply; swap the colours and the typeface.
- **In your own brand:** take the interface (tiles, filters, type, spacing) from your design system, and the visuals from this guide. Don't rebuild web components in a BI tool: translate the design system's rules into a theme instead. The [REN Data design system](https://rendata.nl/design-system/site/dashboards.html) does this, with a stylesheet for web dashboards and a theme for Power BI.

{: .rule }
When the two disagree, this guide decides how the data is shown and the design system decides everything around it. The REN Data design system takes its chart rules from this guide for that reason.

The pages in this section cover what a dashboard needs on top of both:

| Page | Covers |
|:--|:--|
| [Plan and layout](plan-and-layout/) | Purpose, one question per visual, the grid, titles on live data |
| [Navigation and interaction](navigation-and-interaction/) | Pages and items, pickers, filters, cross-filtering, the default view |
| [Numbers and colour](numbers-and-colour/) | Comparisons, status colours, consistency across tiles, colour that survives filtering |
| [Data states and testing](data-states/) | Empty, missing, partial and stale data, labels and scales that hold up, the states to test |
| [Build and maintain](build-and-maintain/) | A theme and starter report in your BI tool, type in BI tools, trust and upkeep, deviations, measuring the payoff |

{: .why }
This section draws on Few's definition of a dashboard as a single screen you take in at a glance, on the dashboard patterns catalogued by Bach et al. (2023), and on Shneiderman's "overview first, zoom and filter, then details on demand". See [references](../background/references/).
