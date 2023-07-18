def soma(x, y):  # Parâmetros
    print(f'{x=} {y=}', '|', 'x + y =', x + y)

# print(soma)  # Nome da função = local na memória
soma(1, 2)  # Argumentos posicionais
soma(x=2, y=1)  # Argumentos nomeados