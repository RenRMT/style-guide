---
title: Build and maintain
parent: Dashboards
nav_order: 5
---

# Build and maintain

How to turn these rules into a theme and starter report in your BI tool, keep a dashboard trustworthy once it's live, and keep the standard itself in shape.

## Theme and starter report

For a dashboard, the closest thing to a design system is a theme and a starter file in the tool you build in. Build them once, so nobody has to apply the rules by hand. Every new dashboard then becomes a matter of filling in a template instead of designing a report.

Theme file
: A Power BI theme (JSON), a Tableau custom palette and template workbook, or a Looker Studio theme. It sets fonts, text sizes, background, tiles, gridlines, tables, buttons, the data colours in order, and the status colours.

Category colour table
: The fixed mapping from [colour that survives filtering](../numbers-and-colour/#colour-that-survives-filtering).

Starter report
: The [grid](../plan-and-layout/#the-grid), with the header, filter rail, KPI row, bands and footer already in place, and a detail page with its subject bar.

Data-state wording
: The sentences from the [data states](../data-states/#data-states) tables, so that every tile says it the same way.

Metric glossary
: A definition, calculation, owner and refresh schedule for each measure. Where you can, build every report on one shared, documented data model, so that the same measure means the same thing everywhere.

The [REN Data design system](https://rendata.nl/design-system/site/dashboards.html) has a worked example: a Power BI theme in this guide's colours and type, the parts of a dashboard page, and what a theme can and can't set.

{: .rule }
Apply the theme first, before you add any visuals. A theme applied later doesn't override formatting a visual already has.

A theme can't do everything. Positions, conditional formatting (such as status colours), the header, the filter rail and alt text are set in each report. If you find yourself typing the same colour or size into every report, the theme is missing a case: fix the theme, not the report.

### Type in BI tools

Most BI services only show fonts that are installed on the reader's computer, so a web font such as IBM Plex Sans falls back to a default. Use Calibri, the guide's [Office typeface](../../typography/#house-typefaces): it's installed on every Windows machine and has the figures numbers need. Use bold where you'd use semibold, because most tools offer only regular and bold. Keep all text at 10.5 pt or larger, including the source line.

## Trust and upkeep

- Show freshness. Put the last-updated time in the header, and flag stale data if a refresh fails.
- Make it screenshot-proof. A screenshot of the page will end up in a memo. Cut off from its filters, it must still say which period and selection it shows and how recent the figures are. That's what the header line and the footer are for, and why they come from the data. A dashboard that can't be screenshotted gets quoted wrongly.
- Define every measure. Link to the glossary from the dashboard, and version definitions when they change, so that past figures stay comparable.
- Make it accessible. Meet the contrast rules, provide keyboard access to filters, and offer the data as a table or download.
- Check it on real devices. Check load time and layout at the screen sizes your readers use, including phones if they use them.
- Retire what isn't used. Review usage once or twice a year. Remove tiles and dashboards that nobody looks at.

## Deviations

Brand guidelines and design systems are made for web pages and print, not for report canvases. Where they clash with what a dashboard needs, the dashboard wins: a readable dashboard that's 95% on brand is worth more than an unreadable one that's 100% on brand.

{: .rule }
Fix it in the standard, not only in your report. A workaround in one file is invisible three months later; a written rule isn't. Keep a list of deliberate deviations, each with its reason and what to build instead, and make every new one an entry on that list.

## Measuring the payoff

A dashboard standard exists to make dashboards cheaper and more useful, not prettier. Measure two things over a quarter:

1. Hours per dashboard request, from start to delivery. This should go down. If it doesn't, the standard isn't earning its place.
2. Use after delivery: how often each dashboard is opened, by how many people, over the first eight weeks. Low use is a reason to build fewer dashboards and spend the time on analysis instead.

{: .adapt }
If you build dashboards as web pages in your own brand, take the interface from your design system and keep the visual rules from this guide. Build the theme and starter report once for each BI tool your team uses.
