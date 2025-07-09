print("=== CALCULADORA SIMPLES ===")
print("Use apenas números para fazer as operações \nou 'sair' para encerrar o programa")
print("Em operação use apenas soma, subtração, multiplicação,\ndivisão ou potência")
print('-' * 60)


resultado = 0

while True:

    entrada_1 = input('Primeiro valor: ')
    entrada_2 = input('Segundo valor: ')
    operacao = input('Digite a operação (soma, subtração, multiplicação...): ')
    operacao_f = operacao.lower()

    try:
        entrada_1c = float(entrada_1)
        entrada_2c = float(entrada_2)

        if operacao_f == 'soma':
            resultado = entrada_1c + entrada_2c
            print(resultado)

        elif operacao_f == 'multiplicação':
            resultado = entrada_1c * entrada_2c
            print(resultado)

        elif operacao_f == 'subtração':
            resultado = entrada_1c - entrada_2c
            print(resultado)

        elif operacao_f == 'divisão':
            if entrada_2c == 0:
                print('ERRO: Divisão por zero')
                continue
            resultado = entrada_1c / entrada_2c
            print(f'{resultado:.4f}')

        elif operacao_f =='potência':
            resultado = entrada_1c ** entrada_2c
            print(resultado)

        else:
            print('Operação inválida, use apenas soma, subtração, multiplicação ou divisão')
            continue

    except:
        print('Digite apenas números ou "sair" para  sair do programa.')
        continue

    sair = input('Encerrar programa s/n?: ')
    if sair == 's':
        print('Programa encerrado.')
        break
    print('-' * 60)