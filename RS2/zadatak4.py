# Zadatak 4: Klase i objekti
class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime} i imam {self.godine} godina."

osoba = Osoba("Ivan", "Ivić", 25)
print(osoba.pozdrav())

class Student(Osoba):
    def __init__(self, ime, prezime, godine, kolegiji):
        super().__init__(ime, prezime, godine)
        self.kolegiji = kolegiji
    def ispis_kolegija(self):
        return f"Moji kolegiji su: {', '.join(self.kolegiji)}."

student = Student("Marko", "Marković", 22, ["Raspodijeljeni sustavi", "Web aplikacije"])
print(student.pozdrav())
print(student.ispis_kolegija())


