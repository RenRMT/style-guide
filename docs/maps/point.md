---
title: Point maps
parent: Maps
nav_order: 4
---

# Point based maps

Point-based maps are used to show information at specific locations. This type of map is useful when the exact position of events or values matters and when the data represent discrete occurrences rather than continuous surfaces.
Dot density, proportional symbol, and diagram maps are all point based techniques, but each serves a different purpose.

- Dot density maps show the distribution of many individual events or items by placing dots inside an area, with each dot representing a fixed amount. 
- Proportional symbol maps use the size of a symbol to show how large a value is, making them suitable for absolute quantities. 
- Diagram maps attach small charts such as pie charts or bar graphs to locations when several variables need to be shown at the same point. 

When designing these maps, it is important to choose visual elements carefully. Dot density maps must make clear that dots are randomly placed within an area unless exact coordinates are available. Proportional symbol maps often need transparent symbols so that overlapping values remain visible. Diagram maps should only include a few variables to avoid overwhelming the reader. All point based maps rely on visual cues such as size, colour, shape, and position. Size is the most effective way to show quantitative differences, while colour and shape help distinguish categories. These techniques should not be used for continuous phenomena or when too many variables would make interpretation difficult.

## Examples:

- Dot density maps can show the spread of individual conflict events, such as each dot representing a recorded security incident to reveal clusters of violence.
- Proportional symbol maps can display absolute numbers, for example the number of displaced people at each site or the number of conflict related fatalities in each locality.
- Diagram maps can attach small charts to locations, such as a pie chart showing the mix of conflict event types in each district.

## Checklist for using visual variable types

1.	Determine the purpose.
    * Showing quantities -> size
    * Showing categories -> colour or shape
    * Showing intensity or density -> transparency, clustering, or binning
2.	Limit the number of meanings carrying variables.
    * Use one primary variable; apply others only for legibility.
3.	Address overplotting.
    * Use transparency.
    * Apply cluster markers or hex/grid binning.
    * Jitter points when exact positions are not critical.
4.	Consider how people perceive symbols
    * Limit to a small number of recognisable shapes.
    * Make sure size differences are clearly visible.
5.	Test across zoom levels.
    * Check that symbols stay clear and meaningful when zoomed in or out.
