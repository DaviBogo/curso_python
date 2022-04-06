"""

--> É uma lista de listas de números inteiros
--> As listas internas tem o tamanho de 10 números
--> As listas internas contém números de 1 à 10 e eles podem ser duplicados

Exercício

--> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda 
            ocorrência (o número duplicado em si).
            Exemplo: [1, 2, 3, ->3<-, 2, 1] 3 
            se não encontrar duplicados na lista, retorne -1 
"""

lista_de_lista_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],    # 1
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],     # 2
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],     # 3
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],     # 4
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],    # 5
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],     # 6
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],  # 7
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],     # 8
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],    # 9
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],     # 10
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],     # 11
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],    # 12
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 10],    # 13
]

def encontra_primeiro_duplicado(param_lista_de_inteiros):
    print(f'Lista {lista_de_lista_de_inteiros.index(param_lista_de_inteiros) + 1}: ')

    valores_lista = set()
    for v in param_lista_de_inteiros:
        if v in valores_lista:
            return f'{v}'
        valores_lista.add(v)
    return -1

for lista_de_inteiros in lista_de_lista_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))
    print()