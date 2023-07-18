cpf_str = '74682489070'
nove_digitos = cpf_str[:9]
multiplicador_regressivo_1 = 10
soma_9_primeiros_digitos = 0

for numero in nove_digitos:
    soma_9_primeiros_digitos += int(numero) * multiplicador_regressivo_1
    multiplicador_regressivo_1 -= 1

resultado_1_digito = (soma_9_primeiros_digitos * 10) % 11
primeiro_digito = resultado_1_digito if resultado_1_digito <= 9 else 0
print(primeiro_digito)

    

    


