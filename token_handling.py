import sys
import json
import logging
import discord

class Discord():
    def __init__(self):
        self.token = ''
        self.client = ''
    
    # Saves Discord Token in a Json File
    def saveDiscordToken(self):
        try:
            token_file = open('credentials.json', 'w')
            token_json = {"TOKEN": self.token}
            token_file.write(json.dumps(token_json))
        except Exception as e: 
            logging.exception(f"{e}")
            
    # Initialize Discor client to make bot available 
    def initializeDiscordClient(self):
        try:
            self.client = discord.Client()
            return self.client.run(self.token)
        except:
            logging.error(f"Couldn't initilize discord client")