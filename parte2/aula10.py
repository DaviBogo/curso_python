"""
Operadores Relacionais
== > >= < <= !=
"""

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

# idade limite para pegar empréstimo
idade_minima = 20
idade_maxima = 30

if idade >= idade_minima and idade <= idade_maxima:
    print(f'{nome} pode pegar um emprestimo')
else:
    print(f'{nome} não pode pegar um emprestimo')
