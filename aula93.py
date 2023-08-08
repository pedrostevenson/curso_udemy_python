# a = 18
# b = 0
# print('Linha 1'[1000])
# print(b[0])
# c = a / b

try:
    a = 18
    b = 0
    print('Linha 1'[1000])
    c = a / b
    print(c)
except ZeroDivisionError:
    print('Dividiu por zero.')
except (TypeError, IndexError) as error:
    print(f'{error.__class__.__name__}: {error}')
except Exception:  
    print('ERRO DESCONHECIDO')