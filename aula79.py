# Exemplo uso de set()
letras = set()
while True:
    letra = input('Digite: ').lower()
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns')
        break

    print(letras)