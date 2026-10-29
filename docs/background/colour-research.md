---
title: Colour research
parent: Background
nav_order: 4
---

# Colour research

## Criteria

I designed the data palette against three criteria, in order of importance:

1. **Clear visual language.** The colours form clearly identifiable categories, the ramp steps are easy to tell apart, and there are enough colours for most needs.
2. **Accessibility.** The palette works with common colour-vision deficiencies, the colours contrast enough with each other and with the background, they stay distinguishable in greyscale, and they work in print and on screen.
3. **Aesthetics.** Only once the first two criteria are met: alignment with the brand, and a pleasant, professional look. These judgements are subjective.

## Starting point

I compared three palettes designed for colour-blind readers: IBM, Okabe–Ito and Paul Tol's. IBM has too few colours, and Tol's are too dark to derive light ramps from. Okabe–Ito was the most flexible. Many published style guides (UNHCR, the WHO, the Urban Institute and the CFPB among them) also follow it to some degree.

I then desaturated the colours for print, replaced black with a neutral grey, and added a purple, Violet. Violet costs a little colour-blind safety next to Baltic, but gives a fourth dark colour for lines. See [Build your own palette](../../colour/build-your-own/#shift-towards-your-brand) for how each colour was derived.

## Why a fixed order

No palette lets every colour contrast strongly with every other. Style guides solve this either by prescribing fixed combinations for each number of colours, or by fixing the order in which colours are added. A fixed order is simpler, and keeps visuals consistent: two-colour charts always use the same two colours. This guide's order maximises the difference between each colour and the ones before it.

## How many colours and steps

- **Categorical:** people can distinguish more than eight hues in some chart types, especially bar charts (Szafir, 2018). But that many categories causes other problems: clutter, small marks and long legends. Eight is the practical maximum.
- **Sequential:** accuracy drops beyond about seven steps, and five or six is safer (Tseng et al., 2024).
- **Diverging:** accuracy drops beyond about nine steps (Tseng et al., 2024).

## Palette test results

I checked the palette with simulated protanopia, deuteranopia and tritanopia (Machado et al., 2009), and measured the colour difference (ΔE, CIELAB) between every pair of base colours:

| Colours used | Worst pair | Result |
|:--|:--|:--|
| First 2 (Teal, Jasmine) | | Clearly distinct for all types |
| First 3–5 | Teal–Baltic, under tritanopia (a rare type) | Distinguishable |
| 6 | Teal–Cherry, under protanopia | Hard to tell apart |
| 8 | Baltic–Violet, under deuteranopia | Nearly identical |

Hence the rule in [Categorical](../../colour/categorical/#how-many-colours): up to five colours are safe without extra help, and from six on, label directly or add shapes.

Contrast against white: Teal 4.3:1, Baltic 6.8:1, Cherry 5.4:1, Violet 6.8:1, Coral 2.1:1, Sky 1.7:1, Blush 1.6:1, Jasmine 1.3:1. The four light colours are for fills only.

---

Sources: Okabe & Ito (2008); Tol (2018); IBM Design Language; Szafir (2018); Tseng et al. (2024); Machado, Oliveira & Fernandes (2009); Brewer (1994). See [references](../references/).
