plik = open('DANE/napisy.txt').readlines()

cyfra = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    for znak in wiersz:
        if znak.isnumeric():
            cyfra = cyfra + 1

print('Zadanie 4.1')
print(cyfra)
