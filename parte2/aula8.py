"""
Entrada de dados
"""
nome = input('Qual seu nome? ')
idade = int(input('Qual a sua idade? '))

ano_nascimento = 2021 - idade

print()
print(f'{nome} tem {idade} anos.\n'
      f'nasceu no ano {ano_nascimento}')
