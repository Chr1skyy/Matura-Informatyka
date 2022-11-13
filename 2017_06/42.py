plik = open('MIN-DANE-2017/punkty.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip().split()
    x = wiersz[0]
    y = wiersz[1]
    set_x = set()
    set_y = set()
    for cyfra in x:
        set_x.add(cyfra)
    for cyfra in y:
        set_y.add(cyfra)
    if set_x == set_y:
        ile += 1

print('Zadanie 4.2')
print(ile)
