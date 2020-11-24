# Este programa gera um numero aleatório de 0 á 5 e o compara com o numero fornecido pelo usuário
from random import randint
from time import sleep
print('=-=-='*10)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar... ')
print('=-=-='*10)

computador = randint(0,5)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)

if jogador == computador:
    print('Acerto mizerável!!!')
else:
    print('Errou!\n Eu pensei no numero {} e não no {}'.format(computador,jogador))
print('=-=-='*10)