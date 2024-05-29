import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS

GOOGLE_API_KEY="AIzaSyA1mZ_nqKNIp_3oCpckldDZaqQ0WGHqotk"
os.environ['GOOGLE_API_KEY']=GOOGLE_API_KEY

def voice_input():
    r=sr.Recognizer()

    with sr.Microphone() as SOURCE:
        print("Listining")
        audio=r.listen(SOURCE)
    
    try:
        text=r.recognize_google(audio)
        print("you said",text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand Audio")
    except sr.RequestError as e:
        print("could not request result from Google speech recognozation service {0}".format(e))


def text_to_speech(text):
    tts=gTTS(text=text,lang='en')
    tts.save(savefile="speech.mp3")


def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(user_text)
    result=response.text
    return result




