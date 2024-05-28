import os
import speech_recognition as sr
import wikipedia
import pyttsx3
import datetime
import webbrowser
import streamlit as st
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning  sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon  sir. How are you doing")

    else:
        speak("Good evening  sir. How are you doing")
    
    speak("I am Adish. Tell me sir how can i help you")


def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        query=""
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

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chittask03@gmail.com','chittask')
    server.sendmail('chittask03@gmail.com',to,content)
    server.close()    

if __name__== "__main__":
        wish_me()
        while True:
            query=takeCommand().lower()
            print(query)
    

            if "wikipedia" in query:
                speak("Searching in Wikipedia")
                results=wikipedia.summary(query,sentences=3)
                speak("According to wikipedia")
                print(results)
                speak(results)
            
            elif "youtube"     in query:
                speak("opening youtube")
                webbrowser.open("www.youtube.com")

            elif 'read something' in query:
                speak("ok sir. please type here what do you want to read")
                webbrowser.open("google.com")

            elif 'music' in query:
                speak("ok sir. please take your seat belt . It's gonna be rock")
                music_dir = 'D:\\song\\Amir\\'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[6]))
            
            elif 'facebook' in query:
                speak("Checking out sir ... take a look")
                webbrowser.open("facebook.com")
            
            elif 'music' in query:
                speak("ok sir. please take your seat belt . It's gonna be rock")
                music_dir = 'D:\\song\\Amir\\'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[6]))
            elif 'intense' in query:
                speak("sorry sir. you are going to like that one")
                music_dir = 'D:\\song\\Amir\\'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[7]))

            elif 'time' in query:
                speak("This is 6 o'clock sir you have been sleeping for 6 hours")

            #This query for say the times
            elif 'time_date' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir the time is {strTime}")
            #This query for open the VS code
            elif 'code' in query:
                codePath = "C:\\Users\\ACT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("Sure sir . give me some while. Opening visual code studio")
                os.startfile(codePath)
            #This query for sent Email
            
            elif 'email' in query:
                try:
                    speak("ok sir. what should i say")
                    content = takeCommand()
                    to = "chittask03@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry sir there is a problem , i haven't been able to send the email")

                
            
            elif "goodbye" in query:
                speak("Good bye..Logging out")
                exit()


