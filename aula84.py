import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
# lista = [1 for numero in range(10)]

# lista = [numero for numero in range(10)]

# lista = [
#     numero * 2
#     for numero in range(10)
# ]

# print(lista)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

atualizacao_preco = [
    {**produto, 'preco': produto['preco'] + (produto['preco'] * 0.05)}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*atualizacao_preco, sep='\n')
# p(atualizacao_preco)

# Filtro
# lista = [n for n in range(10) if n < 5]
atualizacao_preco = [
    {**produto, 'preco': produto['preco'] + (produto['preco'] * 0.05)}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

p(atualizacao_preco)