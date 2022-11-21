from przykladowe_stanowiska import wszystkie_stanowiska_stacji_944

def parametry_stacji(stanowisko):
    return stanowisko['param']['paramName']

def id_stanowiska(stanowisko):
    return stanowisko['id'] < 6080

print('***Parametry stacji***')
parametry = map(parametry_stacji, wszystkie_stanowiska_stacji_944)
print(*parametry, sep='\n')

print('***stanowiska o id < 6080***')
id_stanowisk = filter(id_stanowiska, wszystkie_stanowiska_stacji_944)
print(*id_stanowisk, sep='\n')

