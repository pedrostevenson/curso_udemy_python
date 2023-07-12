import os
lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if len(opcao) > 1:
        print('Digite apenas uma letra.')
        continue
    elif opcao not in 'ial':
        print('Opção inválida')
        continue
    # Inserir
    if opcao == 'i':
        os.system('cls')
        inserir_lista = input('Valor: ')
        lista.append(inserir_lista)
        continue
    # Apagar
    elif opcao == 'a':
        os.system('cls')
        if len(lista) == 0:
            print('Lista vazia. Não há o que ser apagado.')
            continue

        apagar_indice_lista = input('Escolha o índice para apagar: ')

        if apagar_indice_lista.isdigit():
            apagar_indice_lista_int = int(apagar_indice_lista)
        
            if apagar_indice_lista_int > len(lista):
                print('Índice inexistente.')
                continue
            else:
                del lista[apagar_indice_lista_int]
                continue
        else:
            print('Índice inválido.')
    # Listar
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Lista vazia. Não há o que ser listado.')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)
                continue
