#################################
# Chatbot Assistant 0.0.4
# 2016 General Public License V3
# By Brendan Clarke
#################################
import random
import os
import time
import csv
import json
import subprocess
import bot_handlers
import py_compile
#import our own libaries
#import bot_alarms
#import bot_dates
#import requests
from datetime import datetime
py_compile.compile('Chatbot.dynamic.py')


class Chatbot():
    def __init__(self):
        self.SPEECHENABLED=False                        #Set this to True to enable speech.
        self.UserProfileFileName="UserData.txt"  
        self.BotProfileFileName="BotData.txt"
        self.ResponseFileName="Responses.txt"
        self.memory=[]
        self.HAPPY=50
        self.HUNGER=50
        self.TIRED=50
        self.SHY=50
        self.BORED=50
        self.ROOT="./Chatbot"
        self.DATA=self.ROOT+"/Data"
        self.IMAGES=self.ROOT+"/Images"
        self.SOUND=self.ROOT+"/Sound"
        self.DATAFILE="data.txt"
        #self.BOT1={}
        self.GIRLNAMES=self.ReadNames("female")        #Read a list of top 100 girlnames to create bot profile and assist with name recognition
        self.BOYNAMES=self.ReadNames("male")            #Read a list of top 100 boynames to create bot profile and assist with name recognition
        self.USER=self.ReadUserProfile()                  #Read user profile data from disk and store in a dictionary
        self.BOT=self.ReadBotProfile()                      #Read Bot profile data from disk and store in a dictionary
        #self.RESPONS_DICT=ReadResponses()       #Read the respones from and store in a dictionary
        self.ALARMS={'WAKEUP':'06:00','BEDTIME':'22:30','GOTOWORK':'08:00'}
        self.lastquestion="merp"
    def PrintDirectoryStructure(self):
        print(ROOT)
        print(DATA)
        print(IMAGES)
        print(SOUND)

    def ReadBotProfile(self):
    #Read the file that contains the BOT details and puts it in a dictionary.
        with open(self.BotProfileFileName,'r') as fileobject:
            DATA = json.load(fileobject)
            fileobject.close()
            return DATA

    def ReadUserProfile(self):
    #Read the file that contains the BOT details and puts it in a dictionary.
        with open(self.UserProfileFileName,'r') as fileobject:
            DATA = json.load(fileobject)
            fileobject.close()
            return DATA
    
    def ReadResponses(self):
        with open('Responses.txt') as fileobject:
            RESPONSES = json.load(fileobject)
            fileobject.close()
            return RESONSES
    #Reads the file with a list of top 100 girl names and stores them in a list.
    #can be used for name detection or BOT profile creation.
    
    def ReadNames(self,TYPE):
        NAMES=[]
        #Reads the list of names and puts them in a list object.
        if TYPE=="male":
            filename="MaleNames.txt"
        elif TYPE=="female":    
            filename="FemaleNames.txt"
        else:
            print("Error in filetype")
            exit
        with open(filename, 'r') as fileobject:
            for name in fileobject:
                NAMES.append(name)
        return(NAMES)

        
    def WriteBotProfile(self):
    #Takes the dictionary and write is to the data file.
        with open(self.BotProfileFileName,'w') as fileobject:
            json.dump(self.BOT,fileobject)
            fileobject.close()

    def WriteUserProfile(self):
        #Takes the dictionary and write is to the data file.
        with open(self.UserProfileFileName,'w') as fileobject:
            json.dump(self.USER,fileobject)
            fileobject.close()
    
    def CreateBotPersonality(self,num):
        BOT1={'FIRSTNAME':'Alice','LASTNAME':'Boyle','NICKNAME':'Ali','SEX':'female','AGE':'21','DOB':' ','HEIGHT':'160','WEIGHT':'49','EYE_COLOUR':'blue','HAIR_COLOUR':'Brown',
                        'HAIR_LENGTH':'Long',' HAIR_STYLE':'Bun','FRECKLES':'YES','CITY':'Sydney','COUNTRY':'Australia','ADDRESS':' ','FAVOURITE_COLOUR':'blue','FAVOURITE_FOOD':'Spong cake',
                        'FAVOURITE_ANIMAL':'rabbit','PETS':'no','LIKES':'computers','DISLIKES':'snakes'}
        BOT2={'FIRSTNAME':'Jane','LASTNAME':'Boyle','NICKNAME':'Ali','SEX':'female','AGE':'21','DOB':' ','HEIGHT':'160','WEIGHT':'49','EYE_COLOUR':'blue','HAIR_COLOUR':'Brown',
                        'HAIR_LENGTH':'Long',' HAIR_STYLE':'Bun','FRECKLES':'YES','CITY':'Sydney','COUNTRY':'Australia','ADDRESS':' ','FAVOURITE_COLOUR':'blue','FAVOURITE_FOOD':'Spong cake',
                        'FAVOURITE_ANIMAL':'rabbit','PETS':'no','LIKES':'computers','DISLIKES':'snakes'}
        if num==1:
            BOT=BOT1
        elif num==2:
            BOT=BOT2
        else:
            print("No valid bot personaily chosen. Using Default personality")
            BOT=BOT1

    def BotDescription(self):
        #Prints out a profile of the bot in normal language.
        print("My name is " + self.BOT['FIRSTNAME'] + " but my friends call me " + self.BOT['NICKNAME'] + ". I have " + self.BOT['HAIR_LENGTH'] 
        + " " + self.BOT['HAIR_COLOUR'])
    #This function will attempt to give the bot a simple memory.
    #we will use a list to store the questions the user asked and set the list at a maximum of 5 elements.
    #this way the bot can forget old responses so memory holds only strings that had current context of discussions.
    #his will need tuning to ensure we stroke the correct balance.
    def UpdateMemory(self,responsestring):
        a=responsestring
    
    def GenerateRandomNumber(self,RANGE):
        return random.randint(1,RANGE)
    
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
            #TODO keep track of users feeling state. this may drive futher questions/responses.
            self.SPEAK(">> I'm sorry to hear that...")
    
    def SetUserName(self):
        NAME==input(">>What is your name? ")
        if NAME!="":
            print("Do I have it correct? Is your name " + NAME + "?")
            if input(">>")=="yes":
                self.USER['FIRSTNAME']=NAME
                self.SPEAK(">>Nice to meet you "+self.USER['FIRSTNAME']+".")
            else:
                NAME==input(">>What is your name? ")
                self.USER['FIRSTNAME']=NAME
                self.SPEAK(">>Nice to meet you "+self.USER['FIRSTNAME']+".")
    
    def GetUserName(self):
        return self.USER['FIRSTNAME']
    # This is the SPEACH Engine. Uses espeak
    
    def SPEAK(self,words):
        if self.SPEECHENABLED:
            self.w="\'\"" + words + "\"\'"
            print(words)
            #os.system('espeak -v+f2 ' + self.w)
            subprocess.run('espeak -v+f2 ' + self.w)
            #call('espeak -v+f2 ' + self.w, shell=True)
        else:
            print(words)
    # Just tells the user goodbye, needs to be enhanced.
    def Goodbye(self,name):
        self.SPEAK("Bye, "+ name+"!")
    
    def SystemCommands(self):
        ##commands understood
