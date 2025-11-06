def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadrzavati između 8 i 15 znakova.")
        return

    if not any(c.isupper() for c in lozinka) or not any(c.isdigit() for c in lozinka):
        print("Lozinka mora sadrzavati barem jedno veliko slovo i jedan broj.")
        return

    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadrzavati rijeci 'password' ili 'lozinka'.")
        return

    print("Lozinka je jaka!")

# Test
lozinka = input("Unesi lozinku: ")
provjera_lozinke(lozinka)
