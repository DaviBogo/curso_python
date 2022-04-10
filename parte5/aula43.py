"""
    count - itertools
"""
from itertools import count

contador = count(start=5, step=0.4)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break


contador_lista = count(start=1)
lista = ['Luiz', 'Davi', 'Maria']
lista = zip(contador_lista, lista)
print(list(lista))