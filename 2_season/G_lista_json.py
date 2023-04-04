import os
import json


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


def salvar(todo_list, caminho):
    dados = todo_list
    with open(caminho, 'w', encoding='utf8') as arquivo:
        dados = json.dump(todo_list, arquivo, indent=2, ensure_ascii=False)

    return dados


def ler(todo_list, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe, o criando... ')
        salvar(todo_list, caminho)

    return dados


lista = ler([], 'lista.json')
lista_removida = []

while True:

    tarefa = input('Escreva remover, refazer, listar, clear ou algo '
                   'para adicionar:')
    print()
    comandos = {
        'refazer': lambda: do_redo(lista, lista_removida),
        'remover': lambda: do_undo(lista, lista_removida),
        'listar': lambda: listagem(lista),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: add(tarefa, lista),
    }

    # comando = comandos.get(tarefa) if comandos.get(
    #     tarefa) is not None else comandos['adicionar']

    # comando()

    if comandos.get(tarefa):
        comandos.get(tarefa)()
    else:
        comandos['adicionar']()

    salvar(lista, 'lista.json')

    # with open('lista.json', 'w+', encoding='utf8') as arquivo:
    #     json.dump(lista, arquivo, indent=2)
