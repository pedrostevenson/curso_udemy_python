def saudacao(msg, nome, idade):
    return f'{msg}, {nome}! Você tem {idade} anos.'

def executar(funcao, *args):
    return funcao(*args)

print(
    executar(saudacao, 'Bom dia', 'Pedro', 21)
)