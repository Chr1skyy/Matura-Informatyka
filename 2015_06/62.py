plik = open('MIN-R2A1P-153_dane/kody.txt').readlines()

kody_cyfr = ['10101110111010', '11101010101110', '10111010101110', '11101110101010', '10101110101110',
             '11101011101010', '10111011101010', '10101011101110', '11101010111010', '10111010111010']

for wiersz in plik:
    wiersz = wiersz.strip()
    suma_parzyste = 0
    suma_nieparzyste = 0
    for cyfra in range(0, len(wiersz), 2):
        suma_nieparzyste += int(wiersz[cyfra])
    for cyfra in range(1, len(wiersz), 2):
        suma_parzyste += int(wiersz[cyfra])
    cyfra_kontrolna = (3 * suma_parzyste + suma_nieparzyste) % 10
    cyfra_kontrolna = 10 - cyfra_kontrolna
    cyfra_kontrolna = cyfra_kontrolna % 10
    print(cyfra_kontrolna, kody_cyfr[cyfra_kontrolna])
