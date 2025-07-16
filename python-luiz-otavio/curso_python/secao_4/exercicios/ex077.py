# Exercício - sistema de perguntas e respsotas

contador = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for chave in perguntas:
    resposta_certa = chave['Resposta']
    print(chave['Pergunta'], '\n')

    for i, indice in enumerate(chave['Opções']):
        print(f'{i}) {indice}')

        if indice == resposta_certa:
            resposta_certa = i
          
    entrada = input('\nDigite a opção: ')

    if entrada == str(resposta_certa):
        print('\nAcertou!\n')
        contador += 1
    else:
        print('\nErrou!\n')
        
print(f'Você acertou [{contador}] pergunta(s) no total de [{len(perguntas)}] perguntas.')