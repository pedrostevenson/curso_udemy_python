# Variáveis com valores literais iguais
# apontam o mesmo valor na memória

v1 = 'a'
v2 = 'a'
# print(id(v1))
# print(id(v2))

# Flags

condicao = True
passou_no_if = None  # Flag para saber se entrou no if

if condicao:
    passou_no_if = True  # Sempre declarar antes fora do bloco
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
