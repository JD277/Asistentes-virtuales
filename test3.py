import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import threading
import google.generativeai as genai
import os , sys
import subprocess
from gtts import gTTS
#import playsound
import queue
import sounddevice
import json

from vosk import Model, KaldiRecognizer

class AsistenteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente Multimodal Gemini 2.0")
        self.root.geometry("700x500")

        # Configuración del asistente
        self.asistente = Asistente(
            model_name="gemini-2.0-flash",
            audio_path="audio.mp3",
            vosk_path="./models/vosk-model-small-es-0.42",
            key_word="hola",
            config={
                "temperature": 0.8,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            },
            system_instrution="",
            API="AIzaSyDY1Ldl5_yOGcLzwbcj5gqe-LUNm4J--c0",
            vosk_model_lang="es",
        )

        # Interfaz gráfica
        self.label = tk.Label(root, text="Asistente Multimodal Gemini 2.0", font=("Arial", 16))
        self.label.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(pady=10)

        self.entry = tk.Entry(root, width=60)
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.send_button = tk.Button(self.button_frame, text="Enviar", command=self.enviar_mensaje)
        self.send_button.pack(side=tk.LEFT, padx=5)

        self.listen_button = tk.Button(self.button_frame, text="Escuchar", command=self.iniciar_escucha)
        self.listen_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Limpiar", command=self.limpiar_texto)
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def enviar_mensaje(self):
        mensaje = self.entry.get()
        if mensaje:
            self.text_area.insert(tk.END, f"Tú: {mensaje}\n")
            self.entry.delete(0, tk.END)

            # Procesar el mensaje para detectar comandos
            self.procesar_comando(mensaje)

    def iniciar_escucha(self):
        self.text_area.insert(tk.END, "Escuchando...\n")
        threading.Thread(target=self.transcribir_audio).start()

    def transcribir_audio(self):
        texto_transcrito = self.asistente.trascript()
        if texto_transcrito:
            self.text_area.insert(tk.END, f"Tú: {texto_transcrito}\n")
            self.procesar_comando(texto_transcrito)

    def procesar_comando(self, texto: str):
        # Convertir el texto a minúsculas para facilitar la detección de comandos
        texto = texto.lower()

        # Detectar comandos y ejecutar métodos correspondientes
        if "crear documento" in texto or "escribir documento" in texto:
            tema = texto.replace("crear documento", "").replace("escribir documento", "").strip()
            if tema:
                self.asistente.escribir_un_documento(tema)
                self.text_area.insert(tk.END, f"Documento creado sobre: {tema}\n")
            else:
                self.text_area.insert(tk.END, "Por favor, especifica un tema para el documento.\n")

        elif "crear proyecto web" in texto or "hacer proyecto web" in texto:
            tema = texto.replace("crear proyecto web", "").replace("hacer proyecto web", "").strip()
            if tema:
                nombre_proyecto = filedialog.askstring("Nombre del Proyecto", "Ingresa el nombre del proyecto:")
                ruta_proyecto = filedialog.askdirectory(title="Selecciona la ruta para guardar el proyecto")
                if nombre_proyecto and ruta_proyecto:
                    self.asistente.create_a_web_proyect(tema, nombre_proyecto, ruta_proyecto)
                    self.text_area.insert(tk.END, f"Proyecto web '{nombre_proyecto}' creado en: {ruta_proyecto}\n")
                else:
                    self.text_area.insert(tk.END, "Debes proporcionar un nombre y una ruta para el proyecto.\n")
            else:
                self.text_area.insert(tk.END, "Por favor, especifica un tema para el proyecto web.\n")

        elif "crear presentación" in texto or "hacer presentación" in texto:
            tema = texto.replace("crear presentación", "").replace("hacer presentación", "").strip()
            if tema:
                self.asistente.crear_una_presentacion(tema)
                self.text_area.insert(tk.END, f"Presentación creada sobre: {tema}\n")
            else:
                self.text_area.insert(tk.END, "Por favor, especifica un tema para la presentación.\n")

        elif "escribir nota" in texto or "crear nota" in texto:
            tema = texto.replace("escribir nota", "").replace("crear nota", "").strip()
            if tema:
                directorio = filedialog.askdirectory(title="Selecciona la ruta para guardar la nota")
                if directorio:
                    nombre_carpeta = filedialog.askstring("Nombre de la Carpeta", "Ingresa el nombre de la carpeta:")
                    if nombre_carpeta:
                        self.asistente.escribe_una_nota(directorio, nombre_carpeta, tema)
                        self.text_area.insert(tk.END, f"Nota creada en: {os.path.join(directorio, nombre_carpeta)}\n")
                    else:
                        self.text_area.insert(tk.END, "Debes proporcionar un nombre para la carpeta.\n")
                else:
                    self.text_area.insert(tk.END, "Debes seleccionar una ruta para guardar la nota.\n")
            else:
                self.text_area.insert(tk.END, "Por favor, especifica un tema para la nota.\n")

        else:
            # Si no es un comando, obtener respuesta del asistente
            respuesta = self.asistente.answer(texto)
            self.text_area.insert(tk.END, f"Asistente: {respuesta}\n")
            self.hablar(respuesta)

    def hablar(self, texto):
        tts = gTTS(text=texto, lang="es")
        tts.save("respuesta.mp3")
        #playsound.playsound("respuesta.mp3")

    def limpiar_texto(self):
        self.text_area.delete(1.0, tk.END)

