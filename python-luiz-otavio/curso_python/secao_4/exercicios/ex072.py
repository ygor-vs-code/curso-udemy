# Exercícios com funções

"""
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.
"""


entrada_1 = input('Digite valores para multiplicar (separe com espaços): ')

separando_numeros = entrada_1.split(' ')
numeros = []

for i in separando_numeros:
    i = int(i)
    numeros.append(i)

def multiplicar(*args):    
    total = 1
    for n in args:
        total *= n
    return total

print(multiplicar(*numeros))


"""
Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""

entrada_2 = input('Digite um número para saber se é ' \
'ímpar ou par')

def par_impar(x):
    if x % 2 == 0:
        return f'Número {x}, par.'
    return f'Número {x}, ímpar.'

print(par_impar(int(entrada_2)))