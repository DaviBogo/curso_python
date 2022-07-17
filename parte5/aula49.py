"""
Uso de try, except como condicional
"""

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
        except ValueError:
            pass
while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is None:
        print('Por favor, informe um número.')
    else:
        print(numero * 2)