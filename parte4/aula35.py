"""
copy e deepcopy para dicionários em Python
"""
import copy

d1 = {1: 'a', 2: 'b', 3: {'a': 1, 'b': 2, 'c': 3}}
v = d1.copy()
v[1] = 'cu'

#  Valor consegue ser alterado normalmente na cópia
print(d1)
print(v)

print()

#  Valor não consegue ser alterado dentro da chave normalmente da cópia
v[3][2] = 1000
print(d1)
print(v)

print()

d1[3][2] = 3
v2 = copy.deepcopy(d1)

#  Valor consegue ser alterado normalmente com deepcopy
v2[3][2] = 1000
print(d1)
print(v2)