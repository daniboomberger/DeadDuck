import sys
import json
import logging
import discord

class Discord():
    def __init__(self):
        self.token = ''
        self.client = ''
    
    #Saves Discord Token in a Json File
    def saveDiscordToken(self):
        token_file = open('credentials.json', 'w')
        token_json = {"TOKEN": self.token}
        token_file.write(json.dumps(token_json))

    def initialiseDiscordCLient(self):
        self.client = discord.Client()
        self.client.run(self.token)