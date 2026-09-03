import sys
import requests

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})
resolved = set()
# headers = {
#     "User-Agent": "Mozilla/5.0"
# }

def resolver(urls):
    for url in urls:
        if not url:
            continue
        url = url.strip()
        try:
            response = session.get(url,
                                    # headers=headers,
                                    timeout=2
                                    )
        except requests.RequestException:
            continue

        if response.status_code == 200:
            resolved.add(url)

def main():
    urls = sys.stdin
    resolver(urls)
    for r in sorted(resolved):
        print(r)

if __name__ == "__main__":
    main()