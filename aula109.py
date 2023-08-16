from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculina', 'faminina', 'unissex'],
    ['algodão', 'poliester'],
]

# print_iter(combinations(pessoas, 2))  # Ordem não importa
# print_iter(permutations(pessoas, 2))  # Ordem importa
print_iter(product(*camisetas))