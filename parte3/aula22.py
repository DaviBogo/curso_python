"""
For / Else em python
"""

lista = ['Luiz', 'Davi', 'Maria']

for valor in lista:
    print(valor)
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe palavra que começa com J.')
