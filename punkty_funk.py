#Funkcja konwerujaca podany string na liste
def wyznaczanie_prostej(data):
    prosta = [int(wartosc) for wartosc in data.split(sep=',')]
    if prosta[0] >= prosta[1]:
        print('ta prosta jest nieprawidlowa')
        return False
    return prosta

# funkcje wyznaczajace poczatkowy i koncowy punkt nowej prostej na podstawie zadanych odcinkow x i y

def poczatek(x, y):
    if x[0] >= y[0]:
        return x[0]
    else:
        return y[0]


def koniec(x, y):
    if x[1] <= y[1]:
        return x[1]
    else:
        return y[1]
