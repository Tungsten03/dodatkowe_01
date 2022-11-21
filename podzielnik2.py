
liczba1 = int(input('podaj dowolną liczbę całkowitą: '))
liczba2 = int(input('podaj drugą liczbę całkowitą: '))

if liczba1 == liczba2:
    print('najwyzszy podzielnik to:', liczba1)
else:
    lista = [liczba1, liczba2]

a = max(lista)``
b = min(lista)


if a % b == 0:
    print(b)
else:
    while a != 0:
        reszta = a % b
        if a % reszta == 0 and b % reszta == 0:
            print(reszta)
            break
        else:
            a = b
            b = reszta

    1``
