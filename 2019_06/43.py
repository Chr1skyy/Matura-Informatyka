plik = open('MIN-R2A1P-193_dane/pierwsze.txt').readlines()


def waga(x):
    suma = 0
    for i in str(x):
        suma += int(i)
    while suma >= 10:
        suma_temp = suma
        suma = 0
        for i in str(suma_temp):
            suma += int(i)
    return suma


ile = 0
pierwsze = []
for wiersz in plik:
    wiersz = wiersz.strip()
    if waga(wiersz) == 1:
        ile += 1
        pierwsze.append(wiersz)

print('Zadanie 4.3')
print(ile)
print("\nLiczby:")
for i in pierwsze:
    print(i)
