file1 = open('NM_DANE_PR/dane1.txt').readlines()
file2 = open('NM_DANE_PR/dane2.txt').readlines()

ciag_1 = []
ciag_2 = []
for wiersz in file1:
    wiersz = wiersz.strip().split()
    ciag_1.append(wiersz)


for wiersz in file2:
    wiersz = wiersz.strip().split()
    ciag_2.append(wiersz)

ilosc = 0
numer_wiersza = []
for i in range(len(ciag_1)):
    if set(ciag_1[i]) == set(ciag_2[i]):
        ilosc += 1
        numer_wiersza.append(i+1)

print('Zadanie 4.3')
print('Ilość:', ilosc)
print('Wiersze:', numer_wiersza)
