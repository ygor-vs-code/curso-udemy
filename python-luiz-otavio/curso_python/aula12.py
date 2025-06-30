nome = str(input('Digite seu nome:'))
altura = float(input('Digite sua altura em metros:'))
peso = float(input('Digite seu peso em kg:'))
imc = peso / altura ** 2

print(nome, 'tem', f'{altura:.2f}', 'pesa', peso, 'quilos e seu IMC é', f'{imc:.2f}')