"""
Try, Except - Tratando exceções
"""

try:
    a = {}
    print(a[1])
except NameError as erro:
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Código executado com sucesso')
finally:
    print('Finalmente')
    a = 'oi'

print('Bora continuar...')
print(a)