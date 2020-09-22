inimesi = int(input("Sisesta, mitu inimest on kokku: "))
kohti = int(input("Sisesta, mitu kohta on bussis: "))

busse = str(inimesi//kohti)
ülejäävad = str(inimesi%kohti)

print("Tuleb tellida " + busse + " bussi, maha jääb " + ülejäävad + " inimest. ")
