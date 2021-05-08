import asyncio
import aiohttp
import time

async def fetch_page(session, url):
    start = time.time()
    async with session.get(url) as response:
        print(f'{url} took {time.time() - start}')
        return response.status

# merge si fara parametrul loop
async def get_multiple_pages(loop, *urls):
    tasks = []
    # merge si fara parametrul loop
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


if __name__ == '__main__':

    def main():
        loop = asyncio.get_event_loop()
        urls = [
            'http://google.com',
            'http://example.com',
            'http://tecladocode.com/blog'
        ]
        start = time.time()
        # merge si fara parametrul loop
        pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
        #este echivalent cu loop.run_until_cpmplete(asyncio.gather(*tasks) adica fe returneaza functia get_multiple_pages(urls)
        print(f'Total took {time.time() - start}')
        for page in pages:
            print(page)

    main()