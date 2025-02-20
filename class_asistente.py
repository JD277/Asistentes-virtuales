import google.generativeai as genai 
## import playsound 
import vosk 
from vosk import Model, KaldiRecognizer
import os,json,sys,queue,sounddevice
## import pyaudio
import gtts
import docx 
import subprocess

class Asistente:
    def __init__(self, model_name: str,audio_path : str, vosk_path: str, key_word = "hola", config = {}, system_instrution = "", API = "", vosk_model_lang = "es"):
        self.model_name = model_name
        self.audio = audio_path
        self.vosk_path = vosk_path
        self.key_word = key_word
        self.config = config
        self.system_instruction = system_instrution
        self.API = API

        # Inicializando al modelo de IA de Gemini
        if self.API == "" or self.model_name == "" or self.config == {}: 
            raise Exception("Error al configurar gemini")
        try:
            genai.configure(api_key= self.API)
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config = self.config,
            )
            self.chat = self.model.start_chat()
        except Exception as e:
            print(e)
            #raise Exception("Error al configurar Gemini AI")
        # Configuracion el modelo de reconicimiento de voz 
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
                raise Exception("Error al cargar el model de reconocimiento de voz")
    def answer(self, text : str):
        result = self.chat.send_message(text)
        return result.text.replace("*","").replace("/","")
    def talk(self, text: str):
        model = gtts.gTTs(text,lang = self.vosk_model_lang)
        model.save(self.audio_path)
        try:
            playsound.playsound(self.audio_path)
        except Exception as e:
            print("No se pudo reproducir el audio")
    def trascript(self):
    
        try:
            model = Model(self.vosk_path)
        except Exception as e:
            try:
                model= Model(self.vosk_model_lang)
            except Exception as e :
                print("Error al cargar el modelo de voz")
        q = queue.Queue()
        def callback(indata, frames, times, status):
            q.put(bytes(indata))
        silence_duration = 1.5
        with sounddevice.RawInputStream(samplerate=16000,
                                            blocksize= 8000,
                                            dtype="int16",
                                            channels=1,
                                            callback=callback
                                            ):      
            print("Escuchando...")
            silence_counter = 0.0
            recognizer = KaldiRecognizer(model, 16000)
            final_text = ""
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())['text']
                    
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
                    print(partial)
                    if partial == "":
                        silence_counter += 1
                if silence_counter > silence_duration * (16000 / 8000):
                    print("Silence detected, stopping")
                    break
            if final_text != "":
                print("Listo!") 
                return final_text
            else:
                print("Listo!")
                return ""
            
        
    def key_word(self):
        try:
            model = Model(self.vosk_path)
        except Exception as e:
            try:
                model= Model(self.vosk_model_lang)
            except Exception as e :
                print("Error al cargar el modelo de voz")
        q = queue.Queue()
        def callback(indata, frames, times, status):
            q.put(bytes(indata))
        silence_duration = 1.5
        with sounddevice.RawInputStream(samplerate=16000,
                                            blocksize= 8000,
                                            dtype="int16",
                                            channels=1,
                                            callback=callback
                                            ):      
            print("Escuchando...")
            silence_counter = 0.0
            recognizer = KaldiRecognizer(model, 16000)
            final_text = ""
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())['text']
                    silence_counter = 0.0
                    final_tet += f" {result}"
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
                    print(partial)
                   
    def create_a_web_proyect(self,caracteristicas_pagina:str, nombre:str,ruta_proyecto:str):
        """
        Description:

        Args:
            caracteristicas_pagina: Es el tema de la pagina
            nombre: Es el nombre del proyecto 
            ruta_proyecto: Es la ruta donde se creara el proyecto
        """
        nombre_proyecto = nombre
        nombre_ruta_proyecto = ruta_proyecto
        carpeta_nativa = os.path.join(os.path.expanduser("~"), nombre_ruta_proyecto)
        carpeta_final = os.path.join(carpeta_nativa, nombre_proyecto)
        os.makedirs(carpeta_final, exist_ok=True)
        codigo_html = self.model.generate_content([caracteristicas_pagina,"crea una pagina web con estas caracteristicas y este tema, no incluyas ni explicaciones ni texto innecesario solo de vuelve codigo HTML, en el cual los estilos seran creados con la cdn de bootstrap y codigo css que estara en el mismo index HTML"])
        codigo_html = codigo_html.text.split("```html")[1].split('```')[0]
        with open(os.path.join(carpeta_final,"index.html"), "w", ending ="utf-8") as archivo_html:  
            archivo_html.write(codigo_html)
        os.system(f"start msedge {os.path.join(carpeta_final, 'index_html')}")
        os.system(f"start Code{carpeta_final}")
    def escribir_un_documento(self,tema:str):
        """
        Description:

        Args:
            tema: Es el tema del documento
        """
        result = self.model.generate_content([tema, "Redacta un ensayo de 500 palabras sobre el tema empleado"])
        codigo = result.text.split("```python")[1].replace("python","").replace("¬","")
        with open("documento.py","w") as f:
            f.write(codigo)
        subprocess.run(['python','documento.py'])
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
    
gemini = Asistente("gemini-2.0-flash",
                    "audio.mp3",
                    "./models/vosk-model-small-es-0.42",
                    "hola",
                    config={
                        "temperature":0.8,
                        "top_p":0.95,
                        "top_k":64,
                        "max_output_tokens":8192,
                        "response_mime_type": "text/plain",
                    },
                    system_instrution="",
                    API="AIzaSyDY1Ldl5_yOGcLzwbcj5gqe-LUNm4J--c0",   
                    vosk_model_lang="es", 
                    )
gemini.crear_una_presentacion("the legend of zelda")
