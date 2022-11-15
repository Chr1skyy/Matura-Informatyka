plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

suma = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[-1] == '8':
        wiersz = wiersz[:-1]
        suma += int(wiersz, 8)

print('Zadanie 6.4')
print(suma)
