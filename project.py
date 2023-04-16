import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes
from youtube_dl import YoutubeDL
import subprocess
import time
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pytube import YouTube

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print(">>>good morning!")
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        print(">>>good afternoon!")
        speak("good afternoon!")
    else:
        print(">>>good evening!")
        speak("good evening!")
    print(">>>How may i help you?")
    speak("How may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(">>>listening...")
        r.adjust_for_ambient_noise(source)
        audio2 = r.listen(source)

    try:
        print(">>>recognizing...")
        query = r.recognize_google(audio2)
        print(query)

    except:
        print(">>>Sorry. I dint get you...")
        return "None"

    return query


                   

def sorry():
    speak("Sorry. I dint get you")

if __name__ == '__main__':
    wishMe()
    run = 1
    while run:
        query = takeCommand().lower()

        if "your name" in query:
            print(">>>My name is Gia ")
            speak("my name is Gia ")
            exit()

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
            exit()

        if 'search' in query:
            query = query.replace("search", "")
            url = 'https://google.com/search?q=' + query
            webbrowser.get().open(url)
            speak(f"here's what i found for {query}")
            exit()

        if 'find location of' in query:
            query = query.replace("find location of", "")
            url = 'https://google.nl/maps/place/' + query + '/&amp'
            webbrowser.get().open(url)
            speak(f"here's the location for {query}")
            exit()

        elif "open youtube" in query:
            speak("opening youtube...")
            webbrowser.open("youtube.com")
            exit()

        elif "time" in query:
            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            if hour > 12:
                hour -= 12
                if int(datetime.datetime.now().minute) == 0:    
                    print(f">>>The Time is {hour} p.m.")
                    speak(f"The Time is {hour} p.m.") 
                else: 
                    print(f">>>The Time is {hour} {min} p.m.")
                    speak(f"The Time is {hour} {min} p.m.")
            else:
                if int(datetime.datetime.now().minute) == 0:
                    print(f">>>The Time is {hour} a.m.")
                    speak(f"The Time is {hour} a.m.")
                else:
                    print(f">>>The Time is {hour} {min} a.m.")
                    speak(f"The Time is {hour} {min} a.m.")
            exit()

        elif "open code" in query:
            # codePath = "C:\\Users\\navee\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening code...")
            os.startfile(codePath)
            exit()

        elif "open spotify" in query:
            speak("opening spotify...")
            subprocess.call("spotify.exe")
            exit()

        elif "play" and "youtube" in query:
            query = query.replace("play", "")
            query = query.replace("on youtube", "")
            query = query.replace("from youtube", "")
            print(f">>>playing {query} on youtube...")
            speak(f"playing {query} on youtube")
            pywhatkit.playonyt(query)
            exit()

       

        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(f">>>{joke}")
            speak(joke)
            exit()

        elif 'audio' in query:
            query = query.replace('download','')
            query = query.replace('audio','')
            print(f">>>downloading {query} audio...")
            speak(f"downloading {query} audio")
            URL = pywhatkit.playonyt(query)
            audio_downloader = YoutubeDL({'format':'bestaudio'})
            audio_downloader.extract_info(URL)
            exit()

        # elif 'video' in query:
        #     # query = query.replace('download','')
        #     # query = query.replace('video','')
        #     # URL = pywhatkit.playonyt(query)
        #     # yt = YouTube(URL)
        #     # yt.streams.first().download()
        #     # exit()

        elif 'exit' in query:
            print(">>>See you later")
            speak("See you later")
            exit()

        elif "your name" and 'wikipedia' and 'search' and 'find location of' and "open youtube" and "the time" and "open code" and "open spotify" and "joke" and "play" and "on youtube" and "exit" and "download" and "audio" not in query:
            sorry()

    run = 0