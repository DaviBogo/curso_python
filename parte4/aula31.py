"""
Funções (def) em Python
"""

variavel = 'Olá Mundo'


def func():
    print(variavel)


def func2():
    variavel = 'Outro valor'
    print(variavel)


def func3():
    global variavel
    variavel = 'Mudando valor global'


def func4(arg=None):
    return arg.replace('global', 'argumento')


func()
func2()
print(variavel)
func3()
print(variavel)
outra_variavel = func4(arg=variavel)
print(outra_variavel)
