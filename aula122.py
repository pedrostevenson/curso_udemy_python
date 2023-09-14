# Instância da class (objeto) - tem os dados.
# Uma classe pode gerar várias instâncias.
# Na classe, o self é a própria instância.

class Carro:
    def __init__(self, name):
        self.name = name
    
    def acelerar(self):
        print(f'{self.name} está acelerando...')
            
        
fusca = Carro('Fusca')
print(fusca.name)
fusca.acelerar()
Carro.acelerar(fusca)  # Não muito comum


celta = Carro(name='Celta')
print(celta.name)
Carro.acelerar(celta)  # Mesma coisa
celta.acelerar()  # Mesma coisa