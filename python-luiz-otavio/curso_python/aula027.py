"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
obs.: a função len retorna a quantidade
de caracteres da str
"""

variavel = 'Olá mundo'

print(variavel[4:9]) # inicio e final
print(variavel[4:]) # inicio e final omitido
print(variavel[0:5]) # inicio e final
print(variavel[:5]) # inicio omitido e final
print(len(variavel[-8:-2])) # inicio e final negativos
print(len(variavel)) # saber quantos caracteres tem a string
print(variavel[0:len(variavel):2]) # metodo len pode ser usado no final, o 2 serve de quantidades puladas
print(variavel[::-1]) # de trás pra frente
print(variavel[-1:-8:-1]) # de trás pra frente

