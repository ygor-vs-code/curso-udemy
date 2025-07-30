# Try, except, else e finally


try:
    a = 18
    b = 0
    print('linha 1'[1000])
    c = a / b
    print('linha 1')


except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Erro:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')


print('CONTINUAR')