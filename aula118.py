def add_client(name, client_list=None):  # Se o valor for mutável, colocar = None
    if client_list is None:
        client_list = []
    client_list.append(name)
    return client_list

client_1 = add_client('Pedro')
add_client('Paulo', client_1)
add_client('Maria', client_1)

client_2 = add_client('Juliana')
add_client('Helena', client_2)

print(client_1)
print(client_2)
        