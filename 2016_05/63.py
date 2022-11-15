plik = open('Dane_NOWA/dane_6_3.txt').readlines()


def odszyfruj(slowo, klucz):
    klucz = klucz % 26
    odszyfrowane = ''
    for litera in slowo:
        if ord(litera) - klucz < 65:
            x = ord(litera) - 65
            odszyfrowane += chr(91 + x - klucz)
        else:
            odszyfrowane += chr(ord(litera) - klucz)
    return odszyfrowane


for wiersz in plik:
    wiersz = wiersz.strip().split()
    klucz = 0
    x = wiersz[0][0]
    for i in range(26):
        if x == wiersz[1][0]:
            klucz = i
            break
        else:
            x = chr(ord(x)+1)
        if ord(x) > 90:
            x = chr(65)
    if odszyfruj(wiersz[1], i) != wiersz[0]:
        print(wiersz[0])
