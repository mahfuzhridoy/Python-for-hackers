# URL Resolver

A simple and fast URL checker that reads URLs from standard input and checks them concurrently using multiple threads.

## Installation

Install the required Python package:

```bash
pip install requests
```

Make sure you are using Python 3.

## Usage

### Basic Usage

Read URLs from a file:

```bash
cat urls.txt | python3 url_resolver.py
```

By default, the tool uses **50 concurrent threads**.

### Specify Number of Threads

You can specify the number of concurrent requests using `-t` or `--threads`:

```bash
cat urls.txt | python3 url_resolver.py -t 100
```

or:

```bash
cat urls.txt | python3 url_resolver.py --threads 100
```

## What It Does

* Reads URLs from standard input.
* Sends HTTP requests to each URL.
* Uses multiple threads to check URLs concurrently.
* Prints URLs that return HTTP status code `200`.
* Uses a default of **50 threads**.
* Supports a custom number of threads with `-t` / `--threads`.
* Uses a 2-second request timeout.

## Input Example

`urls.txt`:

```text
https://example.com
https://google.com
https://github.com
```

Run:

```bash
cat urls.txt | python3 url_resolver.py
```

The tool will print URLs that successfully return HTTP `200`.
