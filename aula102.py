def concatenar(string_inical):
    valor_final = string_inical

    def interno(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar  # Variável livre
        return valor_final
    
    return interno

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

final = c()
print(final)