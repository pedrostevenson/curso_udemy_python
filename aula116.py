import os
# caminho_arquivo = "C:\\Users\\pedro\\Documents\\curso-python\\udemy\\"
caminho_arquivo = "aula116.txt"

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:  # with abre e fecha automaticamente
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')  # Iterável
#     )
#     arquivo.seek(0, 0)  # Move o cursor 
#     print(arquivo.read())
    
#     print('READLINE')
#     arquivo.seek(0, 0)
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print('-' * 10)


#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())


# print('-' * 10)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# with open(caminho_arquivo, 'a') as arquivo:  # 'a' == append
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')  # Iterável
#     )

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')  # Iterável
    )

# os.remove(caminho_arquivo) #  Ou unlink
# os.rename(caminho_arquivo, 'aula116-novo.txt')