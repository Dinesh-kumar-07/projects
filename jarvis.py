'''
project name    : Jarvis
designed by     : Dinesh Kumar G
designed on     : 06.12.2024 , 19:30
purpose         :Create a Basic Voice Assistant (JARVIS) using Python
'''
# Required libraries
import pyttsx3 # For text-to-speech
import speech_recognition as speech # For speech-to-text (voice input)
import datetime                    # To fetch system time
import webbrowser                  # To open websites in browser
import os                          # Not used here but often for OS-level commands

# Initialize the voice engine
engine=pyttsx3.init('sapi5')# sapi5 is for Windows voice API
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first available voice

# Function to speak the given text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet user based on the current time
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. How can I help You?")      

# Function to capture voice input from the user and convert to text
def takecommand():
    r=speech.Recognizer()# Create a recognizer instance
    with speech.Microphone() as source:
        print("Listening...")
        r.pause_thershold=1 # Wait time between phrases
        audio = r.listen(source)  # Capture audio input
        

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in') # Convert audio to text using Google API
        print(f"User said:{query}\n")

    except Exception as e:
        print("I can't understand.please say again")
        return None
    return query

# Main program execution starts here
if __name__ == "__main__":
    wish()
    while True:
        query=takecommand().lower() # Convert to lowercase for easy comparison
        # Convert to lowercase for easy comparison
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open edge' in query:
            webbrowser.open("edge.com")  
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")   
        # Respond with the current time
        elif 'time ' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")
        # Exit the assistant
        elif 'stop' in query:
            print("thank you...")
            break
