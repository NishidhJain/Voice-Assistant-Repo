import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
#import os
#import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def sendEmail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('youremail@gmail.com','password')
	server.sendmail('youremail@gmail.com',to,content)
	server.close()

def wishMe():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good morning!");

	elif hour>=12 and hour<18:
		speak("Good afternoon!")

	else:
		speak("Good Evening!")

	speak("I am autobot. How may i help you!")


def takeCommand():
 	#string output

 	r=sr.Recognizer()
 	with sr.Microphone() as source:
 		#print("Listening...")
 		r.adjust_for_ambient_noise(source)
 		print("Listening...")
 		r.pause_threshold=1
 		audio=r.listen(source)

 	try:
 		print("Recognizing...")
 		query=r.recognize_google(audio)
 		print(f"User said: {query}\n")

 	except Exception as e:
 		#print(e)
 		print(" Please say it again...")
 		return "None"
 	return query

if __name__ == '__main__':
	#speak("Hi Nishidh")
	wishMe()
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
		webbrowser.open("google.com")

	elif "play music" in query:
		music_dir="C:\\songs"
		songs=os.listdir(music_dir)
		print(songs)
		os.startfile(os.path.join(music_dir,songs[1]))

	elif "the time" in query:
		strTime=datetime.datetime.now().strftime("%H:%M:%S")
		speak(f"The time is {strTime}")

	elif "open Microsoft Word" in query:
		codePath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office"
		os.startfile(codePath)

	elif "send email" in query:
		try:
			speak("What should i say?")
			content=takeCommand()
			to=nishidhjain909@gmail.com
			sendEmail(to,content)
			speak("Email has been send.")

		except Exception as e:
			print(e)
			speak("Email not sent")