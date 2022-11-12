plik = open('DANE/liczby.txt').readlines()

rozne = set()
wszystkie = []
for wiersz in plik:
    wiersz = wiersz.strip()
    rozne.add(wiersz)
    wszystkie.append(wiersz)

wszystkie = sorted(wszystkie)

podwojnie = 0
for i in range(0, len(wszystkie)-2):
    if wszystkie[i] == wszystkie[i+1]:
        podwojnie = podwojnie + 1
        if wszystkie[i] == wszystkie[i+2]:
            podwojnie = podwojnie - 1

potrojnie = 0
for i in range(0, len(wszystkie)-2):
    if wszystkie[i] == wszystkie[i+1] and wszystkie[i] == wszystkie[i+2]:
        potrojnie = potrojnie + 1
        i = i + 2

print('Zadanie 4.4')
print(len(rozne), podwojnie, potrojnie)
