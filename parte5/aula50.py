"""
Módulos padrão do Python:
Módulos são arquivos .py (que contém código Python) e servem para expandir
as funcionalidades padrão da linguagem
Veja os módulos padrão do Python:
https://docs.python.org/3/py-modindex.html
"""
from sys import platform as so
from random import randint as rint
import pymysql

def randint(*args):
    return 'hahaha'

print(so)
for i in range(10):
    print(rint(0, 10))
print(randint())
