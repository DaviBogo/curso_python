"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend
min, max
range
"""

lista = [1, 2, 3, 4, 'Davi', True, 1.2]
print('Primeiros 3 indices:')
print(lista[0:3])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l2 + l1

print('Listas 1 e 2 juntas: ')
print(l3)

l1.append('a')
print('Lista 1 com adicionado um "a": ')
print(l1)

print('Lista 2 trocando primeiro indice por "massa": ')
l2.insert(0, 'massa')
print(l2)

print('Lista 2 extendendo com lista 1: ')
l2.extend(l1)
print(l2)

l1.pop(2)
print('Lista 1 retirando terceiro indice')
print(l1)

print('Valor máximo e mínimo da terceira lista')
print(max(l3), min(l3))

print('Lista criada com Range')
lista = list(range(1, 100, 8))
for valor in lista:
    print(valor, end=' ')

print()
l4 = ['String', True, 10, -30.5]
for elem in l4:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')
