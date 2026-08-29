# URL Keyword Spider

A simple Python script that scans a webpage, extracts links (`<a>` tags), and prints URLs containing a specified keyword.

## Requirements

Make sure Python 3 is installed.

Install the required Python packages:

```bash
pip install requests beautifulsoup4
```

## Save the Script

Save the Python code as:

```text
spider.py
```

The script accepts two command-line arguments:

* `--url` / `-u` — The URL of the page to scan.
* `--keyword` / `-k` — The keyword to search for inside extracted URLs.

## Basic Usage

Run the script with:

```bash
python3 spider.py --url example.com --keyword login
```

Or using the short options:

```bash
python3 spider.py -u example.com -k login
```

### Example

```bash
python3 spider.py -u example.com -k product
```

The script will request:

```text
https://example.com
```

It will then find links on the page and print links containing `product`.

For example:

```text
https://example.com/products
https://example.com/product/123
https://example.com/product/category
```

## How It Works

The script performs the following steps:

1. Takes a domain/URL from the `--url` argument.
2. Adds `https://` to the beginning of the URL.
3. Sends an HTTP GET request using `requests`.
4. Parses the returned HTML using BeautifulSoup.
5. Finds all `<a>` elements.
6. Extracts their `href` attributes.
7. Checks whether the specified keyword exists in each `href`.
8. Converts relative URLs into absolute URLs using `urljoin()`.
9. Stores matching URLs in a `set` to avoid duplicates.
10. Prints the matching URLs.

### Example HTML

If the page contains:

```html
<a href="/login">Login</a>
<a href="/about">About</a>
<a href="https://example.com/login/reset">Reset Password</a>
```

Running:

```bash
python3 spider.py -u example.com -k login
```

could produce:

```text
https://example.com/login
https://example.com/login/reset
```

## Command-Line Arguments

### `--url` / `-u`

Specifies the webpage that will be scanned.

Example:

```bash
python3 spider.py -u example.com
```

### `--keyword` / `-k`

Specifies the keyword that should be searched for in the URLs.

Example:

```bash
python3 spider.py -u example.com -k admin
```

## Important Notes

### The URL should not include `https://`

The current script automatically adds `https://`.

Use:

```bash
python3 spider.py -u example.com -k login
```

instead of:

```bash
python3 spider.py -u https://example.com -k login
```

Otherwise, the script will construct an invalid URL:

```text
https://https://example.com
```

### Keyword Matching Is Case-Sensitive

The current code uses:

```python
if href is not None and keyword in href:
```

Therefore:

```text
Login
```

and:

```text
login
```

are considered different.

For case-insensitive matching, you could change it to:

```python
if href is not None and keyword.lower() in href.lower():
```

### Only the Initial Page Is Scanned

The current implementation scans the links found on the specified page, but it does **not** recursively visit those links.

For example:

```text
example.com
├── /about
├── /login
└── /products
```

The script examines the links on `example.com`, but it does not automatically scan `/about`, `/login`, or `/products`.

## Handling Request Failures

If the HTTP request fails, the script prints:

```text
Request failed https://example.com
https://example.com
```

This can happen because of:

* Invalid domain
* Network problems
* DNS problems
* SSL/TLS problems
* Server blocking the request
* Server requiring additional headers

## Example Workflow

### 1. Install dependencies

```bash
pip install requests beautifulsoup4
```

### 2. Save the script

```text
spider.py
```

### 3. Run it

```bash
python3 spider.py -u example.com -k login
```

### 4. View matching URLs

The matching URLs will be printed directly in the terminal.

## Recommended Improvements

For a more robust version of this tool, consider adding:

* HTTP/HTTPS URL handling
* Recursive crawling
* Maximum crawl depth
* Request timeout
* Better exception handling
* Case-insensitive keyword matching
* `robots.txt` handling
* Rate limiting
* Custom User-Agent
* Output to a file
* Multiple keywords
* Restricting results to the same domain
* Support for multiple input URLs

> **Note:** Only scan websites you own or have permission to test. Respect the site's `robots.txt`, terms of service, and reasonable request rates.
