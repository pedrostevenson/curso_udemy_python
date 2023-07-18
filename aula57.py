salas = [
    ['Maria', 'Helena', ],

    ['Elaine', ],

    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]
]

for i, sala in enumerate(salas):
    print(f'{i}a sala:')
    for aluno in sala:
        print(aluno)