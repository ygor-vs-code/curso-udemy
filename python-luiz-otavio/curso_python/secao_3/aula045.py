"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
inter -> me entregue seu iterador
"""

# for letra in texto:

texto = 'Ygor' # iterável
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
