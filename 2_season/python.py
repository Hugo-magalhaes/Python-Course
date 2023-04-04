import random

lista = ['Tesoura', 'Pedra', 'Papel']

pares = [[x, y]
         for x in lista
         for y in lista]

for i, v in enumerate(pares):
    # print(i, v)
    # Todo multíplo de 4 é empate 0,4,8
    if i % (len(lista)+1) == 0:
        pares[i].append('Empatou')
    # 1,5,6 é vitória
    elif i in [len(lista)-2, len(lista)*2-1, len(lista)*2]:
        pares[i].append('Ganhou')
    # 2,3,7 é derrota
    elif i in [len(lista)-1, len(lista), len(lista)*2+1]:
        pares[i].append('Perdeu')


while True:
    python = random.choice(lista)

    escolha = input(f'''Escolha: \n
                    [1] Tesoura \n
                    [2] Pedra \n
                    [3] Papel  \n
                    ''')

    if escolha.isnumeric():
        escolha = int(escolha)
        escolha = lista[escolha-1]
        par = [python, escolha]
        print(par)
    else:
        continue

    for i, v in enumerate(pares):
        if par == v[:2]:
            print(f' Você {v[-1]}')

    # while True:
    #     python = random.choice(lista)

    #     escolha = input(f'''Escolha: \n
    #                     [1] Pedra \n
    #                     [2] Papel \n
    #                     [3] Tesoura \n
    #                     ''')
    #     if escolha.isnumeric():
    #         escolha = int(escolha)
    #     else:
    #         continue

    #     for i, v in enumerate(lista):
    #         if (escolha-1) == i:
    #             print(f' Python escolheu {python}'
    #                   f' e você {lista[i]} \n')
    #             if python == 'Pedra' and lista[i] == 'Papel':
    #                 print(' Você ganhou \n')
    #                 pass
    #             elif python == 'Pedra' and lista[i] == 'Pedra':
    #                 print(' Empate \n')
    #                 pass
    #             elif python == 'Pedra' and lista[i] == 'Tesoura':
    #                 print(' Você perdeu \n')
    #                 pass

    #             elif python == 'Papel' and lista[i] == 'Tesoura':
    #                 print(' Você ganhou \n')
    #                 pass
    #             elif python == 'Papel' and lista[i] == 'Papel':
    #                 print(' Empate \n')
    #                 pass
    #             elif python == 'Papel' and lista[i] == 'Pedra':
    #                 print(' Você perdeu \n')
    #                 pass

    #             elif python == 'Tesoura' and lista[i] == 'Papel':
    #                 print('Você ganhou \n')
    #                 pass
    #             elif python == 'Tesoura' and lista[i] == 'Tesoura':
    #                 print('Empate \n')
    #                 pass
    #             elif python == 'Tesoura' and lista[i] == 'Pedra':
    #                 print('Você perdeu \n')
    #                 pass
    #         else:
    #             continue
