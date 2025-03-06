
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os

# Create a new presentation
prs = Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)

# Title slide
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Water: The Essence of Life"
subtitle.text = "A Presentation on the Importance of Water"

title.text_frame.paragraphs[0].font.size = Pt(44)
title.text_frame.paragraphs[0].font.name = 'Arial Black'
subtitle.text_frame.paragraphs[0].font.size = Pt(32)
subtitle.text_frame.paragraphs[0].font.name = 'Calibri'


# Add a slide for Water Properties
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
shapes = slide.shapes

title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = "Properties of Water"
title_shape.text_frame.paragraphs[0].font.size = Pt(36)
title_shape.text_frame.paragraphs[0].font.name = 'Arial Black'

tf = body_shape.text_frame
tf.text = "Water is a unique substance with several remarkable properties:\n\n* Polarity: Water molecules are polar, leading to hydrogen bonding.\n* High Specific Heat Capacity: Water resists temperature changes.\n* Excellent Solvent: Water dissolves many substances.\n* Cohesion and Adhesion: Water molecules stick to each other and other surfaces."

for paragraph in tf.paragraphs:
    paragraph.font.size = Pt(24)
    paragraph.font.name = 'Calibri'
    paragraph.alignment = PP_ALIGN.LEFT


# Add a slide for Water's Importance
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
shapes = slide.shapes

title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = "The Importance of Water"
title_shape.text_frame.paragraphs[0].font.size = Pt(36)
title_shape.text_frame.paragraphs[0].font.name = 'Arial Black'

tf = body_shape.text_frame
tf.text = "Water is essential for:\n\n* Human consumption and health\n* Agriculture and food production\n* Industrial processes\n* Ecosystem balance and biodiversity\n* Climate regulation"

for paragraph in tf.paragraphs:
    paragraph.font.size = Pt(24)
    paragraph.font.name = 'Calibri'
    paragraph.alignment = PP_ALIGN.LEFT



#Add a slide for Water Conservation

slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
shapes = slide.shapes

title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = "Water Conservation"
title_shape.text_frame.paragraphs[0].font.size = Pt(36)
title_shape.text_frame.paragraphs[0].font.name = 'Arial Black'

tf = body_shape.text_frame
tf.text = "Conserving water is crucial for a sustainable future.  We can all contribute by:\n\n* Reducing water usage at home\n* Supporting sustainable agriculture\n* Advocating for responsible water management policies"

for paragraph in tf.paragraphs:
    paragraph.font.size = Pt(24)
    paragraph.font.name = 'Calibri'
    paragraph.alignment = PP_ALIGN.LEFT


# Save the presentation
prs.save("water_presentation.pptx")

# Open the presentation (optional)
os.startfile("water_presentation.pptx")
