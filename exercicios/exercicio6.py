"""
Crie uma função que exibe uma saudação com parâmetros para saudação e nome.
"""


def saudacao(msg='Oi', nome='usuário'):
    print(msg, nome)


"""
Crie uma função que exibe 3 números como parâmetros e exiba a soma entre eles
"""


def somatorio(n1=0, n2=0, n3=0):
    print(n1 + n2 + n3)


"""
Crie uma função que receba dois números. O primeiro é um valor e o segundo é um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado 
do aumento do percentual dele mesmo. 
"""


def porcentagem(valor, porcentagem):
    return valor + valor * (porcentagem / 100)


"""
Fizz Buzz - Se o parâmetro da função for divisível por 3, retorna 'Fizz'.
Se o parâmetro da função for divisível por 5, retorna 'Buzz'. Se o parâmetro da
função for divisível por 5 e por 3, retorne 'FizzBuzz', caso contrário, retorne o
número enviado.
"""


def fizzbuzz(valor):
    retorno = ''
    if (valor % 5) == 0:
        retorno += 'Fizz'
    if (valor % 3) == 0:
        retorno += 'Buzz'
    if retorno == '':
        return valor
    else:
        return retorno


saudacao('Olá', 'Manuel')
somatorio(1, 2, 3)
print(porcentagem(100, 50))
print(fizzbuzz(15))
