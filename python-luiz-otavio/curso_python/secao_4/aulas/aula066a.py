"""
Argumentos nomeados  e não nomeados em funçoes Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumentos (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)
soma(1, y=2, z=5)
soma(y=2, z=3, x=1)

print(1, 2, 3, sep='-')