# Este programa simula um jogo de par ou ímpar com o computador
from time import sleep
from random import randint
cont = 1
vitorias = 0
while True:
    print(f'Partida {cont}')
    j = ' '
    while j not in 'PpIi':
        j = str(input('Escolha par ou ímpar [P/I]: ')).strip()[0]
    nj = int(input('Escolha um numero de 0 á 10 ')) # numero do jogador
    while nj < 0 or nj >10:
        nj = int(input('Escolha um numero de 0 á 10 '))  # numero do jogador
    print('Vou escolher meu numero ...')
    sleep(0.5)
    nc = randint(0,10)
    print('=-='*20)
    if j == 'p':
        if (nj+nc) % 2 == 0:
            print(f'Voçê Ganhou!\n\tJogador = {nj}\n\tComputador = {nc}\n\tTotal = {nj+nc}')
            print('Vamos jogar novamente...')
            vitorias += 1
        else:
            print(f'Computador Venceu!\n\tJogador = {nj}\n\tComputador = {nc}\n\tTotal = {nj+nc}')
            print(f'Fim de jogo.\n Voçê teve {vitorias} vitórias')
            break
    if j == 'i':
        if (nj+nc) % 2 == 0:
            print(f'Computador venceu!\n\tJogador = {nj}\n\tComputador = {nc}\n\tTotal = {nj+nc}')
            print(f'Fim de jogo.\n Voçê teve {vitorias} vitórias')
            break
        else:
            print(f'Voçê Ganhou!\n\tJogador = {nj}\n\tComputador = {nc}\n\tTotal = {nj+nc}')
            print('Vamos jogar novamente...')
            vitorias += 1
    cont += 1
    print('=-='*20)
