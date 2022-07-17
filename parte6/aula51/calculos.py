import math

PI = math.pi

def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica_lista(lista):
    r = 1
    for i in lista:
        r *= i
    return r

print(__name__)