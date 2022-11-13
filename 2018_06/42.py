file1 = open('NM_DANE_PR/dane1.txt').readlines()
file2 = open('NM_DANE_PR/dane2.txt').readlines()

parzyste_1 = []
parzyste_2 = []
nieparzyste_1 = []
nieparzyste_2 = []
for wiersz in file1:
    wiersz = wiersz.strip().split()
    ilosc_parzyste = 0
    ilosc_nieparzyste = 0
    for i in wiersz:
        i = int(i)
        if i % 2 == 0:
            ilosc_parzyste += 1
        if i % 2 == 1:
            ilosc_nieparzyste += 1
    parzyste_1.append(ilosc_parzyste)
    nieparzyste_1.append(ilosc_nieparzyste)

for wiersz in file2:
    wiersz = wiersz.strip().split()
    ilosc_parzyste = 0
    ilosc_nieparzyste = 0
    for i in wiersz:
        i = int(i)
        if i % 2 == 0:
            ilosc_parzyste += 1
        if i % 2 == 1:
            ilosc_nieparzyste += 1
    parzyste_2.append(ilosc_parzyste)
    nieparzyste_2.append(ilosc_nieparzyste)

ilosc = 0
for i in range(len(parzyste_1)):
    if parzyste_1[i] == 5 and parzyste_2[i] == 5 and nieparzyste_1[i] == 5 and nieparzyste_2[i] == 5:
        ilosc += 1

print('Zadanie 4.2')
print(ilosc)
