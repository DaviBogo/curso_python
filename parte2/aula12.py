"""
Len - Quantidade de caracteres
"""

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você preisa digitar pelo menos 6 caracteres')
else:
    print('Você está cadastrado no sistema')