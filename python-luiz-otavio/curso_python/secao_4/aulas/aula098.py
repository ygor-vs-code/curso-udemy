# singleton: só pode existir uma instancia daquela coisa no programa
# inteiro quando estiver executando
import importlib

import aula098_m

print(aula098_m.variavel)

for i in range(10):
    importlib.reload(aula098_m)

print('Fim')