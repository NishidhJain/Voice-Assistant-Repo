import kivy
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import smtplib
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        query=r.recognize_google(audio)
        print(f"User said: {query}\n")
        speak("you said ")
        speak(query)

    except Exception as e:
        print("Please try it again..")
        speak("I cannot recognize . Please say it again..")
        return "None"
    return query

def googlecmd():
    print("What do you want to search?")
    speak("What do you want to search")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        question=r.recognize_google(audio)
        print(f"User said: {question}\n")
        speak("you said ")
        speak(question)

    except Exception as e:
        print("Please try it again..")
        speak("I cannot recognize . Please say it again..")
        return "None"
    return question



def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('nmj9609@gmail.com','lovelyjain16')
    server.sendmail('nmj9609@gmail.com',to,content)
    server.close()
    speak("Mail sent successfully")


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good morning!")

    elif hour>=12 and hour<18 :
        speak("Good afternoon!")

    else :
        speak("Good Evening!")

    speak("I am your personal assistant. How may i help you!")


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.rows=4 

        self.inside = GridLayout()
        self.inside.cols=3

        self.add_widget(Label(text="    VOICE\nASSISTANT",font_size=70))
        self.add_widget(Label(text=""))

        self.voicesearch = Button(text=" Voice\nSearch",font_size=40)
        self.voicesearch.bind(on_press=self.pressed)
        self.inside.add_widget(Label(text=""))
        self.inside.add_widget(self.voicesearch)
        self.inside.add_widget(Label(text=""))
        self.add_widget(self.inside)

        self.add_widget(Label(text=""))
    

    def pressed(self,instance):
        speak("I am your personal assistant. How may i help you!")
        query=takeCommand().lower()

        if "wikipedia" in query:
            print("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            query=googlecmd()
            driver = webdriver.Chrome("C:/Program Files (x86)/Google/chromedriver.exe")
            driver.get("http://www.google.co.in")
            driver.maximize_window()
            self.element = driver.find_element_by_name("q")
            self.element.clear()
            self.element.send_keys(query)
            time.sleep(1)
            self.element.send_keys(Keys.RETURN)
            time.sleep(1)
            #self.element = driver.find_element_by_class_name('LC20lb').click()

            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications" : 2}
            options.add_experimental_option("prefs",prefs)
            google().start_google(driver)
            google().search_google(driver,query)

        elif "play music" in query:
            music_dir="C:\\Users\\jainn\\Downloads"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "send email" in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="nishidhjain909@gmail.com"
                sendEmail(to,content)

            except Exception as e:
                print(e)
                speak("Email not sent")


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    MyApp().run()  