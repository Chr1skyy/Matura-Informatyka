plik = open('Dane_PR/liczby.txt').readlines()


def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a


liczby = []
for wiersz in plik:
    wiersz = int(wiersz.strip())
    liczby.append(wiersz)

naj_dlugosc = -1
naj_nwd = -1
naj_poczatek = -1

for i in range(0, len(liczby) - 1):
    dlugosc = 1
    poczatek = 0
    j = i
    wyraz = liczby[j]
    while nwd(wyraz, liczby[j+1]) != 1:
        dlugosc += 1
        wyraz = nwd(wyraz, liczby[j+1])
        if poczatek == 0:
            poczatek = liczby[j]
        j += 1
    if dlugosc > naj_dlugosc:
        naj_dlugosc = dlugosc
        naj_poczatek = poczatek
        naj_nwd = wyraz

print('Zadnaie 4.3')
print('Pierwsza liczba ciągu:', naj_poczatek)
print('Długość:', naj_dlugosc)
print('Największy wspólny dzielnik:', naj_nwd)
