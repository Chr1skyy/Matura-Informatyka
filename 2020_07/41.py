plik = open('DANE/identyfikator.txt').readlines()

sumy = []
for wiersz in plik:
    wiersz = wiersz.strip()
    numer = wiersz[3:9]
    suma = 0
    for cyfra in numer:
        suma += int(cyfra)
    sumy.append(suma)

sumy = sorted(sumy)
sumy = sumy[::-1]
najwyzsza_suma = sumy[0]

najwyzsze_sumy = []
for wiersz in plik:
    wiersz = wiersz.strip()
    numer = wiersz[3:9]
    suma = 0
    for cyfra in numer:
        suma += int(cyfra)
    if suma == najwyzsza_suma:
        najwyzsze_sumy.append(wiersz)

print('Zadanie 4.1')
for i in najwyzsze_sumy:
    print(i)
