from wszystkie_stacje_dane import wszystkie_stacje_pomiarowe

def predykat_miasta(stacja):
    return stacja['city']['name'] == 'Warszawa'

def predykat_wojewodztwa(stacja):
    return stacja['city']['commune']['provinceName'] == 'WIELKOPOLSKIE'

def predykat_id(stacja):
    return stacja['id'] > 15000


print('Wszystkie stacje w Warszawie')
warszawskie = filter(predykat_miasta, wszystkie_stacje_pomiarowe)
print(*warszawskie, sep='\n')

print('Wszystkie stacje w woj. wielkopolskim')
wielkopolskie = filter(predykat_wojewodztwa, wszystkie_stacje_pomiarowe)
print(*wielkopolskie, sep='\n')

print('stacje o id > 15000')
id15000 = filter(predykat_id, wszystkie_stacje_pomiarowe)
print(*id15000, sep='\n')
