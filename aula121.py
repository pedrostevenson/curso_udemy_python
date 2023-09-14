class Carro:
    def __init__(self, name):
        self.name = name
    
    def acelerar(self):
        print(f'{self.name} está acelerando...')
            
        
fusca = Carro('Fusca')
print(fusca.name)
fusca.acelerar()

celta = Carro(name='Celta')
print(celta.name)
celta.acelerar()