"""
Sets em Python
add (adiciona), update(adiciona iterando), clear (limpa), discard,
union | (junta),
intersection & (junta elementos que são presentes em dois sets),
difference - (elementos apenas do set da esquerda,
symmeetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
"""

s1 = set()
s1.add(1)
s1.add(2)
s1.discard(2)
s1.update('Python')

print(s1)

l = [1, 1, 4, 4, 56, 7, 7, 7, 7, 7, 7, 'Davi', 'Davi']
s = set(l)
l = list(s)

print(l)
print()

s2 = {0, 1, 2, 3, 4}
s3 = {1, 2, 3, 4, 5, 6}

s4 = s2 | s3
s5 = s2 & s3
s6 = s2 - s3
s7 = s2 ^ s3
print(s4)
print(s5)
print(s6)
print(s7)
