def zipper(lista1, lista2):
    intercalada = []
    for a, b in zip(lista1, lista2):
        intercalada.append((a, b))
    return intercalada


cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

res = zipper(cidades, estados)
print(res)