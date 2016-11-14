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
		
  def SPEAK(self,words):
		if self.SPEECHENABLED:
			self.w="\'\"" + words + "\"\'"
			print(words)
			#os.system('espeak -v+f2 ' + self.w)
			subprocess.run('espeak -v+f2 ' + self.w)
			#call('espeak -v+f2 ' + self.w, shell=True)
		else:
			print(words)
      
