'''
project name    : Jarvis
designed by     : Dinesh Kumar G
designed on     : 06.12.2024 , 19:30
purpose         :
'''
import pyttsx3 #
import speech_recognition as speech
import datetime
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. How can I help You?")      

def takecommand():
    r=speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...")
        r.pause_thershold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("I can't understand.please say again")
        return None
    return query

if __name__ == "__main__":
    wish()
    while True:
        query=takecommand().lower()
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open edge' in query:
            webbrowser.open("edge.com")  
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")      
        elif 'time ' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")
        elif 'stop' in query:
            print("thank you...")
            break
