import json

lista_json = []
lixeira = []

def escrever():
    with open('/home/ysantos/Documentos/GitHub/curso-udemy/python-luiz-otavio/curso_python/secao_4/exercicios/ex119_lista.json', 'w') as arquivo_lista:
            json.dump(
                lista_json,
                arquivo_lista,
                indent=2,
                ensure_ascii=False
            )

def ler():
    with open('/home/ysantos/Documentos/GitHub/curso-udemy/python-luiz-otavio/curso_python/secao_4/exercicios/ex119_lista.json', 'r') as arquivo_lista:
            lista_json = json.load(arquivo_lista)
            return lista_json


try:
    lista_json = ler()
except (FileNotFoundError, json.JSONDecodeError):
    lista_json = []

while True:
    print('Comandos: listar, desfazer, sair')
    digito = input('Digite uma tarefa ou comando: ')
    
    if digito.lower() == 'sair':
        break

    elif digito.lower() == 'listar':
        if lista_json == []:
            print('Nada para listar')
            continue
        print('TAREFAS:')
        for item in lista_json:
            print(item)

    elif digito.lower() == 'desfazer':
        if lista_json == []:
             print('Nada para desfazer')
             continue
        lixeira.append(lista_json.pop())
        escrever()
    
    elif digito.lower() == 'refazer':
        if lixeira == []:
             print('Nada para refazer')
             continue
        lista_json.append(lixeira.pop())
        escrever()

    else:
        lista_json.append(digito)
        escrever()
