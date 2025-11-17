import asyncio
import random

async def fetch_users():
    await asyncio.sleep(3)
    return [{"name": f"user{i}"} for i in range(5)]

async def fetch_products():
    await asyncio.sleep(5)
    return [{"product": f"item{i}"} for i in range(5)]

async def main():
    t1 = asyncio.create_task(fetch_users())
    t2 = asyncio.create_task(fetch_products())

    r1 = await t1
    r2 = await t2

    print([r1, r2])

asyncio.run(main())
