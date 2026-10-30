---
title: Build your own palette
parent: Colour
nav_order: 4
---

# Build your own palette

Your brand colours will almost never work as data colours. A brand palette usually has too few colours, and they are too similar in lightness, too saturated, or not colour-blind safe. Build a separate data palette instead, in the steps below. It takes about a day, and you can reuse it for years.

## 1. Start from a colour-blind-safe palette

Don't start from your brand colours. Start from a palette that was designed and tested for colour-vision deficiencies. The best general-purpose starting point is the Okabe–Ito palette:

<div class="swatches">
<div class="swatch" style="background:#E69F00;color:#191919"><span class="swatch__name">Orange</span><code class="swatch__hex">#E69F00</code></div>
<div class="swatch" style="background:#56B4E9;color:#191919"><span class="swatch__name">Sky blue</span><code class="swatch__hex">#56B4E9</code></div>
<div class="swatch" style="background:#009E73;color:#191919"><span class="swatch__name">Bluish green</span><code class="swatch__hex">#009E73</code></div>
<div class="swatch" style="background:#F0E442;color:#191919"><span class="swatch__name">Yellow</span><code class="swatch__hex">#F0E442</code></div>
<div class="swatch" style="background:#0072B2;color:#FFFFFF"><span class="swatch__name">Blue</span><code class="swatch__hex">#0072B2</code></div>
<div class="swatch" style="background:#D55E00;color:#FFFFFF"><span class="swatch__name">Vermillion</span><code class="swatch__hex">#D55E00</code></div>
<div class="swatch" style="background:#CC79A7;color:#191919"><span class="swatch__name">Reddish purple</span><code class="swatch__hex">#CC79A7</code></div>
<div class="swatch" style="background:#000000;color:#FFFFFF"><span class="swatch__name">Black</span><code class="swatch__hex">#000000</code></div>
</div>

It has eight colours, works for the common forms of colour blindness, and has a good spread of lightness. Many published style guides are visibly based on it.

| Alternative | When to consider it |
|:--|:--|
| [Paul Tol's schemes](https://sronpersonalpages.nl/~pault/data/colourschemes.pdf) | You want a muted, scientific look. Tol's colours are already dark and desaturated, so it is harder to derive light ramps from them. |
| [IBM Design Language](https://www.ibm.com/design/language/color/) | You need only about five categories. |
| [ColorBrewer](https://colorbrewer2.org) | You mainly need sequential and diverging ramps for maps. |

## 2. Shift it towards your brand
{: #shift-towards-your-brand }

Move each colour a little in hue, saturation or lightness until the set feels like it belongs to your brand. Keep the overall structure: a spread of hues, a spread of lightness, and no two colours that are nearly identical.

- Replace black with a neutral grey. Black is far darker than the other colours. A mid grey sits better beside them and doubles as the "de-emphasised" colour.
- Reduce saturation for print. Highly saturated colours print poorly and feel loud on screen. Desaturate them slightly, or move them towards pastel by adding white.
- Swap out the weakest colour. If one colour contrasts poorly with the rest, or clashes with your brand, replace it. This may cost a little colour-blind safety, so test the result (step 5).
- Keep data colours distinct from brand colours. Make your main data colour a slightly different shade from your primary brand colour, so readers can tell data from branding.

I made this guide's palette this way. The table shows roughly where each colour came from:

| Okabe–Ito | | This guide |
|:--|:-:|:--|
| Bluish green `#009E73` | → | Teal `#338877`, desaturated and the main data colour |
| Yellow `#F0E442` | → | Jasmine `#FFDD77`, warmer and softer |
| Blue `#0072B2` | → | Baltic `#2B5B9B`, darker and closer to navy |
| Orange / vermillion | → | Coral `#FF9779` and Cherry `#BC3C4C` |
| Sky blue `#56B4E9` | → | Sky `#88CCFF`, lighter |
| Reddish purple `#CC79A7` | → | Blush `#FFBBDD`, lighter |
| Black `#000000` | → | Steel `#B8B8B8` (neutral), plus a new Violet `#8833AA` |

## 3. Fix an order

Decide the order in which colours are added, so two-colour charts always look the same. Make each colour contrast as much as possible with the ones before it, so the first few colours are the most distinct. Offer one order only.

## 4. Derive ramps

For each data colour, make a ramp of about ten steps from near-white to near-black, with the base colour in the middle. Mix the base colour with white for the light steps and with black for the dark steps. Then fix which steps to use for 2, 3, 4… classes, so that nobody picks shades by eye. See [Sequential](../sequential/#which-steps).

Check each ramp's lightness. A ramp whose base colour is already light, such as yellow or pink, produces light steps that look the same. Either darken the base colour or use only the dark half of that ramp.

## 5. Test it

| Test | How | Pass when |
|:--|:--|:--|
| Colour blindness | Simulate protanopia, deuteranopia and tritanopia in [Viz Palette](https://projects.susielu.com/viz-palette) or [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/). | The first four or five colours stay distinguishable in every simulation. |
| Greyscale | Desaturate a sample chart. | Neighbouring colours differ in lightness. |
| Contrast | Check each colour against your background with a WCAG contrast checker. | Colours used for lines and text reach 3:1 or more, or you have reserved the light colours for fills. |
| Print | Print a sample chart and a map. | Colours aren't muddy and the light steps are still visible. |
| Real charts | Make a bar chart, a line chart and a choropleth with real data. | Nothing looks wrong to you or a colleague. |

## 6. Document and publish

Give every colour a short, memorable name (not "Data 3"), its hex code, its role, and its place in the order. Then publish the palette where people work:

- in the style guide, as this site does
- as Office theme colours or a chart template
- as CSS variables or code constants
- in an interactive picker. The [colour picker](https://rendata.nl/color-picker/) used here reads a single JSON file per palette. Copy one, edit the colours, and you have your own.

{: .why }
For the research behind these steps, such as how many colours people can distinguish and why saturated colours print poorly, see [Colour research](../../background/colour-research/).
