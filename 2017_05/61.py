plik = open('Dane_PR/dane.txt').readlines()

ciemny = 255
jasny = 0
for wiersz in plik:
    wiersz = wiersz.strip().split()
    for i in wiersz:
        if int(i) > jasny:
            jasny = int(i)
        if int(i) < ciemny:
            ciemny = int(i)

print('Zadanie 6.1')
print('Najjaśniejszy:', jasny)
print('Najciemniejszy:', ciemny)
