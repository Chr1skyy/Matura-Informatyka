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
