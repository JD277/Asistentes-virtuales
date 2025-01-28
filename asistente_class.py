import google.generativeai as genai
import playsound
from vosk import Model, KaldiRecognizer
import os, json, sys, queue, sounddevice
from gtts import gTTS


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

    def key_word(self):
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
                    
                else:
                    partial = json.loads(recognizer.PartialResult())['partial']
        
                        
                # Check if silence has been detected for enough time
                
            

    
                
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



                    