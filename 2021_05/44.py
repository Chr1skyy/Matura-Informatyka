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
    if liczba == 90:
        ascii = chr(65)
    else:
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
    if instrukcja == 'PRZESUN':
        przesun(litera)

haslo_cale = ''
for i in haslo:
    haslo_cale = haslo_cale + i

print('Zadanie 4.4')
print(haslo_cale)
