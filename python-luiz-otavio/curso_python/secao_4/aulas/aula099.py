from sys import path

import aula099_package.modulo
from aula099_package import modulo
from aula099_package.modulo import *
# from aula099_package.modulo import soma_do_modulo

# print(*path, sep='\r\n')
print(soma_do_modulo(1, 2))
print(aula099_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)

