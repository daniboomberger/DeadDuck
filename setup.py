import sys
import discord
import asyncio
import json

class Setup():
    def __init__(self):
        self.discord_token = ''

    #Token validation for Discord Token
    async def validateCredentialsJson(self):
        try:
            with open('credentials.json', 'r') as credentials:
                credentials_json = json.load(credentials.read())
                token = credentials_json['Token']
                assert (token != ''), "Token was not set!"


if __name__ == "__main__":
    setup = Setup()
    setup.discord_token = sys.argv[0]
    pass