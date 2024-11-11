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
@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/sudzythegoat/ButterLoader")
@bot.command()
async def help(ctx):
    message = (
        ".github send ButterLoader github page"
        ".version provides the current version"
        ".help displays commands"
    )
    await ctx.send(message)
@bot.command()
async def ai(ctx, *prompt):
    res = requests.get("https://tilki.dev/api/hercai?soru={prompt}")
    re = res.json()
    answer = re.get["cevap"]
    await ctx.send answer