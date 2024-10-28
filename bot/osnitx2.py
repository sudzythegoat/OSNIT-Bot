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
        