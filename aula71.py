def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1, 2, 3, 4, 5, 6

soma_1_ate_6 = soma(*numeros)
print(sum(numeros))
print(soma_1_ate_6)