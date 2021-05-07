"""
Dicionários em Python
"""
d1 = dict(chave1='valor chave', chave2='valor da outra chave')

d1['nova chave'] = 'Valor da nova chave'
print('Este é o primeiro dicionário:', d1)
print('Este é o tamanho dele:', len(d1))

d2 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 123
}
del d2['str']
print('Este é o segundo dicionário:', d2)
d2['naoexiste'] = 'naoexiste'
print('Aqui retorna se existe uma chave dentro do dicionário 2:', 'naoexiste' in d2)

d3 = {
    'chave1': 'valor',
    'chave4': 'outro valor',
    'chave3': 'mais um valor',
}

for k, v in d3.items():
    print('Chave do terceiro dicionário:', k, '| Valor do terceiro dicionário:', v)

clientes = {
    'cliente1': {
        'nome': 'Davi',
        'sobrenome': 'Bogo'
    },
    'cliente2': {
        'nome': 'Gaba',
        'sobrenome': 'Hilario'
    }
}

for k, v in clientes.items():
    print(f'Exibindo {k}')
    for chave, valor in v.items():
        print(f'Seu {chave} é {valor}')
