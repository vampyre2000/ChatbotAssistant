# Chatbot Assistant 0.0.1
# 2016 General Public License V3
# By Brendan Clarke

import random
import os
import subprocess
import time
from datetime import datetime

class Chatbot():
    def __init__(self):
	#Set this to True to enable speech.
	self.SPEECHENABLED=False
	##BOT VARIABLES
	self.BOT={'FIRSTNAME':'Alice','LASTNAME':'Dunn','SEX':'female','AGE':'21','CITY':'Sydney','FAVOURITE_COLOUR':'Blue'}
	self.USER={'FIRSTNAME':'Jack','LASTNAME':'Daniels','SEX':'male','AGE':'21','CITY':'Sydney','FAVOURITE_COLOUR':'Blue'}
    self.ALARMS={'WAKEUP':'','BEDTIME':'','GOTOWORK':''}
    #Bot will give a self description of themselves.
    #def description(self):
    def BotDescription(self):
        print("My name is " + self.BOT['FIRSTNAME'] + " but my friends call me " + self.BOT['NICKNAME'] + ". I have " + self.BOT['HAIR_LENGTH'] + " " + self.BOT['HAIR_COLOUR']
            + " hair and " + self.BOT['EYE_COLOUR'] + " eyes.")
    def SpeechEnable(self):
        self.SPEECHENABLED=True
    
    def SpeechDisable(self):
        self.SPEECHENABLED=False
        
    def BotProfile(self):
        for name in self.BOT:
            print ("> " + name + ":                    " + self.BOT[name])

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
        elif INPUT=="help":
            self.SPEAK(">> This is the help menu.")
            Help()
        elif INPUT=="settings":
            self.SPEAK(">> Chatbot Settings")
            self.Settings()
        elif INPUT=="joke":
            self.SPEAK(">> Here is a joke")
            TellJoke()
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
        elif INPUT=="Speak-on":
            self.SpeechEnable(self)
        elif INPUT=="Speak-off":
            self.SpeechDisable(self)
        elif INPUT=="Alarms":
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
    bot.greeting()
    USERNAME=bot.getname()
    bot.GetUserInput()
    bot.Goodbye(bot.USER['NAME'])

def Help():
    print("Here are some commands you can use:")
    print(">Help                   This menu item")
    print(">Settings              Chatbot Settings")
    print(">Profile bot           Chatbot personality profile")
    print(">Profile user          Chatbot personality profile")
    print(">Alarms                Chatbot Alarms")
    print(">Speak-on            Turn Speech on")
    print(">Speak-off            Turn Speech off")
    print(">Reset                  Reset the bot. All data lost")
    print(">Joke                   Tells a joke")
    print(">Time                 Tells the current Time")
    print(">Quit                   Quit the program")

def TellJoke():
    JOKEQ="Where do you find a dog with no legs?"
    JOKEA="Where you left him. hahah"
    print (JOKEQ)
    time.sleep(2)
    print (JOKEA)
#Writedata()
#Readdata()
#ReadGirlnames()
talk()
