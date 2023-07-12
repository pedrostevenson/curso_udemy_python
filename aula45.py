# for letra in texto
texto = 'Pedro'  # iterável
iterador = iter(texto)  # iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)