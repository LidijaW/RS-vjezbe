# 1. Ova petlja nema previše smisla jer će se izvršiti samo jednom (i = 1)
for i in range(1, 2):
    print(i)
# Ispis: 1

# 2. Ova petlja ide od 10 do 1 (isključivo), korak 2 → neće ispisati ništa jer je početak > kraj
for i in range(10, 1, 2):
    print(i)
# Ispis: (ništa)

# 3. Ova petlja ide od 10 do 2 (uključivo), korak -1
for i in range(10, 1, -1):
    print(i)
# Ispis: 10, 9, 8, 7, 6, 5, 4, 3, 2
