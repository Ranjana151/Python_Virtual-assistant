# Virtual Assistant
#It help to do work in easy manner which we performed daily

import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)







def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    h = int(datetime.datetime.now().hour)
    #print(h)

    if h >=0 and h <= 12:
        speak("Good Morning")
    elif h >=12 and h <= 16 :
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am here to help u how i can help u ")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print("Searching wikipedia...")

            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            webbrowser.open("https://www.jiosaavn.com")
        elif 'time' in query:
            ti = (datetime.datetime.now().strftime("%H:%M:%S"))
            #print(f" current time is {ti}")
            speak(ti)
        elif 'open desktop' in query:
            os.startfile('C:\\Users\\Asus\\Desktop')




