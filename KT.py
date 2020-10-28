import random
# F-n arvutab inimeste koguarvu turniiril
def inimeste_arv(nk_arv, tugi_arv):
    inimesi = nk_arv*(22+tugi_arv)
    return inimesi

# Sisendid
koht = input("Kus toimub finaalturniir? ")
print("Turniir toimus", koht)
turniire = int(input("Mitu turniiri on kokku: "))

nk_arvud_turniiridel = []
loendur = 0

# Genereerib naiskondade arvud turniiride jarjendisse
while loendur < turniire:
    nk_arvud_turniiridel.append(random.randint(10, 30))
    loendur +=1

summa = 0
# Votab uhekapua jarjendist naiskondade arvud
for i in nk_arvud_turniiridel:
    if i < 15:
        tugiisikuid = 10
        print("Turniiril oli", i, "naiskondi ja vastavalt inimesi:", inimeste_arv(i, tugiisikuid))
        summa = summa + inimeste_arv(i, tugiisikuid)
    else:
        tugiisikuid = 8
        print("Turniiril oli", i, "naiskondi ja vastavalt inimesi:", inimeste_arv(i, tugiisikuid))
        summa = summa + inimeste_arv(i, tugiisikuid)

print("Turniiridel oli kokku", summa, "isikut.")