# Clase Asistente (la que proporcionaste)
class Asistente:
    def __init__(self, model_name: str, audio_path: str, vosk_path: str, key_word="hola", config={}, system_instrution="", API="", vosk_model_lang="es"):
        self.model_name = model_name
        self.audio_path = audio_path
        self.vosk_path = vosk_path
        self.key_word = key_word
        self.config = config
        self.system_instruction = system_instrution
        self.API = API

        # Inicializando al modelo de IA de Gemini
        if self.API == "" or self.model_name == "" or self.config == {}:
            raise Exception("Error al configurar Gemini")
        try:
            genai.configure(api_key=self.API)
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=self.config,
            )
            self.chat = self.model.start_chat()
        except Exception as e:
            print(e)
            raise Exception("Error al configurar Gemini AI")

        # Configuración del modelo de reconocimiento de voz
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
                raise Exception("Error al cargar el modelo de reconocimiento de voz")

    def answer(self, text: str):
        result = self.chat.send_message(text)
        return result.text.replace("*", "").replace("/", "")

    def trascript(self):
        try:
            model = Model(self.vosk_path)
        except Exception as e:
            try:
                model = Model(self.vosk_model_lang)
            except Exception as e:
                print("Error al cargar el modelo de voz")
        q = queue.Queue()

        def callback(indata, frames, times, status):
            q.put(bytes(indata))

        silence_duration = 1.5
        with sounddevice.RawInputStream(samplerate=16000,
                                       blocksize=8000,
                                       dtype="int16",
                                       channels=1,
                                       callback=callback):
            print("Escuchando...")
            silence_counter = 0.0
            recognizer = KaldiRecognizer(model, 16000)
            final_text = ""
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())['text']
                    final_text += f" {result}"
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
                    print(partial)
                    if partial == "":
                        silence_counter += 1
                if silence_counter > silence_duration * (16000 / 8000):
                    print("Silencio detectado, deteniendo...")
                    break
            if final_text != "":
                print("Listo!")
                return final_text
            else:
                print("Listo!")
                return ""

    def escribir_un_documento(self, tema: str):
        result = self.model.generate_content([tema, "Redacta un ensayo de 500 palabras sobre el tema empleado"])
        codigo = result.text.split("```python")[1].replace("python", "").replace("¬", "")
        with open("documento.py", "w") as f:
            f.write(codigo)
        subprocess.run(['python', 'documento.py'])

    def create_a_web_proyect(self, caracteristicas_pagina: str, nombre: str, ruta_proyecto: str):
        nombre_proyecto = nombre
        carpeta_final = os.path.join(ruta_proyecto, nombre_proyecto)
        os.makedirs(carpeta_final, exist_ok=True)
        codigo_html = self.model.generate_content([caracteristicas_pagina, "crea una pagina web con estas caracteristicas y este tema, no incluyas ni explicaciones ni texto innecesario solo de vuelve codigo HTML, en el cual los estilos seran creados con la cdn de bootstrap y codigo css que estara en el mismo index HTML"])
        codigo_html = codigo_html.text.split("```html")[1].split('```')[0]
        with open(os.path.join(carpeta_final, "index.html"), "w", encoding="utf-8") as archivo_html:
            archivo_html.write(codigo_html)
        os.system(f"start msedge {os.path.join(carpeta_final, 'index.html')}")
        os.system(f"start Code {carpeta_final}")

    def crear_una_presentacion(self, tema: str):
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

    def escribe_una_nota(self, directorio_principal: str, carpeta: str, tema: str):
        ruta_final = os.path.join(directorio_principal, carpeta)
        os.makedirs(ruta_final, exist_ok=True)
        nota = self.model.generate_content([tema, "Escribe una nota sobre el tema proporcionado."])
        with open(os.path.join(ruta_final, "nota.txt"), "w", encoding="utf-8") as f:
            f.write(nota.text)

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AsistenteGUI(root)
    root.mainloop()