import discord
from discord.ext import commands
import requests
import json
from googlesearch import search
bot = commands.Bot(command_prefix="?")
@bot.command()
async def ip(ctx, ip_address):
    response = await requests.get(f"http://ip-api.com/json/{ip_address}")
    if response.statuscode == 200:
        data = response.json
        message = (
            f"**IP Address Information**\n"
            f"IP: {data['query']}\n"
            f"City: {data.get('city', 'N/A')}\n"
            f"Region: {data.get('regionName', 'N/A')}\n"
            f"Country: {data.get('country', 'N/A')}\n"
            f"Zip code: {data.get('zip', 'N/A')}\n"
            f"Timezone: {data.get('timezone', 'N/A')}\n"
            f"ISP: {data.get('isp', 'N/A')}\n"
            f"Lat, Long: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}"
        )
        await ctx.send(message)
    else:
        await ctx.send("An error has occurred")
@bot.command()
async def search(ctx, website, name):
    allowed = ["spotify.com/users", "twitter.com", "github.com"]
    if website in allowed:
        searched = await requests.get(f"https://{website}/{name}")
        if searched.text.contains("404"):
            await ctx.send(f"{name} was not found on {website}")
        else:
            await ctx.send(f"{name} found on {website} URL: https://{website}/{name}")
    else:
        await ctx.send("Must be a valid website (use ?allowed to see searchable websites)")
@bot.command()
async def allowed(ctx):
    allowed = ["spotify.com/users", "twitter.com", "github.com"]
    localmessage = "Allowed websites: spotify.com/users, twitter.com, github.com"
    await ctx.send(localmessage)
@bot.command()
async def websearch(ctx, query, urls):
    for url in search(query, num_results=urls):
        searchurl = "\n".join(url)
    urlmessage = f"Searched URLs: {searchurl}"
    await ctx.send(urlmessage)
@bot.command()
async def fullsearch(ctx, name, ip):
    response = await requests.get(f"http://ip-api.com/json/{ip}")
    if response.statuscode == 200:
        data = response.json
        query = name
        for url in search(query, num_results=10):
            prosearch = ", ".join(url)
        sspotify = await requests.get("https://spotify.com/users/{name}")
        if "404" in sspotify.text:
            spotify = "N/A"
        elif not "404" in sspotify.text:
            spotify = "https://spotify.com/users/{name}"
        
        message = (
            f"**Username Info**"
            f"Google Urls: {prosearch}"
            f"Spotify: {spotify}"
            f"**IP Address Information**\n"
            f"IP: {data['query']}\n"
            f"City: {data.get('city', 'N/A')}\n"
            f"Region: {data.get('regionName', 'N/A')}\n"
            f"Country: {data.get('country', 'N/A')}\n"
            f"Zip code: {data.get('zip', 'N/A')}\n"
            f"Timezone: {data.get('timezone', 'N/A')}\n"
            f"ISP: {data.get('isp', 'N/A')}\n"
            f"Lat, Long: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}"
        )
    else:
        await ctx.send("An error has occurred")
bot.run("private_token")
