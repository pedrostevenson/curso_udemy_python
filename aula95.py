def nao_aceito_denimonador_zero(denominador):
    if denominador == 0:
        raise ZeroDivisionError(
            'O denominador de uma divisão não pode ser 0'
)
    return True

def deve_ser_int_ou_float(numero):
    tipo_do_numero = type(numero)
    if not isinstance(numero, (int, float)):
        raise TypeError(
            f'"{numero}" deve ser do tipo int ou float. '
            f'"{tipo_do_numero.__name__}" enviado'
)
    return True


def divide(n, d):
    nao_aceito_denimonador_zero(d)
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    return n / d

print(divide(8, '0'))