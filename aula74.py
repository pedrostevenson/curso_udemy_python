def create_greeting(saudation):
    def salute(nome):
        return f'{saudation}, {nome}!'
    return salute

falar_bom_dia = create_greeting('Bom dia')
falar_boa_noite = create_greeting('Boa noite')

for nome in ['Pedro', 'Maria', 'João']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))