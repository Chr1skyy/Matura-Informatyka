plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[-1] == '8':
        ile += 1

print('Zadanie 6.1')
print(ile)
