def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total

def even_or_odd(x):
    if x % 2 == 0:
        return f'{x} é um número par'
    return f'{x} é um número ímpar'


result = multiply(1, 2, 3, 4, 5)
print(result)
print(even_or_odd(result))
