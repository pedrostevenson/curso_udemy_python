import json
from aula127_a import Pessoa, CAMINHO_ARQUIVO, fazer_dump

# fazer_dump()

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as file:
	data = json.load(file)
	
	p1 = Pessoa(**data[0])
	p2 = Pessoa(**data[1])
	p3 = Pessoa(**data[2])

	print(p1.nome, p1.idade)
	print(p2.nome, p2.idade)
	print(p3.nome, p3.idade)
