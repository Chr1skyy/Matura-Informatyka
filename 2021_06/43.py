plik = open('DANE/napisy.txt').readlines()

pozycja = -1
haslo = ''
for wiersz in plik:
    wiersz = wiersz.strip()
    op1 = wiersz + wiersz[0]
    op2 = wiersz[len(wiersz) - 1] + wiersz
    if op1 == op1[::-1]:
        haslo += op1[25]
    if op2 == op2[::-1]:
        haslo += op2[25]

print('Zadanie 4.3')
print(haslo)
