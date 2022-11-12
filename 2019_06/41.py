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
