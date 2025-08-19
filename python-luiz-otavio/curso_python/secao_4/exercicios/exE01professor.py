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
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4, 5, 6, 7, 8]

nova_lista = []
valor_minimo = len(min(lista_a, lista_b))

for i in range(valor_minimo):
    lista_soma = lista_a[i] + lista_b[i]
    nova_lista.append(lista_soma)

print(nova_lista)