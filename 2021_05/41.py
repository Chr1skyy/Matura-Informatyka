plik = open('DANE_2105/instrukcje.txt').readlines()


def dopisz(x):
    haslo.append(x)


def zmien(x):
    haslo.pop()
    haslo.append(x)


def usun():
    haslo.pop()


def przesun(x):
    pos = haslo.index(x)
    liczba = ord(x)
    ascii = chr(liczba+1)
    haslo[pos] = ascii


haslo = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    instrukcja = wiersz[0]
    litera = wiersz[1]
    if instrukcja == 'DOPISZ':
        dopisz(litera)
    if instrukcja == 'ZMIEN':
        zmien(litera)
    if instrukcja == 'USUN':
        usun()
    if instrukcja == 'przesun':
        przesun(litera)

print('Zadanie 4.1')
print(len(haslo))
