import datetime
import os
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speech_recognition
import wikipedia
import webbrowser
import random
import smtplib
import urllib.request
import re
'''import urllib.request
import re

search_keyword="mozart"
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_ids[0])'''
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
#print(voices[0])
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<=12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening')

    speak("I am jarvis sir. Please tell me how am i help you?")

def takeCommand():
    '''it takes microphone input form user and return string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        # print(e)
        print('Say this again please......')
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("baghelakash1002@gmail.com",'8357918670')
    server.sendmail('baghelakash1002@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishMe()
    #sendEmail('baghelakash1002@gmail.com','akfsdsnhcscnhslfhsfshd')
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            webbrowser.open("youtube.com")
            #q = query.replace("youtube")
            #print(q)
            # search_keyword = query.replace('YouTube','')
            # html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            # video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            # print("https://www.youtube.com/watch?v=" + video_ids[0])




        elif "open google" in query:
            webbrowser.open('google.com')

        elif "play music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,50)]))


        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is{strTime} ")


        elif "open code" in query:
            codePath = "E:\\pycharm\\javrisaivoiceassistent"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "abaghel008@gmail.com"
                sendEmail(to,content)
                speak('Email has been send')
            except Exception as e:
                print(e)
                speak("Sorry bhai,i can not send email!")
        elif "quit" in query:
            exit()





