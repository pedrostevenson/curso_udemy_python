import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# for n in generator:
#     print(n)