"""
Groupby - agrupando valores
"""
from itertools import groupby, tee


alunos = [
    {'nome': 'Luiz', 'nota': 'C'},
    {'nome': 'Davi', 'nota': 'A'},
    {'nome': 'Érica', 'nota': 'A'},
    {'nome': 'Felipe', 'nota': 'B'},
    {'nome': 'Pedro', 'nota': 'C'},
    {'nome': 'Gabriel', 'nota': 'B'},
    {'nome': 'Leticia', 'nota': 'C'},
    {'nome': 'Giovani', 'nota': 'D'},
    {'nome': 'Leandro', 'nota': 'F'},
]
ordena = lambda item: item['nota']
def verifica_quantidade(quantidade): 
    if quantidade > 1: 
        return 'alunos tiraram'
    else:
        return 'aluno tirou'

alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento {agrupamento}:')

    for aluno in va2:
        print(f'\t{aluno["nome"]}')

    quantidade_alunos = len(list(va1))
    print(f'{quantidade_alunos} {verifica_quantidade(quantidade_alunos)} nota {agrupamento}')
 
    print()
    