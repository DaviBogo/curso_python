"""
Funções (def) em python
"""


def funcao(*args, **kwargs):
    print(args)

    nome = kwargs['nome']
    print(nome)


lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
funcao(*lista1, *lista2, idade=30, nome='Luiz Indom')
