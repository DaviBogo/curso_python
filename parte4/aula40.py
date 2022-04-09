"""
    iteráveis, iteradores e geradores
"""
import sys
import time

lista = list(range(10))

print(hasattr(lista, '__iter__'))
print(hasattr(lista, '__next__'))

lista = iter(lista)
print(hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))

lista_tamanho = list(range(1000))
print(sys.getsizeof(lista))

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()

print(hasattr(g, '__next__'))

for v in g:
    print(v)

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))