"""
Split, Join, Enumerate em Python
* Split - Dividir uma string
* Join - Junta uma lista
*Enumerate - Enumerar elementos da lista
"""
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split()
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi "{palavra}"')

for valor in lista_2:
    print(valor.strip().capitalize())

lista = [
    [1, 'Davi'],
    [3, 'João'],
    [5, 'Maria']
]
for i, v in lista:
    print(i, v)

lista = 'Davi João Maria'.split()
for indice, valor in enumerate(lista):
    print(indice, valor)
