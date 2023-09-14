# def soma(a, b, /, x, y):  # / = argumento posicional APENAS, para argumentos antes da barra
#     print(a + b + x + y)
    
# soma(1, 2, 3, y=3)

# def soma(a, b, *, c):  # * = argumento nomeado APENAS, para argumentos depois do *
#     print(a + b + c)
    
# soma(1, 2, c=3)  
# soma(a=1, b=2, c=3)  # Não impede de colocar argumento nomeado antes do *

def soma(a, b, /, *, c):
    print(a + b + c)
    
soma(1, 2, c=3)  
