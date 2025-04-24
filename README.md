# S.P.A.R.K (Smart Project Automation Resourceful Knowledgeable)



## Overview

This project created by **Adacademy** students is an assistant capable of performing various tasks such as answering questions, creating web projects, generating documents and searching youtube videos. The assistant uses Google's Gemini AI through its API key for text generation.

## Description 

- the project uses a class called Assistant, with which we can facilitate programming and add new features such as:

  - **Speech integration:** Uses Vosk's Speech-to-Text model to convert speech to text and Google Text-to-Speech to convert text to speech.

  - **AI responses:** Uses Gemini's API key to generate responses or content based on user requests.

  - **Task Automation:** this project helps in creating web projects, Word documents and creating PowerPoint presentations.

  - **Content Search:** This wizard also facilitates content search, such as searching for YouTube videos on a topic that the user indicates.


## Dependences

This Wizard uses libraries that you will need to install in order to use it: 

- **Google.generativeai:** this library is used to load the Gemini 2.0 Flash AI model.

  ```bash
  pip install googelgenerativeai
  ```

- **Vosk:** this is the speech recognition model

  ```bash
  pip install vosk
  ```

- **gTTS:** this is the Google model that converts speech to text

  ```bash
  pip install gtts
  ```

- **Playsound:** used to play the user's own audio files

  ```bash
  pip install playsound
  ```

- **Sounddevice:** used to record the user's audio input

  ```bash
  pip install sounddevice
  ```

- **Requests:** used to make the HTTP requests necessary for searching YouTube videos

  ```bash
  pip install request
  ```

- **Python-docx and pptx:** are the libraries needed for the creation of Word documents and PowerPoint presentations

  ```bash
  pip install python-docx, python-pptx
  ```

- **Pytube:** are the package that allows downloads videos of Youtube.

  ```bash
  pip instal pytube
  ```

## Module Description:

The asistente class contains the following methods which are the functions that the asistente has:

|                           Methods                            |                             Arg                              |                   Return                    |                         Description                          |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :-----------------------------------------: | :----------------------------------------------------------: |
| ![image-20250327190452849](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250327190452849.png)‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ | ![image-20250327191051445](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250327191051445.png) the prompt of the user |       a plain str with that ai answer       | Generates a Gemini AI response based on the input prompt or text. |
| ![image-20250327190729572](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250327190729572.png) | ![image-20250327191104138](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250327191104138.png) receives a string and converts it to audio |                  **None**                   | this is a function that use gTTS to convert the text to an audio and later play it with playsound |
| ![image-20250327192335827](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250327192335827.png) |                           **None**                           | a string with the audio that the user sends |    transcribes what the user asks or says to the asistant    |
| <br />![](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250401183304387.png)‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ | <br />![image-20250401182509430](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250401182509430.png) is the keyword that is going to be detected |            <br /><br />**None**             | It is a function that detects a keyword to activate the code. |
| <br /><br /><br /><br /><br /><br /><br />![image-20250401184123300](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250401184123300.png) | ![image-20250401184332384](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250401184332384.png)Detailed description of the features and theme of the website you want to create<br />![image-20250401184620632](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250401184620632.png) Name of the project and the main folder to be created<br />![image-20250401185024372](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250401185024372.png)Path where the project folder will be created |   <br /><br /><br /><br /><br />**None**    | Creates a basic web project with a dynamically generated HTML page based on the provided features. The function generates a folder structure at the specified path, creates an `index.html` file with the HTML, CSS (using Bootstrap v5.3), and JavaScript code, and automatically opens the file in the code editor and the default browser. The web page is responsive, includes Bootstrap components such as a navbar, cards, modals, carousel, and more, and uses external images embedded directly from URLs. |
|                                                              |                                                              |                                             |                                                              |
|                                                              |                                                              |                                             |                                                              |
|                                                              |                                                              |                                             |                                                              |

## Getting Started

**Step 1:** Open you browswer

![image-20250401192035321](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250401192035321.png)

**Step 2:** search "Google AI Studio"

![image-20250401192245484](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250401192245484.png)

**Step 3:** sign in in your Google account

![image-20250401192443825](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250401192443825.png)

**Step 4:** Click on "Get API key"

![image-20250402181153199](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250402181153199.png)

**Step 5:** Click on "Create API key" or "Crear clave de API"

![image-20250402181400434](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250402181400434.png)

**Step 6:** Click on "Gemini API"

![image-20250402181519051](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250402181519051.png)

**Step 7:** Finally, click on create API key

![image-20250402181716869](C:\Users\josep\AppData\Roaming\Typora\typora-user-images\image-20250402181716869.png)

## Donations

PLEASE GIVE ME MONEY I'M POOR : ,(

Pago movil: 

