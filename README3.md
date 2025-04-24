# AI Assistant Family Project

## Overview

This project is a fusion of all the AI models created by adakademy students to make a class with seven methods each with a specific function. The gemini API was used for the different queries, vosk for user voice recognition, and other libraries.

---
## Project Descriptions

This project is a model of artificial intelligence capable of performing many tasks, which are | Answer, Talk, Transcription, Keyword, Create a web project, Write documents, Create a presentation, Write a note, Search for video, Download a video.

---
## Constructor

In this part, you set the different variables, initialize the Gemini AI model, and configure the vosk-recognition model.

```python
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
```



- **Atributes:**

  

---
| Method                | Arguments                         | Return            | Description                                                  |
| --------------------- | --------------------------------- | ----------------- | ------------------------------------------------------------ |
| Answer                | text                              | text              | Answer any questions the user asks                           |
| Talk                  | text                              | your audio        | El usuario escucha su texto convertido a voz                 |
| Transcript            | None                              | text              | The user hears your text converted to speech                 |
| Key word              | None                              | none              | Passive listening(does not return anything, only reacts when hearing the key) |
| Create a web project  | Features Page, Name, Project Path | Web proyect       | Create the HTML code of a page of the theme you want and open the page with the VSCode |
| Write documents       | Features Page, Name, Project Path | Word Document     | It allows you to write Word documents on the theme of your choice |
| Create a presentation | Theme                             | presentation PPTX | It creates a PowerPoint presentation of whatever you want    |
| Write a note          | main directory, folder, theme     | file.txt          | It creates notes on Notepad for anything                     |
| Search video          | search                            | youtube link      | It allows you to search for the first video that appears in the YouTube search engine of the topic you want and opens it in Google |
| Download a video      | search, root                      | video             | It allows you to search for the first video that appears in the YouTube search engine of the topic you want and downloads it to you |

## Dependences

The program needs the following functions to work at 100%.

- google.generativeai: It's to use the Gemini model for just about everything.
- vosk: It is used for speech recognition.
- pytube: is for video functions.
- os: to open apps.
- json: It is the standard format for communicating servers and clients (e.g., REST APIs).
- sys: Anointments and variables to interact with the Python interpreter and the operating system.
- queue: 
- sounddevice:
- requests:
- gtts: 
- docx : 
- subprocess: 
- yt_dlp: 

### How to install them?

   1.vosk: pip install vosk
2. google-generative.ai: pip install google-generative
3. pptx: pip install python-pptx
4. docx: pip install pyhon-docx
5. sounddevice: pip install sounddevice
6. playsound: pip install playsound
7. gtts: pip install gtts
8. yt-dlp: pip install yt-dlp



## Getting started

To get started, you need to create an API to use Gemini in your project.

1. Open your browser and search for Google AI Studio

2. Click on the first link in Google AI Studio

3. Click on the get API key button and then the create API button

4. Now click on the search engine and select Gemini.

5. Click create and copy the API.

  

Initialize the assistant:

```python
  python
  asistente = Asistente(
      model_name="gemini-pro",
      audio_path="response.mp3",
      vosk_path="./models/vosk-model-small-es-0.42",
      API="your_gemini_api_key"
  )


```

Basic voice interaction:

```python

  user_input = asistente.transcrip()  # Speak your command  
  response = asistente.answer(user_input)  # Get AI response  
  asistente.talk(response)  # Hear the answer  
```



Create a project:

  

```
  asistente.crear_un_proyecto_wed(
      "Portfolio website", 
      "my_portfolio", 
      "~/projects"
  )
```





## Donations

Here are our donations on Patrean, it would be very helpful if you support us with donations to continue creating and maintaining this activity on GitHub .

https://www.patreon.com
