# filter é um filtro funcional

def print_inter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto5', 'preco': 10.00},
    {'nome': 'Produto1', 'preco': 22.32},
    {'nome': 'Produto3', 'preco': 10.11},
    {'nome': 'Produto2', 'preco': 105.87},
    {'nome': 'Produto4', 'preco': 69.90},
]

def filtrar_preco(produto):
    return produto['preco'] > 100

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 10
# ]
novo_produtos = filter(
    filtrar_preco,
    produtos
)

print_inter(produtos)
print_inter(novo_produtos)