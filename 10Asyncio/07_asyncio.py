import asyncio
import threading
import time

def worker_func():
    while True:
        time.sleep(1)
        print("Logging system health data")

async def player_data():
    await asyncio.sleep(3)
    print("fetching player's data")

threading.Thread(target= worker_func, daemon=True).start()
asyncio.run(player_data())