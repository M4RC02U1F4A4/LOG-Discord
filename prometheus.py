import os
import discord
from dotenv import load_dotenv
import datetime
from prometheus_client import Gauge
from prometheus_client import Counter
from prometheus_client import start_http_server

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')

bot = discord.Client()

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    nOnline = 0
    nNotOffline = 0
    nOffline = 0
    nDnd = 0
    nIdle = 0
    for user in bot.guilds[0].members:
        if(str(user.status) != "offline" and user.bot == False):
            nNotOffline +=1
        if(str(user.status) == "online" and user.bot == False):
            nOnline +=1
        if(str(user.status) == "offline" and user.bot == False):
            nOffline += 1
        if(str(user.status) == "dnd" and user.bot == False):
            nDnd += 1
        if(str(user.status) == "idle" and user.bot == False):
            nIdle +=1
        discord_user_not_offline.set(nNotOffline)
        discord_user_online.set(nOnline)
        discord_user_offline.set(nOffline)
        discord_user_dnd.set(nDnd)       
        discord_user_idle.set(nIdle)
    print("OK", file=open("./out/log.txt", "a"))
    print("OK")

@bot.event
async def on_voice_state_update(member, before, after):
    if(before.channel == None):
        discord_user_connect.inc()
    elif(after.channel == None):
        discord_user_disconnect.inc()

@bot.event
async def on_member_update(before, after):
        nOnline = 0
        nNotOffline = 0
        nOffline = 0
        nDnd = 0
        nIdle = 0
        for user in bot.guilds[0].members:
            if(str(user.status) != "offline" and user.bot == False):
                nNotOffline +=1
            if(str(user.status) == "online" and user.bot == False):
                nOnline +=1
            if(str(user.status) == "offline" and user.bot == False):
                nOffline += 1
            if(str(user.status) == "dnd" and user.bot == False):
                nDnd += 1
            if(str(user.status) == "idle" and user.bot == False):
                nIdle +=1
            discord_user_not_offline.set(nNotOffline)
            discord_user_online.set(nOnline)
            discord_user_offline.set(nOffline)
            discord_user_dnd.set(nDnd)       
            discord_user_idle.set(nIdle)

@bot.event
async def on_message(message):
    discord_message.inc()


print("Starting...")
start_http_server(9324)
discord_user_online = Gauge('discord_user_online', 'Numero di utenti online')
discord_user_offline = Gauge('discord_user_offline', 'Numero di utenti offline')
discord_user_not_offline = Gauge('discord_user_not_offline', 'Numero di utenti non offline')
discord_user_dnd = Gauge('discord_user_dnd', 'Numero di utenti in dnd')
discord_user_idle = Gauge('discord_user_idle', 'Numero di utenti in idle')
discord_message = Counter('discord_message', 'Numero di utenti online')
discord_user_connect = Counter('discord_user_connect', 'Numero di connessioni')
discord_user_disconnect = Counter('discord_user_disconnect', 'Numero di disconnessioni')
bot.run(TOKEN)