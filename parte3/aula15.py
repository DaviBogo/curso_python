"""
Formatando valores com modificadores

:s - Texto
:d - Inteiros
:f - Números de ponto flutuante
:.(NÚMERO)f - Quantidade de casas decimais
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d, f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1140
print(f'{num_1:0<10}')

num_3 = 654
print(f'{num_1:0>10.2f}')

nome = 'Davi'
sobrenome = 'Bogo'
nome_formatado = '{0:-^50}\n{1:=^50}'.format(nome, sobrenome)
print(nome_formatado)

print(nome.lower())
print(nome.upper())
print(nome.title())
