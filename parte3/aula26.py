"""
Operador ternário em Python
"""

logged_user = True
msg = 'Usuário logado' if logged_user else 'Usuário precisa estar logado'
print(msg)

idade = input('Qual a sua idade? ')
if not idade.isnumeric():
    print('Um número deve ser digitado.')
else:
    idade = int(idade)
    print('É de maior') if idade >= 18 else print('É de menor')
