# import sys

# sys.setrecursionlimit(1004)

# def recursiva(inicio=0, fim=10):
    
#     print(inicio, fim)
    
#     # Caso base
#     if inicio >= fim:
#         return fim
        
#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva(0, 1001))

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))