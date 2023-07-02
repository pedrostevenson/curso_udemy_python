# entrada = input('[E]ntrar / [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrando no sistema.')
# else:
#     print('Saindo do sistema.')

# Avaliação de curto circuito
print(False or 0 or False or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)
