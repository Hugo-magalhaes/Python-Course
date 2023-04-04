if __name__ == '__main__':
    import os
    lista = []
    lista_removida = []

    def listagem(lista_1):
        print(lista_1)

    def do_undo(todo_list, undo_list):
        if not todo_list:
            print('Nada a fazer')
            return
        last_todo = todo_list.pop()
        undo_list.append(last_todo)

    def do_redo(todo_list, redo_list):
        if not redo_list:
            print('Nada a fazer')
            return
        last_todo = redo_list.pop()
        todo_list.append(last_todo)

    def add(todo, todo_list):
        todo_list.append(todo)

    while True:
        tarefa = input(
            'Escreva redo, undo, ls, clear ou algo para ser adicionado:')

        if tarefa == 'ls':  # Listar
            listagem(lista)

        elif tarefa == 'undo':  # Desfazer
            do_undo(lista, lista_removida)
        elif tarefa == 'redo':  # Refazer
            do_redo(lista, lista_removida)
        elif tarefa == 'clear':
            os.system('cls')
        else:
            add(tarefa, lista)
