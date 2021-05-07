"""
Desempacotamento de listas em Python
"""
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(n1, n3, ultimo_da_lista)

*_, m1, m2, m3 = lista

print(_[0], _[2], m3)
