import os

palavra_secreta = 'perfume'
tentativas = 0
letras_acertadas = ''

while True:
    letra_usuario = input('Digite uma letra: ')

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra.')
        tentativas += 1
        continue

    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario

    palavra_formatada = ''  # Antes do for para sempre resetar
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada += '*'
    print(palavra_formatada)
    
    if palavra_formatada == palavra_secreta:
        os.system('cls')
        tentativas += 1
        print('Você acertou a palavra!')
        break

    tentativas += 1
print(f'Você acertou em {tentativas} tentativas.')

    
