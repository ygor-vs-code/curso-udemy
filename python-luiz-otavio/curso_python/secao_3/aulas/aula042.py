frase = 'O Python é uma linguagem de programação ' \
    'Multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes =''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if apareceu_mais_vezes < quantas_vezes_letra_apareceu:
        apareceu_mais_vezes = quantas_vezes_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print(letra_apareceu_mais_vezes, apareceu_mais_vezes)