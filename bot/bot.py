import discord
from discord.ext import commands
from g4f.client import Client
import requests
import json
token = ""
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)
client = Client()
@bot.command()
async def gpt(ctx, *, prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    gpt_response = response.choices[0].message.content
    await ctx.send(gpt_response)
@bot.command()
async def search(ctx, username):
    valids = []
    pastebin = requests.get(f"https://pastebin/u/{username}/")
    if not "The requested page does not exist" in pastebin.text:
        valids.append(f"https://pastebin/u/{username}/")
    github = requests.get(f"https://github.com/{username}")
    if not "404" in github.text:
        valids.append(f"https://github.com/{username}")
    if valids:
        message = ", ".join(valids)
        await ctx.send(message)
    else:
        await ctx.send("No profiles found")
bot.run(token)