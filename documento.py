
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.styles import ParagraphStyle
import io
import requests
from PIL import Image


def crear_tesis_golf():
    """
    Crea un documento Word en formato de tesis sobre el golf como deporte de alto rendimiento.
    Incluye portada, indice, introduccion, desarrollo (con tres secciones), conclusion,
    imagenes (descargadas desde URL), y formato profesional.
    """

    document = Document()

    # --- Estilos ---
    estilos = document.styles

    # Estilo para texto normal
    estilo_normal = estilos["Normal"]
    fuente_normal = estilo_normal.font
    fuente_normal.name = "Times New Roman"
    fuente_normal.size = Pt(12)

    # Estilo para titulos
    estilo_titulo1 = estilos.add_style("Titulo1", WD_STYLE_TYPE.PARAGRAPH)
    fuente_titulo1 = estilo_titulo1.font
    fuente_titulo1.name = "Times New Roman"
    fuente_titulo1.size = Pt(16)
    estilo_titulo1.paragraph_format.space_after = Pt(0) #elimina espacio despues del titulo

    # Estilo para subtitulos
    estilo_titulo2 = estilos.add_style("Titulo2", WD_STYLE_TYPE.PARAGRAPH)
    fuente_titulo2 = estilo_titulo2.font
    fuente_titulo2.name = "Times New Roman"
    fuente_titulo2.size = Pt(14)
    estilo_titulo2.paragraph_format.space_after = Pt(0)

    # --- Funciones auxiliares ---
    def agregar_titulo(texto, nivel=1):
        """Agrega un titulo al documento."""
        if nivel == 1:
            paragraph = document.add_paragraph(texto, style="Titulo1")
        elif nivel == 2:
            paragraph = document.add_paragraph(texto, style="Titulo2")
        else:
            paragraph = document.add_heading(texto, level=nivel)

    def agregar_parrafo(texto):
        """Agrega un parrafo al documento con formato estandar."""
        paragraph = document.add_paragraph(texto)
        paragraph_format = paragraph.paragraph_format
        paragraph_format.line_spacing = 1.5

    def agregar_imagen(url, pie_de_foto):
        """Agrega una imagen desde una URL al documento, centrada y con pie de foto."""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Lanza una excepcion para codigos de error HTTP

            # Intenta abrir la imagen con PIL para verificar el formato
            try:
                img = Image.open(io.BytesIO(response.content))
                img.verify()  # Verifica que el archivo este completo
            except Exception as e:
                print(f"Error al procesar la imagen: {e}")
                print("Asegurate de que la URL es valida y la imagen esta en un formato compatible (JPEG, PNG, GIF, etc.).")
                return # Sale de la funcion si la imagen no es valida

            # Agrega la imagen al documento
            paragraph = document.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = paragraph.add_run()
            run.add_picture(io.BytesIO(response.content), width=Inches(6))  # Ajusta el ancho segun sea necesario

            # Agrega el pie de foto
            paragraph_pie_de_foto = document.add_paragraph()
            paragraph_pie_de_foto.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph_pie_de_foto.text = pie_de_foto
            paragraph_pie_de_foto.font.italic = True # Pone el pie de foto en italica

        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la imagen desde {url}: {e}")
            print("Asegurate de tener una conexion a internet y que la URL sea correcta.")
        except Exception as e:
            print(f"Error inesperado al agregar la imagen: {e}")


    # --- Portada ---
    agregar_titulo("El Golf como Deporte de Alto Rendimiento", nivel=1)
    agregar_parrafo("Autor: [Tu Nombre]")
    agregar_parrafo("Fecha: [Fecha]")
    agregar_parrafo("Institucion: [Nombre de la Institucion]")
    document.add_page_break()

    # --- Indice ---
    agregar_titulo("Indice", nivel=1)
    # El indice se genera automaticamente al abrir el documento en Word.
    # Para actualizarlo, haz clic derecho sobre el indice y selecciona "Actualizar campos".
    agregar_parrafo("Para actualizar el indice, haz clic derecho sobre el y selecciona 'Actualizar campos'.")
    document.add_page_break()

    # --- Introduccion ---
    agregar_titulo("Introduccion", nivel=1)
    agregar_parrafo("Este es un texto de ejemplo para la introduccion.  Modificalo para que se ajuste a tu tesis.  Explica la relevancia del golf como deporte de alto rendimiento, sus desafios y el objetivo de la investigacion.")

    # --- Desarrollo ---
    agregar_titulo("Desarrollo", nivel=1)

    # Seccion 1
    agregar_titulo("Historia y Evolucion del Golf", nivel=2)
    agregar_parrafo("Texto de ejemplo para la historia y evolucion del golf. Describe sus origenes, como ha evolucionado a lo largo del tiempo y su popularidad actual.")

    # Subseccion 1.1
    agregar_titulo("El Golf Profesional", nivel=3)
    agregar_parrafo("Texto de ejemplo sobre el golf profesional.  Describe los principales torneos, los jugadores mas destacados y la estructura del circuito profesional.")

    # Seccion 2
    agregar_titulo("Aspectos Fisicos y Tecnicos del Golf", nivel=2)
    agregar_parrafo("Texto de ejemplo sobre los aspectos fisicos y tecnicos del golf.  Explica la importancia de la fuerza, la flexibilidad, la coordinacion y la tecnica en el rendimiento del golfista.")

    # Subseccion 2.1
    agregar_titulo("Biomecanica del Swing de Golf", nivel=3)
    agregar_parrafo("Texto de ejemplo sobre la biomecanica del swing de golf.  Describe los movimientos y fuerzas involucradas en el swing y como optimizarlo para mejorar la potencia y la precision.")

    # Seccion 3
    agregar_titulo("Entrenamiento y Preparacion Fisica para el Golf", nivel=2)
    agregar_parrafo("Texto de ejemplo sobre el entrenamiento y la preparacion fisica para el golf.  Describe los diferentes tipos de entrenamiento que se utilizan para mejorar el rendimiento del golfista, como el entrenamiento de fuerza, el entrenamiento de resistencia y el entrenamiento de flexibilidad.")

    # --- Imagenes ---
    agregar_titulo("Ejemplos de Imagenes", nivel=1)
    agregar_imagen("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Scottish_Open_at_Loch_Lomond_2008.jpg/1280px-Scottish_Open_at_Loch_Lomond_2008.jpg", "Jugador de golf profesional durante un torneo.")
    agregar_imagen("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Golf_driver.jpg/1280px-Golf_driver.jpg", "Un driver de golf, utilizado para golpear la bola a larga distancia.")

    # --- Conclusion ---
    agregar_titulo("Conclusion", nivel=1)
    agregar_parrafo("Este es un texto de ejemplo para la conclusion.  Resume los principales hallazgos de la tesis y destaca la importancia del golf como deporte de alto rendimiento.  Tambien puedes mencionar areas para futuras investigaciones.")

    # --- Guardar el documento ---
    document.save("tesis_golf.docx")
    print("Documento 'tesis_golf.docx' creado exitosamente.")

# --- Ejecutar la funcion ---
if __name__ == "__main__":
    crear_tesis_golf()

