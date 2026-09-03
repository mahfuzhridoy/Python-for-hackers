#!/usr/bin/env python3
import requests # To send request and receive response from the requests
from bs4 import BeautifulSoup # For parsing the response
from urllib.parse import urljoin # Joining the url
import argparse # For adding arguments

visited_urls = set()

headers = {
    "User-Agent": "Mozilla/5.0"
}

def spider_urls(url, keyword=None):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        response = requests.get(url, headers=headers)
        
    except:
        # response = requests.get(url)
        print(f"Request failed {url}")
        print(url)
        return

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")
        a_tag = soup.find_all("a") # returns <class 'bs4.element.ResultSet'>. need to loop for accessing the elements

        for tag in a_tag:
            href = tag.get("href")

            if keyword is None:
                print("No keyword specified. Run the command again with a keyword")
                exit()

            if href is not None and keyword.lower() in href.lower():
                visited_urls.add(urljoin(url, href))

        for i in sorted(visited_urls):
            print(i)






def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--url",
                        "-u",
                        
                        help="url of the page that will be scanned. Multiple space separated urls can be added")

    
    parser.add_argument("--keyword",
                        "-k",
                        help="Keyword that will be searched in url")


    args = parser.parse_args()
    url = args.url
    keyword = args.keyword
    spider_urls(url, keyword)

if __name__ == "__main__":
    main()