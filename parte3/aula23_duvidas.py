"""
* Enumerate
"""

lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu']
]
print(lista[1][2])

enumerada = list(enumerate(lista))
print(enumerada[0][1][2])

for v1, v2 in enumerate(lista, 56):
    nome1, nome2, nome3 = v2
    print(nome1, nome3)