plik = open('Dane_PR/liczby.txt').readlines()

base_10 = []
for wiersz in plik:
    wiersz = wiersz.strip()
    base_10.append(int(wiersz, 2))

najwieksza = max(base_10)
najmniejsza = min(base_10)
najwieksza_pozycja = base_10.index(najwieksza) + 1
najmniejsza_pozycja = base_10.index(najmniejsza) + 1
print('Zadanie 4.3')
print('Numer wiersza najmniejszej liczby:', najmniejsza_pozycja)
print('Numer wiersza największej liczby:', najwieksza_pozycja)
