"""
split e join com list e str
split - divide uma string
join 0 une uma string
"""

frase = '   Olha só que , coisa interessante        '

lista_palavras = frase.split(',')

lista_frases_fixed = []

for i, frase in enumerate(lista_palavras):
    lista_frases_fixed.append(lista_palavras[i].strip())
# print(lista_palavras)
# print(lista_frases_fixed)

frases_unidas = ', '.join(lista_frases_fixed)
print(frases_unidas)