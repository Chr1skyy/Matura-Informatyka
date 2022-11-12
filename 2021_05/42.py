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
