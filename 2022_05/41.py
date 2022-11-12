plik = open('Dane_2205/liczby.txt').readlines()

ilosc = 0
pierwsza = -1
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[0] == wiersz[len(wiersz) -1]:
        if pierwsza == -1:
            pierwsza = wiersz
        ilosc += 1

print('Zadanie 4.1')
print(ilosc, pierwsza)
