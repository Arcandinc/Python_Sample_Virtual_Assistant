from email.mime import audio
from logging.config import listen
import time
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr 
import os
from datetime import datetime 
r = sr.Recognizer()
import random
from random import choice
import webbrowser
import cv2
import numpy as np


def record(ask = False):
    with sr.Microphone() as source :
        r.adjust_for_ambient_noise(source,duration=1)
        if ask:
            print(ask)
        audio= r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım.")
        except sr.RequestError:
            print("Asistan: Sistem Çalışmıyor")
        return voice



def response(voice):
    if "merhaba" in voice:
        speak("sanada merhaba nasılsın")
    
    if "iyiyim" in voice:
        speak("harika çok sevindim")
        
    if "selam" in voice:
        speak("selam nasılsın")
    
    if "nasılsın" in voice:
        speak("çok iyiyim sorduğun için teşekkür ederim.")
        
    if  "kötüyüm" in voice:
        speak("tamamdır peki nedenini öğrenebilir miyim")
        
    if "teşekkür ederim"  in voice:
        speak("rica ederim")
        
    if "görüşürüz" in voice :
        speak("görüşürüz sahip")
        exit()
        
    if "hangi gündeyiz" in voice:
        today= time.strftime("%A")
        print(today)
        if today=="Sunday":
            today = "pazar"
        elif today=="Monday":
           today = "pazartesi"
        elif today=="Tuesday":
           today = "salı"
        elif today=="Wednesday":
           today = "çarşamba"
        elif today=="Thursday":
           today = "perşembe"
        elif today=="Friday":
           today = "cuma"
        elif today=="Saturday":
           today = "cumartesi"
        speak(today)  
    
    if "saat kaç" in voice:
        selection =["saat şuan :", "hemen bakıyorum: "]
        clock= datetime.now().strftime("%H: %M")
        selection= random.choice(selection)
        speak(selection + clock)
             

    if "google'da ara" in voice:
        speak( "ne aramamı istersin?")
        search=record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} için google'da bulduklarımı listeliyorum sahip.".format(search))
        
    if "uygulama aç" in voice:
        speak("hangi uygulamayı açmamı istersin sahip?")
        runApp = record()
        runApp = runApp.lower()
        if "komut istemi" in runApp:
            os.startfile("C:\Windows\system32\cmd.exe")
            speak("hemen başlatıyorum sahip")
            
    if "resim çek" in voice:
        kamera=cv2.VideoCapture(0) # 0 numaralı kayıtlı kamerayı alma
        kamera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #­ Kamera Boyutlandırma
        ret,goruntu=kamera.read() # kamera okumayı başlatma
        cv2.imshow('Normal Goruntu',goruntu) # görüntüyü gösterme
        cv2.imwrite('img/arcan.jpg', goruntu)
        
def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file="answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
    
    
speak("Sana Nasıl Yardımcı Olabilirim Sahip") 
   
while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)

