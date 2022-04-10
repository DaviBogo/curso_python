"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da 
menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

================= resultado
lista_soma  = [2, 4, 6, 8]
"""

from itertools import zip_longest


lista_a = []
lista_b = []


def cria_lista(lista, letra):
    valor = 1
    while valor != 0:
        valor = int(
            input(f'Digite um número para lista {letra} (0 para parar)'))
        if valor != 0:
            lista.append(valor)


cria_lista(lista_a, 'A')
cria_lista(lista_b, 'B')

lista_somada = [a + b for a, b in list(zip(lista_a, lista_b))]
lista_somada_maior = [a + b for a, b in list(zip_longest(lista_a, lista_b, fillvalue=0))]

print(f'Lista A: {lista_a}')
print(f'Lista B: {lista_b}')
print(f'Lista somada: {lista_somada}')
print(f'Lista somada maior: {lista_somada_maior}')
