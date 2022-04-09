"""
    Separe utilizando list comprehension a seguinte string (01234567890123456789012345678901234567890123456789)
    em 5 conjuntos de (0123456789) e depois retorne da seguinte forma (0123456789.0123456789.0123456789.0123456789.0123456789)
"""

string = '01234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i: i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)
