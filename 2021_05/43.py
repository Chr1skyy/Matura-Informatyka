plik = open('DANE_2105/instrukcje.txt').readlines()

litery = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    if wiersz[0] == 'DOPISZ':
        litery.append(wiersz[1])
litery.sort()

biezaca_litera = litery[0]
liczba_wystapien = 1
maks_liczba_wystapien = 0
maks_litera = ''
for i in range(0, len(litery) - 1):
    if biezaca_litera == litery[i + 1]:
        liczba_wystapien += 1
        biezaca_litera = litery[i + 1]
    else:
        biezaca_litera = litery[i + 1]
        liczba_wystapien = 1
    if liczba_wystapien > maks_liczba_wystapien:
        maks_liczba_wystapien = liczba_wystapien
        maks_litera = biezaca_litera

print('Zadanie 4.3')
print(maks_litera, maks_liczba_wystapien)
