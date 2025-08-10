import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.7},
    {'nome': 'Produto 4', 'preco': 69.90},
]

aumento = [
    {**produto, 'preco': round(produto['preco'] * 1.10, 2)}
    for produto in produtos
]

novos_produtos = copy.deepcopy(aumento)
decrescente_nome = sorted(novos_produtos, key=lambda item: item['nome'], reverse=True)


print(*decrescente_nome, sep='\n')

produtos_ordenados_por_nome = copy.deepcopy(aumento)
crescente_preco = sorted(produtos_ordenados_por_nome, key=lambda item: item['preco'])

print()

print(*crescente_preco, sep='\n')