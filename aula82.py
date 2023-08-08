def executar(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador    
    return multiplica

duplica = executar(
    lambda m: lambda n: n * m,
    2
)

print(duplica(2))
print(
    executar(
        lambda x, y: x + y, 2, 3
    ),
)
print(
    executar(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)