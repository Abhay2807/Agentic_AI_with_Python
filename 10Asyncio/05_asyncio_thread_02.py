# Using to_thread
# Python also provides a simpler way to execute blocking functions in a worker thread.

import asyncio
import time

def player_info(name):
    print(f"Searching player {name} info")
    time.sleep(3)#blocking operation
    return f"Player {name} info"

async def main():
    results = await asyncio.gather(
        asyncio.to_thread(player_info, "Rohit"),
        asyncio.to_thread(player_info, "Kohli")
    )

    for result in results:
        print(result)

asyncio.run(main())
