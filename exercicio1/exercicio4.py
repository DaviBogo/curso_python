"""
Validador de CPF
CPF = 168.995.350-09
----------------------------------------------------
1 * 10 = 10             #     1 * 11 = 11 <-
6 * 9 = 54              #     6 * 10 = 60
8 * 8 = 64              #     8 * 9 = 72
9 * 7 = 63              #     9 * 9 = 72
9 * 6 = 54              #     9 * 7 = 63
5 * 5 = 25              #     5 * 6 = 30
3 * 4 = 12              #     3 * 5 = 15
5 * 3 = 15              #     5 * 4 = 20
0 * 2 = 0               # ->  0 * 3 = 0
                        #     0 * 2 = 0
        297             #
11 - (297 % 11) = 11    #       343
11 > 9 = 0              #       11 - (343 % 11) = 9
Digito 1 = 0            #       Digito 2 = 9
"""
while True:
    cpf = input('Digite os numeros de seu CPF: ')
    if cpf.isnumeric() and len(cpf) == 11:
        break
novo_cpf = cpf[:9]

while True:
    valor = 0
    for indice, r in enumerate(range(len(novo_cpf) + 1, 1, -1)):
        valor += int(novo_cpf[indice]) * r
    v = 11 - (valor % 11)
    digito1 = 0
    if len(novo_cpf) == 9:
        digito1 = 0 if v > 9 else v
    else:
        digito1 = v

    novo_cpf = str(novo_cpf) + str(digito1)
    if len(novo_cpf) == 11:
        break

print('CPF é válido') if novo_cpf == cpf else print('CPF é inválido')
