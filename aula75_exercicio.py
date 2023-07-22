import random

# def double(num):
#     return f'O dobro de {num} é {num * 2}'
# def triple(num):
#     return f'O triplo de {num} é {num * 3}'
# def quadruple(num):
#     return f'O quadruplo de {num} é {num * 4}'


# number_double = double(5)
# number_triple = triple(5)
# number_quadruple = quadruple(5)

# print(number_double)
# print(number_triple)
# print(number_quadruple)

def create_multiplier(multiplier):
    def multiply(num):
        return num * multiplier
    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

number_random = random.randint(0, 100)
print(f'Dobro de {number_random}:', double(number_random))
print(f'Triplo de {number_random}:', triple(number_random))
print(f'Quadruplo de {number_random}:', quadruple(number_random))

    


