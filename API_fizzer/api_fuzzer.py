#!/usr/bin/env python3
import requests
import sys
url = sys.argv[1]
wordlist = sys.argv[2]

words = open(wordlist) # why this? Because argv takes input as string, we need to convert it to contents

for i in words:
    i = i.strip()   # Required for removing unwanted characters from words like \n
    res = requests.get(url=f"{url}/{i}/")
    if res.status_code == 200:
        print(i, "\t", res.status_code)