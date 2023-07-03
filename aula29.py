numero_input = input(
    'Vou dobrar o número que você digitar: '
)

try:
    numero_float = float(numero_input)
    print(f'O dobro de {numero_input} é {numero_float * 2}')
except:
    print('Isso não é um número.')
