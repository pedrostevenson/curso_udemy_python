"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero_digitado = input('Digite um número inteiro: ')

# if numero_digitado.isdigit():
#     numero_int = int(numero_digitado)
#     numero_eh_par = numero_int % 2 == 0

#     if numero_eh_par:
#         print(f'{numero_int} é um número par.')
#     else:
#         print(f'{numero_int} é um número ímpar.')
# else:
#     print('Você não digitou um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora_digitada = input('Que horas são? ')
# if hora_digitada.isdigit():
#     hora_int = int(hora_digitada)
#     bom_dia = hora_int >= 0 and hora_int <= 11
#     boa_tarde = hora_int >= 12 and hora_int <= 17
#     boa_noite = hora_int >= 18 and hora_int <= 23

#     if bom_dia:
#         print('Bom dia')
#     elif boa_tarde:
#         print('Boa tarde')
#     elif boa_noite:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora')
# else:
#     print('Valor inválido.')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
nome_curto = len(nome) <= 4 and len(nome) >= 3
nome_normal = len(nome) >= 5 and len(nome) <= 6
nome_grande = len(nome) > 6

if len(nome) == 0:
    print('Você não digitou nada.')
elif nome_curto:
    print('Seu nome é curto')
elif nome_normal:
    print('Seu nome é normal')
elif nome_grande:
    print('Seu nome é muito grande')
else:
    print('Nome inválido.')
