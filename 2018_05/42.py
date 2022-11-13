plik = open('Dane_PR/przyklad.txt').readlines()

max_roznych_liter = -1
max_slowo = ''
for wiersz in plik:
    wiersz = wiersz.strip()
    rozne_litery = set()
    for litera in wiersz:
        rozne_litery.add(litera)
    if len(rozne_litery) > max_roznych_liter:
        max_roznych_liter = len(rozne_litery)
        max_slowo = wiersz

print('Zadanie 4.2')
print(max_slowo, max_roznych_liter)
