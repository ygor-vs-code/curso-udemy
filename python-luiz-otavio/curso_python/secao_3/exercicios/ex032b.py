try:
    horas = int(input('Que horas são? '))
    if horas >= 0 and horas <= 23:
        if horas <= 11:
            print('Bom dia!')
        elif horas <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
    else:
        print('Digite apenas horas igual ou maior que 0 e menor ou igual a 23')
except:
    print('Digite apenas números inteiros')