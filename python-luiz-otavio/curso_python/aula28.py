"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é (letra)
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
ultima_letra = len(nome)

if not nome or not idade:
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido: {nome[::-1]}')
    print("Nome contém espaços?", ' ' in nome)
    print(f'Seu nome tem: {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é {nome[len (nome)-1:len(nome)]}')
    print(f'A última letra do seu nome é {nome[-1]}')
