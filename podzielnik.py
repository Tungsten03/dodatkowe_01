#Program wyliczający NWD dla dwóch liczb podanych przez usera

liczba1 = int(input('podaj dowolną liczbę całkowitą: '))
liczba2 = int(input('podaj drugą liczbę całkowitą: '))

#Sprawdz czy liczby są sobie równe, 
#jeżeli nie to utwórz listę do dalszych działań

if liczba1 == liczba2:
    print('najwyzszy podzielnik to:', liczba1)
else:
    lista = [liczba1, liczba2]



a = max(lista) #
b = min(lista)

dzielnik = b // 2

if a % b == 0:
    print(b)
else:
    if a % dzielnik == 0:
        print(dzielnik)
    else:
        while dzielnik != 0:
            if a % dzielnik == 0 and b % dzielnik == 0:
                print(dzielnik)
                break
            else:
                dzielnik -= 1
      
           
    