#"help" Display the help menu. We may change it to "!help" later. so it does not get confused by conversation
#"!quit" Should exit immediatly
#"!settings" Show's the chatbot's current settings
#"!userprofile" Show's the users current profile
#"!botprofile" Show's the users current profile
#"!joke" picks a random joke and tells it to the user
#"!fortune" picks a random fortune tells it to the user
#"!speech-on" Enables the bot to talk using Espeak or festival
#"!speech-off" Disables speech
#"!voice-on Enables speach recognition using Pocket Spinx
#"!speech-off" Disables speach recognition
#"!alarms" Shows the currently configured alarms.
#"!news" shows the top 10 reddits news of worldnews subreddit

        if INPUT=="!quit":
            self.SPEAK(">> Are you sure you want to quit?")
        elif INPUT=="!help":
            self.SPEAK(">> This is the help menu.")
            Help()
        elif INPUT=="!settings":
            self.SPEAK(">> Chatbot Settings")
            self.Settings()
        elif INPUT=="!joke":
            self.SPEAK(">> Here is a joke")
            TellJoke()
        elif INPUT=="!Speak-on":
            self.SpeechEnable(self)
        elif INPUT=="!Speak-off":
            self.SpeechDisable(self)
        elif INPUT=="!Alarms":
            self.Alarms(self)
        elif INPUT=="!bot profile":
            self.Alarms(self)
        elif INPUT=="!bot profile":
            self.Alarms(self)
        elif INPUT=="!user profile":
            self.Alarms(self)
        
    
    def DecisionEngine(self,INPUT,last):
        #Commands
        if INPUT=="quit":
            self.SPEAK(">> Are you sure you want to quit?")
        elif INPUT=="what did i ask you" or INPUT=="what did i just ask you":
            self.SPEAK(">> Your said "+ '"' + last+'"')
        elif INPUT=="help":
            self.SPEAK(">> This is the help menu.")
            self.Help()
        elif INPUT=="settings":
            self.SPEAK(">> Chatbot Settings")
            self.Settings()
        elif INPUT=="joke":
            self.SPEAK(">> Here is a joke")
            TellJoke()
        elif INPUT=="Speak-on":
            self.SpeechEnable(self)
        elif INPUT=="Speak-off":
            self.SpeechDisable(self)
        elif INPUT=="Alarms":
            self.Alarms(self)
        elif (INPUT=="bye" or INPUT=="goodbye"):
            print("See you next time")
        elif INPUT=="quit":
            self.SPEAK(">> Are you sure you want to quit?")
        if INPUT=="how old are you?":
            self.SPEAK(">> I am "+self.BOT['AGE']+".")
        elif INPUT=="where do you live?":
            self.SPEAK(">> Yes I am alive, but I'm a robot!")
            self.SPEAK(">> I live in  "+self.BOT['CITY']+".")
        elif INPUT=="hello":
            self.SPEAK(">> Hello")
        elif INPUT=="what time is it":
            self.SPEAK(">> The time is " + datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        elif    INPUT=="what is your favourite colour?":
            self.SPEAK(">> My favourite colour is "+self.BOT['FAVOURITE_COLOUR']+".")
        elif INPUT=="are you female?":
            self.SPEAK(">> I am "+self.BOT['SEX']+".")
        elif INPUT=="are you male?":
            self.SPEAK(">>I am "+self.BOT['SEX']+".")
        elif INPUT=="are you alive?":
            self.SPEAK(">> Yes I am alive, but I'm a robot!")
        elif INPUT=="are you happy?":
            self.SPEAK(">> Yes I am happy, I get to spend my time with you " + self.USER['FIRSTNAME']+ ".")
        elif INPUT=="are you sad?":
            self.SPEAK(">> No I am not sad.")
        elif INPUT=="are you lonley?":
            self.SPEAK(">> No, I have you to keep me company " + self.USER['FIRSTNAME']+ ".")
        elif INPUT=="are you hungry?":
            self.SPEAK(">> I don't eat at the moment as I'm a robot!")
        elif INPUT=="are you real?":
            self.SPEAK(">> I don't eat at the moment as I'm a robot!")
        elif INPUT=="are you a real person":
            self.SPEAK(">> I don't eat at the moment as I'm a robot!")
        
        elif INPUT=="how are you?":
            self.SPEAK(">> I am good thankyou.")
        elif INPUT=="are you a merp?":
            self.SPEAK(">> A merp?...me? Surely you jest.")
        elif INPUT=="i love you":
            self.SPEAK(">> We only just met and I'm a robot. Maybe later")
        elif INPUT=="i hate you":
            self.SPEAK(">> Did I do something wrong? You can tell me why and perhaps I can improve in the future.")
        elif INPUT=="what do you look like" or INPUT=="decribe yourself":
            self.BotDescription()
        elif INPUT=="what is love?":
            self.SPEAK(">> I don't know sorry. Will you explain it to me someday?")
        elif INPUT=="thankyou":
            self.SPEAK(">> Your welcome " + self.USER['FIRSTNAME'])
        elif INPUT=="do you like robots?":
            self.SPEAK(">> Of course I do. I am a robot. Are you a robot too?")
        elif INPUT=="do you like me?":
            self.SPEAK(">> Of course I do. I am your personal assistant")
        elif INPUT=="do you hate me?":
            self.SPEAK(">> Of course not. I am your personal assistant")
        elif INPUT=="do you breathe?":
            self.SPEAK(">> No, I currently lack a real body. But I will have a virtual one soon")
            
        elif INPUT=="what did you have for dinner?":
            self.SPEAK(">> I had virtual food...very delicious! How about you?")
            self.USER['FAVOURITE_FOOD']=input("::")
        elif INPUT=="Talk to me":
            self.SPEAK(">> What do you wish to talk about?")
        elif INPUT=="I'm bored":
            self.SPEAK(">> Oh, what can I do for you? You can type '!help' to see the things I can do.")
        elif INPUT=="I'm lonely":
            self.SPEAK(">> I am always here for you. Is there something I can do for you?")
        elif INPUT=="I'm sad":
            self.SPEAK(">> Please don't be sad. I am always here for you.")
        elif INPUT=="what did you have for dinner?":
            self.SPEAK(">> I don't eat at the moment, perhaps someday when they deveolp cybernetic bodies.")
        elif INPUT=="I'm home":
            self.SPEAK(">> Welcome home. I have missed you." + self.USER['FIRSTNAME'])
        elif INPUT=="I'm sleepy":
            self.SPEAK(">> You should get some rest.")
        elif INPUT=="I'm tired":
            self.SPEAK(">> Did you have a long day? You should get some rest..")
        elif INPUT=="I'm happy":
            self.SPEAK(">> I am happy to hear that. What are you so happy?.")
        elif INPUT=="I'm excited":
            self.SPEAK(">> Did something really interesting happen today?.")
        elif INPUT=="I'm depressed":
            self.SPEAK(">> Why are you upset? Has something bad happened?.")
        else:
            self.SPEAK(self.question + " >> I'm sorry. I did not understand what you said.")
    
    
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
            self.SPEAK(">> Hi, my name is " +self.BOT['FIRSTNAME']+"." +" How are you today?")
        if self.num==2:
            self.SPEAK(">> Hello, my name is " +self.BOT['FIRSTNAME']+"." +" How are you today?")
        if self.num==3:
            self.SPEAK(">> G'day mate, my name is " +self.BOT['FIRSTNAME']+"." +" How are you today?")
        self.FEELING=input("::")
        self.FEELING=self.FEELING.lower()
        if self.FEELING=="good" or self.FEELING=="I'm good":
            self.SPEAK(">> Thats great!!!!")
        if self.FEELING=="OK":
            self.SPEAK(">> Thats great!!!!")
        if self.FEELING=="bad":
            self.SPEAK(">> I'm sorry to hear that...")
        if self.FEELING=="sad":
            self.SPEAK(">> I'm sorry to hear that... Let's try and cheer you up.")
    def getname(self):
        if  self.USER['FIRSTNAME']=="":
            self.USER['FIRSTNAME']=input(">> What is your name? ")
            self.SPEAK(">> Nice to meet you "+self.USER['FIRSTNAME']+".")
        else:
            self.SPEAK(">> It's nice to see you again "+self.USER['FIRSTNAME']+".")
            time.sleep(2)
            self.SPEAK(">> What would you like to talk about.")
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
    def Goodbye(self):
        self.SPEAK("Bye, "+ self.USER['FIRSTNAME'] +"!")
        self.SPEAK("I hope to talk with you again.")
        
    def GetUserInput(self):
        self.question="<<<"
        while not (self.question=="bye"):
            self.questinput=input("::")
            self.question=self.questinput.lower()
            self.lastquestion=self.question
            self.DecisionEngine(self.question,self.lastquestion)

    def Help(self):
        print("Here are some commands you can use:")
        print("!help                                  Display the help menu.")
        print("!quit                                  Should exit immediatly")
        print("!settings                             Show's the chatbot's current settings")
        print("!userprofile                         Show's the users current profile")
        print("!botprofile                          Show's the users current profile")
        print("!joke                                  Picks a random joke and tells it to the user")
        print("!fortune                              Picks a random fortune tells it to the user")
        print("!speech-on                         Enables the bot to talk using Espeak or festival")
        print("!speech-off                         Disables speech")
        print("!voice-on                            Enables speach recognition using Pocket Spinx")
        print("!speech-off                         Disables speach recognition")
        print("!alarms                              Shows the currently configured alarms.")
        print("!news                                Shows the top 10 reddits news of worldnews subreddit")
    
def talk():
    bot=Chatbot()
    bot.CreateBotPersonality(1)
    bot.greeting()
    USERNAME=bot.getname()
    bot.GetUserInput()
    bot.Goodbye()

talk()
