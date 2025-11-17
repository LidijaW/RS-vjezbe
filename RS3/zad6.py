import asyncio

async def fetch_data(param):
    print(f"Nešto radim s {param} ...")
    await asyncio.sleep(param)
    print(f"Dovršio sam s {param}.")
    return f"Rezultat {param}"

async def main():
    task = asyncio.create_task(fetch_data(2))
    print("Ovo se ispisuje odmah bez await fetch_data!")
    result = await task
    print(result)

asyncio.run(main())
