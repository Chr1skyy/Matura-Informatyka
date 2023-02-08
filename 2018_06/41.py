file1 = open('NM_DANE_PR/dane1.txt').readlines()
file2 = open('NM_DANE_PR/dane2.txt').readlines()

ilosc = 0
ostanie_1 = []
ostanie_2 = []
for wiersz in file1:
    wiersz = wiersz.strip().split()
    ostanie_1.append(wiersz[-1])

for wiersz in file2:
    wiersz = wiersz.strip().split()
    ostanie_2.append(wiersz[-1])

for i in range(len(ostanie_1)):
    if ostanie_1[i] == ostanie_2[i]:
        ilosc += 1

print('Zadanie 4.1')
print(ilosc)
