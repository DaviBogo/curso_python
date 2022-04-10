"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Felipe', 'Davi', 'Érica']

print('Combinações: ')
for grupo in combinations(pessoas, 2):
    print(grupo)

print('Permutações: ')
for grupo in permutations(pessoas, 2):
    print(grupo)

print('Produtos: ')
for grupo in product(pessoas, repeat=2):
    print(grupo)
