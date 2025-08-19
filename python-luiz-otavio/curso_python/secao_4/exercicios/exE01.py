"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

=================== resultado
lista_soma = [2, 4, 6, 8]
"""


l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]
nova_lista = [i[0] + i[1] for i in zip(l1, l2)]
print(nova_lista)
