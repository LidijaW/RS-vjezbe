import asyncio
import random

async def fetch_numbers():
    numbers = [i for i in range(1, 11)]
    await asyncio.sleep(3)
    print("Podaci dohvaceni")
    return numbers

async def main():
    task = asyncio.create_task(fetch_numbers())
    result = await task
    print(result)

asyncio.run(main())
