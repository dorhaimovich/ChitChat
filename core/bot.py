# bot.py
import os

import discord
from dotenv import load_dotenv
from ..GPT2.textGenerator import generateText

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()

client = discord.Client(intents=intents)
numberOfMessages = 0


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        print(f'{client.user} is connected to the following guild:\n'
              f'{guild.name}')

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    global numberOfMessages
    if message.author == client.user or message.author.name == "ChitChat.ai Logger Bot":
        return
    numberOfMessages = numberOfMessages + 1
    if numberOfMessages % 3 == 0:
        await message.channel.typing()
        response = generateText(message.content)
        await message.reply(response)
    # if message.content == 'hello':
    #     response = 'Hello!'
    #     await message.channel.send(response)
    #
    # if message.content == 'bye':
    #     response = 'Goodbye!'
    #     await message.channel.send(response)
    #
    # if message.content == 'pizza':
    #     with open('data/pizza.jpeg', 'rb') as f:
    #         picture = discord.File(f)
    #         await message.channel.send(file=picture)


client.run(TOKEN)
