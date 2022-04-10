"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

"""
Faça um programaa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal": maior que 6 escreva "Seu nome é muito grande".
"""
# Primeiro
num1 = input('Digite um número inteiro: ')

try:
    if int(num1) % 2 == 0:
        print(f'{num1} É par')
    else:
        print(f'{num1} É ímpar')
except:
    print('O valor inserido não é inteiro')

# Segundo
horario = input('Digite um horário (0-23): ')

try:
    if 0 <= int(horario) <= 11:
        print('Bom dia')
    elif 12 <= int(horario) <= 17:
        print('Boa tarde')
    elif 18 <= int(horario) <= 23:
        print('Boa noite')
    else:
        print('Horário inválido')
except:
    print('Horário inválido')

# Terceiro
nome = input('Digite o nome do usuário: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto')
elif 5 <= tamanho <= 6:
    print('Seu nome é normal')
elif tamanho > 6:
    print('Seu nome é muito grande')
