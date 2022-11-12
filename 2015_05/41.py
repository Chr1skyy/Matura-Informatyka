plik = open('Dane_PR/liczby.txt').readlines()

ile_liczb = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    ilosc_jedynek = 0
    ilosc_zer = 0
    for litera in wiersz:
        if litera == '0':
            ilosc_zer += 1
        if litera == '1':
            ilosc_jedynek += 1
    if ilosc_zer > ilosc_jedynek:
        ile_liczb += 1

print('Zadanie 4.1')
print(ile_liczb)
