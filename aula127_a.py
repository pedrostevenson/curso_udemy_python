import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa():
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    print('FAZENDO DUMP')
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as file:
        json.dump(bd, file, ensure_ascii=False, indent=2)
    
if __name__ == '__main__':
    fazer_dump()