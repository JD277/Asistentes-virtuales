
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os

# Create a presentation object
prs = Presentation()

# --- Slide 1: Title Slide ---
slide_layout = prs.slide_layouts[0]  # Title slide layout
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "The Legend of Zelda: A Journey Through Hyrule"
subtitle.text = "An Overview of the Iconic Series"

# --- Slide 2: Introduction ---
slide_layout = prs.slide_layouts[1]  # Title and Content layout
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "What is The Legend of Zelda?"

tf = body.text_frame
tf.text = "A beloved action-adventure fantasy series created by Nintendo."

p = tf.add_paragraph()
p.text = "Follows the hero Link on his quest to save Princess Zelda and Hyrule from the evil Ganon (or Ganondorf)."
p.alignment = PP_ALIGN.LEFT

p = tf.add_paragraph()
p.text = "Known for its exploration, puzzles, combat, and compelling story."
p.alignment = PP_ALIGN.LEFT

# --- Slide 3: Key Characters ---
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "Key Characters"

tf = body.text_frame
tf.text = "Link: The Hero of Hyrule, destined to wield the Master Sword and defeat evil."

p = tf.add_paragraph()
p.text = "Zelda: The Princess of Hyrule, often possessing wisdom and magical abilities."
p.alignment = PP_ALIGN.LEFT

p = tf.add_paragraph()
p.text = "Ganon/Ganondorf: The primary antagonist, a powerful sorcerer seeking to conquer Hyrule."
p.alignment = PP_ALIGN.LEFT

# --- Slide 4: Core Gameplay Elements ---
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "Core Gameplay Elements"

tf = body.text_frame
tf.text = "Exploration: Discovering Hyrule's vast landscapes, dungeons, and secrets."

p = tf.add_paragraph()
p.text = "Combat: Engaging enemies with swords, bows, and other weapons."
p.alignment = PP_ALIGN.LEFT

p = tf.add_paragraph()
p.text = "Puzzles: Solving intricate puzzles within dungeons and the overworld."
p.alignment = PP_ALIGN.LEFT

p = tf.add_paragraph()
p.text = "Items and Equipment: Collecting powerful items like the Hookshot, Bombs, and Bow."
p.alignment = PP_ALIGN.LEFT

# --- Slide 5: Recurring Themes ---
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "Recurring Themes"

tf = body.text_frame
tf.text = "The Triforce: A symbol of power, wisdom, and courage, often sought after by Ganon."

p = tf.add_paragraph()
p.text = "The Master Sword: The blade of evil's bane, capable of vanquishing Ganon."
p.alignment = PP_ALIGN.LEFT

p = tf.add_paragraph()
p.text = "The Cycle of Reincarnation: Link, Zelda, and Ganon are often reborn to repeat their roles."
p.alignment = PP_ALIGN.LEFT

# --- Slide 6: Notable Games ---
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "Notable Games"

tf = body.text_frame
tf.text = "The Legend of Zelda (NES, 1986): The game that started it all."

p = tf.add_paragraph()
p.text = "The Legend of Zelda: Ocarina of Time (N64, 1998): Widely considered one of the greatest games of all time."
p.alignment = PP_ALIGN.LEFT

p = tf.add_paragraph()
p.text = "The Legend of Zelda: Breath of the Wild (Switch, 2017): A revolutionary open-world adventure."
p.alignment = PP_ALIGN.LEFT

# --- Slide 7: Conclusion ---
slide_layout = prs.slide_layouts[5]  # Blank Slide
slide = prs.slides.add_slide(slide_layout)

left = top = width = height = Inches(1)
txBox = slide.shapes.add_textbox(left, top, width, height)
tf = txBox.text_frame

tf.text = "The Legend of Zelda continues to captivate audiences with its timeless adventures and compelling characters.  Thank you!"
tf.alignment = PP_ALIGN.CENTER

for paragraph in tf.paragraphs:
    paragraph.font.size = Pt(36)
    paragraph.alignment = PP_ALIGN.CENTER

# Save the presentation
prs.save("zelda_presentation.pptx")

# Open the presentation using OS
os.startfile("zelda_presentation.pptx")
