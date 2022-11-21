from slownik import setki, dziesiatki, nastki, jednosci

liczba = input('podaj liczbe w zakresie 0-999: ')
lista = [int(i) for i in liczba]
zakres = len(lista)

match zakres:
    case 1:
        print(jednosci[lista[0]])
    case 2:
        if lista[0] == 1:
            print(nastki[lista[1]])
        else:
            if lista[1] == 0:
                print(dziesiatki[lista[0]])
            else:
                print(dziesiatki[lista[0]] + jednosci[lista[0]])
    case 3:
        if lista[1] == 0 and lista[2] == 0:
            print(setki[lista[0]])
        elif lista[2] != 0 and lista[1] == 1:
            print(setki[lista[0]] + nastki[lista[2]])
        elif lista[2] == 0 and lista[1] != 1:
            print(setki[lista[0]] + dziesiatki[lista[1]])
        elif lista[2] != 0 and lista[1] == 0:
            print(setki[lista[0]] + jednosci[lista[2]])
        else:
            print(setki[lista[0]] + dziesiatki[lista[1]] + jednosci[lista[2]])
