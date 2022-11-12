plik = open('DANE/liczby.txt').readlines()

podzielne = []
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    if int(odbicie) % 17 == 0:
        podzielne.append(odbicie)

print('Zadanie 4.1')
for i in podzielne:
    print(i)
