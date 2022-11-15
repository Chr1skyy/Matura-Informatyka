plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[-1] == '2':
        wiersz = wiersz[:-1]
        if int(wiersz, 2) % 2 == 0:
            ile += 1

print('Zadanie 6.3')
print(ile)
