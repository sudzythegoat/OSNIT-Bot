import discord
from discord.ext import commands
from g4f.client import Client
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
async def search(ctx, username):
    
bot.run(token)