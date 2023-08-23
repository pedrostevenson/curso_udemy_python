# caminho_arquivo = "C:\\Users\\pedro\\Documents\\curso-python\\udemy\\"
caminho_arquivo = "aula116.txt"

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:  # with abre e fecha automaticamente
    print('Olá mundo')
    print('Arquivo será fechado')