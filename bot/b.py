import discord
from discord.ext import commands
import requests
import json
from googlesearch import search
bot = commands.Bot(command_prefix=".")
@bot.command()
async def update(ctx, *version):
    with open("version.txt", "w") as file:
        file.write(" ".join(version))
    await ctx.send("Updated to:", version)
@bot.command()
async def version(ctx):
    with open("version.txt", "r") as file:
        currentv = file.read()
    await ctx.send("Current Version:", currentv")