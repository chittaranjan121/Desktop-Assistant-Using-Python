import os
import speech_recognition as sr
import wikipedia
import pyttsx3
import datetime
import webbrowser
import streamlit as st

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing User Voice")
            query=r.recognize_google(audio,language="en")
            print(f"user said is {query}\n")
        except Exception as e:
            print("Please try again")
            print("None")
        return query