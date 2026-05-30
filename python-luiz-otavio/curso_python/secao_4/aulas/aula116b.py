caminho_arquivo = '/home/ysantos/Documentos/GitHub/curso-udemy/python-luiz-otavio/curso_python/secao_4/aulas/'
caminho_arquivo += 'aula116tb.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )