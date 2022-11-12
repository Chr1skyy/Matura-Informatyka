plik = open('DANE_PR/dane4.txt').readlines()

liczby = []
luki = []
for wiersz in plik:
    wiersz = wiersz.strip()
    liczby.append(int(wiersz))

for i in range(len(liczby)-1):
    luka = abs(liczby[i]-liczby[i+1])
    luki.append(luka)

print('Zadanie 4.1')
print('Maksymalna luka:', max(luki))
print('Minimalna luka:', min(luki))
