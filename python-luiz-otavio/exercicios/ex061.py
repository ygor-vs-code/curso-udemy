entrada = input('Digite o CPF (com ou sem pontuação): ')
cpf_numeros = ''.join(c for c in entrada if c.isdigit())

nove_digitos = cpf_numeros[:9]
multiplicador_1 = 10
multiplicador_2 = 11
soma_1 = 0
soma_2 = 0

if len(cpf_numeros) == 11:


    for numero in nove_digitos:
        soma_1 += int(numero) * multiplicador_1
        multiplicador_1 -= 1

    digito_1 = (soma_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0


    dez_digitos = nove_digitos + str(digito_1)

    for numero_2 in dez_digitos:
        soma_2 += int(numero_2) * multiplicador_2
        multiplicador_2 -= 1

    digito_2 = (soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    dois_ultimos_digitos = str(digito_1) + str(digito_2)

    if dois_ultimos_digitos == cpf_numeros[9:]:
        print(f'CPF {cpf_numeros} Válido.')
    else:
        print(f'CPF {cpf_numeros} Inválido')
else:
    print('CPF Inválido [CPF maior ou menor que 11 digitos.]')