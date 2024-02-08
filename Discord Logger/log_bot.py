import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from Msg_Table import MsgLogger

load_dotenv()

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
logger = MsgLogger.MsgLogger()


@client.event
async def on_ready():
    print("The bot is ready for use!")


@client.event
async def on_message(message):
    logger.push_msg({'Time': message.created_at, 'Author': message.author, 'Message Content': message.content})
    print (logger.msg_tb)
    await client.process_commands(message)


@client.command()
async def start(ctx):
    print(ctx)
    await ctx.send("Recording Conversation")



client.run(os.getenv('BOT_TOKEN'))