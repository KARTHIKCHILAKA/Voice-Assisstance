#installed and imported packages
import requests
import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki
import os
import datetime
from bs4 import BeautifulSoup
import cv2
import pandas as pd
from tkinter import *
import random
import pyperclip
import calendar
from tkinter import *
import phonenumbers
from phonenumbers import geocoder
import copy
import random
import pygame
from subprocess import call




#listens from user....
listener = sr.Recognizer()
#speaks to user....
speaker = pyttsx3.init()


""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
speaker.setProperty('rate', 150)     # setting up new voice rate


"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


#speaks to user....
def speak(text):
    speaker.say('yes boss, ' + text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()

sec=15
va_name = 'laila'

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak_ex('good morning boss')
    elif hour>12 and hour<18:
        speak_ex('good afternoon boss')
    else:
        speak_ex('good evening boss')
    speak_ex('i am laila , how can i help you')

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + '','')
    except:
        print("check your microphone....")
    return command

clicked = False
r = g = b = xpos = ypos = 0
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)
text='color'

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)



# To create a root window of GUI in python
tk=Tk()
tk.geometry('300x300')
tk.configure(background='yellow')

# To store/retrieve the string value entered by user
pswd=StringVar()

# To store/retrieve the Integer value entered by user
passlen=IntVar()
passlen.set('Enter Length')


# Function to generate a random password
def password_generator():
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()'
    password=''
    if passlen.get()>=8:
        for i in range(passlen.get()):
            password+=random.choice(characters)
        pswd.set(password)


# Function to copy generated password to clipboard
def copyclipboard():
    random_password = pswd.get()
    pyperclip.copy(random_password)
    Label(tk,text="Copied to Clipboard",bg="red").pack(pady=6)


def showCalender():
    gui = Tk()
    gui.config(background='white')
    gui.title("Calender")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
    calYear.grid(row=4, column=1, padx=20)
    gui.mainloop()



# class CallBlackJack(object):
#
#     def __int__(self, path='Batch-15/main2.py'):
#         self.path = path
#
#     def call_python_file(self):
#         call(["Python3", "{}".format(self.path)])





