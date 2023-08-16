def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        resultado += ' qualquer coisa'
        print(f'O resultaddo foi {resultado}')
        print('Te decorei')
        return resultado
    
    return interna

@criar_funcao  # Syntax Sugar
def inverte_string(string):
    return string[::-1]

def is_string(parameter):
    if not isinstance(parameter, str):
        raise TypeError('Parametro deve ser str')

testando = inverte_string('123')
print(testando)