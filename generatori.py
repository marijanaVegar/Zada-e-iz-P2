
#zadaca 2 "generatori"

def generiraj_parne_i_neparne(gornja_granica):
    for broj in range(gornja_granica):
        if broj % 2 == 0:
            yield broj, "parni"
        else:
            yield broj, "neparni"


gornja_granica = 10
generator = generiraj_parne_i_neparne(gornja_granica)

print(f"Parni i neparni brojevi manji od {gornja_granica}:")
for broj, tip in generator:
    print(f"{broj} je {tip}")




        
