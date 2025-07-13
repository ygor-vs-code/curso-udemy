"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_a.extend(lista_b)
print(lista_a) # [1, 2, 3, 4, 5, 6]