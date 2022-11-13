plik = open('Dane_PR/sygnaly.txt').readlines()

haslo = ''
for i in range(39, len(plik), 40):
    haslo += plik[i][9]

print('Zadanie 4.1')
print(haslo)
