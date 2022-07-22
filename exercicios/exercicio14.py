"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original       = 04.252.011/0001-10
Válido

Recap.
543298765432  -> Primeiro digito
6543298765432 -> Segundo digito
"""

list1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
list2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def get_cnpj_numeric_list(cnpj):
    return [int(s) for s in cnpj if s.isnumeric()]


def get_cnpj_next_number(numbers_cnpj, comparable_list):
    sum = 0
    for i in range(len(comparable_list)):
        sum += numbers_cnpj[i] * comparable_list[i]

    return 0 if (11 - (sum % 11)) > 9 else (11 - (sum % 11))


if __name__ == '__main__':

    while True:

        cnpj = input('Digite um cnpj para validar, ou "sair" para sair: ')

        if cnpj == 'sair':
            break

        try:
            numbers_cnpj = get_cnpj_numeric_list(cnpj[:-2])

            numbers_cnpj.append(
                get_cnpj_next_number(numbers_cnpj, list1))

            numbers_cnpj.append(
                get_cnpj_next_number(numbers_cnpj, list2))

            if numbers_cnpj == get_cnpj_numeric_list(cnpj):
                print('CNPJ válido')
            else:
                raise Exception()
                
        except Exception:
            print('CPNJ inválido.')