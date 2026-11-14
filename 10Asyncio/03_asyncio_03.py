# Fetch multiple web requests 
# Website with delay of 2 secs

import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    print(f"trying to fetch URL : {url}")
    async with session.get(url, ssl=False) as response:
        print(f"fetched the URL : {url}, with status : {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks= [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

start_time=time.time()
asyncio.run(main())
end_time=time.time()
print(f"Total process took {start_time-end_time:.3f} seconds")







