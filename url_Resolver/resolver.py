#!/usr/bin/env python3
import sys
import requests
from concurrent.futures import ThreadPoolExecutor  # For creating multiple threads
import argparse

session = requests.Session() # session creation
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})


def resolver(url):
    url = url.strip()
    try:
        response = session.get(url,
                                timeout=2
                                )
    except requests.RequestException:
        return

    if response.status_code == 200:
        print(url)

def main():
    urls = sys.stdin.readlines()


    parser = argparse.ArgumentParser()

    parser.add_argument("--threads",
                        "-t",
                        type=int,
                        default=50,
                        help="Number of concurrent requests to be sent. default treads 50"
)
    args = parser.parse_args()

    threads = args.threads

    # Creating multiple threads.

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for url in urls:
            executor.submit(resolver, url)
    

if __name__ == "__main__":
    main()