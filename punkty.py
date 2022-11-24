from punkty_funk import wyznaczanie_prostej, poczatek, koniec

user1 = input('podaj wspolzedne punktu pierwszego (format: A,B): ')
prosta1 = wyznaczanie_prostej(user1)
user2 = input('podaj wspolzedne punktu drugiego (format: A,B): ')
prosta2 = wyznaczanie_prostej(user2)

#wyznacz poczatek i koniec nowej prostej

c = poczatek(prosta1, prosta2)
d = koniec(prosta1, prosta2)

#porównaj poczatkowe i koncowe punkty podanych prostych i wyznacz czesc wspolna

if c > d:
    print('podane odcinki nie maja czesci wspolnej.')
else:
    wspolna = [c, d]
    print(f'czesc wspolna podanych odcinkow to: {wspolna}')
