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
async def ip(ctx, ip_address):
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    if response.statuscode == 200:
        data = response.json
        message = (
            f"**IP Address Information**\n"
            f"IP: {data['query']}\n"
            f"City: {data.get('city', 'N/A')}\n"
            f"Region: {data.get('regionName', 'N/A')}\n"
            f"Country: {data.get('country', 'N/A')}\n"
            f"Zip code: {data.get('zip', 'N/A')}"
            f"Timezone: {data.get('timezone', 'N/A')}"
            f"ISP: {data.get('isp', 'N/A')}\n"
            f"Lat, Long: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}"
        )
        await ctx.send(message)
    else:
        await ctx.send("An error has occurred")
#end cmd
bot.run("private_token")