
from pptx import Presentation
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# Crear una nueva presentacion
prs = Presentation()

# Slide 1: Titulo
slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Pizza: A Culinary Delight"
subtitle.text = "An Overview of Pizza"

# Slide 2: History of Pizza
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "A Brief History"

tf = body.text_frame
tf.text = "Pizza has a long and rich history."
p = tf.add_paragraph()
p.text = "Its roots can be traced back to ancient civilizations."
p = tf.add_paragraph()
p.text = "Modern pizza originated in Naples, Italy, in the 18th century."
p = tf.add_paragraph()
p.text = "It quickly became popular among the working class."

# Slide 3: Types of Pizza
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "Popular Types of Pizza"

tf = body.text_frame
tf.text = "Neapolitan: Simple, with San Marzano tomatoes and mozzarella."
p = tf.add_paragraph()
p.text = "New York-Style: Large, thin, and foldable slices."
p = tf.add_paragraph()
p.text = "Sicilian: Thick crust, rectangular shape."
p = tf.add_paragraph()
p.text = "Chicago Deep-Dish: Thick crust filled with cheese and toppings."

# Slide 4: Ingredients
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "Key Ingredients"

tf = body.text_frame
tf.text = "Dough: Typically made from flour, water, yeast, and salt."
p = tf.add_paragraph()
p.text = "Sauce: Usually tomato-based, seasoned with herbs and spices."
p = tf.add_paragraph()
p.text = "Cheese: Mozzarella is the most common, but others are used."
p = tf.add_paragraph()
p.text = "Toppings: Endless possibilities, from pepperoni to vegetables."

# Slide 5: Nutritional Value
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "Nutritional Information"

tf = body.text_frame
tf.text = "Pizza can be a source of carbohydrates, protein, and fat."
p = tf.add_paragraph()
p.text = "Nutritional value varies depending on the ingredients and portion size."
p = tf.add_paragraph()
p.text = "Choose whole-wheat crust and load up on vegetables for a healthier option."
p = tf.add_paragraph()
p.text = "Be mindful of portion sizes and frequency of consumption."

# Slide 6: World Wide Popularity
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
body = slide.placeholders[1]

title.text = "Global Phenomenon"

tf = body.text_frame
tf.text = "Pizza is enjoyed in almost every country around the world."
p = tf.add_paragraph()
p.text = "Each region has its own unique variations and preferences."
p = tf.add_paragraph()
p.text = "It's a versatile and customizable food that appeals to diverse tastes."
p = tf.add_paragraph()
p.text = "Pizza is a common choice for parties, gatherings, and casual meals."

# Slide 7: Conclusion
slide_layout = prs.slide_layouts[5] # Blank slide
slide = prs.slides.add_slide(slide_layout)

left = top = width = height = Inches(1)

shape = slide.shapes.add_textbox(left, top, width*8, height)
tf = shape.text_frame
tf.text = "In conclusion, pizza is a delicious and globally loved dish with a rich history and endless possibilities!"
tf.alignment = PP_ALIGN.CENTER
p = tf.add_paragraph()
p.text = "Thank you!"
p.alignment = PP_ALIGN.CENTER

# Guardar la presentacion
prs.save("pizza_presentation.pptx")

#Abrir el archivo
import os
os.startfile("pizza_presentation.pptx")
