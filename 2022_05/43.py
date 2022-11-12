plik = open('Dane_2205/liczby.txt').readlines()

liczby = []
for wiersz in plik:
    wiersz = int(wiersz.strip())
    liczby.append(wiersz)

dobre_trojki = []
for i in range(0, len(liczby) - 1):
    x = liczby[i]
    for j in range(0, len(liczby) - 1):
        if j == i:
            continue
        y = liczby[j]
        if y % x == 0:
            for k in range(0, len(liczby) - 1):
                if k == j:
                    continue
                z = liczby[k]
                if y % x == 0 and z % y == 0:
                    dobre_trojki.append([x, y, z])


dobre_piatki = []
for i in range(0, len(liczby) - 1):
    n1 = liczby[i]
    for j in range(0, len(liczby) - 1):
        if j == i:
            continue
        n2 = liczby[j]
        if n2 % n1 == 0:
            for k in range(0, len(liczby) - 1):
                if k == j:
                    continue
                n3 = liczby[k]
                if n3 % n2 == 0:
                    for l in range(0, len(liczby) - 1):
                        if l == k:
                            continue
                        n4 = liczby[l]
                        if n4 % n3 == 0:
                            for m in range(0, len(liczby) - 1):
                                if m == l:
                                    continue
                                n5 = liczby[m]
                                if n5 % n4 == 0:
                                    dobre_piatki.append([n1, n2, n3, n4, n5])

print('Zadanie 4.3')
print('a) dobre trójki:', len(dobre_trojki))
for i in dobre_trojki:
    print(i[0], i[1], i[2])
print('\nb) dobre piątki:', len(dobre_piatki))
for i in dobre_piatki:
    print(i[0], i[1], i[2], i[3], i[4])
