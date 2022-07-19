"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

    ['Tarefa 1']                <- listar tarefas
    ['Tarefa 1', 'Tarefa 2']    <- adicionar tarefa
    ['Tarefa 1']                <- Desfazer
    ['Tarefa 1', 'Tarefa 2']    <- Refazer

    input <- Nova tarefa
"""


def show_ls(todo_list):
    print()
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a Desfazer')
        return

    # Tira o último valor do todo_list e joga para o redo_list
    redo_list.append(todo_list.pop())


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a Refazer')
        return

    # Tira o último valor do redo_list e joga para o todo_list
    todo_list.append(redo_list.pop())


def add_todo(todo_list, todo):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if (todo == 'ls'):
            show_ls(todo_list)
            continue
        if (todo == 'undo'):
            do_undo(todo_list, redo_list)
            continue
        if (todo == 'redo'):
            do_redo(todo_list, redo_list)
            continue
        add_todo(todo_list, todo)
