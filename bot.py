import discord
from discord.ext import commands
import requests
bot = commands.Bot(command_prefix="?")
infostuff = "## Welcome to Starry, and open source OSNIT discord bot\n"
#cmds
@bot.command()
async def info(ctx):
    await ctx.send(infostuff)
@bot.command()
async def ip(ctx):
    ipy = [ip:4]
    requests.post
#end cmd
bot.run("private_token")