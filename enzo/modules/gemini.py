import os
import google.generativeai as genai 
import urllib
import requests
import yt_dlp 

funtions=[]
API_KEY="AIzaSyD--kHOT3Vp6QiuaXNyBA_Zx0L6CQ-lUls"
genai.configure(api_key=API_KEY)

config={
    "temperature":0.8,
    "top_p":0.95,
    "top_k":64,
    "max_output_tokens":8192,
    "response_mime_type": "text/plain",
}
activado=False
def buscar_un_video(busqueda:str):
    global activado
    """buscar en liena
    description: es una funcion que va a buscar en navegador
    lo que se 
    le indique cuando el usuario diga 'busca un video sobre...'  o algo parecido
    args: 
    busqueda:la busqueda de que el usario indique """

    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={busqueda}&type=video&key=AIzaSyDj-uVEZb31MJcg5VYm_5VPKP9mt8q-m6Q&maxResults=1"
    reply = requests.get(url)
    data = reply.json()
    if reply.status_code == 200:
        print("Listo")
        # Verifica que se obtuvieron resultados
        if "items" in data and len(data["items"]) > 0:
            # Obtiene el ID del primer video
            video_id = data["items"][0]["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            print("Tu video se encuentra en el navegador ya!")
            os.system(f"start msedge {video_url} &")
            download_video(video_url)
        activado = True

model= genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config =config,
    tools=[buscar_un_video]
)

chat=model.start_chat(enable_automatic_function_calling=True)

def answer(text:str):
    global activado
    result = chat.send_message(text)
    if not activado:
        return result.text.replace("*","").replace("/","")
    else:
        return "Acción realizada"


def download_video(video_url):
        yld_ops= {
            'format': 'bestvideo',
            'outtmpl':'%(title)s.%(ext)s',
            'mergue_output_format': 'mp4'
        }
        print("Iniciando")
        try:
            with yt_dlp.YoutubeDL(yld_ops) as ydl:
                ydl.download([video_url])
            print("listo")
        except Exception as e:
            print("Hubo un error en la descarga"[e])

