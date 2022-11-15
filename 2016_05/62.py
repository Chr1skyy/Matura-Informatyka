plik = open('Dane_NOWA/dane_6_2.txt').readlines()


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
    slowo = wiersz[0]
    klucz = int(wiersz[1])
    print(odszyfruj(slowo, klucz))
