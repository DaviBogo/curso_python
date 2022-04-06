"""
Sistema de perguntas e respostas
"""

from urllib import response


perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4'
        },
        'resposta_certa': 'd'
    },
    'Pergunta 2': {
        'pergunta': 'Qual a capital de Santa Catarina?',
        'respostas': {
            'a': 'Urubici',
            'b': 'Blumenau',
            'c': 'Florianópolis',
            'd': 'Joinvile'
        },
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quem descobriu o Brasil?',
        'respostas': {
            'a': 'Pedro Álvarez Cabral',
            'b': 'Pedro Domingo',
            'c': 'Cristóvão Colombo',
            'd': 'Nikola Tesla'
        },
        'resposta_certa': 'a'
    },
    'Pergunta 4': {
        'pergunta': 'Qual a capital de Santa Catarina?',
        'respostas': {
            'a': 'Urubici',
            'b': 'Blumenau',
            'c': 'Florianópolis',
            'd': 'Joinvile'
        },
        'resposta_certa': 'c'
    },
}

qtd_perguntas = len(perguntas)
qtd_respostas_corretas = 0

for pk, pv in perguntas.items():
    print()
    print(f'{pk}: {pv["pergunta"]}')
    
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    
    print()
    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        qtd_respostas_corretas += 1
        print('Você acertou!')
    else:
        print('Você errou')
    
print()    
porcentagem_acerto = qtd_respostas_corretas / qtd_perguntas * 100   

print(f'Você acertou {qtd_respostas_corretas} dentre {qtd_perguntas} perguntas')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
