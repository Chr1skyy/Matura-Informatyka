plik = open('Dane_PR2/pary.txt').readlines()

lista = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    liczba = int(wiersz[0])
    slowo = wiersz[1]
    if liczba == len(slowo):
        lista.append((liczba, slowo))

lista = sorted(lista)

print('Zadanie 4.3')
for liczba, slowo in lista:
    print(liczba, slowo)
    break
