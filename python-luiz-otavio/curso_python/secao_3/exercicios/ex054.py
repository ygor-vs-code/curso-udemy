import os

lista = []

while True:
    opcao = input('Selecione uma opção\n'
                  '[i]nserir [a]pagar [l]istar [e]xcluir [s]sair: ')
    
    if opcao.lower() == 'i':
        
        valor = input('Valor: ')

        if valor in lista:
            print('Esse valor já foi inserido.')
        else:
            lista.append(valor)
            os.system('clear')
            print(f'Item "{valor}" inserido.')

    elif opcao.lower() == 'a':
        try:
            apagar = int(input('Selecione o índice: '))
            os.system('clear')
            print(f'Item "{lista[apagar]}" apagado.')
            lista.pop(apagar)
        except:
            print('Selecione um índice válido.')

    elif opcao.lower() == 'l':
        if lista == []:
            print('Lista vazia.')
        else:
            os.system('clear')
            for indice, nome in enumerate(lista):
                print(indice, nome)

    elif opcao.lower() == 'e':
        os.system('clear')
        lista.clear()
        print('Lista excluida.')

    elif opcao.lower() == 's':
        print('Programa encerrado.')
        break

    else:
        os.system('clear')
        print('Selecione uma opção válida.')
