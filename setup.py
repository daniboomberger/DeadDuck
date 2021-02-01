import discord_client
import sys

class Setup:
    def __init__(self):
        pass
    
    '''
        Function creates discord client & saves token in json file
        parameter: token, given in first run in setup.py
        returns: Discord Class Object
    '''
    def initializeDiscordClient(self, token):
        discord = discord_client.Discord()
        discord.token = token
        discord.initializeDiscordClient()
        discord.saveDiscordToken()
        yield discord

if __name__ == '__main__':
    setup = Setup()
    setup.initializeDiscordClient(sys.argv[1])

    