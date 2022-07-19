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


def adicionar_tarefa(tarefa):
    lista_tarefas.append(tarefa)


if __name__ == '__main__':
    lista_tarefas = []
    dict_comandos = {'add': [], 'undo': []}

    while True:
        comando = input('add = Adicionar Tarefa\n' +
                        'list = Listar Tarefas\n' +
                        'undo = Desfazer\n' +
                        'redo = Refazer\n' +
                        'Digite um comando: ')

        if(comando == 'add'):
            tarefa = input('Digite a tarefa: ')
            adicionar_tarefa(tarefa)
            dict_comandos['add'].append(tarefa)
            print()
            continue

        if(comando == 'list'):
            print('\nTarefas:')
            print(lista_tarefas)
            print()
            continue

        if(comando == 'undo'):
            lista_tarefas.remove(dict_comandos['add'][-1])
            dict_comandos['undo'].append(dict_comandos['add'][-1])
            dict_comandos['add'].remove(dict_comandos['add'][-1])
            print()
            continue

        if(comando == 'redo'):
            lista_tarefas.append(dict_comandos['undo'][-1])
            dict_comandos['add'].append(dict_comandos['undo'][-1])
            dict_comandos['undo'].remove(dict_comandos['undo'][-1])
            print()
