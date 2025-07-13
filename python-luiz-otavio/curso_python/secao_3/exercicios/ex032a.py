try:
    n = int(input('Digite um valor inteiro: '))
    if n % 2 == 0:
        print('Valor digitado é Par')
    else:
        print('Valor digitado é Ímpar')
except:
    print('Digite um número inteiro válido')