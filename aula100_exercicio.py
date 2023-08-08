import copy

import dados


novos_produtos = [
    {**produto, 'preco': round(produto['preco'] + (produto['preco'] * 0.10), 2)} 
    for produto in dados.produtos
]

# print(*dados.produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')


produtos_ordenados_por_nome = sorted(
    copy.deepcopy(dados.produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# print(*dados.produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(dados.produtos),
    key=lambda p: p['preco']
)


# FINAL
print(*dados.produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
