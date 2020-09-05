import os
import time 
import playsound
from gtts import gTTS
import speech_recognition as sr
from twitchio.ext import commands
import random


e = [" Try playing the Italien Game" , " Try playing the Ruy Lopez", " Try playing the Sicilian Defense", " Try playing the French Defense", " Try playing the Caro-kann Defense", " Try playing the Pirc Defense", " Try playing the Queen's Gambit", " Try playing the Indian Defenses", " Try the English Opening", " Try the Reti Opening", " Try playing the Center Game", " Try playing the Danish Gambit", " Try playing the Sokolsky", " Try playing the Blackmar-Diemer Gambit", " Try playing the Latvian Gambit", " Try playing the Budapest Gambit" ]


class chess(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=', client_id='', nick='', prefix='!',
                         initial_channels=[''])

      # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
    	new_line = str(message.content)
    	with open("python.txt", "a") as f:
    		f.write("\n")
    		f.write(new_line)
    		print(message.content)
    		await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='chess')
    async def my_command(self, ctx):
        await ctx.send(f'{e[random.randint(0,16)]} @{ctx.author.name}!')
while True:
    chess = chess()
    chess.run()3
