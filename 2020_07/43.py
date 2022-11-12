plik = open('DANE/identyfikator.txt').readlines()

niepoprawne = []
for wiersz in plik:
    wiersz = wiersz.strip()
    cyfra_kontrolna = int(wiersz[3:4])
    num_1 = (ord(wiersz[0]) - 55) * 7
    num_2 = (ord(wiersz[1]) - 55) * 3
    num_3 = (ord(wiersz[2]) - 55) * 1
    num_5 = int(wiersz[4]) * 7
    num_6 = int(wiersz[5]) * 3
    num_7 = int(wiersz[6]) * 1
    num_8 = int(wiersz[7]) * 7
    num_9 = int(wiersz[8]) * 3
    waga = num_1 + num_2 + num_3 + num_5 + num_6 + num_7 + num_8 + num_9
    cyfra_kontrolna_check = waga % 10
    if cyfra_kontrolna != cyfra_kontrolna_check:
        niepoprawne.append(wiersz)

print('Zadanie 4.3')
for i in niepoprawne:
    print(i)
