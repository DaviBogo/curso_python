"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa.
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-strings (com chaves)
"""
import datetime

nome = 'Davi'
idade = 21
altura = 1.85
peso = 65.00

ano_atual = datetime.datetime.now().year
ano_nascimento = ano_atual - idade

imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade,\n'
      f'{altura}m de altura e {peso}kgs.\n'
      f'tem um imc de {imc:.2f}\n'
      f'nasceu no ano de {ano_nascimento}')
