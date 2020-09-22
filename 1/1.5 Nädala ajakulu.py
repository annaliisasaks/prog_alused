ainepunktid = int(input("Sisestage ainepunktide arv: "))
nädal = int(input("Sisestage nädalate arv: "))

aeg = ainepunktid*26
ajakulu = round(aeg//nädal + 0.5)

print("Eeldatav ajakulu on " + ajakulu)