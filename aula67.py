def soma(x, y, z=None):
    if z is None:
        print(f'{x=} {y=}', '|', 'x + y =', x + y)
    else:
        print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 3)
soma(10, 43)
soma(5, 7, 2)

        