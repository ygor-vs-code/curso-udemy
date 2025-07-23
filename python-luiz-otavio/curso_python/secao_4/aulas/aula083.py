a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'alutra': 1.6
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# args e kwargs
# args (já vimos)
# kwargs - keyword argumentos (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, nome='joana', qlq=123)
# mostro_argumentos_nomeados(**pessoa_completa)

configs = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configs)