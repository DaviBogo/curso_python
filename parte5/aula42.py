"""
Zip - Unindo iteráveis
Zip_longest - itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte',
           'Salvador', 'Monte Belo', 'Florianópolis']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    cidades,
    estados
)

for indice, cidade, estado in cidades_estados:
    print(indice, cidade, estado)

cidades_estados_longest = zip_longest(cidades, estados, fillvalue='estado')

for cidade, estado in cidades_estados_longest:
    print(cidade, estado)
