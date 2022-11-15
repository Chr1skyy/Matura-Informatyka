plik = open('Dane_PR/dane.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip().split()
    for x in range(len(wiersz)):
        if wiersz[x] != wiersz[319-x]:
            ile += 1
            break

print('Zadanie 6.2')
print(ile)
