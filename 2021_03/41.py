plik = open('Dane_2103/galerie.txt').readlines()

galerie = dict()
for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    kraj = wiersz[0]
    galerie[kraj] = 0

for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    kraj = wiersz[0]
    galerie[kraj] = galerie[kraj] + 1

print('Zadanie 4.1')
for x in galerie.keys():
    print(x, galerie[x])
