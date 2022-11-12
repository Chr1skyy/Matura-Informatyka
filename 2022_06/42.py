plik = open('DANE/liczby.txt').readlines()

roznica = -1
liczba = -1
maks_roznica = -1
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    roznica = abs(int(wiersz) - int(odbicie))
    if roznica > maks_roznica:
        maks_roznica = roznica
        maks_liczba = wiersz

print('Zadanie 4.2')
print(maks_liczba, maks_roznica)
