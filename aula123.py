class Animal:
    def __init__(self, nome):
        self.nome = nome
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    def exectar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)  

morcego = Animal('Morcego')
print(morcego.exectar('banana e maçã'))
