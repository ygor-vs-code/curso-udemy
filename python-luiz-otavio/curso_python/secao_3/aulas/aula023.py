# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
elif senha == '1234':
    print('Entrar')
else:
    print('Senha incorreta.')
