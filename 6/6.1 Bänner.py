#f-n et tagastada suurte tähtedega
def banner(sonum):
    sonum = sonum.upper()
    return sonum

#sisendid
kordi = int(input('Mitu korda soovite reklaamlauset kuvada? '))
lause = input('Millist reklaamlauset soovite? ')

# valjastab reklaamlause vastava arvu kordi
while kordi > 0:
    print(banner(lause))
    kordi -= 1
