# set_1 = set()  # Criar set() vazio
# set_1 = {'Pedro', 1, 2, 3}
# print(set_1, type(set_1))

# for item in set_1:
#     print(item)

# print(3 in set_1)

set_1 = set()
set_1.add('Pedro')
set_1.add(1)
set_1.update(('Olá mundo', 1, 2, 3, 4))  # Adiciona iterando
set_1.discard('Olá mundo')
set_1.discard('Pedro')
# set_1.clear()
# print(set_1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # Unão
s3 = s1 & s2  # Intersecção
s3 = s1 - s2  # Diferneça (itens do set da esquerda)
s3 = s1 ^ s2  # Diferença simétrica
print(s3)

