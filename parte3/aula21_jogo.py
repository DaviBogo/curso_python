"""
Jogo palavra secreta
"""

secreta = 'Davi'.lower()
chances = 3
letras_digitadas = []

while True:
    if chances <= 0:
        print('Acabaram as chances, você perdeu!')
        break

    letra = input('Digite uma letra: ').lower()
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    if letra in secreta:
        print(f'Letra "{letra}" existe na palavra secreta.')
        letras_digitadas.append(letra)
    else:
        print(f'Letra "{letra}" não existe na palavra secreta')
        chances -= 1

    secreta_temp = ''
    for letra_secreta in secreta:
        if letra_secreta in letras_digitadas:
            secreta_temp += letra_secreta
        else:
            secreta_temp += '_'
    if secreta_temp == secreta:
        print('Você ganhou!!')
        break
    else:
        print(secreta_temp)

    print(f'Você ainda tem {chances} chances!')
    print()
