# Manipulando chaves e valores em dicionários

pessoa = {}





chave = 'nome'

pessoa[chave] = 'Ygor Victor'
pessoa['sobrenome'] = 'Santos'


print(pessoa[chave])

pessoa[chave] = 'Maria'


del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
