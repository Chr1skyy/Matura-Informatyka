plik = open('Dane_PR/sygnaly.txt').readlines()

dobre = []
for wiersz in plik:
    wiersz = wiersz.strip()
    maksimum = 0
    minimum = ord(wiersz[0])
    for i in wiersz:
        if ord(i) > maksimum:
            maksimum = ord(i)
        if ord(i) < minimum:
            minimum = ord(i)
    if maksimum - minimum <= 10:
        dobre.append(wiersz)

print('Zadanie 4.3')
for i in dobre:
    print(i)
