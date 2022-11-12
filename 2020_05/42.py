plik = open('Dane_PR2/pary.txt').readlines()

print('Zadanie 4.2')
for wiersz in plik:
    wiersz = wiersz.strip().split()
    slowo = wiersz[1]
    fragment = slowo[0]
    najdluzszy_fragment = slowo[0]
    for i in range(1, len(slowo)):
        if slowo[i] == slowo[i-1]:
            fragment += slowo[i - 1]
        else:
            fragment = slowo[i]
        if len(fragment) > len(najdluzszy_fragment):
            najdluzszy_fragment = fragment
    print(najdluzszy_fragment, len(najdluzszy_fragment))
