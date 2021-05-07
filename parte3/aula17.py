"""
While em python
utilizando para realizar ações enquanto
uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

x = 1
while x <= 5:
    if x == 2:
        x = x + 1
        continue

    if x == 4:
        x = x + 1
        break

    print(x)
    x = x + 1

print('Acabou')

x = 0
while x < 5:
    y = 0
    while y < 3:
        print(f'{x}, {y}')
        y += 1
    x += 1
print('Acabou')
