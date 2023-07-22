import copy

# pessoa = {
#     'nome': 'Pedro',
#     'sobrenome': 'Stevenson',
#     'idade': 21,
#     'altura': 1.80,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321}
#     ]
# }

# for dados in pessoa:
#     print(dados, pessoa[dados])

##################################

# pessoa = {}

# chave = 'nome'

# pessoa[chave] = 'Pedro'
# pessoa['sobrenome'] = 'Stevenson'

# print(pessoa[chave])

# pessoa[chave] = 'Maria'
# # del pessoa['sobrenome']
# print(pessoa)

# if pessoa.get('sobrenome') is None:
#     print('Não existe')
# else:
#     print(pessoa['sobrenome'])

##################################

# pessoa = {
#     'nome': 'Pedro',
#     'sobrenome': 'Stevenson',
#     'idade': 21
# }

# pessoa.setdefault('idade', 'Idade não informada')
# print(pessoa['idade'])
# print(len(pessoa))
# print(tuple(pessoa.keys()))  # retorna as chaves
# print(list(pessoa.values()))  # retorna os valores dentro das chaves
# print(list(pessoa.items()))

# for valores in pessoa.values():
#     print(valores)

# for chave, valor in pessoa.items():
#     print(chave, valor)

##################################

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# shallow copy = valores mutáveis dentro do dicionário apontam para o mesmo local na memória
# d2 = d1.copy()  # <-- shallow copy
# d2 = copy.deepcopy(d1) 

# d2['c1'] = 1000
# d2['l1'][1] = 100

# print('d1:', d1)
# print('d2:', d2)

##################################

# c1 = d1.pop('c1')  # apaga a chave e retorna o valor apagado
# print(c1)
# print(d1)
 
# ultima_chave = d1.popitem()  # apaga e última chave e retorna a chave e o valor apagado
# print(ultima_chave)
# print(d1)

##################################

# d1.update({  # Atualiza e adiciona chaves no dicionário
#     'c1': 5,
#     'c3': 15,
# })
# d1.update(c1=5, c3=15)  # update() com argumentos nomeados
tupla = (('c1', 5), ('c3', 15))  # update() com tuplas
d1.update(tupla)
print(d1)