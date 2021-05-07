"""
Funções  - def em Python
"""


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('a', '4')
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)
