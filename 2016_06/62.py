plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[-1] == '4':
        if '0' not in wiersz:
            ile += 1

print('Zadanie 6.2')
print(ile)
