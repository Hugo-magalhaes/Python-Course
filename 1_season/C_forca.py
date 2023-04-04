import getpass
secreto = input('Digite uma palavra: ')
acertos = []
chances = 3
while True:

    if chances <= 0:
        print(f'Você tentou {chances} vezes, você perdeu')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Você digitou algo errado')
        continue
    if letra in secreto:
        print(f'A letra "{letra}" está correta')
        acertos.append(letra)
    else:
        print(f'A letra "{letra}" está incorreta')
        chances -= 1
        print(f'Você ainda tem {chances} chances')

    secreto_temporario = ''
    # Isso faz letra_secreta correr em cima de secreto
    # Dessa forma o secreto_temporario terá a mesma quantidade de casas que a palavra secreta
    for letra_secreta in secreto:
        if letra_secreta in acertos:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '_'
    print(secreto_temporario)

    if secreto_temporario == secreto:
        print(f'Parábens, você acertou a palavra "{secreto}"!!')
        break