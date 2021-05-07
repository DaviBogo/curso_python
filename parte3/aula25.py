"""
Trocando valor entre variáveis
"""

# Outras linguagens
print('Trocando valores em outras linguagens')
x = 10
y = 'Luiz'

print(f'x = {x} e y = {y}')
z = x
x = y
y = z

print(f'x = {x} e y = {y}')

# Python
print('Trocando valores em python')
x = 10
y = 'Luiz'

print(f'x = {x} e y = {y}')
x, y = y, x

print(f'x = {x} e y = {y}')

# Com muitas variáveis
print('Trocando vários valores em python')
n1 = 'Davi'
n2 = 'Pedro'
n3 = 'Felipe'
n4 = 'Jonas'

print(f'n1 = {n1}, n2 = {n2}, n4 = {n3} e n4 = {n4}')
n1, n2, n3, n4 = n2, n3, n1, n4

print(f'n1 = {n1}, n2 = {n2}, n4 = {n3} e n4 = {n4}')
