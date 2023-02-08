## Egzamin maturalny z Informatyki Rozszerzonej
Arkusze maturalne z plikami oraz moimi rozwiazaniami. \
Discord: **Chriskyy#0181**.
### 2015
- Maj [2015_05](2015_05)
	- [Arkusz część 1](2015_05/informatyka-2015-maj-matura-rozszerzona.pdf)
	- [Arkusz część 2](2015_05/informatyka-2015-maj-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2015_05/informatyka-2015-maj-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2015_05/Dane_PR.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('Dane_PR/liczby.txt').readlines()

ile_liczb = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    ilosc_jedynek = 0
	ilosc_zer = 0
	for litera in wiersz:
        if litera == '0':
			ilosc_zer += 1
		if litera == '1':
			ilosc_jedynek += 1
	if ilosc_zer > ilosc_jedynek:
    	ile_liczb += 1

print('Zadanie 4.1')
print(ile_liczb)
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('Dane_PR/liczby.txt').readlines()

podzielne_8 = 0
podzielne_2 = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    base_10 = int(wiersz, 2)
    if base_10 % 2 == 0:
        podzielne_2 += 1
  	if base_10 % 8 == 0:
        podzielne_8 += 1

print('Zadanie 4.2')
print('Podzielne przez 2:', podzielne_2)
print('Podzielne przez 8:', podzielne_8)
```

</details>

<details>
<summary>4.3</summary>

```python
plik = open('Dane_PR/liczby.txt').readlines()

base_10 = []
for wiersz in plik:
    wiersz = wiersz.strip()
    base_10.append(int(wiersz, 2))

najwieksza = max(base_10)
najmniejsza = min(base_10)
najwieksza_pozycja = base_10.index(najwieksza) + 1
najmniejsza_pozycja = base_10.index(najmniejsza) + 1
print('Zadanie 4.3')
print('Numer wiersza najmniejszej liczby:', najmniejsza_pozycja)
print('Numer wiersza największej liczby:', najwieksza_pozycja)
```

</details>

</details>

- Czerwiec [2015_06](2015_06)
	- [Arkusz część 1](2015_06/informatyka-2015-czerwiec-matura-rozszerzona.pdf)
	- [Arkusz część 2](2015_06/informatyka-2015-czerwiec-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2015_06/informatyka-2015-czerwiec-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2015_06/MIN-R2A1P-153_dane.zip)


<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>6.1</summary>

```python
plik = open('MIN-R2A1P-153_dane/kody.txt').readlines()

for wiersz in plik:
    wiersz = wiersz.strip()
    suma_parzyste = 0
    suma_nieparzyste = 0
    for cyfra in range(0, len(wiersz), 2):
        suma_nieparzyste += int(wiersz[cyfra])
    for cyfra in range(1, len(wiersz), 2):
        suma_parzyste += int(wiersz[cyfra])
    print(suma_parzyste, suma_nieparzyste)
```

</details>

<details>
<summary>6.2</summary>

```python
plik = open('MIN-R2A1P-153_dane/kody.txt').readlines()

for wiersz in plik:
    wiersz = wiersz.strip()
    suma_parzyste = 0
    suma_nieparzyste = 0
    for cyfra in range(0, len(wiersz), 2):
        suma_nieparzyste += int(wiersz[cyfra])
    for cyfra in range(1, len(wiersz), 2):
        suma_parzyste += int(wiersz[cyfra])
    cyfra_kontrolna = (suma_parzyste + suma_nieparzyste) % 10
    cyfra_kontrolna = 10 - cyfra_kontrolna
    cyfra_kontrolna = cyfra_kontrolna % 10
    print(cyfra_kontrolna, wiersz)
```

</details>

<details>
<summary>6.3</summary>

```python
plik = open('MIN-R2A1P-153_dane/kody.txt').readlines()

for wiersz in plik:
    wiersz = wiersz.strip()
    suma_parzyste = 0
    suma_nieparzyste = 0
    kod = ''
    start = '11011010'
    stop = '11010110'
    x = '11101110101010'
    for cyfra in range(0, len(wiersz), 2):
        suma_nieparzyste += int(wiersz[cyfra])
    for cyfra in range(1, len(wiersz), 2):
        suma_parzyste += int(wiersz[cyfra])
    cyfra_kontrolna = (suma_parzyste + suma_nieparzyste) % 10
    cyfra_kontrolna = 10 - cyfra_kontrolna
    cyfra_kontrolna = cyfra_kontrolna % 10
    kod += start

    for cyfra in wiersz:
        match cyfra:
            case '0':
                kod += '10101110111010'
            case '1':
                kod += '11101010101110'
            case '2':
                kod += '10111010101110'
            case '3':
                kod += '11101110101010'
            case '4':
                kod += '10101110101110'
            case '5':
                kod += '11101011101010'
            case '6':
                kod += '10111011101010'
            case '7':
                kod += '10101011101110'
            case '8':
                kod += '11101010111010'
            case '9':
                kod += '10111010111010'

    match str(cyfra_kontrolna):
        case '0':
            kod += '10101110111010'
        case '1':
            kod += '11101010101110'
        case '2':
            kod += '10111010101110'
        case '3':
            kod += '11101110101010'
        case '4':
            kod += '10101110101110'
        case '5':
            kod += '11101011101010'
        case '6':
            kod += '10111011101010'
        case '7':
            kod += '10101011101110'
        case '8':
            kod += '11101010111010'
        case '9':
            kod += '10111010111010'
    kod += stop
    print(kod)
```

</details>

</details>

### 2016
- Maj [2016_05](2016_05)
	- [Arkusz część 1](2016_05/informatyka-2016-maj-matura-rozszerzona.pdf)
	- [Arkusz część 2](2016_05/informatyka-2016-maj-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2016_05/informatyka-2016-maj-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2016_05/Dane_NOWA.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>6.1</summary>

```python
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
```

</details>

<details>
<summary>6.2</summary>

```python
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
```

</details>

<details>
<summary>6.3</summary>

```python
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
```

</details>

</details>

- Czerwiec [2016_06](2016_06)
	- [Arkusz część 1](2016_06/informatyka-2016-czerwiec-matura-rozszerzona.pdf)
	- [Arkusz część 2](2016_06/informatyka-2016-czerwiec-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2016_06/informatyka-2016-czerwiec-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2016_06/MIN-R2A1P-163_dane.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>6.1</summary>

```python
plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[-1] == '8':
        ile += 1

print('Zadanie 6.1')
print(ile)
```

</details>

<details>
<summary>6.2</summary>

```python
plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[-1] == '4':
        if '0' not in wiersz:
            ile += 1

print('Zadanie 6.2')
print(ile)
```

</details>

<details>
<summary>6.3</summary>

```python
plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[-1] == '2':
        wiersz = wiersz[:-1]
        if int(wiersz, 2) % 2 == 0:
            ile += 1

print('Zadanie 6.3')
print(ile)
```

</details>

<details>
<summary>6.4</summary>

```python
plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

suma = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[-1] == '8':
        wiersz = wiersz[:-1]
        suma += int(wiersz, 8)

print('Zadanie 6.4')
print(suma)
```

</details>

<details>
<summary>6.5</summary>

```python
plik = open('MIN-R2A1P-163_dane/liczby.txt').readlines()

max_liczba = 0
max_liczba_kod = 0
min_liczba = 999
min_liczba_kod = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    system = int(wiersz[-1])
    match system:
        case 2:
            liczba = int(wiersz[:-1], 2)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 3:
            liczba = int(wiersz[:-1], 3)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 4:
            liczba = int(wiersz[:-1], 4)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 5:
            liczba = int(wiersz[:-1], 5)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 6:
            liczba = int(wiersz[:-1], 6)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 7:
            liczba = int(wiersz[:-1], 7)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 8:
            liczba = int(wiersz[:-1], 8)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz
        case 9:
            liczba = int(wiersz[:-1], 9)
            if liczba > max_liczba:
                max_liczba = liczba
                max_liczba_kod = wiersz
            if liczba < min_liczba:
                min_liczba = liczba
                min_liczba_kod = wiersz

print('Zadanie 6.5')
print('Największa kod:', max_liczba_kod)
print('Wartość:', max_liczba)
print('Najmniejsza:', min_liczba_kod)
print('Wartość:', min_liczba)
```

</details>

</details>

### 2017
- Maj [2017_05](2017_05)
	- [Arkusz część 1](2017_05/informatyka-2017-maj-matura-rozszerzona.pdf)
	- [Arkusz część 2](2017_05/informatyka-2017-maj-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2017_05/informatyka-2017-maj-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2017_05/Dane_PR.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>6.1</summary>

```python
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
```

</details>

<details>
<summary>6.2</summary>

```python
plik = open('Dane_PR/dane.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip().split()
    for x in range(len(wiersz)):
        if wiersz[x] != wiersz[319-x]:
            ile += 1
            break

print('Zadanie 6.2')
print(ile)
```

</details>

<details>
<summary>6.3</summary>

```python
plik = open('Dane_PR/dane.txt').readlines()

mapa = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    mapa.append([int(x) for x in wiersz])

sasiedzi = ((0, 1), (0, -1), (1, 0), (-1, 0))
kontrastujace = 0
for x in range(320):
    for y in range(200):
        ile = 0
        for s in sasiedzi:
            if x + s[0] > 319 or x + s[0] < 0 or y + s[1] > 199 or y + s[1] < 0:
                continue
            if abs(mapa[y][x] - mapa[y + s[1]][x + s[0]]) > 128:
                ile += 1
        if ile != 0:
            kontrastujace += 1

print('Zadanie 6.3')
print(kontrastujace)
```

</details>

<details>
<summary>6.4</summary>

```python
plik = open('Dane_PR/dane.txt').readlines()

mapa = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    mapa.append([int(x) for x in wiersz])

maks_dlugosc = 0
for y in range(320):
    dlugosc = 1
    for x in range(199):
        if mapa[x][y] == mapa[x + 1][y]:
            dlugosc += 1
        else:
            if dlugosc > maks_dlugosc:
                maks_dlugosc = dlugosc
            dlugosc = 1

print('Zadanie 6.4')
print(maks_dlugosc)
```

</details>

</details>

- Czerwiec [2017_06](2017_06)
	- [Arkusz część 1](2017_06/informatyka-2017-czerwiec-matura-rozszerzona.pdf)
	- [Arkusz część 2](2017_06/informatyka-2017-czerwiec-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2017_06/informatyka-2017-czerwiec-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2017_06/MIN-DANE-2017.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('MIN-DANE-2017/punkty.txt').readlines()


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


ile = 0
for wiersz in plik:
    wiersz = wiersz.strip().split()
    x = int(wiersz[0])
    y = int(wiersz[1])
    if isPrime(x) and isPrime(y):
        ile += 1

print('Zadanie 4.1')
print(ile)
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('MIN-DANE-2017/punkty.txt').readlines()

ile = 0
for wiersz in plik:
    wiersz = wiersz.strip().split()
    x = wiersz[0]
    y = wiersz[1]
    set_x = set()
    set_y = set()
    for cyfra in x:
        set_x.add(cyfra)
    for cyfra in y:
        set_y.add(cyfra)
    if set_x == set_y:
        ile += 1

print('Zadanie 4.2')
print(ile)
```

</details>

<details>
<summary>4.3</summary>

```python
import math
plik = open('MIN-DANE-2017/punkty.txt').readlines()


def odleglosc(x1, x2, y1, y2):
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2))


punkty = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    x = int(wiersz[0])
    y = int(wiersz[1])
    punkty.append((x, y))

punkt1 = None
punkt2 = None
najdalej = 0

for x1, y1 in punkty:
    for x2, y2 in punkty:
        odleg = odleglosc(x1, x2, y1, y2)
        if odleg > najdalej:
            najdalej = odleg
            punkt1 = (x1, y1)
            punkt2 = (x2, y2)
print('Zadanie 4.3')
print(punkt1)
print(punkt2)
print(najdalej)
```

</details>

<details>
<summary>4.4</summary>

```python
plik = open('MIN-DANE-2017/punkty.txt').readlines()

punkty = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    x = int(wiersz[0])
    y = int(wiersz[1])
    punkty.append((x, y))

wewnatrz = 0
bok = 0
zewnatrz = 0

for x, y in punkty:
    if x < 5000 and y < 5000:
        wewnatrz += 1
    elif x == 5000 and y <= 5000 or x <= 5000 and y == 5000:
        bok += 1
    elif x > 5000 or y > 5000:
        zewnatrz += 1

print('Zadanie 4.4')
print(wewnatrz, bok, zewnatrz)
```

</details>

</details>

### 2018
- Maj [2018_05](2018_05)
	- [Arkusz część 1](2018_05/informatyka-2018-maj-matura-rozszerzona.pdf)
	- [Arkusz część 2](2018_05/informatyka-2018-maj-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2018_05/informatyka-2018-maj-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2018_05/Dane_PR.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('Dane_PR/sygnaly.txt').readlines()

haslo = ''
for i in range(39, len(plik), 40):
    haslo += plik[i][9]

print('Zadanie 4.1')
print(haslo)
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('Dane_PR/przyklad.txt').readlines()

max_roznych_liter = -1
max_slowo = ''
for wiersz in plik:
    wiersz = wiersz.strip()
    rozne_litery = set()
    for litera in wiersz:
        rozne_litery.add(litera)
    if len(rozne_litery) > max_roznych_liter:
        max_roznych_liter = len(rozne_litery)
        max_slowo = wiersz

print('Zadanie 4.2')
print(max_slowo, max_roznych_liter)
```

</details>

<details>
<summary>4.3</summary>

```python
plik = open('Dane_PR/sygnaly.txt').readlines()

dobre = []
for wiersz in plik:
    wiersz = wiersz.strip()
    maksimum = 0
    minimum = ord(wiersz[0])
    for i in wiersz:
        if ord(i) > maksimum:
            maksimum = ord(i)
        if ord(i) < minimum:
            minimum = ord(i)
    if maksimum - minimum <= 10:
        dobre.append(wiersz)

print('Zadanie 4.3')
for i in dobre:
    print(i)
```

</details>

</details>

- Czerwiec [2018_06](2018_06)
	- [Arkusz część 1](2018_06/informatyka-2018-czerwiec-matura-rozszerzona.pdf)
	- [Arkusz część 2](2018_06/informatyka-2018-czerwiec-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2018_06/informatyka-2018-czerwiec-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2018_06/NM_DANE_PR.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
file1 = open('NM_DANE_PR/dane1.txt').readlines()
file2 = open('NM_DANE_PR/dane2.txt').readlines()

ilosc = 0
ostanie_1 = []
ostanie_2 = []
for wiersz in file1:
    wiersz = wiersz.strip().split()
    ostanie_1.append(wiersz[-1])

for wiersz in file2:
    wiersz = wiersz.strip().split()
    ostanie_2.append(wiersz[-1])

for i in range(len(ostanie_1)):
    if ostanie_1[i] == ostanie_2[i]:
        ilosc += 1

print('Zadanie 4.1')
print(ilosc)
```

</details>

<details>
<summary>4.2</summary>

```python
file1 = open('NM_DANE_PR/dane1.txt').readlines()
file2 = open('NM_DANE_PR/dane2.txt').readlines()

parzyste_1 = []
parzyste_2 = []
nieparzyste_1 = []
nieparzyste_2 = []
for wiersz in file1:
    wiersz = wiersz.strip().split()
    ilosc_parzyste = 0
    ilosc_nieparzyste = 0
    for i in wiersz:
        i = int(i)
        if i % 2 == 0:
            ilosc_parzyste += 1
        if i % 2 == 1:
            ilosc_nieparzyste += 1
    parzyste_1.append(ilosc_parzyste)
    nieparzyste_1.append(ilosc_nieparzyste)

for wiersz in file2:
    wiersz = wiersz.strip().split()
    ilosc_parzyste = 0
    ilosc_nieparzyste = 0
    for i in wiersz:
        i = int(i)
        if i % 2 == 0:
            ilosc_parzyste += 1
        if i % 2 == 1:
            ilosc_nieparzyste += 1
    parzyste_2.append(ilosc_parzyste)
    nieparzyste_2.append(ilosc_nieparzyste)

ilosc = 0
for i in range(len(parzyste_1)):
    if parzyste_1[i] == 5 and parzyste_2[i] == 5 and nieparzyste_1[i] == 5 and nieparzyste_2[i] == 5:
        ilosc += 1

print('Zadanie 4.2')
print(ilosc)
```

</details>

<details>
<summary>4.3</summary>

```python
file1 = open('NM_DANE_PR/dane1.txt').readlines()
file2 = open('NM_DANE_PR/dane2.txt').readlines()

ciag_1 = []
ciag_2 = []
for wiersz in file1:
    wiersz = wiersz.strip().split()
    ciag_1.append(wiersz)


for wiersz in file2:
    wiersz = wiersz.strip().split()
    ciag_2.append(wiersz)

ilosc = 0
numer_wiersza = []
for i in range(len(ciag_1)):
    if set(ciag_1[i]) == set(ciag_2[i]):
        ilosc += 1
        numer_wiersza.append(i+1)

print('Zadanie 4.3')
print('Ilość:', ilosc)
print('Wiersze:', numer_wiersza)
```

</details>

<details>
<summary>4.4</summary>

```python
file1 = open('NM_DANE_PR/dane1.txt').readlines()
file2 = open('NM_DANE_PR/dane2.txt').readlines()

ciagi_1 = []
for wiersz in file1:
    wiersz = wiersz.strip().split()
    ciagi_1.append(wiersz)

ciagi_2 = []
for wiersz in file2:
    wiersz = wiersz.strip().split()
    ciagi_2.append(wiersz)

print('Zadanie 4.4')
for i in range(len(ciagi_1)):
    ciag = ciagi_1[i] + ciagi_2[i]
    ciag.sort(key=lambda x: int(x))
    print(' '.join(ciag))
```

</details>

</details>

### 2019
- Maj [2019_05](2019_05)
	- [Arkusz część 1](2019_05/informatyka-2019-maj-matura-rozszerzona.pdf)
	- [Arkusz część 2](2019_05/informatyka-2019-maj-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2019_05/informatyka-2019-maj-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2019_05/Dane_PR.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
file1 = open('NM_DANE_PR/dane1.txt').readlines()
file2 = open('NM_DANE_PR/dane2.txt').readlines()

ciagi_1 = []
for wiersz in file1:
    wiersz = wiersz.strip().split()
    ciagi_1.append(wiersz)

ciagi_2 = []
for wiersz in file2:
    wiersz = wiersz.strip().split()
    ciagi_2.append(wiersz)

print('Zadanie 4.4')
for i in range(len(ciagi_1)):
    ciag = ciagi_1[i] + ciagi_2[i]
    ciag.sort(key=lambda x: int(x))
    print(' '.join(ciag))
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('Dane_PR/liczby.txt').readlines()

wynik = []
for wiersz in plik:
    wiersz = wiersz.strip()
    liczba = int(wiersz)
    suma = 0
    for i in wiersz:
        cyfra = int(i)
        silnia = 1
        for j in range(1, cyfra+1):
            silnia *= j
        suma += silnia
    if suma == liczba:
        wynik.append(liczba)

print('Zadanie 4.2')
for i in wynik:
    print(i)
```

</details>

<details>
<summary>4.3</summary>

```python
plik = open('Dane_PR/liczby.txt').readlines()


def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a


liczby = []
for wiersz in plik:
    wiersz = int(wiersz.strip())
    liczby.append(wiersz)

naj_dlugosc = -1
naj_nwd = -1
naj_poczatek = -1

for i in range(0, len(liczby) - 1):
    dlugosc = 1
    poczatek = 0
    j = i
    wyraz = liczby[j]
    while nwd(wyraz, liczby[j+1]) != 1:
        dlugosc += 1
        wyraz = nwd(wyraz, liczby[j+1])
        if poczatek == 0:
            poczatek = liczby[j]
        j += 1
    if dlugosc > naj_dlugosc:
        naj_dlugosc = dlugosc
        naj_poczatek = poczatek
        naj_nwd = wyraz

print('Zadnaie 4.3')
print('Pierwsza liczba ciągu:', naj_poczatek)
print('Długość:', naj_dlugosc)
print('Największy wspólny dzielnik:', naj_nwd)
```

</details>

</details>

- Czerwiec [2019_06](2019_06)
	- [Arkusz część 1](2019_06/informatyka-2019-czerwiec-matura-rozszerzona.pdf)
	- [Arkusz część 2](2019_06/informatyka-2019-czerwiec-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2019_06/informatyka-2019-czerwiec-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2019_06/MIN-R2A1P-193_dane.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('MIN-R2A1P-193_dane/liczby.txt').readlines()


def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


print('Zadanie 4.1')
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    if int(wiersz) >= 100 and int(wiersz) <= 5000:
        if isPrime(int(wiersz)):
            print(wiersz)
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('MIN-R2A1P-193_dane/pierwsze.txt').readlines()


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print('Zadanie 4.2')
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    if isPrime(int(wiersz)) and isPrime(int(odbicie)):
        print(wiersz)
```

</details>

<details>
<summary>6.3</summary>

```python
plik = open('MIN-R2A1P-193_dane/pierwsze.txt').readlines()


def waga(x):
    suma = 0
    for i in str(x):
        suma += int(i)
    while suma >= 10:
        suma_temp = suma
        suma = 0
        for i in str(suma_temp):
            suma += int(i)
    return suma


ile = 0
pierwsze = []
for wiersz in plik:
    wiersz = wiersz.strip()
    if waga(wiersz) == 1:
        ile += 1
        pierwsze.append(wiersz)

print('Zadanie 4.3')
print(ile)
print("\nLiczby:")
for i in pierwsze:
    print(i)
```

</details>

</details>

### 2020
- Kwiecień (próbna) [2020_04](2020_04)
	- [Arkusz część 1](2020_04/informatyka-2020-kwiecien-probna-rozszerzona.pdf)
	- [Arkusz część 2](2020_04/informatyka-2020-kwiecien-probna-rozszerzona-2.pdf)
	- [Odpowiedzi](2020_04/informatyka-2020-kwiecien-probna-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2020_04/DANE_PR.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('DANE_PR/dane4.txt').readlines()

liczby = []
luki = []
for wiersz in plik:
    wiersz = wiersz.strip()
    liczby.append(int(wiersz))

for i in range(len(liczby)-1):
    luka = abs(liczby[i]-liczby[i+1])
    luki.append(luka)

print('Zadanie 4.1')
print('Maksymalna luka:', max(luki))
print('Minimalna luka:', min(luki))
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('DANE_PR/dane4.txt').readlines()

liczby = []
for wiersz in plik:
    wiersz = wiersz.strip()
    liczby.append(int(wiersz))

ciag = []
max_ciag = []
max_dlugosc = 0
dlugosc = 1
for i in range(len(liczby)-2):
    aktualna_luka = abs(liczby[i]-liczby[i+1])
    nastepna_luka = abs(liczby[i+1]-liczby[i+2])
    if aktualna_luka == nastepna_luka:
        ciag.append(liczby[i])
        dlugosc += 1
    else:
        ciag.append(liczby[i+1])
        if dlugosc > max_dlugosc:
            max_ciag = ciag
            max_dlugosc = dlugosc
        ciag = []
        dlugosc = 1

print('Zadanie 4.2')
print('Długość fragmentu:', max_dlugosc + 1)
print('Początek:', max_ciag[0])
print('Koniec', max_ciag[-1])
```

</details>

<details>
<summary>4.3</summary>

```python
from collections import Counter
plik = open('DANE_PR/dane4.txt').readlines()

liczby = []
luki = []
for wiersz in plik:
    wiersz = wiersz.strip()
    liczby.append(int(wiersz))

for i in range(len(liczby)-1):
    luka = abs(liczby[i]-liczby[i+1])
    luki.append(luka)

count = Counter(luki).most_common()
print('Zadanie 4.3')
print('Luka, krotność:')
for luka, krotnosc in count:
    print(luka, krotnosc)
```

</details>

</details>

- Maj [2020_05](2020_05)
	- [Arkusz część 1](2020_05/informatyka-2020-maj-matura-rozszerzona.pdf)
	- [Arkusz część 2](2020_05/informatyka-2020-maj-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2020_05/informatyka-2020-maj-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2020_05/Dane_PR2.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('Dane_PR2/pary.txt').readlines()


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print('Zadanie 4.1')
for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    liczba = int(wiersz[0])
    for i in range(3, liczba):
        roznica = liczba - i
        if isPrime(i) and isPrime(roznica) and roznica != 2:
            if i < roznica:
                print(liczba, i, roznica)
            else:
                print(liczba, roznica, i)
            break
```

</details>

<details>
<summary>4.2</summary>

```python
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
```

</details>

<details>
<summary>4.3</summary>

```python
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
```

</details>

</details>

- Lipiec [2020_07](2020_07)
	- [Arkusz część 1](2020_07/informatyka-2020-lipiec-matura-rozszerzona.pdf)
	- [Arkusz część 2](2020_07/informatyka-2020-lipiec-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2020_07/informatyka-2020-lipiec-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2020_07/DANE.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('DANE/identyfikator.txt').readlines()

sumy = []
for wiersz in plik:
    wiersz = wiersz.strip()
    numer = wiersz[3:9]
    suma = 0
    for cyfra in numer:
        suma += int(cyfra)
    sumy.append(suma)

najwyzsze_sumy = []
for wiersz in plik:
    wiersz = wiersz.strip()
    numer = wiersz[3:9]
    suma = 0
    for cyfra in numer:
        suma += int(cyfra)
    if suma == max(sumy):
        najwyzsze_sumy.append(wiersz)

print('Zadanie 4.1')
for i in najwyzsze_sumy:
     print(i)
```

</details>

<details>
<summary>4.2</summary>

```python
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
```

</details>

<details>
<summary>4.3</summary>

```python
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
```

</details>

</details>

### 2021
- Marzec (próbna) [2021_03](2021_03)
	- [Arkusz część 1](2021_03/informatyka-2021-marzec-probna-rozszerzona.pdf)
	- [Arkusz część 2](2021_03/informatyka-2021-marzec-probna-rozszerzona-2.pdf)
	- [Odpowiedzi](2021_03/informatyka-2021-marzec-probna-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2021_03/Dane_2103.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('Dane_2103/galerie.txt').readlines()

galerie = dict()
for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    kraj = wiersz[0]
    galerie[kraj] = 0

for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    kraj = wiersz[0]
    galerie[kraj] = galerie[kraj] + 1

print('Zadanie 4.1')
for x in galerie.keys():
    print(x, galerie[x])
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('Dane_2103/galerie.txt').readlines()

max_pow = 0
max_pow_miasto = ''
min_pow = 9999
min_pow_miasto = ''

print('Zadanie 4.2')
for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    miasto = wiersz[1]
    ilosc_lokali = 0
    powierzchnia = 0
    for lokal in range(2, len(wiersz), 2):
        if int(wiersz[lokal]) > 0:
            ilosc_lokali += 1
            powierzchnia = powierzchnia + int(wiersz[lokal]) * int(wiersz[lokal+1])
    if powierzchnia > max_pow:
        max_pow = powierzchnia
        max_pow_miasto = miasto
    if powierzchnia < min_pow:
        min_pow = powierzchnia
        min_pow_miasto = miasto
    print(miasto, powierzchnia, ilosc_lokali)
print('')
print(max_pow_miasto, max_pow)
print(min_pow_miasto, min_pow)
```

</details>

<details>
<summary>4.3</summary>

```python
plik = open('Dane_2103/galerie.txt').readlines()

max_roznych = 0
max_roznych_miasto = ''
min_roznych = 999
min_roznych_miasto = ''

for wiersz in plik:
    wiersz = wiersz.strip().split(' ')
    miasto = wiersz[1]
    rozne = set()
    for i in range(2, len(wiersz), 2):
        if int(wiersz[i]) > 0:
            powierzchnia = int(wiersz[i]) * int(wiersz[i+1])
            rozne.add(powierzchnia)
    if len(rozne) > max_roznych:
        max_roznych = len(rozne)
        max_roznych_miasto = miasto
    if len(rozne) < min_roznych:
        min_roznych = len(rozne)
        min_roznych_miasto = miasto

print('Zadanie 4.3')
print(max_roznych_miasto, max_roznych)
print(min_roznych_miasto, min_roznych)
```

</details>

</details>

- Maj [2021_05](2021_05)
	- [Arkusz część 1](2021_05/informatyka-2021-maj-matura-rozszerzona.pdf)
	- [Arkusz część 2](2021_05/informatyka-2021-maj-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2021_05/informatyka-2021-maj-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2021_05/DANE_2105.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('DANE_2105/instrukcje.txt').readlines()


def dopisz(x):
    haslo.append(x)


def zmien(x):
    haslo.pop()
    haslo.append(x)


def usun():
    haslo.pop()


def przesun(x):
    pos = haslo.index(x)
    liczba = ord(x)
    ascii = chr(liczba+1)
    haslo[pos] = ascii


haslo = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    instrukcja = wiersz[0]
    litera = wiersz[1]
    if instrukcja == 'DOPISZ':
        dopisz(litera)
    if instrukcja == 'ZMIEN':
        zmien(litera)
    if instrukcja == 'USUN':
        usun()
    if instrukcja == 'przesun':
        przesun(litera)

print('Zadanie 4.1')
print(len(haslo))
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('DANE_2105/instrukcje.txt').readlines()

instrukcje = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    instrukcje.append(wiersz[0])

biezaca_instrukcja = instrukcje[1]
biezacy_streak = 1
maks_streak = 0
streak_instrukcja = ''

for i in range(0, len(instrukcje) -1):
    if biezaca_instrukcja == instrukcje[i + 1]:
        biezaca_instrukcja = instrukcje[i + 1]
        biezacy_streak += 1
    else:
        biezaca_instrukcja = instrukcje[i + 1]
        biezacy_streak = 1
    if biezacy_streak > maks_streak:
        maks_streak = biezacy_streak
        streak_instrukcja = biezaca_instrukcja

print('Zadanie 4.2')
print(streak_instrukcja, maks_streak)
```

</details>

<details>
<summary>4.3</summary>

```python
plik = open('DANE_2105/instrukcje.txt').readlines()

litery = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    if wiersz[0] == 'DOPISZ':
        litery.append(wiersz[1])
litery.sort()

biezaca_litera = litery[0]
liczba_wystapien = 1
maks_liczba_wystapien = 0
maks_litera = ''
for i in range(0, len(litery) - 1):
    if biezaca_litera == litery[i + 1]:
        liczba_wystapien += 1
        biezaca_litera = litery[i + 1]
    else:
        biezaca_litera = litery[i + 1]
        liczba_wystapien = 1
    if liczba_wystapien > maks_liczba_wystapien:
        maks_liczba_wystapien = liczba_wystapien
        maks_litera = biezaca_litera

print('Zadanie 4.3')
print(maks_litera, maks_liczba_wystapien)
```

</details>

<details>
<summary>4.4</summary>

```python
plik = open('DANE_2105/instrukcje.txt').readlines()


def dopisz(x):
    haslo.append(x)


def zmien(x):
    haslo.pop()
    haslo.append(x)


def usun():
    haslo.pop()


def przesun(x):
    pos = haslo.index(x)
    liczba = ord(x)
    if liczba == 90:
        ascii = chr(65)
    else:
        ascii = chr(liczba+1)
    haslo[pos] = ascii


haslo = []
for wiersz in plik:
    wiersz = wiersz.strip().split()
    instrukcja = wiersz[0]
    litera = wiersz[1]
    if instrukcja == 'DOPISZ':
        dopisz(litera)
    if instrukcja == 'ZMIEN':
        zmien(litera)
    if instrukcja == 'USUN':
        usun()
    if instrukcja == 'PRZESUN':
        przesun(litera)

haslo_cale = ''
for i in haslo:
    haslo_cale = haslo_cale + i

print('Zadanie 4.4')
print(haslo_cale)
```

</details>

</details>

- Czerwiec [2021_06](2021_06)
	- [Arkusz część 1](2021_06/informatyka-2021-czerwiec-matura-rozszerzona.pdf)
	- [Arkusz część 2](2021_06/informatyka-2021-czerwiec-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2021_06/informatyka-2021-czerwiec-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2021_06/DANE.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('DANE/napisy.txt').readlines()

cyfra = 0
for wiersz in plik:
    wiersz = wiersz.strip()
    for znak in wiersz:
        if znak.isnumeric():
            cyfra = cyfra + 1

print('Zadanie 4.1')
print(cyfra)
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('DANE/napisy.txt').readlines()

haslo = ''
i = 0
for x in range(19, len(plik), 20):
    haslo = haslo + plik[x][i]
    i += 1

print('Zadanie 4.2')
print(haslo)
```

</details>

<details>
<summary>4.3</summary>

```python
plik = open('DANE/napisy.txt').readlines()

pozycja = -1
haslo = ''
for wiersz in plik:
    wiersz = wiersz.strip()
    op1 = wiersz + wiersz[0]
    op2 = wiersz[len(wiersz) - 1] + wiersz
    if op1 == op1[::-1]:
        haslo += op1[25]
    if op2 == op2[::-1]:
        haslo += op2[25]

print('Zadanie 4.3')
print(haslo)
```

</details>

<details>
<summary>4.4</summary>

```python
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
```

</details>

</details>

### 2022
- Maj [2022_05](2022_05)
	- [Arkusz część 1](2022_05/informatyka-2022-maj-matura-rozszerzona.pdf)
	- [Arkusz część 2](2022_05/informatyka-2022-maj-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2022_05/informatyka-2022-maj-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2022_05/Dane_2205.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('Dane_2205/liczby.txt').readlines()

ilosc = 0
pierwsza = -1
for wiersz in plik:
    wiersz = wiersz.strip()
    if wiersz[0] == wiersz[len(wiersz) -1]:
        if pierwsza == -1:
            pierwsza = wiersz
        ilosc += 1

print('Zadanie 4.1')
print(ilosc, pierwsza)
```

</details>

<details>
<summary>4.2</summary>

```python
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
```

</details>

<details>
<summary>4.3</summary>

```python
plik = open('Dane_2205/liczby.txt').readlines()

liczby = []
for wiersz in plik:
    wiersz = int(wiersz.strip())
    liczby.append(wiersz)

dobre_trojki = []
for i in range(0, len(liczby) - 1):
    x = liczby[i]
    for j in range(0, len(liczby) - 1):
        if j == i:
            continue
        y = liczby[j]
        if y % x == 0:
            for k in range(0, len(liczby) - 1):
                if k == j:
                    continue
                z = liczby[k]
                if y % x == 0 and z % y == 0:
                    dobre_trojki.append([x, y, z])


dobre_piatki = []
for i in range(0, len(liczby) - 1):
    n1 = liczby[i]
    for j in range(0, len(liczby) - 1):
        if j == i:
            continue
        n2 = liczby[j]
        if n2 % n1 == 0:
            for k in range(0, len(liczby) - 1):
                if k == j:
                    continue
                n3 = liczby[k]
                if n3 % n2 == 0:
                    for l in range(0, len(liczby) - 1):
                        if l == k:
                            continue
                        n4 = liczby[l]
                        if n4 % n3 == 0:
                            for m in range(0, len(liczby) - 1):
                                if m == l:
                                    continue
                                n5 = liczby[m]
                                if n5 % n4 == 0:
                                    dobre_piatki.append([n1, n2, n3, n4, n5])

print('Zadanie 4.3')
print('a) dobre trójki:', len(dobre_trojki))
for i in dobre_trojki:
    print(i[0], i[1], i[2])
print('\nb) dobre piątki:', len(dobre_piatki))
for i in dobre_piatki:
    print(i[0], i[1], i[2], i[3], i[4])
```

</details>

</details>

- Czerwiec [2022_06](2022_06)
	- [Arkusz część 1](2022_06/informatyka-2022-czerwiec-matura-rozszerzona.pdf)
	- [Arkusz część 2](2022_06/informatyka-2022-czerwiec-matura-rozszerzona-2.pdf)
	- [Odpowiedzi](2022_06/informatyka-2022-czerwiec-matura-rozszerzona-odpowiedzi.pdf)
	- [Dane ZIP](2022_06/DANE.zip)

<details>
<summary>Rozwiązanie Python</summary>

<details>
<summary>4.1</summary>

```python
plik = open('DANE/liczby.txt').readlines()

podzielne = []
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    if int(odbicie) % 17 == 0:
        podzielne.append(odbicie)

print('Zadanie 4.1')
for i in podzielne:
    print(i)
```

</details>

<details>
<summary>4.2</summary>

```python
plik = open('DANE/liczby.txt').readlines()

roznica = -1
liczba = -1
maks_roznica = -1
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    roznica = abs(int(wiersz) - int(odbicie))
    if roznica > maks_roznica:
        maks_roznica = roznica
        maks_liczba = wiersz

print('Zadanie 4.2')
print(maks_liczba, maks_roznica)
```

</details>

<details>
<summary>4.3</summary>

```python
plik = open('DANE/liczby.txt').readlines()


def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


pierwsze = []
for wiersz in plik:
    wiersz = wiersz.strip()
    odbicie = wiersz[::-1]
    wiersz = int(wiersz)
    odbicie = int(odbicie)
    if isPrime(wiersz) and isPrime(odbicie):
        pierwsze.append(wiersz)

print('Zadanie 4.3')
for i in pierwsze:
    print(i)
```

</details>

<details>
<summary>4.3</summary>

```python
plik = open('DANE/liczby.txt').readlines()

rozne = set()
wszystkie = []
for wiersz in plik:
    wiersz = wiersz.strip()
    rozne.add(wiersz)
    wszystkie.append(wiersz)

wszystkie = sorted(wszystkie)

podwojnie = 0
for i in range(0, len(wszystkie)-2):
    if wszystkie[i] == wszystkie[i+1]:
        podwojnie = podwojnie + 1
        if wszystkie[i] == wszystkie[i+2]:
            podwojnie = podwojnie - 1

potrojnie = 0
for i in range(0, len(wszystkie)-2):
    if wszystkie[i] == wszystkie[i+1] and wszystkie[i] == wszystkie[i+2]:
        potrojnie = potrojnie + 1
        i = i + 2

print('Zadanie 4.4')
print(len(rozne), podwojnie, potrojnie)
```

</details>

</details>
