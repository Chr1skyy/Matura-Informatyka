plik = open('Dane_PR/liczby.txt').readlines()

wynik = []
for wiersz in plik:
    wiersz = wiersz.strip()
    liczba = int(wiersz)
    suma = 0
    for i in wiersz:
        cyfra = int(i)
        silnia = 1
        for j in range(1, cyfra+1):
            silnia *= j
        suma += silnia
    if suma == liczba:
        wynik.append(liczba)

print('Zadanie 4.2')
for i in wynik:
    print(i)
