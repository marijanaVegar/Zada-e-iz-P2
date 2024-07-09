#zadaca 1 "ponavljanje-kolekcije"

import random


imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']


radnici = []
for i in range(15):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    satnica = round(random.uniform(4, 6), 2)
    radnik = {"ime": ime, "prezime": prezime, "satnica": satnica}
    radnici.append(radnik)


for radnik in radnici:
    radnik["tjedni_sati"] = random.randint(20, 30)


isplate = []
for radnik in radnici:
    ime = radnik["ime"]
    prezime = radnik["prezime"]
    satnica = radnik["satnica"]
    tjedni_sati = radnik["tjedni_sati"]
    isplata = round(satnica * tjedni_sati, 2)
    isplate.append((ime, prezime, isplata))


print("Podaci o radnicima:")
for ime, prezime, isplata in isplate:
    print(f"{ime} {prezime}: {isplata} kn")


ukupna_isplata = sum(isplata for _, _, isplata in isplate)
prosjecna_isplata = ukupna_isplata / len(isplate)

print("\nUkupna isplata za tjedan:", ukupna_isplata, "kn")
print("Prosječna isplata za tjedan:", prosjecna_isplata, "kn")


print("\nRadnici s isplatom iznad prosjeka:")
for ime, prezime, isplata in isplate:
    if isplata > prosjecna_isplata:
        print(f"{ime} {prezime}")


