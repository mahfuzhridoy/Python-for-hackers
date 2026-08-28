#!/usr/bin/env python3
# https://en.wikipedia.org/wiki/Programmer
import requests
import sys
from bs4 import BeautifulSoup
# from urllib import *

visited_urls = set()
headers = {
    "User-Agent": "Mozilla5/0"
}

def spider_urls(url, keyword):
    try:
        response = requests.get(url, headers=headers)
        # print(response.status_code)
    except:
        # response = requests.get(url)
        print(f"Request failed {url}")
        return

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")
        a_tag = soup.find_all("a") # returns <class 'bs4.element.ResultSet'>. need to loop for accessing the elements
        # href = a_tag.get("href")
        # print(type(a_tag))
        # urls = []
        for tag in a_tag:
            href = tag.get("href")

            if href is not None and keyword in href:
                visited_urls.add(href)

        for i in visited_urls:
            print(i)



url = sys.argv[1]
keyword = input("enter scope keyword: ")
spider_urls(url, keyword)