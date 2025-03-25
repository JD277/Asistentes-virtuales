from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Inches
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import ns
from docx.oxml.ns import qn
import requests
from io import BytesIO

def agregar_imagen_desde_url(documento, url, descripcion):
    """Agrega una imagen desde una URL a un documento de Word."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        image_bytes = BytesIO(response.content)
        paragraph = documento.add_paragraph()
        run = paragraph.add_run()
        run.add_picture(image_bytes, width=Inches(4))  # Ajusta el ancho según necesites
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        # Pie de imagen
        paragraph = documento.add_paragraph()
        run = paragraph.add_run(descripcion)
        run.font.size = Pt(10)
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen desde {url}: {e}")
    except Exception as e:
        print(f"Error al agregar la imagen: {e}")

def crear_documento_tesis(nombre_archivo):
    """Crea un documento de Word con formato de tesis."""
    document = Document()

    # Estilos
    styles = document.styles
    style = styles.add_style('TituloTesis', WD_STYLE_TYPE.PARAGRAPH)
    style.base_style = styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(16)
    style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    style = styles.add_style('Titulo1', WD_STYLE_TYPE.PARAGRAPH)
    style.base_style = styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(14)

    style = styles.add_style('Titulo2', WD_STYLE_TYPE.PARAGRAPH)
    style.base_style = styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    style.paragraph_format.left_indent = Inches(0.5)

    style = styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.5

    # Portada
    titulo = document.add_paragraph('Título de la Tesis sobre Contaminación de la Tierra', 'TituloTesis')
    document.add_paragraph('Autor: Tu Nombre', 'Normal')
    document.add_paragraph('Fecha: Octubre 26, 2023', 'Normal')
    document.add_paragraph('Institución: Nombre de la Institución', 'Normal')
    document.add_page_break()

    # Índice (se generará al final)
    document.add_paragraph('Índice', 'Titulo1')
    indice = document.add_paragraph('', 'Normal')
    document.add_page_break()

    # Introducción
    document.add_paragraph('Introducción', 'Titulo1')
    document.add_paragraph('Texto de ejemplo para la introducción. Puedes modificar este texto.', 'Normal')

    # Desarrollo
    document.add_paragraph('Desarrollo', 'Titulo1')

    document.add_paragraph('Sección 1', 'Titulo2')
    document.add_paragraph('Texto de ejemplo para la sección 1. Puedes modificar este texto.', 'Normal')
    agregar_imagen_desde_url(document, "https://www.nationalgeographic.com.es/medio-ambiente/contaminacion-del-suelo-causas-consecuencias-y-soluciones", "Contaminación del suelo")

    document.add_paragraph('Sección 2', 'Titulo2')
    document.add_paragraph('Texto de ejemplo para la sección 2. Puedes modificar este texto.', 'Normal')
    agregar_imagen_desde_url(document, "https://www.ecologiaverde.com/contaminacion-del-suelo-causas-consecuencias-y-soluciones-173.html", "Efectos de la contaminación en la agricultura")

    document.add_paragraph('Sección 3', 'Titulo2')
    document.add_paragraph('Texto de ejemplo para la sección 3. Puedes modificar este texto.', 'Normal')
    agregar_imagen_desde_url(document, "https://www.acciona.com/es/impacto-ambiental/contaminacion-del-suelo/", "Soluciones para la contaminación del suelo")

    # Conclusión
    document.add_paragraph('Conclusión', 'Titulo1')
    document.add_paragraph('Texto de ejemplo para la conclusión. Puedes modificar este texto.', 'Normal')

    # Guardar el documento
    document.save(nombre_archivo)

    # Generar el índice
    indice.clear()
    for paragraph in document.paragraphs:
        if paragraph.style.name.startswith('Titulo'):
            nivel = int(paragraph.style.name[-1])
            texto = paragraph.text
            indice.add_paragraph(f'{"  " * (nivel - 1)}{texto}', 'Normal')

# Ejemplo de uso
crear_documento_tesis('tesis_contaminacion_tierra.docx')