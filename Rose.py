import speech_recognition as sr
import pyttsx3
import wikipedia
from datetime import datetime as date
import requests,json
import subprocess
import random
import cv2
import os
Birthday=date(2020,6,29)
today=date(date.now().year,date.now().month,date.now().day)
#loop for the assistant's constant reply.
def process():
    print("Anything Else ?")
    speak("anything else ?")
    try:
        user_input=userInput().lower()
    except:
        try:
            print('I am not able to hear anything. Let\'s try again!!')
            speak('I am not able to hear anything. Let\'s try again!!')
            user_input=userInput().lower()
        except:
            print("Sorry ! I am not able to hear anything. I have to shut down. Have a nice day!")
            speak("Sorry ! I am not able to hear anything. I have to shut down. Have a nice day!")
            return 0
            
    if user_input=='no':
        speak("Okay! Have a nice day")
        return 0
    else:
        if user_input=="who are you" or user_input=="what is your name" or user_input=="tell me about yourself"or user_input=="introduce yourself":
            introduction()
        elif "weather" in user_input:
            weather()
        elif 'open' in user_input:
            open_program(user_input)
        elif 'flip' in user_input and 'coin' in user_input:
            coin_flip()
        elif 'roll' in user_input and 'dice' in user_input:
            roll_dice()
        elif 'date' in user_input:
            print('Date is '+ str(date.now().day)+'/'+str(date.now().month)+'/'+str(date.now().year))
            speak('Date is '+ str(date.now().day)+' '+str(date.now().month)+' '+str(date.now().year))
        elif 'time' in user_input and 'tell' in user_input:
            print('Current time is '+ str(date.now().hour)+":"+str(date.now().minute)+":" +str(date.now().second))
            speak('Current time is '+ str(date.now().hour)+" hours "+str(date.now().minute)+" minutes " +str(date.now().second)+" seconds")
        elif user_input=="go to sleep rose" or user_input=="shut down rose" or user_input=="shut down yourself":
            print("Okay! Have a nice day Sir...")
            speak("Okay! Have a nice day Sir...")
            exit()
        elif user_input=="shut down system":
            print("Shutting down system in")
            speak("Shutting down system in")
            print("Three")
            speak("Three")
            print("Two")
            speak("Two")
            print("One")
            speak("One")
            os.system("shutdown /s /t 1")
        elif user_input=="restart system":
            print("Restart system in")
            speak("Restarting system in")
            print("Three")
            speak("Three")
            print("Two")
            speak("Two")
            print("One.")
            speak("One.")
            os.system("shutdown /r /t 1")
        else:
            wiki(user_input)
    return process()
            
