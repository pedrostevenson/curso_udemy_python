frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
letra_apareceu_mais = ''
vezes_letra_apareceu = 0
while i < len(frase):
    letra = frase[i]
   
    if letra == ' ':
        i += 1
        continue
    
    letra_count = frase.count(letra)

    if letra_count > vezes_letra_apareceu:
        letra_apareceu_mais = letra
        vezes_letra_apareceu = letra_count

    i += 1

print(letra_apareceu_mais, vezes_letra_apareceu)