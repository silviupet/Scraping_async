import aiohttp
import asyncio
import time

async def fetch_page(url):
    page_start = time.time()
    # este context manager - deschide o sesione dat fiind async (async contest manager) poate avea un yield
    # in the enter or in the exit method or both
    # este un mod de a suspenda executia unui context manager cand porneste sau cand se opreste si reluare apoi
    async with aiohttp.ClientSession() as session:

        # ask the server for the contents
        async with session.get(url) as response:
            print(f"It took {time.time()-page_start} for 1 page  ")
            print(response.status)
            return response.status
    # asyncio library allow us to schedule and manage the above coroutines (tasks)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_page('http://google.com'))

    #  pana aici avem o singura pagina
    # ca sa trimitem la mai multe
loop = asyncio.get_event_loop()
tasks = [fetch_page('http://google.com') for i in range(30)]
start= time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f"All pages took {time.time()-start}")
    # *tasks means unpacking lista de tasks