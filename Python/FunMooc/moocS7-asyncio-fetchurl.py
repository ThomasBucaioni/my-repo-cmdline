#!/bin/python3
import sys
import time
import requests
def sequential(urls):
    for url in urls:
        req = requests.get(url)
        print(f"{url} returned {len(req.text)} chars")

import asyncio
import aiohttp

async def fetch(url):

    async with aiohttp.ClientSession() as session:
        print(f"fetching {url}")

        async with session.get(url) as response:
            print(f"{url} response status {response.status}")
            raw = await response.read()
            print(f"{url} returned {len(raw)} bytes")

async def fetch2(url, i):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url} response status {response.status}")
            # avec ici une itération asynchrone
            async for line in response.content:
                print(f'{i}', end='')
                sys.stdout.flush()
    # dans la vidéo il y a ce return, c'est une différence
    # par rapport à la première variante mais ce n'est pas important
    return url


import argparse

default_urls = [
    "http://www.irs.gov/pub/irs-pdf/f1040.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
    "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf",
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs='*',
                        default=default_urls,
                        help="URL's to be fetched")
    parser.add_argument("-s", "--sequential", default=False, action='store_true',
                        help="run sequentially")
    parser.add_argument("-d", "--details", default=False, action='store_true',
                        help="show details of lines as they show up (using fetch2)")

    args = parser.parse_args()
    urls = args.urls

    loop = asyncio.get_event_loop()

    # mode séquentiel
    if args.sequential:
        print(f"Running sequential mode on {len(urls)} URLs")
        beg = time.time()
        sequential(urls)
        print(f"duration = {time.time()-beg}s")

    # mode asynchrone
    else:

        # sans option on utilise juste fetch
        if (not args.details):
            print(f"Running simple mode (fetch) on {len(urls)} URLs")
            jobs = (fetch(url) for url in urls)
        else:
            print(f"Running detail mode (fetch2) on {len(urls)} URLs")
            jobs = (fetch2(url, i) for i, url in enumerate(urls))
        # il n'y a plus qu'à
        beg = time.time()
        loop.run_until_complete(asyncio.gather(*jobs))
        print(f"duration = {time.time()-beg}s")

if __name__ == '__main__':
    main()

