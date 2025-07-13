nome = input('Digite seu primeiro nome: ')
quantidade = len(nome)

if quantidade <= 4:
    print('Seu nome é curto.')
elif quantidade <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')