"""
Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada
"""


def funcao1(arg):
    return arg


def funcao2(n1, n2):
    return n1 + n2


"""
Crie uma função 1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""


def child1(num):
    return num + 1


def child2(num, numero):
    return num + 2 - numero


def parent(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


print(funcao1(funcao2(1, 2)))
print(parent(child1, 1))
print(parent(child2, 2, numero=5))
