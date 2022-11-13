file1 = open('NM_DANE_PR/dane1.txt').readlines()
file2 = open('NM_DANE_PR/dane2.txt').readlines()

ciagi_1 = []
for wiersz in file1:
    wiersz = wiersz.strip().split()
    ciagi_1.append(wiersz)

ciagi_2 = []
for wiersz in file2:
    wiersz = wiersz.strip().split()
    ciagi_2.append(wiersz)

print('Zadanie 4.4')
for i in range(len(ciagi_1)):
    ciag = ciagi_1[i] + ciagi_2[i]
    ciag.sort(key=lambda x: int(x))
    print(' '.join(ciag))
