import os

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print()

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []


while True:
    print('Comandos: listar, defazer e refazer')
    tarefa = input('Digite uma tarefa ou um comando:')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        continue
