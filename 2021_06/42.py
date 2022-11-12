plik = open('DANE/napisy.txt').readlines()

haslo = ''
i = 0
for x in range(19, len(plik), 20):
    haslo = haslo + plik[x][i]
    i += 1

print('Zadanie 4.2')
print(haslo)
