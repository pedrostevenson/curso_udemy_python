def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABAOU GEN1')

def gen3():
    print('COMEÇOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABAOU GEN3')

def gen2(gen=None):
    if gen is not None:
        yield from gen
    print('COMEÇOU GEN2')
    yield 4
    yield 5
    yield 6
    print('ACABAOU GEN2')

g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for numero in g1:
    print(numero)
print()

for numero in g2:
    print(numero)
print()

for numero in g3:
    print(numero)
print()
