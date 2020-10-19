# F-n arvutamaks kogu kuluvat raha
def eelarve(k_arv):
    sook = k_arv*10
    rent = 55
    kogusumma = sook + rent
    return kogusumma

#Sisendid
kutsutud = int(input('Mitu inimest on kutsutud? '))
tuleb = int(input('Mitu inimest tuleb? '))

#Maksimaalne
print('Maksimaalne eelarve: ' + str(eelarve(kutsutud)) + ' eurot.')

#Minimaalne
print('Minimaalne eelarve: ' + str(eelarve(tuleb)) + ' eurot.')