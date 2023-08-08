try:
    print('Abrir arquivo')
    # 8/0
except ZeroDivisionError:
    print('Divisão por zero.')
else:
    print('Nenhum erro ocorrido.')
finally:
    print('Fechar arquivo')
