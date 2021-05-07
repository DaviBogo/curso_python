"""
For in em Python
Iterando strings com for
Função range(start = 0, stop, step = 1)
"""

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)

for n, letra in enumerate(texto):
    print(n, letra)

for numero in range(20, 10, -2):
    print(numero, end=' ')