#this opens an inbuilt program
def open_program(string):
    try:
        software=string.replace('open ','')
        print("Opening "+software)
        speak("Opening "+software)
        if "camera" in software:
            open_camera()
        elif "paint" in software:
            subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
        elif "notepad" in software:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        elif "wordpad" in software:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
        elif "calculator" in software:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        elif "chrome" in software:
            subprocess.call('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
        elif "control panel" in software:
            subprocess.Popen('C:/Windows/System32/control.exe')
        elif "command" in software:
            subprocess.Popen('C:/Windows/System32/cmd.exe')
        elif "snipping" in software:
            subprocess.Popen('C:/Windows/System32/SnippingTool.exe')
        elif "internet explorer" in software:
            subprocess.Popen('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
        elif "reader" in software:
            subprocess.Popen('C:/Program Files (x86)/Adobe/Reader 11.0/Reader/AcroRd32.exe')
        elif "compiler" in software:
            if "python" not in software:
                subprocess.Popen('C:/Program Files (x86)/Dev-Cpp/devcpp.exe')
            else:
                subprocess.Popen('C:/Users/Lenovo/AppData/Local/Programs/Python/Python38/python.exe')
        elif "media player" in software:
            if 'windows' in software:
                subprocess.Popen('C:/Program Files (x86)/Windows Media Player/wmplayer.exe')
            else:
                subprocess.Popen('C:/Program Files (x86)/VideoLAN/VLC/vlc.exe')
        elif 'teamviewer' in software:
            subprocess.Popen('C:/Program Files (x86)/TeamViewer/TeamViewer.exe')
        elif 'microsoft' in software:
            if 'excel' in software:
                subprocess.Popen('C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe')
            elif 'outlook' in software:
                subprocess.Popen('C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.exe')
            elif 'powerpoint' in software:
                subprocess.Popen('C:/Program Files/Microsoft Office/root/Office16/POWERPNT.exe')
            elif 'word' in software:
                subprocess.Popen('C:/Program Files/Microsoft Office/root/Office16/WINWORD.exe')
            #This is incomplete and you have to add all the programs you can add.
    except:
        print("Sorry! I am unable to open it.")
        speak("Sorry! I am unable to open it.")
            
#this tells the weather
def weather():
    api_key = "b50a65b07845594a8e96375a2bd4f28a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name='jaipur'
    complete_url=base_url+'appid='+api_key+'&q='+city_name
    response=requests.get(complete_url)
    x=response.json()
    if x['cod']!='404':
        y=x['main']
        z=x['weather']
        print(" Temperature (in kelvin unit) = " +
					str(y['temp']-273.15) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(y['pressure']) +
		"\n humidity (in percentage) = " +
					str(y['humidity']) +
		"\n description = " +
					str(z[0]['description']))
        speak("Current temperature is "+str(y['temp']-273.15) +
              "degree celsius with pressure "+str(y['pressure'])+
              " hectopascal and humidity is "+str(y['humidity'])+"percent")
        speak("Overall today's weather can be predicted as "+str(z[0]['description']))
    else:
        print("Sorry! I'm unable to connect at this moment")
        speak("Sorry! I'm unable to connect at this moment")
        
#this is the introduction of rose
def introduction():
    age=today-Birthday
    print("My name is rose. I am "+str(age.days)+
          " days old. I am a personal assistant developed using python programming language and I am still learning a lot of things. I would like to say more about myself but that's it for now. Thank you for asking")
    speak("My name is rose. I am "+str(age.days)+" days old. I am a personal assistant developed using python programming language and I am still learning a lot of things. I would like to say more about myself but that's it for now. Thank you for asking")
#this is the voice of my assistant.
def speak(string):
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')
    engine.setProperty('rate',200)
    engine.setProperty('voice',voices[1].id)
    engine.say(string)
    engine.runAndWait()
#this for user Input
def userInput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now...")
        audio=r.listen(source)
        query=r.recognize_google(audio)
    return query
#If anything was supposed to ask from wiki
def wiki(query):
    try:
        results=wikipedia.summary(query,sentences=3)
        print(results)
        speak("wikipedia said:")
        speak(results)
    except:
        speak("I cannot find this on wikipedia. Sorry!")
        print("I cannot find this on wikipedia. Sorry!")
#Flipping a coin
def coin_flip():
    coin=random.choice(['Heads','Tails'])
    print('It\'s '+coin)
    speak('It\'s '+coin)
    speak("Want to flip again ?")
    user_input=userInput().lower()
    if user_input=='no':
        speak("Okay !")
        return 0
    else:
        return coin_flip()
#Rolling a dice
def roll_dice():
    dice=random.choice(['One','Two','Three','Four','Five','Six'])
    print('It\'s '+dice)
    speak('It\'s '+dice)
    speak("Want to roll again ?")
    user_input=userInput().lower()
    if user_input=='no':
        speak("Okay !")
        return 0
    else:
        return roll_dice()
#opening the camera
def open_camera():
    speak('To close the camera window Please press Escape key from keyboard.')
    print('To close the camera window Please press Escape key from keyboard.')
    cv2.namedWindow('Camera Opened by Rose')
    vc=cv2.VideoCapture(0)
    if vc.isOpened():
        rval,frame=vc.read()
    else:
        rval=False
    while rval:
        cv2.imshow('Camera Opened by Rose',frame)
        rval,frame=vc.read()
        key=cv2.waitKey(20)
        if key==27:
            break
    cv2.destroyWindow('Camera Opened by Rose')
#Starting of the program.
hour=date.now().hour
if hour<12:
    print("good morning sir")
    speak("good morning sir")
elif hour==12 and date.now().minute==00:
    print("good noon sir")
    speak("good noon sir")
elif hour>=12 and hour<16:
    print("good afternoon sir")
    speak("good afternoon sir")
else:
    print("good evening sir")
    speak("good evening sir")
print("So! what can I do for you today ?")
speak("So! what can I do for you today ?")
try:
    user_input=userInput().lower()
except:
    user_input=''
print("You Said: "+user_input)
if user_input=="who are you" or user_input=="what is your name" or user_input=="tell me about yourself"or user_input=="introduce yourself":
    introduction()
elif "weather" in user_input:
    weather()
elif 'open' in user_input:
    open_program(user_input)
elif 'flip' in user_input and 'coin' in user_input:
    coin_flip()
elif 'roll' in user_input and 'dice' in user_input:
    roll_dice()
elif user_input=='':
    print('Sorry! I am unable to hear anything.')
    speak('Sorry! I am unable to hear anything.')
elif 'date' in user_input:
    print('Date is '+ str(date.now().day)+'/'+str(date.now().month)+'/'+str(date.now().year))
    speak('Date is '+ str(date.now().day)+' '+str(date.now().month)+' '+str(date.now().year))
elif 'time' in user_input and 'tell' in user_input:
    print('Current time is '+ str(date.now().hour)+":"+str(date.now().minute)+":" +str(date.now().second))
    speak('Current time is '+ str(date.now().hour)+" hours "+str(date.now().minute)+" minutes " +str(date.now().second)+" seconds")
elif user_input=="go to sleep rose" or user_input=="shut down rose" or user_input=="shut down yourself":
    print("Okay! Have a nice day Sir...")
    speak("Okay! Have a nice day Sir...")
    exit()
elif user_input=="shut down system":
    print("Shutting down system in")
    speak("Shutting down system in")
    print("Three")
    speak("Three")
    print("Two")
    speak("Two")
    print("One")
    speak("One")
    os.system("shutdown /s /t 1")
elif user_input=="restart system":
    print("Restart system in")
    speak("Restarting system in")
    print("Three")
    speak("Three")
    print("Two")
    speak("Two")
    print("One.")
    speak("One.")
    os.system("shutdown /r /t 1")
else:
    wiki(user_input)
process()
