numero = input('Numero: ')
if numero.isdigit():
    int_numero = int(numero)
    condicao = 10 == int_numero
    variavel = 'Valor' if condicao else 'Outro valor'
    print(variavel)
else:
    print('Você não digitou um número.')

# print('Valor' if True else 'Outro valor' if True else 'Fim')