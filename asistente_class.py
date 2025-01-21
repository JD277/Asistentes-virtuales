import google.generativeai as genai
import playsound
from vosk import Model, KaldiRecognizer
import os
import json
import sys
import queue
import sounddevice
from gtts import gTTS


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
        

    