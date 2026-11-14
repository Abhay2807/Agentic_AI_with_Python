# Asyncio and multi threading together

import asyncio
import time
# To execute computations using threads / processes in an async way
from concurrent.futures import ThreadPoolExecutor # executes the threads one by one

def player_info(name):
    print(f"Searching player {name} info")
    time.sleep(3)#blocking operation
    return f"Player {name} info"

async def main():
    loop = asyncio.get_running_loop() # designed For threads
    # async is not a replacement of threads / processes, it makes them more faster / compatible when used along
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, player_info, "Rohit")
        # run in executor > allows asyncio to run a sync function in another thread
        # runs threads in a separate thread
        # not blocking main thread, spinning up another thread
        print(result)

asyncio.run(main())

