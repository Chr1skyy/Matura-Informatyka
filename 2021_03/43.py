plik = open('Dane_2103/galerie.txt').readlines()

max_roznych = 0
max_roznych_miasto = ''
min_roznych = 999
min_roznych_miasto = ''

for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    miasto = wiersz[1]
    rozne = set()
    for i in range(2, len(wiersz), 2):
        if int(wiersz[i]) > 0:
            powierzchnia = int(wiersz[i]) * int(wiersz[i+1])
            rozne.add(powierzchnia)
    if len(rozne) > max_roznych:
        max_roznych = len(rozne)
        max_roznych_miasto = miasto
    if len(rozne) < min_roznych:
        min_roznych = len(rozne)
        min_roznych_miasto = miasto

print('Zadanie 4.3')
print(max_roznych_miasto, max_roznych)
print(min_roznych_miasto, min_roznych)