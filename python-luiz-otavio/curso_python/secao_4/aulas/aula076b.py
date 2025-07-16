"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adicionar valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Ygor Victor',
    'sobrenome': 'Santos',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])

# print(len(pessoa))
# print(tuple(pessoa.keys()))
# print(tuple(pessoa.values()))
# print(tuple(pessoa.items()))



# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)