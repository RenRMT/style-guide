---
title: Fluency
layout: default
parent: Design principles
nav_order: 6
---
# Processing fluency & cognitive load

## Insights from processing fluency research

Most research supports the anecdotal idea that the way our data visualizations looks can strongly influence how people think about the information it shows. When a chart is very easy to read people are more likely to trust it and accept the message without questioning it. This means that visuals should have clear text, strong contrast, and “feel right”

On the other hand, if a design is too smooth and familiar, readers may overlook mistakes or misleading elements. Finally, mismatched visual styles can subtly shift how viewers feel about the data they are presented with. Good data visualization design should use fluency to make data clear, but we should avoid slick-looking data visualizations if we cannot ensure that what we’re presenting is correct.

### Prioritize readability to support accurate interpretation.

Highly legible colours, clear contrast, and clean typefaces make information easier to process; and people are more likely to trust content that is easy to read. Avoid low visibility colour combinations or overly decorative fonts unless you intentionally want to slow the reader down.

### Be aware that ease of reading can bias truth judgments.

When text is visually fluent, people may interpret the feeling of ease as a signal that the information is true or familiar. Ensure that high fluency design accompanies accurate, high quality information.


### Use reduced fluency strategically when deeper thinking is required.
Harder to read text can prompt more analytic processing. This can help viewers spot inconsistencies, misleading claims, or surprising insights. This is an interesting insight, but it is questionable whether this should actively be applied in data visualisation.

### Match presentation to the message.

Visualisation elements such as typeface or colour convey emotional tone before people fully read the content. Make sure your design choices reinforce your message. Avoid pairing emotionally incongruent design elements with the content you want to communicate.

### Ensure perceptual differences are intentional and meaningful.

Small visual differences between similar fonts or colours may not produce meaningful effects. Make deliberate, clear choices when emphasizing or differentiating information.

### Use naming, labels, and terminology that are easy to process.

Hard to read or hard to pronounce labels can be misinterpreted as unfamiliar or risky. When designing legends, category names, or metrics, choose terminology that is simple, clear, and pronounceable.

### Design with awareness that readers rely on intuitive, feeling based cues.

Visual fluency shapes judgments about truth, familiarity, safety, risk, and emotional tone. Ensure your design supports the kind of intuitive reaction you want the viewer to have.


## Insights from cognitive load research

Data visualizations create cognitive load when viewers must interpret legends, axes, scales, colour schemes, or unfamiliar chart types. When the insight is trivial, this effort feels unnecessary and reduces trust and engagement; when the insight is meaningful, the cognitive investment feels justified.

To improve effectiveness, designers should minimize extraneous effort by using clean, high contrast visuals and intuitive encodings, keeping decorative elements to a minimum, and placing labels close to the data. The visualization’s key message should be immediately visible: highlight the central pattern without letting aesthetics overshadow clarity. Visual style must also match the content, with colour and hierarchy reinforcing the tone and relative importance of the information.

Managing complexity is essential. Chunk information into multiple panels, use progressive disclosure, or rely on small multiples rather than a single dense chart. Guide attention purposefully through selective highlighting, annotations, and contextual markers like baselines or thresholds.

Ultimately, any cognitive load placed on the viewer must pay off. Use complex visuals only when they reveal insights that simpler forms cannot and always consider whether the viewer’s effort is warranted by the value of the insight.

### Design for the audience, not the analyst.

Exploratory charts can be messy because the creator understands the data, but explanatory charts used in reports must guide unfamiliar readers. Always design with the viewer’s knowledge, context, and needs in mind.

### Reduce extraneous cognitive load by removing anything that doesn’t help comprehension.

Clutter, decorative elements, ambiguous labels, unnecessary 3D effects, and overly complex chart types all force the audience to spend working memory on presentation instead of meaning. Streamline visuals so all attention goes to the message.

### Guide the viewer’s eye and highlight the “why.”

Use clear titles, annotations, thresholds, callouts, and visual hierarchy to show what matters most. Don’t make people figure out the point of the chart. Instead state the key takeaway explicitly.

### Structure visualizations like a story.

Organize charts so they unfold logically and match audience mental models. Sequence information intentionally, use consistent design choices, and group related data to reduce unnecessary mental effort.

### Match chart type to the message.

Choose simple, conventional forms that align with the relationship you want to show (e.g., bars for comparisons, lines for trends, scatterplots for relationships). Avoid novelty where it adds complexity without insight.

### Account for intrinsic load but optimize what you can control.

Some datasets are inherently complex. You can’t change the data, but you can simplify how it’s presented, add context, or break it into digestible pieces to prevent overload.

### Adapt design based on the audience’s expertise (germane load).

### Novices need more explanation, context, and simplification; experts can handle denser detail. Tailor labels, terminology, and the complexity of visuals accordingly.

### Use cognitive load spectrums instead of rigid rules.

Effective visualization is about balancing data complexity, audience familiarity, and design choices. There are no universal rules, only context specific adjustments.

### Ensure ethical and accurate communication.

Avoid distortions such as truncated axes, misleading colour scales, cherry picked timeframes, or effects that exaggerate differences. Clarity and honesty reduce unnecessary cognitive effort and prevent misinterpretation.

# References (processing fluency)

* Reber, R. & Schwarz, N. (1999) ‘Effects of perceptual fluency on judgments of truth’, Consciousness and Cognition, 8, pp. 338–342.
* Song, H. & Schwarz, N. (2008) ‘Fluency and the detection of misleading questions: Low processing fluency attenuates the Moses illusion’, Social Cognition, 26(6), pp. 791–799.
* Hazlett, R.L., Larson, K., Shaikh, A.D. & Chaparro, B.S. (2013) ‘Two studies on how a typeface congruent with content can enhance onscreen communication’, Information Design Journal, 20(3), pp. 207–219.
* Song, H. & Schwarz, N. (2009) ‘If it’s difficult to pronounce, it must be risky: Fluency, familiarity, and risk perception’, Psychological Science, 20(2), pp. 135–138.

# References (cognitive load)

* data.europa.eu (2026) Data communication. Available at: https://data.europa.eu/apps/data-visualisation-guide/data-communication
* Sibinga, E. & Waldron, E. (2021) Cognitive Load as a Guide: 12 Spectrums to Improve Your Data Visualizations. Nightingale. Available at: https://nightingaledvs.com/cognitive-load-as-a-guide-12-spectrums-to-improve-your-data-visualizations/
* Turning Data Into Wisdom (2025) Clear Data Visualization – Reducing Cognitive Load & Preventing Misunderstanding. Available at: https://www.turningdataintowisdom.com/content/files/2025/05/data-visualization-design-guide-1.html
* Szafir, D.A. & Szafir, D. (2016) Cognitive Load in Visualization: Myths & Misconceptions. University of Colorado Boulder. Available at: https://cmci.colorado.edu/visualab/papers/16-c4pgv-cogload.pdf