plik = open('Dane_PR/dane.txt').readlines()

mapa = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    mapa.append([int(x) for x in wiersz])

maks_dlugosc = 0
for y in range(320):
    dlugosc = 1
    for x in range(199):
        if mapa[x][y] == mapa[x + 1][y]:
            dlugosc += 1
        else:
            if dlugosc > maks_dlugosc:
                maks_dlugosc = dlugosc
            dlugosc = 1

print('Zadanie 6.4')
print(maks_dlugosc)
