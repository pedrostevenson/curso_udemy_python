pessoa = {
    'nome': 'Helena',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 17,
    'altura': 1.60
}

pessoa_completa = {
    **pessoa, **dados_pessoa
}

def mostra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    print('Nomeados:', kwargs)

# mostra_argumentos_nomeados(nome='Pedro', sobrenome='Stevenson')
mostra_argumentos_nomeados(**pessoa_completa)
print('')
mostra_argumentos_nomeados(5, 6, nome='Pedro', sobrenome='Stevenson')
