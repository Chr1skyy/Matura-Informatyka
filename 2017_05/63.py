plik = open('Dane_PR/dane.txt').readlines()

mapa = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    mapa.append([int(x) for x in wiersz])

sasiedzi = ((0, 1), (0, -1), (1, 0), (-1, 0))
kontrastujace = 0
for x in range(320):
    for y in range(200):
        ile = 0
        for s in sasiedzi:
            if x + s[0] > 319 or x + s[0] < 0 or y + s[1] > 199 or y + s[1] < 0:
                continue
            if abs(mapa[y][x] - mapa[y + s[1]][x + s[0]]) > 128:
                ile += 1
        if ile != 0:
            kontrastujace += 1

print('Zadanie 6.3')
print(kontrastujace)
