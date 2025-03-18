import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import google.generativeai as genai
import os
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
        self.root.geometry("600x400")

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

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
        self.text_area.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
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

            # Obtener respuesta del asistente
            respuesta = self.asistente.answer(mensaje)
            self.text_area.insert(tk.END, f"Asistente: {respuesta}\n")

            # Reproducir la respuesta en audio
            self.hablar(respuesta)

    def iniciar_escucha(self):
        self.text_area.insert(tk.END, "Escuchando...\n")
        threading.Thread(target=self.transcribir_audio).start()

    def transcribir_audio(self):
        texto_transcrito = self.asistente.trascript()
        if texto_transcrito:
            self.text_area.insert(tk.END, f"Tú: {texto_transcrito}\n")
            respuesta = self.asistente.answer(texto_transcrito)
            self.text_area.insert(tk.END, f"Asistente: {respuesta}\n")
            self.hablar(respuesta)

    def hablar(self, texto):
        tts = gTTS(text=texto, lang="es")
        tts.save("respuesta.mp3")
        playsound.playsound("respuesta.mp3")

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

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AsistenteGUI(root)
    root.mainloop()