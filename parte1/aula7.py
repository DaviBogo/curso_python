"""
Formatação de strings
"""
nome = 'Luiz'
idade = 32
altura = 1.85
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e sem imc é {imc:.2f}')
print('{} tem {} anos de idade e sem imc é {}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e sem imc é {im}'.format(n=nome, i=idade, im=imc))
