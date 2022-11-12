plik = open('DANE_PR/dane4.txt').readlines()

liczby = []
for wiersz in plik:
    wiersz = wiersz.strip()
    liczby.append(int(wiersz))

ciag = []
max_ciag = []
max_dlugosc = 0
dlugosc = 1
for i in range(len(liczby)-2):
    aktualna_luka = abs(liczby[i]-liczby[i+1])
    nastepna_luka = abs(liczby[i+1]-liczby[i+2])
    if aktualna_luka == nastepna_luka:
        ciag.append(liczby[i])
        dlugosc += 1
    else:
        ciag.append(liczby[i+1])
        if dlugosc > max_dlugosc:
            max_ciag = ciag
            max_dlugosc = dlugosc
        ciag = []
        dlugosc = 1

print('Zadanie 4.2')
print('Długość fragmentu:', max_dlugosc + 1)
print('Początek:', max_ciag[0])
print('Koniec', max_ciag[-1])
