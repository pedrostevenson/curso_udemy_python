class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
p1 = Pessoa('Pedro', 'Stevenson')  # Instância
# p1.nome = 'Pedro'  # Atributo 
# p1.sobrenome = 'Stevenson'

p2 = Pessoa('Maria', 'Helena')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)