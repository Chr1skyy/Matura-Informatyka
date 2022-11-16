plik = open('MIN-R2A1P-153_dane/kody.txt').readlines()

for wiersz in plik:
    wiersz = wiersz.strip()
    suma_parzyste = 0
    suma_nieparzyste = 0
    for cyfra in range(0, len(wiersz), 2):
        suma_nieparzyste += int(wiersz[cyfra])
    for cyfra in range(1, len(wiersz), 2):
        suma_parzyste += int(wiersz[cyfra])
    print(suma_parzyste, suma_nieparzyste)
