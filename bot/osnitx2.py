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