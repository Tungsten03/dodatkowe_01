from slownik import setki, dziesiatki, nastki, jednosci

liczba = input('podaj liczbe w zakresie 0-999: ')
lista = [int(i) for i in liczba]
zakres = len(lista)
slownie = ''

if zakres == 3:
    slownie += setki[lista[0]]
    if lista[1] == 1:
        slownie += nastki[lista[2]]
    else:
        slownie += dziesiatki[lista[1]]
        if lista[2] == 0:
            pass
        else:
            slownie += jednosci[lista[2]]
elif zakres == 2:
    if lista[0] == 1:
        slownie += nastki[lista[1]]
    else:
        slownie += dziesiatki[lista[0]]
        if lista[1] == 0:
            pass
        else:
            slownie += jednosci[lista[1]]
else:
    slownie += jednosci[lista[0]]

print(slownie)
