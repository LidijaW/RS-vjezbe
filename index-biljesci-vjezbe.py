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

print(all(map(lambda putnik: putnik["uplata"], putnici))) # Falsešš