string = 'Pedro'
metodo = 'lower'

if hasattr(string, metodo):
    print('Existe o método', metodo)
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)