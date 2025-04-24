import google.generativeai as genai
import playsound
from vosk import Model, KaldiRecognizer
import os
import json, sys, queue, sounddevice, requests
from gtts import gTTS
import docx
import subprocess
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import yt_dlp

class Asistente:
    def __init__(self, model_name: str, audio_path: str, vosk_path :str, key_word ="hola", config = {}, system_instruction ="", API ="", vosk_model_lang ="es"):
        #recibimos los parametros necesarios para la creacion del
        self.model_name = model_name
        self.audio_path = audio_path
        self.vosk_path = vosk_path
        self.key_word = key_word
        self.config = config
        self.system_instruction = system_instruction
        self.API = API
        self.vosk_model_lang = vosk_model_lang

        # inicializando el modelo de ia de gemini
        if self.API == "" or self.model_name == "" or self.config == {}:
            raise Exception("Error al configurar gemini AI")
        try:
            genai.configure(api_key=self.API)
            self.model = genai.GenerationModel(
                model_name=self.model_name,
                generation_config = self.config,
            )
            self.chat = self.model.start_chat()
        except Exception as e:
            raise Exception("Error al configurar Gemini AI")
        # Configurando el modelo de reconocimiento de voz
        self.q =queue.Queue()
        self.device_id = None
        self.sample_rate = 16000
        try:
            vosk_model = Model(self.vosk_path)
        except:
            try:
                print("Error al cargar el modelo de voz, colocando el modelo español...")
                self.vosk_model = Model(self.vosk_model_lang)
            except Exception as e:
                raise Exception("Error al cargar el modelo de reconocimiento de voz")

    def answer(self,text:str):
        result = self.chat.send_message(text)
        return result.text.replace("*","").replace("/","")
    
    def talk(self,text):
        model = gTTS(text,lang= self.vosk_model_lang)
        model.save("audio.mp3")
        print('todo chevere')
        try:
            playsound.playsound('C:/Users/Ada-Amarillo/Desktop/jesus/Constructores/proyecto-1/stan-jesu/audio.mp3')
        except Exception as e:
            print("No se pudo reproducir el audio")
        os.remove(self.audio_path)
    
    def transcript(self):
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
        with sounddevice.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16", channels=1, callback=callback):
            print("Escuchando...")
            silence_counter = 0
            recognizer = KaldiRecognizer(model, 16000)
            final_text = ""
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())['text']
                    silence_counter = 0
                    final_text += f" {result}"
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
                    print(partial)
                    print(partial)
                    if partial == "":
                        silence_counter += 1
                    print(silence_counter)

                if silence_counter >= silence_duration * (16000 / 8000):
                    print("Silence detected, stopping...")
                    break
            if final_text != "":
                print("Listo!")
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
        
        with sounddevice.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16", channels=1, callback=callback):
            print("Escuchando...")
            recognizer = KaldiRecognizer(model, 16000)
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())['text']
                    if word in result:
                        return True                   
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
                    if word in result:
                        return True
                    
    def crear_un_proyecto_web(self, caracteristicas_pagina:str, nombre:str, ruta_proyecto:str):
        
        """
        Description:
            Esta función realiza una serie de pasos para crear un proyecto web básico, generar un archivo HTML, guardarlo en una carpeta específica y abrir tanto el archivo HTML en un navegador como la carpeta del proyecto en un editor de código.
            Esta funcion  se activa cuando el usuario dice:'Necesito una pagina web sobre...', 'Realiza una pagina web sobre...', 'Haz una pagina web sobre...'
        Args:
            caracteristicas_pagina: es el tema de la pagina web
            nombre: es el nombre delproyecto
            ruta_proyecto: Es la ruta donde se crea el proyecto
        """
        
        nombre_proyecto = nombre
        nombre_ruta_proyecto = ruta_proyecto
        carpeta_nativa = os.path.join(os.path.expanduser(~), nombre_ruta_proyecto)
        carpeta_final = os.path.join(carpeta_nativa, nombre_proyecto)
        os.makedirs(carpeta_final, exist_ok=True)
        codigo_html = self.model.generate_content([caracteristicas_pagina, ""])
        codigo_html = codigo_html.text.split("´´´html")[1].split('´´´')[0]
        with open(os.path.join(carpeta_final, "index.html"), "w", encoding="utf-8") as archivo_html:
            archivo_html.write(codigo_html)
        os.system(f"start msedge {os.path.join(carpeta_final, 'index.html')}")
        os.system(f"start Code {carpeta_final}")

    def escribir_un_proyecto(self,tema:str):
        """
        Description:
            Esta función utiliza un modelo para generar un script de Python que crea un documento de Word sobre un tema específico.
            Esta funcion se activa cuando el usuario dice: 'Crea un trabajo sobre...', 'Haz un trabajo sobre...', 'realiza un trabajo sobre...', 'hazme un trabajo sobre...'
        Args:
            tema: Es el tema del proyecto
        """
        result = self.model.generate_content([tema, "Redacta un trabajo de 500 palabras sobre el tema"])
        codigo = result.text.split("```")[1].replace("python", "").replace("~", "")
        with open ("document.py", "w") as f:
            f.write(codigo)
        subprocess.run(['python', 'documento.py'])
    #resultado = model2.generate_content([f"Crea un trabajo de word sobre {tema} utilizando la libreria 'docx'","Recuerda que tu resultado sera un script de python que con la libreria docx genere un trabajo, solo devuelve el codigo y recuerda al final abrir dicho archivo docx usando la libreria os y que el archivo", "En las cadenas de textos ni en los comentarios no uses caracteres especiales ni uses acentos como 'ñ' o 'á', tampoco uses componetes como iamgenes ni dada parecido porque provocara errores en el código"])

    def crear_una_presentacion(self,tema:str):
        """
        Esta es una función que crea una presentación de PowerPoint cuando el usuario dice
        "crea una presentación" o algo así.
        Args:
            tema: Es el tema de la presentación.
        """
        try:
            resultado = self.model.generate_content([
                f"Créame una presentación de PowerPoint sobre {tema} en inglés",
                "Recuerda que tu resultado será un script de Python que con la librería pptx genere una presentación de PowerPoint, SOLO DEVUELVE EL CÓDIGO y recuerda al final abrir dicho archivo pptx usando la librería OS.",
                "En las cadenas de textos ni en los comentarios no uses caracteres especiales ni uses acentos como 'ñ' o 'á' y no coloques imagenes."
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
        
    def escribir_notas(self, directorio_principal:str,carpeta:str,tema:str):
        """
        Description:
            esta funcion es para crear una nota txt cuando el usuario expresa que quiere crear una nota sobre un tema, en un directorio indicado por el usuario
        Args:
            directorio_principal: Es el directorio principal donde se creara la carpeta
            carpeta: Es el nombre de la carpeta
            tema: Es el tema de la nota
        """
        result = self.model.generate_content([f"""Crear una nota sobre {tema}"""])
        carpeta_nativa = os.path.join(os.path.expanduser(~), directorio_principal)
        carpeta_nota = os.path.join(carpeta_nativa, carpeta)
        os.makedirs(carpeta_nota, exist_ok=True)
        result = result.text.replace("#","").replace("*","")
        with open(os.path.join(carpeta_nota, f"{tema}.txt"), "w", encoding="utf-8") as archivo:
            archivo.write(result)
        subprocess.run(['notepad', os.path.join(carpeta_nota, f"{tema}.txt")])

    def buscar_un_video(self, busqueda:str):
        """
        Description:
            Esta funcion realiza la accion de buscar videos en youtube y descargarlos
        Args:
            Es la busqueda que hace el usuario en youtube
        """
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={busqueda}&type=video&key=AIzaSyDNKAhvs-o_2PhVLMIO7AS1it7ez13_Nms&maxResults=1"
        reply = requests.get(url)
        data = reply.json
        if reply.status_code == 200:
            print("Listo")
            if "items" in data and len(data["items"]) > 0:
            video_id = data["items"][0]["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={id}"
            subprocess.run(['msedge', video_url])

    def descargar_un_video(self, busqueda:str, ruta:str):
        """
        Description:

        Args:
            video_url: Es la busqueda que el usuario quiere hacer en youtube
            ruta: Es la ruta donde se guardara el video
        """
        ydl_ops= {
            'format': 'bestvideo',
            'outtmpl': f'{ruta}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4'
            }
        try:
            print("iniciando")
            url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={busqueda}&type=video&key=AIzaSyDNKAhvs-o_2PhVLMIO7AS1it7ez13_Nms&maxResults=1"
            reply = requests.get(url)
            data = reply.json
            if reply.status_code == 200:
                print("Listo")
                if "items" in data and len(data["items"]) > 0:
                video_id = data["items"][0]["id"]["videoId"]
                video_url = f"https://www.youtube.com/watch?v={id}"
                with yt_dlp.YoutubeDL(ydl_ops) as ydl:
                    ydl.download([video_url])
        except Exception as e:
            print("Error al descargar el video")
gemini = Asistente("gemini-2.0-flash", "audio.mp3", "./models/vosk-model-small-es-0.42", "hola", config={"temperature":0.8,"top_p":0.95, "top_k":64, "max_output_tokens":8192, "response_mime_type": "text/plain"}, system_instruction="", API="AIzaSyDY1Ldl5_yOGcLzwbcj5gqe-LUNm4J--c0", vosk_model_lang="es")
gemini.transcript()

#gemini.crear_un_proyecto_web("""crea una pagina web en la cual tenga bootstrap, css y javascript y compares el ford gt40 contra el ferrari 330 p4, utiliza colores alusivos a ferrari y a ford""", "ford_v_ferrari", "")