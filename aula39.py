nome = 'Pedro'
indice = 0
novo_nome = ''
while indice < len(nome):
    # print(nome[indice])
    novo_nome += f'*{nome[indice]}'
    indice += 1
novo_nome += '*'
print(novo_nome)
