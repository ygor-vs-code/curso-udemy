# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('ygor')
adiciona_clientes('joana',cliente1)
cliente1.append('edu')

cliente2 = adiciona_clientes('helena')
adiciona_clientes('maria',cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
