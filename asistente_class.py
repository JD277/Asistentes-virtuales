import google.generativeai as genai
import playsound
from vosk import Model, KaldiRecognizer
import os, json, sys, queue, sounddevice, requests
from gtts import gTTS
import docx
import subprocess
from pptx import Presentation
import pptx
from pytube import YouTube

class Asistente:
    def __init__(self, model_name: 
                str,audio_path: str, 
                vosk_path: str, 
                key_word: str, 
                config: dict, 
                system_instruction: str, 
                API: str,vosk_model_lang: str):
    #Recibimos los parametros necesarios para la creación del asistente virtual 
        self.model_name = model_name
        self.audio_path = audio_path
        self.vosk_path = vosk_path
        self.key_word = key_word
        self.config = config
        self.system_instruction = system_instruction
        self.API = API
        self.vosk_model_lang = vosk_model_lang
        
    # Inicializando al modelo de IA de gemini 
        if self.API == "" or self.model_name == "" or self.config == {}:
            raise Exception("Error al configurar Gemini AI")
        try:
            genai.configure(api_key=self.API)
            self.model = genai.GenerativeModel(
                model_name=self.model_name, 
                generation_config= self.config,
            )
            self.chat = self.model.start_chat()
        except Exception as e:
            raise Exception("Error al configurar Gemini AI")
        # Configurando el modelo de reconocimiento del voz 
        self.q = queue.Queue()
        self.device_id = None
        self.sample_rate = 16000
        vosk_model = Model(self.vosk_path)

        try:
            vosk_model = Model(self.vosk_path)
        except Exception as e :
            try:
                print("Error al cargar el modelo de voz, cambiando a español...")
                self.vosk_model = Model(self.vosk_model_lang)
            except Exception as e:
                raise Exception("Error al cargar el modelo de reconocimiento de voz")

    def answer(self,text:str):
        result = self.chat.send_message(text)
        return result.text.replace("*","").replace("/","")

    def talk(self,text:str):
        model = gTTS(text,lang = self.vosk_module_lang)
        model.save(self.audio_path)
        try:
            playsound.playsound(self.audio_path)
        except Exception as e:
            print("No se pudo reproducir el audio")
        os.remove(self.audio_path)
        
    def trascript(self):
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

        silence_duration = 1.5
        with sounddevice.RawInputStream(samplerate=16000, 
                                        blocksize= 8000, 
                                        dtype= "int16",
                                        channels=1, 
                                        callback=callback):
            print("Escuchando...")
            silence_counter = 0
            recognizer = KaldiRecognizer(model, 16000)
            final_text = ""
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())["text"]
                    silence_counter = 0
                    final_text += f" {result}"
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
                    if partial == "":
                        silence_counter += 1
                # Check if silence has been detected for enough time
                if silence_counter >= silence_duration * (16000 / 8000):
                    print('Silence detected, stopping...')
                    break
            if final_text != "":
                print("listo !")
                return final_text
            else:
                print("Listo!")
                return ""

    def key_word(self,word):
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

        with sounddevice.RawInputStream(samplerate=16000, 
                                        blocksize= 8000, 
                                        dtype= "int16",
                                        channels=1, 
                                        callback=callback):
            print("Escuchando...")
            recognizer = KaldiRecognizer(model, 16000)
            
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())["text"]
                    if word in result:
                        return True
                    
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
                    if word in result:
                        return True
                        
                # Check if silence has been detected for enough time

    def crear_un_proyecto_web(self, caracteristicas_pagina:str, nombre:str, ruta_proyecto:str):
        """
        Description:
            Crea una pagina web y lo abre en el navegador y en VS code, cuando el usuario diga: 
            Crea una pagina sobre..., crea un sitio web..., crea una pagina...
        Args: 
            caracteristicas_pagina: Es el tema de la pagina web
            nombre: Es el nombre del proyecto
            ruta_proyecto: Es la ruta donde se creara el proyecto
        """
        nombre_proyecto = nombre
        nombre_ruta_proyecto = ruta_proyecto
        carpeta_nativa= os.path.join(os.path.expanduser("~"), nombre_ruta_proyecto)
        carpeta_final= os.path.join(carpeta_nativa, nombre_proyecto)
        os.makedirs(carpeta_final, exist_ok=True)
        codigo_html = self.model.generate_content([caracteristicas_pagina, "Crea un pagina web que incluya caractristicas que pida el usuario, utilizando html, css y java script pero no incluyas texto innecesario ni explicaciones, ahora solamente tienes que regresar el codigo html en donde vas a utlizar la cdn de bootstrap y codigo css que estaran en el mismo index html."])
        codigo_html = codigo_html.text.split("```html")[1].split("```")[0]
        with open(os.path.join(carpeta_final, "index.html"), "w", encoding="utf-8") as archivo_html:
            archivo_html.write(codigo_html)
        os.system(f"start msedge {os.path.join(carpeta_final, 'index.html')}")
        os.system(f"start Code {carpeta_final}")

        pass             
            
    def escribir_un_documento(self,tema,str):
        """
        Description:
            Empieza a escrbir en un documento word sobre un tema que te pida el usuario. Ejemplo, 
            Quiero que hagas un documento word sobre... o haz un documento sobre...
        Args:
            tema: Es el tema del documento 
        """
        result = self.model.generate_content([tema, "Crea un texto sobre algun tema que diga el usuario, tambien pondras algunos elementos que ayuden a mejorar la estructura del documento, utilizando letra negrita con palabras importantes por ejemplo. Intenta no utilizar caracteres especiales como Ñ o á."])
        codigo = result.text.split("```python")[1].replace("```", "").replace("")
        with open ("documento.py", "w") as f:
            f.write(codigo)
        subprocess.run("python", "documento.py")

    def crear_una_presentacion (self,tema:str):
        """
        Esta es una funcion que crea una presentacion de power point cuando el usuario dice
        "crea una presentacion sobre..." o algo asi

        Arg:
        tema: es el tema de la presentacion
        """

        try:
            resultado = self.model.generate_content([
                f"Créame una presentación de PowerPoint sobre {tema} en inglés",
                "Recuerda que tu resultado será un script de Python que con la librería pptx genere una presentación de PowerPoint, SOLO DEVUELVE EL CÓDIGO y recuerda al final abrir dicho archivo pptx usando la librería OS.",
                "En las cadenas de textos ni en los comentarios no uses caracteres especiales ni uses acentos como 'ñ' o 'á' y no coloques imagenes, has que la presentacion utilise dos estilos de letra y estilos visuales para la presentacion."
            ])

            # Verifica si el resultado contiene un bloque de código
            if "```" in resultado.text:
                codigo = resultado.text.split("```")[1].replace("python", "").replace("�", "")
            else:
                codigo = resultado.text  # Si no hay bloque de código, usa el texto completo

            # Escribe el código en un archivo Python
            with open("presentacion2.py", "w", encoding="utf-8") as f:
                f.write(codigo)

            # Ejecuta el archivo Python generado
            subprocess.run([sys.executable, "presentacion2.py"])
        except Exception as e:
            print(f"Error al crear la presentación: {e}")

    def escribir_una_nota(self, directorio_principal:str,carpeta:str,tema:str):

        """
            Description:
                Esta funcion crea una nota txt cuando el usuario expresa que quiere crear una nota sobre un tema , 
                en un directorio indicado por el usuario, por ejemplo, "crea una nota sobre..."
            Asrs:
                directorio_principal: Es el directorio principal donde se creara la carpeta
                carpeta: Es el nombre de la carpeta
                tema: Es el tema de la nota
        """
        result = self.model.generate_content([f"""Crea una nota sobre {tema}"""])
        carpeta_nativa = os.path.join(os.path.expanduser("~"), directorio_principal)
        carpeta_nota = os.path.join(carpeta_nativa, carpeta)
        os.makedirs(carpeta_nota, exist_ok=True)
        result = result.text.replace("#", "").replace("*", "")
        with open(os.path.join(carpeta_nota, f"{tema}.txt"), "w", encoding="utf-8") as archivo:
            archivo.write(result)
        subprocess.run([ 'notepad', os.path.join(carpeta_nota, f"{tema}.text")])
    
    def buscar_un_video(self, busqueda:str):
        """
        Description:

        Ags:
                busqueda: Es la busqueda que el usuario quiere hacer en youtube
        """  
        print("iniciando")      
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={busqueda}&type=video&key=AIzaSyC5cxHnowJ54rkppj8TMaRvD8HD8dnx6Ew&maxResults=1"
        reply = requests.get(url)
        data = reply.json()
        if reply.status_code == 200:
            print("Listo")
            if "items" in data and len(data["items"]) > 0:
                pass
            video_id = data["items"][0]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={id}" 
        subprocess.run(['msedge', video_url])

    def descargar_un_video(self,video_url:str):
        """
        Description:

    
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

gemini = Asistente("gemini-1.5-flash","audio.mp3",
                    "./models/vosk-model-small-es-0.42",
                    "hola",
                    config={
                        "temperature":0.8,
                        "top_p":0.95,
                        "top_k":64,
                        "max_output_tokens":8192,
                        "response_mime_type": "text/plain",
                    },
                    system_instruction="",
                    API="AIzaSyAKIXenE4WIyx96A9T6WgLCD1feLk-DOYY", 
                    vosk_model_lang="es",
                    )



gemini.crear_una_presentacion("el agua")



                    