"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembrete de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1, 2, 3, 4, 5, 6

soma_1_2_3 = soma(*numeros)
print(soma_1_2_3)

# print(sum((1, 2, 3, 4, 5, 6)))