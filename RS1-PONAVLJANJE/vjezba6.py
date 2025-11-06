#suma svih parnih brojeva
suma = 0
for i in range(1,101):
    if i % 2 == 0:
        suma += i
print("suma svih parnih brojeva od 1 do 100 je:", suma)


#while
suma = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        suma += i
    i += 1
print("Suma svih parnih brojeva od 1 do 100 je:", suma)

#prvih 10 neparnih brojeva u obrnutom redolsijedu FOR
neparni =[i for i in range (1,20,2)]
neparni.reverse()
print(neparni)

#while
neparni = []
broj = 1
while len(neparni) < 10:
    if broj % 2 != 0:
        neparni.append(broj)
    broj += 1
neparni.reverse()
print(neparni)

#fibbonaccijev niz do 1000 FOR
a, b = 0, 1
print(a, b, end=" ")
for _ in range(2, 1000):
    c = a + b
    if c > 1000:
        break
    print(c, end=" ")
    a, b = b, c

# while
a, b = 0, 1
print("fibonaccijev niz do 1000:")
while a <= 1000:
    print(a, end=" ")
    a, b = b, a + b
