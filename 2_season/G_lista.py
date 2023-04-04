if __name__ == '__main__':
    import os
    lista = []
    lista_removida = []
    while True:
        print()
        tarefa = input('Escreva um dos números a seguir para:'
                       '\n[1] Escreva uma tarefa para listar '
                       '\n[2] Listar a(s) ação(ões)'
                       '\n[3] Desfazer a última ação'
                       '\n[4] Refazer a última ação \n'
                       '\n[5] Limpar terminal'
                       # '\n [5] Remover a tarefa '
                       # '\n (Obs: Digite as 3 primeiras letras) \n'
                       )
        if tarefa == '2':  # Listar
            print()
            print(f'\t{lista}')
            continue

        elif tarefa == '3' and lista:  # Desfazer
            valor = lista.pop()
            lista_removida.append(valor)
            continue

        elif tarefa == '4' and lista_removida:  # Refazer
            valor = lista_removida.pop()
            lista.append(valor)
            if len(lista) > 1:
                if lista[-1] == lista[-2]:
                    lista.pop()
            continue
        elif tarefa == '5':
            os.system('cls')
            continue

        elif tarefa[1:]:  # Adicionar
            lista.append(tarefa)
            continue

        else:
            continue
