plik = open('DANE/napisy.txt').readlines()

haslo = ''
for wiersz in plik:
    wiersz = wiersz.strip()
    num1 = -1
    num2 = -1

    for znak in wiersz:
        if znak.isdigit() and num1 == -1:
            num1 = znak
        elif znak.isdigit():
            num2 = znak

            liczba = int(num1 + num2)

            if liczba >= 65 and liczba <= 90:
                haslo += chr(liczba)

            num1 = -1
            num2 = -1

    if haslo.endswith('XXX'):
        break

print('Zadanie 4.4')
print(haslo)
