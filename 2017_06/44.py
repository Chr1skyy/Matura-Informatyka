plik = open('MIN-DANE-2017/punkty.txt').readlines()

punkty = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    x = int(wiersz[0])
    y = int(wiersz[1])
    punkty.append((x, y))

wewnatrz = 0
bok = 0
zewnatrz = 0

for x, y in punkty:
    if x < 5000 and y < 5000:
        wewnatrz += 1
    elif x == 5000 and y <= 5000 or x <= 5000 and y == 5000:
        bok += 1
    elif x > 5000 or y > 5000:
        zewnatrz += 1

print('Zadanie 4.4')
print(wewnatrz, bok, zewnatrz)
