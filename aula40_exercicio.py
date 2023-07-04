while True:
    num_1_str = input('Digite um número: ')
    num_2_str = input('Digite outro número: ')

    if len(num_1_str) == 0 or len(num_2_str) == 0:
        print('Você esqueceu de digitar.\nTente novamente.')
        continue
    
    print('[+] Adição\n[-] Subtração\n[*] Multiplicação\n[/] Divisão')
    operador = input('Escolha uma operação: ')

    try:
        num_1_float = float(num_1_str)
        num_2_float = float(num_2_str)    
    except:
        print('Digite números apenas.')
        continue

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')
    else:
        print('Operador inválido.\nTente novamente.')
        continue

    continuar = input('Deseja continuar? [S/N]: ').upper().startswith('S')
    if continuar:
        continue
    else:
        break