while True:
    # wish()
    user_command = take_command()
    if 'hello' in user_command or 'hi' in user_command:
        wish()

    elif 'generate a password' in user_command or 'create a password' in user_command:
        speak_ex('yes boss , enter lenght of the password in the box displayed')
        Label(tk, text="Enter the number to get password \n (Minimum length should be 8)", bg='Blue', fg='white').pack(pady=3)
        # To store the entry of user
        Entry(tk, textvariable=passlen).pack(pady=3)
        # To generate Random password and confirmation by the button click
        Button(tk, text="Generate Password", command=password_generator, bg='black', fg='white').pack(pady=7)
        Entry(tk, textvariable=pswd).pack(pady=3)
        Button(tk, text="Copy to clipboard", command=copyclipboard, bg='black', fg='white').pack()
        # To initiate and display the root window we created
        tk.mainloop()

    elif 'detect my surroundings' in user_command or 'investigate my surroundings' in user_command:
        speak_ex('yes boss , detecting your surroundings')
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_function)
        cap = cv2.VideoCapture(0)
        while (1):
            ret, img = cap.read()
            if (clicked):
                cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
                text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
                clicked = False
            cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("image", img)
            if cv2.waitKey(20) & 0xFF == 27:
                break
        cv2.destroyAllWindows()

    elif 'find details of the indian phone number' in user_command:
        #speak_ex('yes boss . tell the phone number')
        print('listening....')
        # number = take_command()
        speak_ex(' boss enter the phone number ')
        number = input('enter the phone number : ')
        print(number)
        pepnummber = phonenumbers.parse(number)
        location = geocoder.description_for_number(pepnummber, "en")
        speak_ex(f" yes boss given phone number is from {location}")
        from phonenumbers import carrier
        service_pro = phonenumbers.parse(number)
        service = carrier.name_for_number(service_pro, "en")
        #speak_ex(' and it is an ',service,' number')
        speak_ex(f" and it is  {service} number")

    elif 'show calendar' in user_command:
        speak_ex('enter specified year and check the calender boss')
        new = Tk()
        new.config(background='saddle brown')
        new.title("Calender")
        new.geometry("500x500")
        cal = Label(new, text="Calender", bg="saddle brown",fg="bisque", font=("times", 28, "bold"))
        cal.grid(row=1, column=1)
        year = Label(new, text="Enter Year", bg="saddle brown",fg="bisque", font=("times", 20))
        year.grid(row=2, column=1)
        year_field = Entry(new, bg="bisque", )
        year_field.grid(row=3, column=1)
        button = Button(new, text="Show Calender", fg="saddle brown",bg="bisque", command=showCalender)
        button.grid(row=4, column=1)
        new.mainloop()

    elif 'open notepad' in user_command:
        npath = 'C:\\Windows\\SysWOW64\\notepad.exe'
        speak_ex('notepad opened sir')
        os.startfile(npath)

    elif 'close' in user_command or 'quit' in user_command:
        #print(' I will be there when ever you call me.')
        speak(' I will be there when ever you call me.')
        break

    elif 'what is your date of birth' in user_command:
        speak_ex('i was born on october 23 , 2022')

    elif 'how can you help me' in user_command:
        speak_ex('im an artificial intellegence machine designed by Mister KARTHIK . i can help you in getting information about your surroundings')

    elif 'cool' in user_command:
        speak_ex('yes boss its really cool.')

    elif 'what are your features' in user_command or 'what are your internal features' in user_command or 'what are your external features' in user_command:
        if 'internal features' not in user_command:
            speak_ex('Mister KARTHIK designed me using python programming language , Like humans internally i have hands legs and all , i can think very fast when compared to humans.')
        else:
            speak_ex('sorry user! its personal')

    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime("%I:%M %p")
        #print(cur_time)
        speak(cur_time)

    elif 'play' in user_command:
        user_command = user_command.replace('play ','')
        user_command = user_command.replace('laila ','')
        #print('playing ' + user_command)
        speak('playing ' + user_command + ' enjoy boss')
        pk.playonyt(user_command)

    elif 'search for' in user_command or 'google' in user_command:
        user_command = user_command.replace('search for ','')
        user_command = user_command.replace('google ', '')
        #print('searching for ' + user_command)
        speak('searching for ' + user_command)
        pk.search(user_command)

    elif 'who is ' in user_command:
        user_command = user_command.replace('who is ','')
        info = wiki.summary(user_command, 2)
        print(info)
        speak(info)

    elif 'open mobile camera' in user_command:
        import urllib.request
        import cv2
        import numpy as np
        import time
        import imutils
        url = "http://192.168.110.5:8080/shot.jpg"
        while True:
            # img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
            # img = cv2.imdecode(img_arr,-1)
            # cv2.imshow('IPWebcam',img)
            # # q = cv2.waitKey(1000)
            # # if q == ord("q"):
            # #     break
            #
            # if 0xFF == 27:
            #     break
            img_resp = requests.get("http://192.168.110.5:8080/shot.jpg")
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            #img = imutils.resize(img, width=1000, height=1800)
            cv2.imshow("Android_cam", img)
            # Press Esc key to exit
            # if cv2.waitKey(1) == 27:
            #     break
            if cv2.waitKey(1) & 0XFF == ord('q'):
                break

            cv2.destroyAllWindows()

    elif 'alarm' in user_command:
        speak_ex('boss plz tell me the time to set alarm in the form of normal time , for example set alarm to 5:30 PM or AM')
        tt = take_command()
        tt = tt.replace('set alarm to ','')
        tt = tt.replace('.','')
        tt = tt.upper()
        import MyAlarm
        MyAlarm.alarm(tt)

    elif 'who are you' in user_command or 'your name' in user_command:
        speak_ex('im '+va_name +' please to meet you')

    elif 'shutdown' in user_command:
        os.system(f'shutdown /s /t {sec}')
        pyttsx3.speak(f'ok boss im shutting down in next {sec} seconds')

    elif 'temperature' in user_command or 'climatic conditions' in user_command:
        #search = 'temperature in vijayawada'
        speak_ex("in which place you want me to search for climatic conditions boss?")
        print("say the place....")
        search=''
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            search = listener.recognize_google(voice)
            search = search.lower()
        url = f'https://www.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f'current {search} is{temp}')

    elif 'thank you' in user_command:
        speak_ex("never mind boss its my pleasure")

    elif 'activate how to do ' in user_command:
        speak_ex("How to do mode activated")
        while True:
            speak_ex("please tell me what you want to know")
            from pywikihow import search_wikihow
            how = take_command()
            try:
                if 'exit' in how or 'close' in how or 'deactivate' in how:
                    speak_ex('okay boss , how to do mode is deactivated')
                    break
                else:
                    max_results = 1
                    how_to = search_wikihow(how,max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak_ex(how_to[0].summary)
            except Exception as e:
                speak_ex("sorry boss , i am unable to find this")

    elif 'boring' in user_command:
        class CallBlackJack(object):

            def __init__(self, path = 'D:\PROJECTS_BATCH_15\Batch-15\main3.py'):
                self.path = path

            def call_python_file(self):
                call(['Python3', '{}'.format(self.path)])

        if __name__ == "__main__":
            c = CallBlackJack()
            c.call_python_file()


    else:
        speak_ex('please say it again boss')