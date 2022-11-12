plik = open('Dane_2103/galerie.txt').readlines()

max_pow = 0
max_pow_miasto = ''
min_pow = 9999
min_pow_miasto = ''

print('Zadanie 4.2')
for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    miasto = wiersz[1]
    ilosc_lokali = 0
    powierzchnia = 0
    for lokal in range(2, len(wiersz), 2):
        if int(wiersz[lokal]) > 0:
            ilosc_lokali += 1
            powierzchnia = powierzchnia + int(wiersz[lokal]) * int(wiersz[lokal+1])
    if powierzchnia > max_pow:
        max_pow = powierzchnia
        max_pow_miasto = miasto
    if powierzchnia < min_pow:
        min_pow = powierzchnia
        min_pow_miasto = miasto
    print(miasto, powierzchnia, ilosc_lokali)
print('')
print(max_pow_miasto, max_pow)
print(min_pow_miasto, min_pow)
