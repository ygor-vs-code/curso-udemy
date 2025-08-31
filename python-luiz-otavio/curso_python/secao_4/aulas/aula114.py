# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
import sys
sys.setrecursionlimit(3000)
sys.set_int_max_str_digits(10000)
# def recursiva(inicio=0, fim=10):
#     # Caso base
#     if inicio >= fim:
#         return fim
    
#     print(inicio, fim)

#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva(0, 1004))

def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n - 1)

print(fatorial(20))
