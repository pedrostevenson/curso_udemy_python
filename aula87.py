lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Pedro'}
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        print(item)

    elif isinstance(item, str):
        print('STR')
        print(item)

    elif isinstance(item, (int, float)):
        print('NUM')
        print(f'{item} * 2 =', item * 2)

    else:
        print('OUTRO')
        print(item)
    