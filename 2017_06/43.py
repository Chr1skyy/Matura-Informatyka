import math
plik = open('MIN-DANE-2017/punkty.txt').readlines()


def odleglosc(x1, x2, y1, y2):
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2))


punkty = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    x = int(wiersz[0])
    y = int(wiersz[1])
    punkty.append((x, y))

punkt1 = None
punkt2 = None
najdalej = 0

for x1, y1 in punkty:
    for x2, y2 in punkty:
        odleg = odleglosc(x1, x2, y1, y2)
        if odleg > najdalej:
            najdalej = odleg
            punkt1 = (x1, y1)
            punkt2 = (x2, y2)
print('Zadanie 4.3')
print(punkt1)
print(punkt2)
print(najdalej)
