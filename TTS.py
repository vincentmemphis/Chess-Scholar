import os
import time 
import playsound
from gtts import gTTS
from twitchio.ext import commands
import random
import time
import keyboard        

def speak(text,):

	try:

		file = open("python.txt", "r").read()
		tts = gTTS(text= str(file), lang="en-nz", slow="False")
		filename = str(random.randint(0,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
		f = open('python.txt', 'r+')
		f.truncate(0)
		tts.save(filename)
		playsound.playsound(filename)
		speak(file)
	except Exception as e:
		time.sleep(3)
		speak == speak('python.txt')
		speak.run()
		print(e)


#speak(e[random.randint(0,16)]) Speaks a random opening
while True:
	speak = speak('python.txt')


#accents
 #'en-us': 'English (US)',
 #       'en-ca': 'English (Canada)',
  #      'en-uk': 'English (UK)',
   #     'en-gb': 'English (UK)',
    #    'en-au': 'English (Australia)',
     #   'en-gh': 'English (Ghana)',
      #  'en-in': 'English (India)',
       # 'en-ie': 'English (Ireland)',
        #'en-nz': 'English (New Zealand)',
         #'en-ng': 'English (Nigeria)',
          #'en-ph': 'English (Philippines)',
           #'en-za': 'English (South Africa)',
            #'en-tz': 'English (Tanzania)',