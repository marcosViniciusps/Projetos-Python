# Este programa exibe a raíz quadrada do numero fornecido através da biblioteca math
# Caso seja utilizada a biblioteca geral, é necessário utilizar o 'math' antes de cada função da biblioteca:
##print('A raíz de {} é: {}'.format(num, math.floor(raiz)))
from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raíz de {} é: {}'.format(num,floor(raiz)))
