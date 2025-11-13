# Zadatak 5: Moduli i paketi

class Student:
    def __init__(self, ime, prezime, kolegiji):
        self.ime = ime
        self.prezime = prezime
        self.kolegiji = kolegiji
    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime}."
    def ispis_kolegija(self):
        return f"Moji kolegiji su: {', '.join(self.kolegiji)}."

# operacije.py
import random
def ocjene(kolegiji):
    return {kolegij: [] for kolegij in kolegiji}
def simuliraj_ocjene(kolegiji):
    return {kolegij: [random.randint(1, 5) for _ in range(5)] for kolegij in kolegiji}

# main.py
from faculty import studenti, operacije
student = studenti.Student("Marko", "Marković", ["Raspodijeljeni sustavi", "Web aplikacije"])
print(student.pozdrav())
print(student.ispis_kolegija())
print(operacije.ocjene(student.kolegiji))
print(operacije.simuliraj_ocjene(student.kolegiji))