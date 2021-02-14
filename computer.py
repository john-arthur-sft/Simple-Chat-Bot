# computer project

"""
project details

This is an automatic chatbot named BAYMAX which can be very useful in in many things

"""

# importing module

from tkinter import messagebox

from tkinter import *

from random import randint

import pyttsx3

from pygame import mixer

import time

from PIL import ImageTk, Image

import webbrowser

import os

import random

import datetime



# setting up pygame mixer

mixer.init()

# setting up pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice',1)

# creating an speech function

def cmd(text):
    
    pyttsx3.speak(text)


# setting up submit button sound

path  = "Support\\Login.wav"

def s(path):
    
    a = mixer.Sound(path)
    
    a.set_volume(1.0)
    
    a.play()


# creating a logical Login windows


root = Tk()

root.resizable(0,0)

root.geometry("520x520")

root.title('class 12 project')

canvas1 = Canvas(root,bg = 'yellow',width = 1000,height = 100).place(x = 0,y = 0)

header = Label(canvas1,text = "class 12 Baymax computer project",font = ('georgia',20,'bold'),fg = 'red',bg = 'yellow')

header.place(x = 25,y = 25)

# user name properties

name = Label(root,text= 'Name : ',fg = 'orange',font = ('georgia',15,'bold'))

name.place(x = 10,y = 150)

Name = Entry(root,font = ('georgia',15,'italic'),bg ='violet',fg = 'black')

Name.place(x = 170,y = 150)

# password properties

pswd = Label(root,text = 'Password : ',fg = 'orange',font = ('georgia',15,'bold'))

pswd.place(x = 10,y = 250)

Pswd = Entry(root,font = ('georgia',15,'bold'),show = '*',bg = 'violet',fg = 'black')

Pswd.place(x = 170,y = 250)

# submit button function

def sub():
    
    s("Support\\Login.wav")
    
    NAme = ["john",
            "John",]
    
    if Name.get() in NAme and Pswd.get() == "admin":
        
        root.destroy()    

    else :

        messagebox.showwarning("Check registration","You are not a verified user")
        

submit = Button(root,text = 'SUBMIT',bg = 'orange',font = ('georgia',15,'bold'),command = sub).place(x = 170,y = 350)

root.mainloop()


screen = Tk()

screen.geometry('650x650')

screen.title('BAYMAX - John project - CHATBOT')

screen.resizable(0,0)

time.sleep(1.5)

cmd("Welcome to this Program. it is a special chat bot programe")

mixer.music.load("Support\\bg.mp3")

mixer.music.play(50)

canvas1 = Canvas(screen,bg = 'red',width = 1000,height = 100).place(x = -5,y = -5)

mixer.music.set_volume(0.3)

cmd("I am Baymax. created by john arthur")

cmd("I am A bot can handle anything")

cmd("Just ask what you want")

q_pic  = Image.open('Support\\question.jpg')

resized = q_pic.resize((300,250),Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

pic_label = Label(screen,image = new_pic)

pic_label.place(x = 350,y = 100)


Header = Label(canvas1,text = "Class 12 project by John ~ Chat bot",font = ("gabriola",20,"bold"),
               fg = 'black',bg = 'red')

Header.place(x = 100,y = 30)


def sub():
    mixer.music.set_volume(0.2)    
    
    query = str(entry1.get())
    
    if 'hello' in query:
                
        cmd("Hey there, welcome here")
                
        cmd("Nice to meet you")
        
        pass
    
    elif 'do' in query:
        
        cmd("I can display weather report,or search anything in web, if you have a active data connection")
                
        cmd("I can shutdown the computer or reboot the computer")        
        
        cmd("What other feature do you want...?")
        
        pass
    
    elif 'system' in query:
        
        cmd("Welcome into the Operating system protocol")
                
        res = int(input("Command number : "))

        if res == 1:
            
            os.system('Shutdown /s /t 10 /c "Activated shutdown protocol by admin" ')            
            
            cmd("Shutdown protocol is activated")
            
        elif res == 2:
            
            os.system('Shutdown /r /t 10 /c "Activated reboot protocol by admin"')
            
            cmd("Reboot protocol is activated")
            
        elif res == 3:
            
            os.system("Shutdown /a")
            
            
            cmd("Aborted the protocol")

    elif 'weather' in query:

        
        cmd("Loading weather report")   
        
        cmd("Connect to a acive ethernet cable or data connection")   
        
        webbrowser.open('https://www.accuweather.com/en/in/india-weather')
        
    elif  'about' in query:
        
        cmd("It is a simple text based system")
               
        cmd("Created by john arthur and yelil for class 12 computer project")       
        
        cmd("It can be worked with online and affline also")
                
        cmd("This is a login user controlled programme")

    elif 'bye' in query:

        msg = messagebox.askquestion("Review","Do you like this program ? ")

        if msg == 'yes':
            
            
            cmd("Thanks for using the program. looking ahead for you to use this programme")
            
        
        elif msg =='no':

            cmd("Report why are you not satisfied with me ? 'to admin'")
            
            exit()

    elif 'facts' in query:
        
        list = ["The first computer programmer was a female, named Ada Lovelace.",
                "The first game was created in 1961. Fun facts are that it didn’t earn any money.",
                "The first computer “bug” was identified in1947 as a dead moth.",
                "Computer programming is one of the fastest growing occupations currently.",
                "The language name C because it succeeds another language called B.",
                "APIs are like stars, once a class is there everybody will assume it will always be there.",
                "Perl is sometimes known as the “Swiss-Army knife” of programming languages.",]
        
        seq = random.choice(list)
        
        cmd(seq)

    elif 'take a note' in query:

        cmd("Yes ! i am taking the note, please enter the message in the IDLe env here.")

        # opening a file for writing and appending a data

        data = input("Message Please : ")

        file = open("Support\\note.txt","a")
        file.write("\n\n\t----------Note started----------\n\n")
        file.write(data)
        file.write("\n\n\t----------End_of_the_note----------\n\n")
        cmd("Note taken")
        

    elif 'time' in query:
        
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        cmd(f"the time is {strTime}")
        
        print ("Time asked at :",f'{strTime}')

        

    else :

        cmd("Connecting")
        
        webbrowser.open(query)

        cmd("Opened")
        
# creating a main entry panel

entry1 = Entry(screen,bg = '#9400D3',fg = "#ADFF2F",width = 25,font = ("mv boli",25,'italic'))

entry1.place(x = 25,y = 400)


sub = Button(screen,text = "Proceed",font = ("Courier new",15,"bold"),fg = "#00FFFF",
             bg = "#F5DEB3",command = sub).place(x = 300,y = 500)
