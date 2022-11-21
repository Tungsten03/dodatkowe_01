def wyznaczanie_prostej(data):
    prosta = [int(wartosc) for wartosc in data.split(sep=',')]
    if prosta[0] >= prosta[1]:
        print('ta prosta jest nieprawidlowa')
        return False
    return prosta

def wyznacz_czesc_wspolna(koordy1, koordy2):
    x = set([*range(koordy1[0], koordy1[1]+1, 1)])
    y = set([*range(koordy2[0], koordy2[1]+1, 1)])
    wspolny_zbior = x.intersection(y)
    czesc_wspolna = [min(wspolny_zbior), max(wspolny_zbior)]
    return czesc_wspolna




user1 = input('podaj wspolzedne punktu pierwszego (format: A,B): ')
prosta1 = wyznaczanie_prostej(user1)
user2 = input('podaj wspolzedne punktu drugiego (format: A,B): ')
prosta2 = wyznaczanie_prostej(user2)

if not prosta1 or not prosta2:
    print('Nie mozna wykonac dzialania. Nalezy podac 2 prawidlowe proste.')    
    
else:
    wynik = wyznacz_czesc_wspolna(prosta1, prosta2)
    print('czesc wspolna podanych punktow to:', wynik)
    
