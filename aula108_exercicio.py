def soma_lista(l1, l2):
    intervalo = min(len(l1), len(l2))
    lista_somada = []
    
    for i in range(intervalo):
        lista_somada.append(lista_a[i] + lista_b[i])

    return lista_somada
        

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_c = soma_lista(lista_a, lista_b)
print(lista_c)