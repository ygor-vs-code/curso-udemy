lista = []

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        break

    if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
        numero = int(entrada)
        lista.append({'num': numero})
    else:
        print("Entrada inválida. Digite apenas números ou 'sair'.")

if lista:
    menor = maior = lista[0]['num']

    for item in lista:
        if item['num'] < menor:
            menor = item['num']
        if item['num'] > maior:
            maior = item['num']

    print("Menor número:", menor)
    print("Maior número:", maior)
else:
    print("Nenhum número foi inserido.")
