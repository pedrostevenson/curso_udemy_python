# Debug pra entender
x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        y = 2
        x = 11
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)
