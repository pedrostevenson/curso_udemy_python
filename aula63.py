import re
import sys

# cpf_str = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('CPF: ')
cpf_usuario = re.sub(
    r'[^0-9]',
    '',    
    entrada
)

entrada_repetida = entrada == entrada[0] * len(entrada)
if entrada_repetida:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_usuario[:9]
multiplicador_regressivo_1 = 10
soma_9_primeiros_digitos = 0

for numero in nove_digitos:
    soma_9_primeiros_digitos += int(numero) * multiplicador_regressivo_1
    multiplicador_regressivo_1 -= 1

resultado_1_digito = (soma_9_primeiros_digitos * 10) % 11
primeiro_digito = resultado_1_digito if resultado_1_digito <= 9 else 0


dez_digitos = cpf_usuario[:9] + str(primeiro_digito)
multiplicador_regressivo_2 = 11
soma_10_primeiros_digitos = 0

for digito in dez_digitos:
    soma_10_primeiros_digitos += int(digito) * multiplicador_regressivo_2
    multiplicador_regressivo_2 -= 1

resultado_2_digito = (soma_10_primeiros_digitos * 10) % 11
segundo_digito = resultado_2_digito if resultado_2_digito <= 9 else 0

validando_cpf = cpf_usuario[:9] + str(primeiro_digito) + str(segundo_digito)
print('CPF válido' if validando_cpf == cpf_usuario else 'CPF inválido')

