"""
Expressões Lambds (expressões anônimas) - Python
"""

lista = [
    ['P1', 13],
    ['P3', 5],
    ['P2', 2],
    ['P4', 7],
    ['P5', 15],
]


def func(item):
    return item[1]


lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
print(sorted(lista, key=lambda i: i[0]))
