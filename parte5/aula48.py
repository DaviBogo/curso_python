"""
raise
https://docs.python.org/3/library/exceptions.html
"""


def divide1(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print('Log:', erro)
        raise


def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.')
    return n1/n2


try:
    print(divide1(2, 1))
    print(divide2(3, 0))
except (ZeroDivisionError, ValueError) as erro:
    print('Erro:', erro)
