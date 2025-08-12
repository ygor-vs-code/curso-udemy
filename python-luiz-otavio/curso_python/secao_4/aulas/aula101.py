# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def executa(funcao, *args):
    return funcao(*args)

soma_com_cinco = executa(soma, 5)
multiplica_por_dez = executa(multiplica, 10)