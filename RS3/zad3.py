import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirkol23@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x',  'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032','email': 'deso032@gmail.com'},
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123',   'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic',   'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x',    'lozinka': 'S324SDFfd$234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autorizacija(korisnik, lozinka):
    await asyncio.sleep(2)
    for entry in baza_lozinka:
        if entry["korisnicko_ime"] == korisnik and entry["lozinka"] == lozinka:
            return f"Korisnik {korisnik}: Autorizacija uspješna."
    return f"Korisnik {korisnik}: Autorizacija neuspješna."


async def autentifikacija(data):
    korisnik = data["korisnicko_ime"]
    email = data["email"]
    lozinka = data["lozinka"]

    await asyncio.sleep(3)

    for entry in baza_korisnika:
        if entry["korisnicko_ime"] == korisnik and entry["email"] == email:
            t = asyncio.create_task(autorizacija(korisnik, lozinka))
            return await t

    return f"Korisnik {korisnik} nije pronađen."


async def main():
    unos = {"korisnicko_ime":"mirko123", "email":"mirkol23@gmail.com", "lozinka":"lozinka123"}
    rezultat = await autentifikacija(unos)
    print(rezultat)

asyncio.run(main())
