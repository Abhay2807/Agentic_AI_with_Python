# Multiprocesses with asyncio

import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt_data(data):
    return f" encrypted {data} "

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt_data, "Abhay Singh age is 24")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())


