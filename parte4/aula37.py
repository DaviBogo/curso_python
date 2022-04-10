"""
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas do set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
"""

# Iterando um set

print()
print('Iterando')

s1 = {1, 2, 3, 4, 5}

for v in s1:
    print(v)

# Adicionando e descartando elementos do set

print()
print('Adicionando e descartando')

s2 = set()
s2.add(1)
s2.add((4, 3, 2, 'Davi'))

print(s2)

s2.discard(1)

print(s2)

# Atualizando um set

print()
print('Atualizando')

s3 = set()
s3.update('Python')

print(s3)

# Removendo duplicados de uma lista

print()
print('Removendo duplicados de uma lista')

l1 = [1, 1, 1, 1, 3, 4 , 4, 4, 'Davi', 'Davi']
l1 = set(l1)
l1 = list(l1)

print(l1)

# Une |, intersecta &, diferencia - e tira diferença simétrica ^ dois sets diferentes

print()
print('Une, intersecta, diferencia e tira diferença simétrica')

s4 = {1, 2, 3, 4, 5, 7}
s5 = {1, 2, 3, 4, 5, 6}
s6 = s4 | s5
s7 = s4 & s5
s8 = s4 - s5
s9 = s4 ^ s5

print(s6)
print(s7)
print(s8)
print(s9)
