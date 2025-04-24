import google.generativeai as genai
import playsound
from vosk import Model, KaldiRecognizer
import os
import json
import sys
import queue
import sounddevice
from gtts import gTTS
import subprocess
import requests
from pytube import YouTube
import yt_dlp



class Asistente:
    def __init__(self, model_name:str, audio_path:str, vosk_path:str, key_word:str, config = {}, system_instruccion = "", API = "", vosk_model_lang = "es"):
        self.model_name = model_name
        self.audio_path = audio_path
        self.vosk_path = vosk_path
        self.key_word = key_word
        self.config = config
        self.system_instruccion = system_instruccion
        self.API = API
        self.vosk_model_lang = vosk_model_lang
        
        
        #Iniciando al modelo de IA de Gemini
        if self.API == "" or self.model_name == "" or self.config == {}: 
            raise Exception("Error al configurar Gemini")
        try:
            genai.configure(api_key=self.API)
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=self.config
            )
            self.chat = self.model.start_chat()
        except Exception as e:
            raise Exception("Error al configurar Gemini")
        
        #configurando el modelo de reconocimiento de voz
        self.q = queue.Queue()
        self.device_id = None
        self.sample_rate = 16000
        try:
            self.vosk_model = Model(self.vosk_path)
        except:
            try:
                print("Error al cargar el modelo de voz, colocando el modelo español...")
                self.vosk_model = Model(self.vosk_model_lang)
            except Exception as e:
                raise Exception("Error al cargar el modelo de voz")

    def answer(self,text:str):
        result = self.chat.send_message(text)
        return result.text.replace("*","").replace("/","")
    
    def talk(self, text:str):
        model = gTTS(text=text, lang=self.vosk_model_lang)
        model.save(self.audio_path)
        try:
            playsound.playsound(self.audio_path)
        except Exception as e:
            print("No se puedo reproducir el audio")
        os.remove(self.audio_path)

    def transcript(self):
        try:
            model = Model(self.vosk_path)
        except Exception as e:
            try:
                Model = Model(self.vosk_model_lang)
            except Exception as e:
                print("Error al cargar el modelo de voz")

        q = queue.Queue()
        def callback(indata, frames, tiem, status):
            q.put(bytes(indata))
        
        silence_duration = 1.5
        with sounddevice.RawInputStream(samplerate=16000, 
                                        blocksize=8000, 
                                        dtype="int16",
                                        channels=1, 
                                        callback=callback):    
            print("Escuchando...")
            silecne_counter = 0
            recognizer = KaldiRecognizer(model, 16000)
            final_text = ""
            while True:
                data = q.get()

                # Perform voice activity detection
                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())['text']
                    silence_counter = 0
                    final_text += f" {result}"
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
                    if partial == "":
                        silence_counter += 1
                        
                # Check if silence has been detected for enough time
                if silence_counter > silence_duration * (16000 / 8000):  # convert to frames
                    print("Silence detected, stopping...")
                    break
                
            # Send the final text to the AI model
            if final_text != "":
                print("Listo!")
                return final_text
            else: 
                print("Listo!")
                return ""
    
    def key_word(self, word:str):
        try:
            model = Model(self.vosk_path)
        except Exception as e:
            try:
                model = Model(self.vosk_model_lang)
            except Exception as e:
                print("Error al cargar el modelo de voz")

        q = queue.Queue()
        def callback(indata, frames, time, status):
            q.put(bytes(indata))
        
        with sounddevice.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16", channels=1, callback=callback):
            print("Escuchando...")
            recognizer = KaldiRecognizer(model, 16000)
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())['text']
                    final_text += f" {result}"
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
                    print(partial)
                    
    def crear_un_proyecto_web(self, caracteristicas_pagina: str, nombre: str, ruta_proyecto: str):
        """
        Description:
        Crea un proyecto web básico con una página HTML generada dinámicamente a partir de las características proporcionadas.
        La función genera una estructura de carpetas en la ruta especificada, crea un archivo `index.html` con el código HTML, CSS (usando Bootstrap v5.3) y JavaScript,
        y abre automáticamente el archivo en el editor de código y en el navegador predeterminado.
        La página web es responsive, incluye componentes de Bootstrap como navbar, cards, modals, carousel, entre otros, y utiliza imágenes externas integradas directamente desde URLs.

        Args:
        caracteristicas_pagina (str): Descripción detallada de las características y el tema de la página web que se desea crear.
        nombre (str): Nombre del proyecto y de la carpeta principal que se creará.
        ruta_proyecto (str): Ruta donde se creará la carpeta del proyecto.
        """
        nombre_proyecto = nombre
        nombre_ruta_proyecto = ruta_proyecto
        carpeta_nativa = os.path.join(os.path.expanduser("~"), nombre_proyecto)
        carpeta_final = os.path.join(carpeta_nativa, nombre_proyecto)
        os.makedirs(carpeta_final, exist_ok=True)
        codigo_html = self.model.generate_content([caracteristicas_pagina, "Crea una página web con las siguientes características y el tema proporcionado. El código debe incluir HTML, CSS (usando Bootstrap v5.3 desde su CDN y estilos personalizados en una etiqueta <style>), y JavaScript (en una etiqueta <script> si es necesario). La página debe integrar imágenes relevantes usando URLs directas de Google Images y otros repositorios de imágenes web. No incluyas explicaciones ni texto innecesario, solo devuelve el código completo y funcional. Asegúrate de que la página sea responsive y utilice componentes de Bootstrap como navbar, cards, modals, carousel, o cualquier otro que sea relevante para el tema. Incluye comentarios en el código para indicar las secciones principales y marcar dónde se implementa la integración de imágenes externas"])
        codigo_html = codigo_html.text.split("```html")[1].split('```')[0]
        with open(os.path.join(carpeta_final, "index.html"), "w", encoding="utf-8") as f:
            f.write(codigo_html)
        os.system(f"start msg {os.path.join(carpeta_final, 'index.html')}")
        os.system(f"start Code {carpeta_final}")

    def crear_un_documento(self, tema:str):
        """
        Description:
        Genera un código en Python utilizando la librería `python-docx` para crear un documento Word en formato de tesis.
        El documento incluye una estructura completa con portada, índice, introducción, desarrollo, conclusión y la capacidad de agregar imágenes desde URLs externas.
        El formato del documento es profesional, con fuentes como Times New Roman, tamaño 12, interlineado de 1.5 y márgenes estándar.
        El código generado está bien comentado para que el usuario pueda entender y modificar cada parte según sea necesario.

        Args:
        tema (str): El tema de la tesis que se utilizará para generar el contenido del document
        """
        result = self.model.generate_content([f""""Genera un código en Python utilizando la librería docx para crear un documento Word en formato de tesis. el tema se la tesis es {tema}. El documento debe incluir lo siguiente:
                                                        Portada: Con el título de la tesis, el nombre del autor, la fecha y el nombre de la institucion.
                                                        Índice: Generado automáticamente con los títulos y subtítulos.
                                                        Introducción: Una sección con un texto de ejemplo que el usuario pueda modificar.
                                                        Desarrollo: Incluye al menos tres secciones con títulos y subtítulos, y texto de ejemplo en cada una.
                                                        Conclusión: Una sección final con texto de ejemplo.
                                                        Imágenes: Incluye la funcionalidad para agregar imágenes desde Google o cualquier página web de imágenes. Las imágenes deben estar centradas y con un pie de imagen descriptivo.
                                                        Formato: Usa un formato profesional, con fuentes como Times New Roman, tamaño 12, interlineado de 1.5 y márgenes estándar.
                                                        Requisitos adicionales:
                                                        No uses caracteres especiales ni acentos en el código.
                                                        Asegúrate de que el código sea fácil de ejecutar y que el documento generado sea compatible con Word.
                                                        Proporciona instrucciones claras para que el usuario pueda modificar el texto y agregar sus propias imágenes.
                                                        El código debe estar bien comentado para que el usuario pueda entender y modificar cada parte según sea necesario."""])
        codigo = result.text.split("```")[1].replace("python", "").replace("¬", "")

        with open("documento.py", "w") as f:
            f.write(codigo)
        subprocess.run(["python", "documento.py"])

    
    def crear_una_pesentacion_de_power_point(self, tema:str):
        """
        Description:
        Esta es una funcion que crea una presentacion de power point cuando el usuario dice
        "crea una presentacion" o algo asi

        Arg:
            tema: es el tema de la presentacion
        """
        prompt = (
    f"Genera un codigo en Python utilizando la libreria pptx para crear una presentacion de PowerPoint sobre {tema} con bastantes diapositivas, donde cada diapositiva incluya un titulo y un texto descriptivo; asegurate de que las diapositivas tengan fondos llamativos usando diseños nativos de PowerPoint y agreguen decoraciones nativas como letras de colores o figuras para resaltar los textos; todas las decoraciones deben ser exclusivamente nativas de PowerPoint; incluye al inicio del codigo la declaracion de codificacion UTF-8 para evitar errores de sintaxis; ademas, utiliza solo caracteres basicos del alfabeto ingles (sin acentos, eñes ni simbolos especiales) en todo el texto del codigo, reemplazando cualquier palabra o frase problematica por su equivalente sin caracteres especiales; devuelve solo el codigo sin explicaciones adicionales, al final del codigo abre el archivo pptx con la libreira os, que los textos de informacion esten en español"
)
    
        result = self.model.generate_content(prompt)
        codigo = result.text.split("```")[1].replace("python", "")
        # fin = f"# This Python file uses the following encoding: utf-8 {codigo}"

        with open("presentacion2.py", "w") as f:
            f.write(codigo)
        subprocess.run(["python", "presentacion2.py"])
        
    def escribir_una_nota(self, directorio_principal:str, carpeta:str, tema:str):
        """
        Description:
        Crea una nota en un archivo de texto dentro de una carpeta específica, ubicada en un directorio principal.
        La nota se organiza bajo un tema específico, y el archivo se guarda con un nombre basado en el tema.
        Si la carpeta o el archivo no existen, se crean automáticamente. El contenido de la nota se solicita al usuario
        durante la ejecución de la función.

        Args:
            directorio_principal (str): Ruta del directorio principal donde se almacenarán las notas.
            carpeta (str): Nombre de la carpeta dentro del directorio principal donde se guardará la nota.
            tema (str): Tema o título de la nota. Este se utiliza para nombrar el archivo de la nota.
        """
        result = self.model.generate_content([f"crea una nota sobre {tema}"])
        carpeta_nativa = os.path.join(os.path.expanduser("~"), directorio_principal)
        carpeta_nota = os.path.join(carpeta_nativa, carpeta)
        os.makedirs(carpeta_nota, exist_ok=True)
        result = result.text.replace("#", "").replace("*", "")
        with open(os.path.join(carpeta_nota, f"{tema}.txt"), "w") as archivo:
            archivo.write(result)
        subprocess.run(["notepad.exe", os.path.join(carpeta_nota, f"{tema}.txt")])

    def buscar_un_video(self, busqueda:str):
        """
        Description:
        Esta funcion busca un video en youtube cuando el usuario dice "busca un video"
        """
        url = f"https://www.googleapis.com/youtbe/v3/search?part=snippet&q={busqueda}&type=video&key=AIzaSyBp-EGz2ViQpmVvBZhUOcog4SQmimixWtc&maxResults=1"
        reply = requests.get(url)
        data = reply.json()
        if reply.status_code == 200:
            print("listo")
            if "items" in data and len(data["items"]) > 0:
                pass

        video_url = f"https://www.youtube.com/watch?v={id}"
        subprocess.run(['msedge', video_url])
        
    def descargar_un_video(self,video_url:str):
        """
        description:
        Esta función permite descargar videos de YouTube a partir de su URL, 
        con opciones para seleccionar el formato, la calidad y la ubicación 
        de guardado.

    
        Args:
            video_url: Es al url del video que el usuario quiere descargar    
        """

        yld_ops = {
            'format': ' bestvideo',
            'outtmpl': f'{ruta}/%(title)s.%(ext)s',
            'mergue_output_format': 'mp4'
        }
        try:
            print("iniciando")      
            url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={busqueda}&type=video&key=AIzaSyC5cxHnowJ54rkppj8TMaRvD8HD8dnx6Ew&maxResults=1"
            reply = requests.get(url)
            data = reply.json()
            if reply.status_code == 200:
                print("Listo")
                if "items" in data and len(data["items"]) > 0:
                    video_id = data["items"][0]["videoId"]
                    video_url = f"https://www.youtube.com/watch?v={id}"
                    with yt_dlp.YoutubeDL(yld_ops) as ydl:
                        ydl.download([video_url]) 
        except Exception as e:
            print("Error al descargar el video")

gemini = Asistente("gemini-2.0-flash", "audio.mp3", "./models/vosk-model-small-es-0.42", "hola", config={"temperature":0.8,"top_p":0.95, "top_k":64, "max_output_tokens":8192, "response_mime_type": "text/plain"}, system_instruccion="", API="AIzaSyDY1Ldl5_yOGcLzwbcj5gqe-LUNm4J--c0", vosk_model_lang="es")

gemini.buscar_un_video("como hacer una pizza")