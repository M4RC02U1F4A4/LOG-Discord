import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD_NAME')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n' + f'{guild.name}(id: {guild.id})\n')

    num = 0
    for member in range(len(guild.members)):
        print(str(guild.members[member]).encode("utf-8"))
        num += 1

client.run(TOKEN)