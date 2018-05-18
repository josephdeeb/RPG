import discord
import asyncio
import game
import world

client = discord.Client()

accounts = {}

async def registerAccount(ID, name):
    accounts[ID] = Account(name)

db = DatabaseWrapper("game.db")

class DiscordIOWrapper(IOWrapper):
    async def input():
        pass


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
    if message.content.startswith("$"):
        


client.run('MzgxMTYwNDA3NzUyMTE0MTg2.DPK4BA.BnaIF6GKxpRJ7iHkN0OxfJHM8cY')
