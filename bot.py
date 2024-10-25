import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="?")
infostuff = "## Welcome to Starry, and open source OSNIT discord bot\n"
@bot.command()
async def info(ctx):
    await ctx.send(infostuff)

bot.run("private_token")