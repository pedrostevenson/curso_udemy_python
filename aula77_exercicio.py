perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5'
    },
]

acertos = 0

for i, pergunta in enumerate(perguntas):
    print('Pergunta:', perguntas[i]['Pergunta'])
    
    for j, opcao in enumerate(perguntas[i]['Opções']):
        print(f'{j})', opcao)
    
        if opcao == perguntas[i]['Resposta']:
            opcao_correta = str(j)
            resposta_pergunta = perguntas[i]['Resposta']
    
    opcao_escolhida = input('Escolha uma opção: ')

    if opcao_escolhida == opcao_correta:
        print('Você acertou!')
        acertos += 1
    else:
        print(
            f'Você errou! A opção correta era:\n{opcao_correta}) {resposta_pergunta}'
    )
        
    print('')

print(f'Você acertou {acertos}\nde {len(perguntas)} perguntas')