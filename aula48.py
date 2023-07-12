# lista = [123, True, 'Pedro', 1.2, []]
# for i in range(5):
#     if i == 3:
#         lista[2] = 'Maria'
#     print(lista, i)

# lista = [10, 20, 30, 40]
# del lista[1]
# lista.append(50)
# valor_removido = lista.pop(1)
# lista.insert(-1, 666)
# print(lista, 'Valor removido:', valor_removido)

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b  # concatenação de listas
# lista_a.extend(lista_b)
# print('Lista A:', lista_a)
# print('Lista C:', lista_c)

lista_a = ['Maria', 'João']
# lista_b = lista_a  # Apontam para o mesmo local da memória
lista_b = lista_a.copy()
lista_a[0] = 'Outro nome'

print(lista_a)
print(lista_b)