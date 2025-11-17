import asyncio

async def secure_data(osjetljivi):
    await asyncio.sleep(3)
    return {
        "prezime": hash(osjetljivi["prezime"]),
        "broj_kartice": hash(osjetljivi["broj_kartice"]),
        "CVV": hash(osjetljivi["CVV"])
    }

async def main():
    lista = [
        {"prezime":"Horvat", "broj_kartice":"1111222233334444", "CVV":"123"},
        {"prezime":"Anić",   "broj_kartice":"5555666677778888", "CVV":"321"},
        {"prezime":"Božić",  "broj_kartice":"9999000011112222", "CVV":"777"},
    ]

    tasks = [asyncio.create_task(secure_data(x)) for x in lista]

    rezultati = []
    for t in tasks:
        rezultati.append(await t)

    print(rezultati)

asyncio.run(main())
