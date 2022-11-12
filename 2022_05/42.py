plik = open('Dane_2205/liczby.txt').readlines()


def rozkladNaCzynniki(num):
    dzielniki = []
    i = 2
    while num != 1:
        while num % i == 0:
            num /= i
            dzielniki.append(i)
        i += 1
    return dzielniki


ilosc_dzielnikow = -1
maks_ilosc_dzielnikow = -1
maks_liczba = -1
ilosc_dzielnikow_rozne = -1
maks_ilosc_dzielnikow_rozne = -1
maks_liczba_rozne = -1

for wiersz in plik:
    wiersz = wiersz.strip()
    ilosc_dzielnikow = len(rozkladNaCzynniki(int(wiersz)))
    ilosc_dzielnikow_rozne = len(set(rozkladNaCzynniki(int(wiersz))))
    if ilosc_dzielnikow > maks_ilosc_dzielnikow:
        maks_ilosc_dzielnikow = ilosc_dzielnikow
        maks_liczba = wiersz
    if ilosc_dzielnikow_rozne > maks_ilosc_dzielnikow_rozne:
        maks_ilosc_dzielnikow_rozne = ilosc_dzielnikow_rozne
        maks_liczba_rozne = wiersz

print('Zadanie 4.2')
print('Najwięcej czynników pierwszych:', maks_ilosc_dzielnikow, maks_liczba)
print('Najwięcej różnych czynników pierwszych:', maks_ilosc_dzielnikow_rozne, maks_liczba_rozne)
