plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

max_liczba = 0
max_liczba_kod = 0
min_liczba = 999
min_liczba_kod = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    system = int(wiersz[-1])
    match system:
        case 2:
            liczba = int(wiersz[:-1], 2)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 3:
            liczba = int(wiersz[:-1], 3)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 4:
            liczba = int(wiersz[:-1], 4)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 5:
            liczba = int(wiersz[:-1], 5)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 6:
            liczba = int(wiersz[:-1], 6)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 7:
            liczba = int(wiersz[:-1], 7)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 8:
            liczba = int(wiersz[:-1], 8)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 9:
            liczba = int(wiersz[:-1], 9)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz

print('Zadanie 6.5')
print('Największa kod:', max_liczba_kod)
print('Wartość:', max_liczba)
print('Najmniejsza:', min_liczba_kod)
print('Wartość:', min_liczba)
