import requests
import json
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from googlesearch import search
class OsnitX:
    @staticmethod
    def phonelocation(number):
        parsed = phonenumbers.parse(number, None)
        location = geocoder.description_for_number(parsed, "en")
        return location
    @staticmethod
    def iplocation(ip):
        reqip = requests.get(f"http://ip-api.com/json/{ip}")
        ipinfo = reqip.json()
        returned = f'Location: {ipinfo.get["city", "N/A"]}, {ipinfo.get["region", "N/A"]}, {ipinfo.get["country", "N/A"]}'
        return returned
    @staticmethod
    def socials(name):
        actives = []
        pastebin = requests.get(f"https://pastebin.com/u/{name}")
        if not "The requested page does not exist" in pastebin.text:
            actives.append(f"https://pastebin.com/u/{name}")
        github = requests.get(f"https://github.com/{name}")
        if not "404" in github.text:
            actives.append(f"https://github.com/{name}")
        if actives:
            urls = ", ".join(actives)
            return urls
        else:
            return f"No urls found for {name}"
    @staticmethod
    def google(query):
        searches = []
        for url in search(query, num_results=10):
            searches.append(url)
        if searches:
            urls = ", ".join(searches)
            return urls
        else:
            return "Error"
    def 
