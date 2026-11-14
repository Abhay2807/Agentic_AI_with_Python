# Running Multiple coroutines

import asyncio
import time

async def player_info(name):
    print(f"Displaying player: {name} information ")
    await asyncio.sleep(2)
    print(f"Player {name} info displayed")


async def main():
    await asyncio.gather(
        player_info("Rohit"),
        player_info("Kohli")
    )

start_time=time.time()
asyncio.run(main())
end_time=time.time()
print(f"Total process took {end_time - start_time:.2f} seconds..")



