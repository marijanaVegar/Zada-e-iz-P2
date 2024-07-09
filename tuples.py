def ucitaj_podatke(datoteka):
    rezultati = []
    with open(datoteka, 'r', encoding='utf-8') as file:
        for line in file:
            ime, prezime, bodovi = line.strip().split(',')
            bodovi = int(bodovi)
            rezultati.append((ime, prezime, bodovi))
    return rezultati

def ispisi_polozeni(rezultati):
    print("Studenti koji su položili ispit (bodovi > 49):")
    for ime, prezime, bodovi in rezultati:
        if bodovi > 49:
            print(f"{ime} {prezime}")

def sortiraj_po_prezimenima(rezultati):
    return sorted(rezultati, key=lambda student: student[1])  # Sortiranje po prezimenima (indeks 1)

def generiraj_bodovni_rang(rezultati):
    bodovni_rangovi = {
        'Nedovoljan (0-49%)': 0,
        'Dovoljan (50-65%)': 0,
        'Dobar (65-80%)': 0,
        'Vrlo dobar (80-90%)': 0,
        'Izvrstan (90-100%)': 0
    }
    
    for ime, prezime, bodovi in rezultati:
        postotak = (bodovi / 100) * 100
        
        if postotak < 50:
            bodovni_rangovi['Nedovoljan (0-49%)'] += 1
        elif 50 <= postotak < 65:
            bodovni_rangovi['Dovoljan (50-65%)'] += 1
        elif 65 <= postotak < 80:
            bodovni_rangovi['Dobar (65-80%)'] += 1
        elif 80 <= postotak < 90:
            bodovni_rangovi['Vrlo dobar (80-90%)'] += 1
        elif 90 <= postotak <= 100:
            bodovni_rangovi['Izvrstan (90-100%)'] += 1
    
    return bodovni_rangovi

# Učitavanje podataka
rezultati = ucitaj_podatke('rezultati.csv')

# Ispis studenata koji su položili ispit (bodovi > 49)
ispisi_polozeni(rezultati)

# Sortiranje po prezimenima
sortirani_rezultati = sortiraj_po_prezimenima(rezultati)

# Ispis sortirane liste po prezimenima
print("\nSortirana lista po prezimenima:")
for ime, prezime, bodovi in sortirani_rezultati:
    print(f"{ime} {prezime}: {bodovi}")

# Generiranje novog rječnika s bodovnim rangovima
bodovni_rangovi = generiraj_bodovni_rang(rezultati)

# Ispis novog rječnika
print("\nBroj ostvarenih ocjena po bodovnom rangu:")
for rang, broj_ocjena in bodovni_rangovi.items():
    print(f"{rang}: {broj_ocjena}")
