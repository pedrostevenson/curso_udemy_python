import json

# pessoa = {
#     'nome': 'Pedro',
#     'sobrenome': 'Stevenson',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},  
# 	],
#     'altura': 1.80,
#     'dev': True,
#     'nada': None,
# }


# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])

