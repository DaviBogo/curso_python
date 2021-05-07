"""
Operadores lógicos
and, or, not
in e not in
"""

# Verdadeiro E Verdadeiro
print(2 == 2) and (3 == 3)

# Verdadeira ou Verdadeira
print(2 == 3 or 2 == 2)

# Verdadeiro é Falso, Falso é Verdadeiro
print(not 2 == 2)

# Está presente
if 'u' in 'urubu':
    print(True)
else:
    print(False)

# Não está presente
if 'u' not in 'urubu':
    print(True)
else:
    print(False)
