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
name = input("Alias: ")
def find(type):
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
def main():
  find(spotify)
  find(yt)
  find(github)
  find(tiktok)
  find(instagram)
  print("Valid links:")
  for url in prinvalid:
    print(url)
  print("Invalid links:")
  for url in prininvalid:
    print(url)
if __name__ == "__main__":
  main()