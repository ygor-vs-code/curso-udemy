# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

# a, b, c, *_, ap, u = lista
# print(a, u, ap)z
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')