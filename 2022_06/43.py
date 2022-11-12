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
