import os
import urllib.parse
import urllib
import google.generativeai as genai
from docx import Document


API_KEY = "AIzaSyAKIXenE4WIyx96A9T6WgLCD1feLk-DOYY"
genai.configure( api_key=API_KEY)

config = {
    "temperature" : 0.8,
    "top_p" : 0.95,
    "top_k" : 64,
    "max_output_tokens" : 8192,
    "response_mime_type" : "text/plain"
}


activado = False
def Buscar_en_linea_o_en_la_web(busqueda:str):

    global activado, chat_session

    """
        Es una funcion que hace una busqueda en linea en el navegador
        de algo sobre lo que el usuario dice "hola me podrias brindarme ...."
    
        ARGS:
            a: Es un numero entero
            b: La busqueda....
    """
    url = f"https://www.google.co.ve/search?q={urllib.parse.quote(busqueda)}"
    os.system(f"start msedge {url}")
    activado = True


def crear_proyecto_web(características_pagina:str, nombre:str):
    """
    Crea el proyecto web y lo abre en el navegador y VS Code.
    cuando el usuario dice "crea una pagina web sobre...", "crea un sitio web...", "crea una pagina"

    Args: 
        características_pagina: es un texo que define las caracteristicas de la misma pagina como el color
        nombre: es un nombre que eliges segun el tema que dijo el usuario en las caracteristicas.
    """

    try:
        nombre_proyecto = nombre    

        escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
        ruta_proyecto = os.path.join(escritorio, nombre_proyecto)
        os.makedirs(ruta_proyecto, exist_ok=True)

        codigo_html = model2.generate_content([características_pagina, "crea una pagina web con estas caracteristica y este tema, no incluyas ni explicaciones ni texto innecesario solo devuelve codigo HTML, en el cual los estilos serán creados con la cdn de bootstrap y codigo css que estara en el mismo index HTML"])
        codigo_html = codigo_html.text.split("```html")[1].split('```')[0]
        with open(os.path.join(ruta_proyecto, "index.html"), "w", encoding="utf-8") as archivo_html:
            archivo_html.write(codigo_html)

        ruta_index_html = "file://" + os.path.join(ruta_proyecto, "index.html") 
        os.system(f"start msedge {ruta_index_html}") 

        os.system(f"start Code {ruta_proyecto}")

        print(f"Proyecto creado en: {ruta_proyecto}")
    except Exception as e:
        print(f"Error al crear el proyecto: {e}")


def answer(text:str):
    global activado
    result = chat.send_message(text)
    if not activado:
        return result.text.replace("*","").replace("/","")
    else:
        return "Acción realizada"
function = [Buscar_en_linea_o_en_la_web,crear_proyecto_web]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config= config,
    tools=[function]
)

model2 = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config= config,
)
chat = model.start_chat(enable_automatic_function_calling=True)

