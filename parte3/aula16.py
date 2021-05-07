"""
Manipulando Strings
* String índices
* Fatiamento de Strings
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo
"""

# positivos  [012345678]
texto = 'Python s2'
# negativos -[987654321]
print(texto[8])

url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto[2:6]
print(nova_string)

python_string = texto[:6]
print(python_string)

s2_string = texto[7:]
print(s2_string)

novo_texto = texto[0:6:2]
print(novo_texto)

for letra in texto:
    print(letra)
