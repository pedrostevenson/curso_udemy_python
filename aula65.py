# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome=''):
    if nome == '':
        print('Você não tem um nome.')
    else:
        print(f'Olá, {nome}!')

for nomes in range(5):
    nome = input('Qual é o seu nome? ').strip()
    saudacao(nome)

