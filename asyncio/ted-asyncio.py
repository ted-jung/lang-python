# =============================================================================
# Title: asyncio
# Created: 22, May 2025
# Updated: 22, May 2025
# Writer: Ted, Jung
# Description:
#       함수	                         설명
#       asyncio.run(coro)	            run the main coroutine
#       asyncio.create_task(coro)	    envelop coroutin in task and run in background
#       await asyncio.sleep(sec)	    asynchronously wait
#       await asyncio.gather(*coros)	run multiple coroutin parallely
#       asyncio.wait()	                the same feature of gather() with more control
#       asyncio.get_event_loop()	    advanced control event loop
# =============================================================================


import asyncio
import aiohttp
import ssl

# Create an unverified SSL context
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

async def task(name):
    print(f"{name} 시작")
    await asyncio.sleep(1)
    print(f"{name} 끝")


async def fetch(session, url):
    async with session.get(url, ssl=ssl_context) as resp:
        return await resp.text()


async def run_agent(agent, review_text: str):
    return review_text




async def main():
    # example0 (basic)
    t1 = asyncio.create_task(task("작업1"))
    t2 = asyncio.create_task(task("작업2"))
    await t1
    await t2

    total_str = t1.get_name() + t2.get_name()
    print(total_str)


    # example1 (asyncio, aiohttp)
    urls = ["https://httpbin.org/get", "https://httpbin.org/get"]
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(fetch(session, url) for url in urls))
        for r in results:
            print(len(r))


    # example2 (multiple coroutine and wait)
    parallel_agents=["agent1", "agent2", "agent3"]
    responses = await asyncio.gather(
            *(run_agent(agent, "test") for agent in parallel_agents)
        )
    print(responses)
    

asyncio.run(main())



