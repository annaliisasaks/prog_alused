nimi = str(input("Sisestage oma nimi: "))
lubKiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegKiirus = int(input("Sisestage tegelik kiirus (km/h): "))
esialgneV = (tegKiirus-lubKiirus)*3
trahv= str(min(190,esialgneV))

print(nimi + ", kiiruse ületamise eest on teie trahv " + trahv + " eurot.")