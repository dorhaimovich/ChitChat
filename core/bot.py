# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

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
    if message.author == client.user:
        return

    if message.content == 'hello':
        response = 'Hello!'
        await message.channel.send(response)

    if message.content == 'bye':
        response = 'Goodbye!'
        await message.channel.send(response)

    if message.content == 'pizza':
        with open('data/pizza.jpeg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

client.run(TOKEN)