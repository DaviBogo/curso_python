"""
Perguntas e respostas
"""

perguntas = {
    'Pergunta1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '2',
            'd': '3',
        },
        'resposta_certa': 'b',
    },
    'Pergunta2': {
        'pergunta': 'Qual o maior país do mundo?',
        'respostas': {
            'a': 'Argentina',
            'b': 'Brasil',
            'c': 'Estados Unidos',
            'd': 'Russia',
        },
        'resposta_certa': 'd',
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for opcao, resposta in pv['respostas'].items():
        print(f'{opcao} - {resposta}')
    resposta = input('Digite a opção correta: ')
    if resposta == pv['resposta_certa']:
        print('Acertou mizeravi!')
        respostas_certas += 1
    else:
        print(f'Errou! a resposta correta seria: {pv["resposta_certa"]} - {pv["respostas"][pv["resposta_certa"]]}')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} perguntas!')
print(f'Você ficou com um resultado de {porcentagem_acerto}% de acerto!')