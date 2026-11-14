# asyncio basics

import asyncio

# define coroutine

async def player_info():
    print("Preparing player's data")
    await asyncio.sleep(2) #sleep
    print("Player's  data is ready")

# running async function
asyncio.run(player_info())

