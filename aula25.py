# Interpolação básica de strings
# s - strings
# d e i - int
# f - float
# x e X - hexadecimal

nome = 'Pedro'
preco = 1000.345
variavel = '%s, o preço é %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (1500, 1500))
