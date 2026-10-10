# Style guide

A data visualisation style guide: practical rules first, theory in a separate Background section, and notes throughout on adapting it into your own guide. Built with Jekyll and the just-the-docs theme, hosted on GitHub Pages at [rendata.nl/style-guide](https://rendata.nl/style-guide/).

The colours also live in the [interactive colour picker](https://rendata.nl/color-picker/).

## Structure

| Path | What |
|---|---|
| `index.md` | Home: the short version and the pre-publish checklist |
| `docs/` | The guide. Each folder with an `index.md` is a section in the sidebar. |
| `docs/background/` | Theory and research, linked from the practical pages via `{: .why }` callouts |
| `_data/palette.json` | All colours. Generated, so don't edit it by hand. |
| `_includes/swatches.html`, `ramp.html`, `diverging.html` | Render colour swatches from the palette data |
| `_sass/color_schemes/ren.scss`, `_sass/custom/custom.scss` | Site theme, matching rendata.nl |
| `resources/` | Source documents. Not committed and not published. |

## Updating colours

Colours are defined once, in the color-picker repository (`ren.json`). After changing them there, run:

```sh
python tools/sync_palette.py ../color-picker/ren.json
```

## Callouts

Put one of these above a paragraph: `{: .rule }`, `{: .avoid }`, `{: .adapt }` (notes for people building their own guide) or `{: .why }` (a link to the background).
