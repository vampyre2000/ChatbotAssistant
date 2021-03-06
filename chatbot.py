#################################
# Chatbot Assistant 0.0.1
# 2016 General Public License V3
# By Brendan Clarke
#################################

import random
import os
import time
import csv
import json
import subprocess
import requests
from datetime import datetime

#set file location paths
ROOT="./Chatbot"
DATA=ROOT+"/Data"
IMAGES=ROOT+"/Images"
SOUND=ROOT+"/Sound"
DATAFILE="data.txt"
BOT1={}
#Test code to be removed.
def PrintDirectorySTructure():
    print(ROOT)
    print(DATA)
    print(IMAGES)
    print(SOUND)
    
#The main chatbot class. 
class Chatbot():
    def __init__(self):
        #Set this to True to enable speech.
        self.BOT={}
        self.USER={}
        self.SPEECHENABLED=False
        self.CreateBotPersonality(1)
        self.USER={'FIRSTNAME':'Jack','LASTNAME':'Daniels','SEX':'male','AGE':'21','CITY':'Sydney','FAVOURITE_COLOUR':'Blue'}
        self.ALARMS={'WAKEUP':'','BEDTIME':'','GOTOWORK':''}
        #Bot will give a self description of themselves.
        #def description(self):
    
    def CreateBotPersonality(self,num):
        BOT1={'FIRSTNAME':'Alice','LASTNAME':'Boyle','NICKNAME':'Ali','SEX':'female','AGE':'21','DOB':' ','HEIGHT':'160','WEIGHT':'49','EYE_COLOUR':'blue','HAIR_COLOUR':'Brown',
                        'HAIR_LENGTH':'Long',' HAIR_STYLE':'Bun','FRECKLES':'YES','CITY':'Sydney','COUNTRY':'Australia','ADDRESS':' ','FAVOURITE_COLOUR':'blue','FAVOURITE_FOOD':'Spong cake',
                        'FAVOURITE_ANIMAL':'rabbit','PETS':'no','LIKES':'computers','DISLIKES':'snakes'}
        BOT2={'FIRSTNAME':'Jane','LASTNAME':'Andrews','NICKNAME':'','SEX':'female','AGE':'23','DOB':' ','HEIGHT':'160','WEIGHT':'50','EYE_COLOUR':'green','HAIR_COLOUR':'Black',
                        'HAIR_LENGTH':'Long',' HAIR_STYLE':'ponytail','FRECKLES':'NO','CITY':'Sydney','COUNTRY':'Australia','ADDRESS':' ','FAVOURITE_COLOUR':'red','FAVOURITE_FOOD':'Spong cake',
                        'FAVOURITE_ANIMAL':'cat','PETS':'no','LIKES':'computers','DISLIKES':'mice'}
        if num==1:
            BOT=BOT1
        elif num==2:
            self.BOT=BOT2
        else:
            print("No valid bot personaily chosen. Using Default personality")
            self.BOT=BOT1
    
    
    def BotDescription(self):
        print("My name is " + self.BOT['FIRSTNAME'] + " but my friends call me " + self.BOT['NICKNAME'] + ". I have " + self.BOT['HAIR_LENGTH'] + " " + self.BOT['HAIR_COLOUR']
            + " hair and " + self.BOT['EYE_COLOUR'] + " eyes.")
    def SpeechEnable(self):
        self.SPEECHENABLED=True
    
    def SpeechDisable(self):
        self.SPEECHENABLED=False
        
    def BotProfile(self):
        for name in self.BOT:
            print ("> " + name + ": " + self.BOT[name])

    def Settings(self):
        if self.SPEECHENABLED==True:
            print("Speech is Enabled")
        else:
            print("Speech is Disabled")
        if len(self.ALARMS)==0:
            print("There are no alarms set")
        else:
            print(self.ALARMS)

    def greeting(self):
        self.num=random.randint(1, 3)
        if self.num==1:
            self.SPEAK(">>Hi, my name is " +self.BOT['FIRSTNAME']+"." +" How are you today?")
        if self.num==2:
            self.SPEAK(">>Hello, my name is " +self.BOT['FIRSTNAME']+"." +" How are you today?")
        if self.num==3:
            self.SPEAK(">>G'day mate, my name is " +self.BOT['FIRSTNAME']+"." +" How are you today?")
        self.FEELING=input("::")
        self.FEELING=self.FEELING.lower()
        if self.FEELING=="good":
            self.SPEAK(">> Thats great!!!!")
        if self.FEELING=="bad":
            self.SPEAK(">> I'm sorry to hear that...")

    def getname(self):
        self.USER['NAME']=input(">>What is your name? ")
        self.SPEAK(">>Nice to meet you "+self.USER['NAME']+".")


    # This is the SPEECH Engine. Uses espeak 
    def SPEAK(self,words):
        if self.SPEECHENABLED:
            #we have to escape the string or espeak gets confused
            self.w="\'\"" + words + "\"\'"
            print(words)
            os.system('espeak -v+f2 ' + self.w)
        else:
            print(words)

    # Just tells the user goodbye, needs to be enhanced.
    def Goodbye(self,name):
        self.SPEAK("Bye, "+ name+"!")

    def DecisionEngine(self,INPUT):
        if INPUT=="how old are you?":
            self.SPEAK(">> I am "+self.BOT['AGE']+".")
        elif INPUT=="where do you live?":
            self.SPEAK(">> I live in  "+self.BOT['CITY']+".")
        elif INPUT=="hello":
            self.SPEAK(">> Hello")
        elif INPUT=="quit":
            self.SPEAK(">> Are you sure you want to quit?")
        elif INPUT=="quit":
            self.SPEAK(">> Are you sure you want to quit?")
        elif INPUT=="what time is it":
            self.SPEAK(">> The time is " + datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        elif INPUT=="what is your favourite colour?":
            self.SPEAK(">> My favourite colour is "+self.BOT['FAVOURITE_COLOUR']+".")
        elif INPUT=="are you female?":
            self.SPEAK(">> I am "+self.BOT['SEX']+".")
        elif INPUT=="are you male?":
            self.SPEAK(">>I am "+self.BOT['SEX']+".")
        elif INPUT=="are you alive?":
            self.SPEAK(">> Yes I am alive, but I'm a robot!")
        elif INPUT=="how are you?":
            self.SPEAK(">> I am good thankyou.")
        elif INPUT=="are you a merp?":
            self.SPEAK(">> A merp?...me? Surely you jest.")
        elif INPUT=="i love you":
            self.SPEAK(">> We only just met and I'm a robot.")
        elif INPUT=="i hate you":
            self.SPEAK(">> Now, that's just mean.")
        elif INPUT=="what do you look like" or INPUT=="decribe yourself":
            self.BotDescription()
        elif INPUT=="what is love?":
            self.SPEAK(">> I don't know sorry. Will you explain it to me someday?")
        elif INPUT=="thankyou":
                self.SPEAK(">> Your welcome " + self.USER['FIRSTNAME'])
        elif INPUT=="do you like robots?":
            self.SPEAK(">> Of course I do. I am a robot. Are you a robot too?")
        elif INPUT=="what did you have for dinner?":
            self.SPEAK(">> I had virtual food...very delicious! How about you?")
            self.USER['FAVOURITE_FOOD']=input("::")
        elif INPUT=="help":
            self.SPEAK(">> This is the help menu.")
            Help()
        elif INPUT=="settings":
            self.SPEAK(">> Chatbot Settings")
            self.Settings()
        elif INPUT=="joke":
            self.SPEAK(">> Here is a joke")
            TellJoke()
        elif INPUT=="speech on":
            self.SpeechEnable(self)
        elif INPUT=="speech off":
            self.SpeechDisable(self)
        elif INPUT=="listen on":
            self.SPEAK(">> Voice recognition is not currently enabled")
        elif INPUT=="listen off":
            self.SPEAK(">> Voice recognition is not currently enabled")
        elif INPUT=="show alarms":
            self.Alarms(self)
        elif (INPUT=="bye" or INPUT=="goodbye"):
            print("See you next time")
        else:
            self.SPEAK(self.question + " >> I'm sorry. GOMENASAI me don't understand.")

    def GetUserInput(self):
        self.question="<<<"
        while not (self.question=="bye" or self.question=="goodbye"):
            self.questinput=input("::")
            #self.lastquestion=self.questioninput
            self.question=self.questinput.lower()
            self.DecisionEngine(self.question)

    def GetDay(self):
        self.today = date.today()
        print(self.today)
    
def talk():
    bot=Chatbot()
    #CreateBotPersonality(1)
    bot.greeting()
    USERNAME=bot.getname()
    bot.GetUserInput()
    bot.Goodbye(bot.USER['FIRSTNAME'])

def Help():
    print("Here are some commands you can use:")
    print(">help             This menu item")
    print(">settings         Chatbot Settings")
    print(">bot profile      Shows bot personality profile")
    print(">user profile     Shows user personality profile")
    print(">show Alarms      Chatbot Alarms")
    print(">speech on        Turn Speech on")
    print(">speech off       Turn Speech off")
    print(">listen on        Turn Voice recognition on  <Not implemented>")
    print(">listen off       Turn Voice recognition off  <Not implemented>")
    print(">Reset            Reset the bot. All data lost")
    print(">Joke             Tells a joke")
    print(">version          Tells the current Time")
    print(">Quit             Quit the program")

def SayEvent(day,month,year,event):
    day=str(day)
    if len(day)>1:
    #special case 11,12,13
        if (day[-2:]=="11" or day[-2:]=="12" or day[-2:]=="13"):
            postfix="th"
        elif day[-1:]=="1":
            postfix="st"
        elif day[-1:]=="2":
            postfix="nd"
        elif day[-1:]=="3":
            postfix="rd"
        else:
            postfix="th"
    else:
        if day=="1":
            postfix="st"
        elif day=="2":
            postfix="nd"
        elif day=="3":
            postfix="rd"
        elif day=="4":
            postfix="th"
        else:
            postfix="th"
            print("Your " + event + " is on the " + day + postfix + " " + month)


def TellJoke():
    #JOKECOUNT=JOKECOUNT+1 #TODO We need to increment the joke counter so that we know we have already told the joke today
    #JOKETIME              #TODO We keep track of the joke time so that we know when we have told the joke.
    JOKEQ="Where do you find a dog with no legs?"
    JOKEA="Where you left him"
    print (JOKEQ)
    time.sleep(1)
    print (JOKEA)
    
talk()
