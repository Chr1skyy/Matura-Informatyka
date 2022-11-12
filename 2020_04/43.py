from collections import Counter
plik = open('DANE_PR/dane4.txt').readlines()

liczby = []
luki = []
for wiersz in plik:
    wiersz = wiersz.strip()
    liczby.append(int(wiersz))

for i in range(len(liczby)-1):
    luka = abs(liczby[i]-liczby[i+1])
    luki.append(luka)

count = Counter(luki).most_common()
print('Zadanie 4.3')
print('Luka, krotność:')
for luka, krotnosc in count:
    print(luka, krotnosc)
