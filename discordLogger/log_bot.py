import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from Msg_Table import MsgLogger
from Network import Network
from datetime import datetime

load_dotenv()

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
logger = MsgLogger.MsgLogger()
network = Network.Network()


def get_member_names(c: commands.Bot, author: str):
    r = []
    for guild in c.guilds:
        for member in guild.members:
            if member != client.user and member.name != author:
                r.append(member.name)
    return r


@client.event
async def on_ready():
    print("The bot is ready for use!")



@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author != client.user:
        logger.push_msg(
            {'Time': message.created_at, 'Author': message.author.name, 'Message Content': message.content,
             'Mentions': [m.name for m in message.mentions]})
        if not message.mentions and not message.reference:
            network.add_edges(message.author.name, get_member_names(client, message.author.name))
        if message.mentions:
            network.add_edges(message.author.name, [m.name for m in message.mentions])
        if message.reference:
            referenced_message = await message.channel.fetch_message(message.reference.message_id)
            referenced_author_name = referenced_message.author.name
            network.add_edges(message.author.name, [referenced_author_name])
    print(logger.msg_tb)


@client.command()
async def start(ctx):
    await ctx.send("Recording Conversation")
    logger.enable()


@client.command()
async def pause(ctx):
    logger.disable()
    await ctx.send("Recording Paused")


@client.command()
async def resume(ctx):
    await ctx.send("Recording Resumed")
    logger.enable()


@client.command()
async def end(ctx):
    logger.disable()
    time_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    logger.export_to_csv(time_str + "_msg_log")
    network.save_image(time_str + "_graph_img")
    await ctx.send("Recording Stopped")
    await ctx.send(file=discord.File('./' + time_str + '_msg_log.csv'))
    await ctx.send(file=discord.File('./' + time_str + '_graph_img.png'))
    logger.clear()
    network.clear()


client.run(os.getenv('DISCORD_LOGGER_BOT_TOKEN'))
