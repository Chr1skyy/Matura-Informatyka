plik = open('Dane_PR/liczby.txt').readlines()

podzielne_8 = 0
podzielne_2 = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    base_10 = int(wiersz, 2)
    if base_10 % 2 == 0:
        podzielne_2 += 1
    if base_10 % 8 == 0:
        podzielne_8 += 1

print('Zadanie 4.2')
print('Podzielne przez 2:', podzielne_2)
print('Podzielne przez 8:', podzielne_8)
