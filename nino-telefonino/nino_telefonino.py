def validiraj_broj_telefona(broj: str) -> dict:
    # Tablice pozivnih brojeva RH 
    fiksne = {
        "01": "Grad Zagreb i Zagrebačka županija",
        "020": "Dubrovačko-neretvanska županija",
        "021": "Splitsko-dalmatinska županija",
        "022": "Šibensko-kninska županija",
        "023": "Zadarska županija",
        "031": "Osječko-baranjska županija",
        "032": "Vukovarsko-srijemska županija",
        "033": "Virovitičko-podravska županija",
        "034": "Požeško-slavonska županija",
        "035": "Brodsko-posavska županija",
        "040": "Međimurska županija",
        "042": "Varaždinska županija",
        "043": "Bjelovarsko-bilogorska županija",
        "044": "Sisačko-moslavačka županija",
        "047": "Karlovačka županija",
        "048": "Koprivničko-križevačka županija",
        "049": "Krapinsko-zagorska županija",
        "051": "Primorsko-goranska županija",
        "052": "Istarska županija",
        "053": "Ličko-senjska županija",
    }

    mobilne = {
        "091": "A1 Hrvatska",
        "092": "Tomato",
        "095": "Telemach",
        "097": "bonbon",
        "098": "Hrvatski Telekom",
        "099": "Hrvatski Telekom",
    }

    posebne = {
        "0800": "Besplatni pozivi",
        "060": "Komercijalni pozivi",
        "061": "Glasovanje telefonom",
        "064": "Usluge s neprimjerenim sadržajem",
        "065": "Nagradne igre",
        "069": "Usluge namijenjene djeci",
        "072": "Jedinstveni pristupni broj za posebne usluge",
    }

    #  funkcija za čišćenje broja
    def ocisti_broj(b):
        dozvoljeno = "+0123456789"
        return ''.join(ch for ch in b if ch in dozvoljeno)

    broj = ocisti_broj(broj)

    # Uklanjanje međunarodnih prefiksa 
    if broj.startswith("+385"):
        broj = broj[4:]
    elif broj.startswith("00385"):
        broj = broj[5:]
    elif broj.startswith("385"):
        broj = broj[3:]
    # Ukloni vodeću nulu ako postoji
    if broj.startswith("0"):
        broj = broj[1:]

    rezultat = {
        "pozivni_broj": None,
        "broj_ostatak": None,
        "vrsta": None,
        "mjesto": None,
        "operater": None,
        "validan": False
    }

    # Pronalaženje pozivnog broja 
    svi_pozivni = list(fiksne.keys()) + list(mobilne.keys()) + list(posebne.keys())
    svi_pozivni.sort(key=len, reverse=True)  # da duži (npr. 0800) ide prije kraćih (08)

    pozivni = None
    for p in svi_pozivni:
        if broj.startswith(p):
            pozivni = p
            break

    if not pozivni:
        return rezultat  # nepoznat pozivni broj

    ostatak = broj[len(pozivni):]
    rezultat["pozivni_broj"] = pozivni
    rezultat["broj_ostatak"] = ostatak

    # Određivanje vrste i validacije 
    if pozivni in fiksne:
        rezultat["vrsta"] = "fiksna mreža"
        rezultat["mjesto"] = fiksne[pozivni]
        rezultat["operater"] = None
        if ostatak.isdigit() and len(ostatak) in (6, 7):
            rezultat["validan"] = True

    elif pozivni in mobilne:
        rezultat["vrsta"] = "mobilna mreža"
        rezultat["mjesto"] = None
        rezultat["operater"] = mobilne[pozivni]
        if ostatak.isdigit() and len(ostatak) in (6, 7):
            rezultat["validan"] = True

    elif pozivni in posebne:
        rezultat["vrsta"] = "posebne usluge"
        rezultat["mjesto"] = None
        rezultat["operater"] = None
        if ostatak.isdigit() and len(ostatak) == 6:
            rezultat["validan"] = True

    return rezultat

if __name__ == "__main__":
    print(validiraj_broj_telefona("+385 91 721 7633"))
    print(validiraj_broj_telefona("00385(01)2345678"))
    print(validiraj_broj_telefona("0800-123456"))
    print(validiraj_broj_telefona("091/234-5678"))
    print(validiraj_broj_telefona("385052123456"))

if __name__ == "__main__":
    print(validiraj_broj_telefona("+385 91 721 7633"))