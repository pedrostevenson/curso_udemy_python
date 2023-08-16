def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    
    return interna

def inverte_string(string):
    return string[::-1]

def is_string(parameter):
    if not isinstance(parameter, str):
        raise TypeError('Parametro deve ser str')

testando = criar_funcao(inverte_string)
print(testando(123))