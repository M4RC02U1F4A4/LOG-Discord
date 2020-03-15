import os
import discord
from dotenv import load_dotenv
import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')

bot = discord.Client()

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print("OK", file=open("log.txt", "a"))

@bot.event
async def on_voice_state_update(member, before, after):
    if(before.channel == None):
        print(datetime.datetime.now(), "|", member, "| CONNECTED |", str(after.channel), file=open("log.txt", "a"))
        print(datetime.datetime.now(), "|", member, "| CONNECTED |", str(after.channel))
    elif(after.channel == None):
        print(datetime.datetime.now(), "|", member, "| DISCONNECTED |", str(before.channel), file=open("log.txt", "a"))
        print(datetime.datetime.now(), "|", member, "| DISCONNECTED |", str(before.channel))
    elif(before.channel != after.channel):
        print(datetime.datetime.now(), "|", member, "| MOVED |", str(before.channel), "->", str(after.channel), file=open("log.txt", "a"))
        print(datetime.datetime.now(), "|", member, "| MOVED |", str(before.channel), "->", str(after.channel))
    elif(before.self_stream != after.self_stream):
        print(datetime.datetime.now(), "|", member, "| STREAMING |", str(after.self_stream).replace("True", "ON").replace("False", "OFF"), file=open("log.txt", "a"))
        print(datetime.datetime.now(), "|", member, "| STREAMING |", str(after.self_stream).replace("True", "ON").replace("False", "OFF"))

print("Starting...", file=open("log.txt", "a"))
bot.run(TOKEN)