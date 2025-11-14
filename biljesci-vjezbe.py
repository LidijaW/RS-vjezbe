#dict() list() tuple() set()
lista = [1, False , "123" ,[1,2], 4.0]
print(lista)

for index , value in enumerate(lista):
    if index = -1 :
        for element in value:
            print(element)
        continue     
    print()

for broj in range (1,100):
    print(broj)


#lista vs tuple

lista =[1,2,3,4,5]

tapl=(1,2,3,4,5)

#dictionary

osoba = {
    "ime" : "Marko",
    "prezime" : "Marić",
    2 : "Pero",
    (1,2,3): False
}

# set
lista =[20,30,40,50]
skup = {1,2,3,4,5} # set

skup_iz_liste = tuple(set(lista))

print(skup)


#lambda funkcija

def kvadriraj(x):
    return x ** 2

# lambda arguments : expression
broj = 5
kvadriraj("123")

lambda x : x ** 2


#fukcija koja ce primijeniti drugu funkciju na svaki element

def primijeni_na_sve(lista : list, funkcija : callable):
    nova_lista = []
    for element in lista:
        nova_Vrijednost = funkcija(element)
        nova_lista.append(nova_Vrijednost)
    return nova_lista
    
def uvecaj_pa_kvadriraj(x):
    return (x + 1) ** 2    
lista = [1,2,3,4,5]

primijeni_na_sve()


#sintaksa
#lambda arguments : expressions if true else expression_2

#lambda izraz kvadrira ako je paran, inace kub
lista = [1,2,3,4,5]

f = lambda x : x **2 if x % 2 = 0 else x ** 3

print(f([1,2,3]))



#map 

lista = [1,2,3,4,5]


print (list(map(lambda x: x **3,lista)))

lsita_Stringova = ["pero","marko","sanja","josip"]

#sa map funkcijom napsati fn
#koja vraca listu duljina imena

studenti = [
    {"ime": "Ivan","prezime":"Ivić","jmbag": "0303077889"}
    {"ime": "Ivan","prezime":"Ivić","jmbag": "0303077889"}
    {"ime": "Ivan","prezime":"Ivić","jmbag": "0303077889"}
    {"ime": "Ivan","prezime":"Ivić","jmbag": "0303077889"}


]
      
print(list(map(lambda student: student ["jmbag"]), studenti))

print(lambda student, studenti ["jmbag"], studenti)

#filter
#expression mora bit Bool()
#filter vraca reduciranu iterable/kolekciju
#Sintaksa:
#filter(function,iterablers)

lista =[1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x: x % 2 = 0 ,lista)))



#podskup studenata koji su ispod 2001
#rezultat lista dictionarya tih studenata

putnici = [
    {"ime": "Ivan", "prezime": "Ivić", "uplata": True},
    {"ime": "Marko", "prezime": "Marković", "uplata": True},
    {"ime": "Ana", "prezime": "Anić", "uplata": False}
]

print(all(map(lambda putnik: putnik["uplata"], putnici))) # False






#asyncio vjezbe 14/11/25

def sinkrona_funkcija(param : str) -> str:
    pass

nis = sinkrona_funkcija() #none

async def korutina(param : int):
    pass

nis_korutina = korutina

print(type(korutina))

#################################################################
#korutina

import asyncio
import time

def funkcija():
    print("nesto")
    time.sleep(3)   #I/O blocking funkcija
    print("opet nesto")
    return "NEsto trece"

async def korutina(param : int):
    print(f"Korutina pozvana ... {param}")
    return param

objekt = korutina(3) # corutine object
print(type(korutina(3))) # corutine object

async def main():
    print("Pozvana main korutina ... ")
    await korutina(3)

asyncio.run(main()) # pozvali smo bez await 

###############################################################

import asyncio #non blocking I/O
import time #blocking I/0

def funkcija():
    print("nesto")
    time.sleep(3)   #I/O blocking funkcija
    print("opet nesto")
    return "NEsto trece"

asyncio.run(funkcija())


################################################################
#event loop
import asyncio #non blocking I/O
import time #blocking I/0

def funkcija():
    print("nesto")
    print(asyncio.get_event_loop())
    time.sleep(3)   #I/O blocking funkcija
    print("opet nesto")
    return "NEsto trece"

asyncio.run(funkcija())
print(asyncio.get_ebent_loop())


#sinkrono dvije funkcije

import time

def fetch_data(parametar):
    print(f"Delam nesto s {parametar}")
    time.sleep(parametar)
    print("Zavrsavam fetch_data funkciju...")
    return f"fetch_data rezultat: {parametar}" #str

def main():
    print("Izvrsavam main funkciju")
    rezultat_1 = fetch_data(3)
    rezultat_2 = fetch_data(2)
    print("Zavrsavam main funkciju...")
    return rezultat_1 , rezultat_2 #tuple(str,str)

t1 = time.perf_counter()
main()
t2 = time.perf_counter()

print(f"Vrijeme izvrsavanja je : {round(t2 - t1, 2)} sekundi ")



#korutina

import time,asyncio

async def fetch_data(parametar):
    print(f"Delam nesto s {parametar}")
    await asyncio.sleep(parametar)
    print("Zavrsavam fetch_data funkciju...")
    return "fetch_data rezultat: {parametar}" #str

async def main():
    print("Izvrsavam main funkciju")
    task_1 = asyncio.create_task(fetch_data(2))
    task_2 = asyncio.create_task(fetch_data(3)) #scheduele
    rezultat_2 = await task_2 # run
    rezultat_1 = await task_1 #run
    print("Zavrsavam main funkciju...")
    return rezultat_1 , rezultat_2 #tuple(str,str)

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()

print(f"Vrijeme izvrsavanja je : {round(t2 - t1, 2)} sekundi ")








