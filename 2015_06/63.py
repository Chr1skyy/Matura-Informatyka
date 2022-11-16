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
