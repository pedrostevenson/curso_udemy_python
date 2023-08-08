# import sys

# from aula99_package.modulo import *  # Má prática
# import aula99_package.modulo
# # from aula99_package.modulo import soma_do_modulo
# from aula99_package import modulo


# # print(*sys.path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)

# from aula99_package.modulo import soma_do_modulo, fala_oi
# print(__name__)
# print(soma_do_modulo(2, 3))
# fala_oi()

import aula99_package

print(aula99_package.soma_do_modulo(2, 5))
print(aula99_package.variavel)
aula99_package.fala_oi()