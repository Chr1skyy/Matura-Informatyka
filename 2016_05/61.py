plik = open('Dane_NOWA/dane_6_1.txt').readlines()


def szyfruj(slowo, klucz):
    klucz = klucz % 26
    zaszyfrowane = ''
    for litera in slowo:
        if ord(litera) + klucz > 90:
            x = abs(90 - ord(litera) - klucz)
            zaszyfrowane += chr(64 + x)
        else:
            zaszyfrowane += chr(ord(litera) + klucz)
    return zaszyfrowane


for wiersz in plik:
    wiersz = wiersz.strip()
    print(szyfruj(wiersz, 107))
