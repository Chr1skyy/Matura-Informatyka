plik = open('DANE/identyfikator.txt').readlines()

palindromy = []
for wiersz in plik:
    wiersz = wiersz.strip()
    seria = wiersz[:3]
    numer = wiersz[3:9]
    if seria == seria[::-1] or numer == numer[::-1]:
        palindromy.append(wiersz)

print('Zadanie 4.2')
for i in palindromy:
    print(i)
