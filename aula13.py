nome = 'Pedro Stevenson'
altura = 1.80
peso = 65
imc = peso / altura ** 2

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso}kg e seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)