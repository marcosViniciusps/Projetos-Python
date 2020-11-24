# Este programa é um melhoramento do desafio 28, com as seguintes diferenças:
# Agora o programa gera um numero de 0 á 10, pergunta até que ocorra o acerto e exibe o numero de tentativas
from random import randint
from time import sleep
print('=-=-='*10)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar... ')
print('=-=-='*10)

tentativas = 1
computador = randint(0,10)

while tentativas != -1:
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    if jogador == computador:
        print('Acerto mizerável!!!')
        print('Voçê gastou {} tentativas! '.format(tentativas))
        tentativas = -1
    else:
        print('Errou!')
        tentativas += 1
print('=-=-='*10)
