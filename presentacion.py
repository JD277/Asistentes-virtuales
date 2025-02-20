
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.transition import PP_TRANSITION

# Crear una nueva presentación
prs = Presentation()

# Título de la presentación
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Beneficios del Ejercicio Físico"
subtitle.text = "Mejora tu Salud y Bienestar"

# Agregar una imagen al slide de título
left = Inches(1)
top = Inches(2.5)
pic = slide.shapes.add_picture('imagen_ejercicio.jpg', left, top, width=Inches(6)) # Reemplaza 'imagen_ejercicio.jpg' con la ruta de tu imagen


# Segunda diapositiva: Beneficios para la salud física
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
shapes = slide.shapes

title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = "Beneficios para la Salud Física"
tf = body_shape.text_frame
tf.text = "• Mejora la salud cardiovascular\n• Reduce el riesgo de enfermedades crónicas\n• Fortalece los músculos y huesos\n• Ayuda a controlar el peso"

# Agregar una imagen a la segunda diapositiva
left = Inches(6)
top = Inches(1.5)
pic = slide.shapes.add_picture('corazon_saludable.jpg', left, top, width=Inches(3)) # Reemplaza 'corazon_saludable.jpg' con la ruta de tu imagen

# Tercera diapositiva: Beneficios para la salud mental
slide = prs.slides.add_slide(slide_layout)
shapes = slide.shapes

title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = "Beneficios para la Salud Mental"
tf = body_shape.text_frame
tf.text = "• Reduce el estrés y la ansiedad\n• Mejora el estado de ánimo\n• Promueve el sueño reparador\n• Aumenta la autoestima"


# Agregar una imagen a la tercera diapositiva
left = Inches(6)
top = Inches(1.5)
pic = slide.shapes.add_picture('mente_sana.jpg', left, top, width=Inches(3)) # Reemplaza 'mente_sana.jpg' con la ruta de tu imagen


# Cuarta diapositiva: Conclusión
slide = prs.slides.add_slide(slide_layout)
shapes = slide.shapes

title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = "Conclusión"
tf = body_shape.text_frame
tf.text = "El ejercicio físico es esencial para una vida sana y plena.  Incorpora actividad física regular en tu rutina diaria."

# Establecer una transición para la diapositiva de conclusión
slide.slide_layout.transition.type = PP_TRANSITION.SPLIT

# Guardar la presentación
prs.save("Beneficios_Ejercicio.pptx")

print("Presentación creada exitosamente!")
