"""
comportamento de geradores e ieradores
"""

from operator import le


nome = 'Davi Bogo'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador)) # D

print('Valores')
for letra in gerador:
    print(letra)

print(next(iterador)) # D
print(next(iterador)) # a
print(next(iterador)) # v
print(next(iterador)) # i
print(next(iterador)) #  
print(next(iterador)) # B
# print(next(iterador)) # o
# print(next(iterador)) # g
# print(next(iterador)) # o

print('Valores')
for letra in iterador:
    print(letra)
