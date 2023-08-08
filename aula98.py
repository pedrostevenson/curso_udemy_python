import importlib  

import aula98_m  # Singleton

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)  # Recarregando o código do módulo
    print(i)

print('ACABOU')
