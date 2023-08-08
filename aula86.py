dicionario = {
    'produto': 'Caneta Azul',
    'preco': 2.50,
    'categoria': 'Escritório'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in dicionario.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

# dc = {
#     chave: valor 
#     for chave, valor in lista
# }

print(dict(dc))  # Consegue converter se parece com um dicionário

s1 = set(i ** 2 for i in range(10))
print(s1)