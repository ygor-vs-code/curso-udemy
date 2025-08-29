# map - para mapear dados
from functools import partial
from types import GeneratorType

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

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos =[
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])}
#     for p in produtos
# ]
def muda_preco(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

novos_produtos = map(
    muda_preco,
    produtos
)

print_inter(produtos)
print_inter(novos_produtos)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
)
))