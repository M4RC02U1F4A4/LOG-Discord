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
    print("OK")

@bot.event
async def on_voice_state_update(member, before, after):
    if(before.channel == None):
        print(datetime.datetime.now(), "| CONNECTED |", member, "|", str(after.channel), file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| CONNECTED |", member, "|", str(after.channel))
    elif(after.channel == None):
        print(datetime.datetime.now(), "| DISCONNECTED |", member, "|", str(before.channel), file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| DISCONNECTED |", member, "|", str(before.channel))
    elif(before.channel != after.channel):
        print(datetime.datetime.now(), "| MOVED |", member, "|", str(before.channel), "->", str(after.channel), file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| MOVED |", member, "|", str(before.channel), "->", str(after.channel))
    elif(before.self_stream != after.self_stream):
        print(datetime.datetime.now(), "| STREAMING |", member, "|", str(after.self_stream).replace("True", "ON").replace("False", "OFF"), file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| STREAMING |", member, "|", str(after.self_stream).replace("True", "ON").replace("False", "OFF"))
    elif(before.self_video != after.self_video):
        print(datetime.datetime.now(), "| VIDEO |", member, "|", str(after.self_video).replace("True", "ON").replace("False", "OFF"), file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| VIDEO |", member, "|", str(after.self_video).replace("True", "ON").replace("False", "OFF"))
    if(before.self_deaf != after.self_deaf and after.channel != None):
        print(datetime.datetime.now(), "| DEAF |", member, "|", str(after.self_deaf).replace("True", "YES").replace("False", "NO"), file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| DEAF |", member, "|", str(after.self_deaf).replace("True", "YES").replace("False", "NO"))
        if(after.self_mute == True and after.self_deaf == False):
            print(datetime.datetime.now(), "| MUTE |", member, "|", str(after.self_mute).replace("True", "YES"), file=open("./out/log.txt", "a"))
            print(datetime.datetime.now(), "| MUTE |", member, "|", str(after.self_mute).replace("True", "YES"))
    elif(before.self_mute != after.self_mute and after.channel != None):
        print(datetime.datetime.now(), "| MUTE |", member, "|", str(after.self_mute).replace("True", "YES").replace("False", "NO"), file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| MUTE |", member, "|", str(after.self_mute).replace("True", "YES").replace("False", "NO"))
    if(before.channel == None and after.channel != None):
        if(after.self_deaf == True):
            print(datetime.datetime.now(), "| DEAF |", member, "|", str(after.self_deaf).replace("True", "YES"), file=open("./out/log.txt", "a"))
            print(datetime.datetime.now(), "| DEAF |", member, "|", str(after.self_deaf).replace("True", "YES"))
        elif(after.self_mute == True):
            print(datetime.datetime.now(), "| MUTE |", member, "|", str(after.self_mute).replace("True", "YES"), file=open("./out/log.txt", "a"))
            print(datetime.datetime.now(), "| MUTE |", member, "|", str(after.self_mute).replace("True", "YES"))
    

@bot.event
async def on_invite_create(invite):
    print(datetime.datetime.now(), "| INVITE |", invite.inviter, "|", str(invite.code), file=open("./out/log.txt", "a"))
    print(datetime.datetime.now(), "| INVITE |", invite.inviter, "|", str(invite.code))

@bot.event
async def on_member_join(member):
    print(datetime.datetime.now(), "| JOIN |", member, "|", member.display_name, file=open("./out/log.txt", "a"))
    print(datetime.datetime.now(), "| JOIN |", member, "|", member.display_name)

@bot.event
async def on_member_remove(member):
    print(datetime.datetime.now(), "| LEAVE |", member, "|", member.display_name, file=open("./out/log.txt", "a"))
    print(datetime.datetime.now(), "| LEAVE |", member, "|", member.display_name)

@bot.event
async def on_guild_update(before, after):
    if(before.region != after.region):
        print(datetime.datetime.now(), "| REGION |", before.region, "->", after.region, file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| REGION |", before.region, "->", after.region)
    if(before.verification_level != after.verification_level):
        print(datetime.datetime.now(), "| SECURITY |", before.verification_level, "->", after.verification_level, file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| SECURITY |", before.verification_level, "->", after.verification_level)

@bot.event
async def on_member_ban(guild, user):
    print(datetime.datetime.now(), "| BAN |", user.name,  file=open("./out/log.txt", "a"))
    print(datetime.datetime.now(), "| BAN |", user.name)

@bot.event
async def on_member_unban(guild, user):
    print(datetime.datetime.now(), "| UNBAN |", user.name,  file=open("./out/log.txt", "a"))
    print(datetime.datetime.now(), "| UNBAN |", user.name)

@bot.event
async def on_user_update(before, after):
    print(datetime.datetime.now(), "| USERNAME |", before.name, "->", after.name, file=open("./out/log.txt", "a"))
    print(datetime.datetime.now(), "| USERNAME |", before.name, "->", after.name,)

@bot.event
async def on_member_update(before, after):
    if(before.nick != after.nick):
        print(datetime.datetime.now(), "| NICK |", (before.nick.encode('utf-8')), "->", (after.nick.encode('utf-8')), file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| NICK |", (before.nick.encode('utf-8')), "->", (after.nick.encode('utf-8'))) 
    if(before.mobile_status != after.mobile_status):
        print(datetime.datetime.now(), "| STATUS |", before, "|", "mobile |", before.mobile_status, "->", after.mobile_status, file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| STATUS |", before, "|", "mobile |", before.mobile_status, "->", after.mobile_status) 
    if(before.desktop_status != after.desktop_status):
        print(datetime.datetime.now(), "| STATUS |", before, "|", "desktop |", before.desktop_status, "->", after.desktop_status, file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| STATUS |", before, "|", "desktop |", before.desktop_status, "->", after.desktop_status)
    if(before.web_status != after.web_status):
        print(datetime.datetime.now(), "| STATUS |", before, "|", "web |", before.web_status, "->", after.web_status, file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| STATUS |", before, "|", "web |", before.web_status, "->", after.web_status)
    if(before.roles != after.roles):
        print(datetime.datetime.now(), "| ROLE |", before, "|", *(after.roles), file=open("./out/log.txt", "a"))
        print(datetime.datetime.now(), "| ROLE |", before, "|", *(after.roles))
    if(any(after.activities)):
        controllo = True
        for role in after.roles:
            if str(role.name) == "BOT":
                controllo = False
        if(controllo):
            print(datetime.datetime.now(), "|", before, "|", str(after.activities).encode("utf-8"), file=open("./out/activities.txt", "a"))
            print(datetime.datetime.now(), "|", before, "|", str(after.activities).encode("utf-8"))

@bot.event
async def on_message(message):
    if(len(message.attachments) != 0):
        if(str(message.content) == ""):
            print(datetime.datetime.now(), "|", message.id, "|", message.channel, "|", message.author, "|", message.attachments[0].filename, "|", message.attachments[0].url, file=open("./out/chat.txt", "a"))
            print(datetime.datetime.now(), "|", message.id, "|", message.channel, "|", message.author, "|", message.attachments[0].filename, "|", message.attachments[0].url)
        else:
            print(datetime.datetime.now(), "|", message.id, "|", message.channel, "|", message.author, "|", str(message.content).encode("utf-8"), "|", message.attachments[0].filename, "|", message.attachments[0].url, file=open("./out/chat.txt", "a"))
            print(datetime.datetime.now(), "|", message.id, "|", message.channel, "|", message.author, "|", str(message.content).encode("utf-8"), "|", message.attachments[0].filename, "|", message.attachments[0].url)
    else:
        print(datetime.datetime.now(), "|", message.id, "|", message.channel, "|", message.author, "| TTS = ", message.tts, "|", str(message.content).encode("utf-8"), file=open("./out/chat.txt", "a"))
        print(datetime.datetime.now(), "|", message.id, "|", message.channel, "|", message.author, "| TTS = ", message.tts, "|", str(message.content).encode("utf-8"))

@bot.event
async def on_message_edit(before, after):
    if(before.content != after.content):
        print(datetime.datetime.now(), "|", before.id, "|", str(after.content).encode("utf-8"), file=open("./out/chat.txt", "a"))
        print(datetime.datetime.now(), "|", before.id, "|", str(after.content).encode("utf-8"))


print("Starting...")
bot.run(TOKEN)