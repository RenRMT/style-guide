---
title: Basemaps and symbols
parent: Maps
nav_order: 2
---

# Basemaps and symbols

## Basemap

Choose the simplest, least detailed basemap that still supports the message. To decide, ask:

- What is the map trying to show, and to whom?
- Will it be printed or viewed on screen?
- Does the basemap compete with the data for attention?

| Basemap | Use when | Notes |
|:--|:--|:--|
| **Country outline** (shapefile or polygons) | No context outside the country is needed. This suits most integrated maps. | Show admin divisions only if the message needs them, and only at the level of the data: admin-1 data gets admin-1 boundaries. |
| **World outline** | The country needs geographic context, but the map needs no detail. | Add rivers and lakes only if the message needs them. A light hillshade is fine for terrain-dependent data. |
| **Light grey vector basemap** (for example, ArcGIS Light Gray Canvas) | Readers need place names and roads for orientation. | The first choice among vector basemaps: enough detail, without drawing attention. |
| Streets or topographic | The purpose requires detailed location or navigation context. | Use with care, as it competes with the data. |
| Terrain or hillshade | Terrain is part of the message. | |
| Imagery | The data is remote sensing or environmental. | Raster imagery blurs when zoomed in. |

{: .avoid }
Don't use a detailed, colourful basemap by default. It's the most common reason a map looks busy.

## Lines

- **Primary lines** are the subject of the map, such as a key route or a road used by aid convoys. Draw them clearly, on top of everything else.
- **Secondary lines** are context, such as roads near incidents or rivers. Draw them thin and subtle, in Steel or a light blue.

## Polygons

- Use at most two levels of nested admin boundaries, such as country plus province.
- To avoid crowding, label only the smallest admin level shown.
- Fill standalone polygons, such as lakes or affected areas, in a colour that clearly separates them from the admin areas.

## Icons

Avoid icons in general. Use one only when it is the clearest way to show something, such as an ✕ for a road blockage. Keep icons few, simple and explained.

{: .why }
Visual variables (position, size, colour, shape and so on) each suit different kinds of data. See [Visual variables](../../background/visual-variables/).
