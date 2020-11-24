# Este programa gera cinco numeros aleatórios em uma tupla
# Em seguida exibe os numeros gerados, o maior e o menor
from random import randint
tupla = (randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000))
print(tupla)
print(f'O maior numero da tupla é: {max(tupla)}')
print(f'O menor numero da tupla é: {min(tupla)}')
