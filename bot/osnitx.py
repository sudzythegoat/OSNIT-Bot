import requests
import os
import random
from colorama import Fore, Style
import time
error = "not found"
prinvalid = []
startnum = False
prininvalid = []
numcount = 0
spotify = "https://open.spotify.com/user/"
yt = "https://youtube.com/@"
github = "https://github.com/"
instagram = "https://instagram.com/"
tiktok = "https://www.tiktok.com/@"
def find(type, name):
  while True:
    global startnum, numcount
    if numcount >= 10:
      break
    time.sleep(0.5)
    url = type + name
    if startnum:
      numcount += 1
      url = type + name + str(numcount)
    check = requests.get(url)
    if "Page not found" in check.text or "This page isn't available." in check.text or "Didn’t find anything here!" in check.text or "Couldn't find this account." in check.text:
      inval = f"{Fore.RED}{url}{Style.RESET_ALL}"
      if not startnum:
        prininvalid.append(inval)
      startnum = True
    else:
      val = f"{Fore.GREEN}{url}{Style.RESET_ALL}"
      prinvalid.append(val)
      break
class osnitx:
  @staticmethod
  def general(name):
    find(spotify, name)
    find(yt, name)
    find(github, name)
    find(tiktok, name)
    find(instagram, name)
osntix = osnitx()