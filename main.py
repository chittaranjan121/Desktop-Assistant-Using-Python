import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

##taking volume from screen
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)


####speak function

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing my voice")  
            query=r.recognize_google(audio,language='en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            print("Say that again pls")
            return "None"
        return query
    
print("Before Welcome")
if __name__== "__main__":

    query=takeCommand().lower()
    print(query)

if "wikipedia" in query:
    speak("Searching wikipedia")
    query=query.replace('wikipedia',"")
    results=wikipedia.summary(query,sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)
elif "youtube" in query:
    speak("opening youtube")  
    webbrowser.open("youtube.com")
elif "cricinfo" in query:
    speak("opening cricinfo")  
    webbrowser.open("cricinfo.com")





#speak("Hello my name is Adish")   
#text=takeCommand()
#speak(text)


