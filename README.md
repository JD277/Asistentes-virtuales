# AI Assistant Family Project
## Table of Contents:

1) [Overview](Overview)
1) [Descriptions](Description)
1) [Dependences](Dependence)
1) [Methods description](Methods Description)
1) Getting started
1) Donations



## Overview 

​	Students developed this project from adakademy. The project's main goal was to create different models of AI using the API key of Gemini. Each model can answer some questions from the user and do all that with advanced technology, but only if it is related to their task, so, they decide that it is better to fusion those models into one. In addition, they used Vosk AI for local speech recognition, this improves the way to say questions to the model with better quality, making it easier.

The models demonstrate a good use of each, with a lot of creativity and productivity. Besides, some of them can be considered as a little shortcut depending on the model you use. Below, you will find a precise description of each model with its features.

---

## Descriptions

​	The project has a lot of model that are fused into one, so it can do more thing than the separated models, each model can do only one thing, for example, download a video from YouTube or tell stories in a Word document, each one has the API key of Gemini, so all the tests we did with those models was to try to work with the function of the model and do a prompt in Gemini that specify to answer with only the task I suggest and answer without any unnecessary text so after we found the right prompt that could work, we copy and paste the prompt to the function of the model. Every student worked on their models and developed their tasks.

---

## Dependence 

​	During the classes, we implemented frameworks that helped the models a lot and were necessary for each one of the models, which are: 

*  **GTTS**
*  **Genai(Google.generativeai)**
*  **Vosk**
*  **Playsound**
*  **Soundevice**
*  **python-pptx**
*  **python-docx**
*  **pytube**

****

## Methods Description 

​	

| Methods                | Args                                                         | Description                                                  | return                                                       |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Answer                 | NONE                                                         | It tries to generate the answer                              | It returns the result of the answer                          |
| Talk                   | NONE                                                         | This method records user speech for 10 seconds and responds with *"Audio could not be played"* if no input is detected. | Returns the audio of the user                                |
| Transcript             | NONE                                                         | This method records the user's audio for 10 seconds, signaling *"Listening..."* during recording, *"Ready!"* on success, *"Error loading voice model"* if it fails, and *"Silence detected, stopping..."* if no speech is detected. | Returns the final text of what the user said                 |
| Key_word               | NONE                                                         | This method requires the user to say the wake word **"hola"** to activate the model before speaking, otherwise, it remains inactive. | Returns "True" when the user say the key word                |
| crear_un_proyecto_web  | **caracteristicas_pagina:** Es el tema de la pagina web<br />**nombre:** Es el nombre del proyecto<br />**ruta_proyecto:** Es la ruta donde se creara el proyecto | Creates a web page and opens it in the browser and in VS code, when the user says: <br/>            Create a page about..., create a web site..., create a page.... | Returns the web page of what the user said                   |
| escribir_un_documento  | **Tema:** Es el tema del documento                           | Start writing in a Word document on a topic requested by the user. Example, <br/>            I want you to make a Word document about... or make a document about... | Returns a Word document of what the user said his specifications |
| crear_una_presentacion | **Tema:** es el tema de la presentacion                      | This is a function that creates a PowerPoint presentation when the user says<br/>        “Create a presentation about...” or something like that. | Returns the power point presentation of what the user said.  |
| escribir_una_nota      | **directorio_principal**: Es el directorio principal donde se creara la carpeta<br/>**carpeta**: Es el nombre de la carpeta<br />**tema:** Es el tema de la nota | This function creates a txt note when the user expresses that he wants to create a note about a subject, <br/>                In a directory specified by the user, e.g, “create a note about...”. | Returns the txt note of what the user said.                  |
| buscar_un_video        | **busqueda**: Es la busqueda que el usuario quiere hacer en youtube | This function searches for a youtube video requested by the user, for example,<br/>            "I want the video about..." or "I want a video about..." | Returns a URL of a video from YouTube of what the user wants to see |
| descargar_un_video     | **video_url**: Es al url del video que el usuario quiere descargar | This function downloads a video requested by the user, for example, <br/>            “I want you to download the following video” or ‘I want you to download a video about...’. | Returns a YouTube video of what the user said.               |

---



## Getting started 



1.Open the navigator:

![image-20250401192346752](C:\Users\Juan\AppData\Roaming\Typora\typora-user-images\image-20250401192346752.png)









