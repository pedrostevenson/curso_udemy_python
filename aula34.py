condicao = True

while condicao:
    nome = input('Digite seu nome: ')

    if nome == 'sair':
        break
    
    print(f'Seu nome é {nome}')

print('Acabou')
