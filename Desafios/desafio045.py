# Este programa simula um jogo de pedra-papel-tesoura ou Jokenpô entre o computador e o usuário
from random import randint
from time import sleep
v = ['Pedra','Papel','Tesoura']
print('{:=^30}'.format(' JOKENPÔ '))
print('''
[1]- para PEDRA
[2]- para PAPEL
[3]- para TESOURA''')
jogador = int(input('\nQual a sua jogada? '))
print('=-='*10)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
print('=-='*10)
computador = randint(1,3)
if jogador == computador:
    print('Empate!!!  \n\nJogador -> {} \nComputador -> {}'.format(v[jogador -1],v[computador -1]))
elif jogador == 1 and computador == 3:
    print('Voce venceu!!! \n\nJogador -> {} \nComputador -> {}'.format(v[jogador -1],v[computador -1]))
elif jogador == 2 and computador == 1:
    print('Voçê venceu!!! \n\nJogador -> {} \nComputador -> {}'.format(v[jogador -1],v[computador -1]))
elif jogador == 3 and computador == 2:
    print('Voçê venceu!!! \n\nJogador -> {} \nComputador -> {}'.format(v[jogador - 1], v[computador - 1]))
else:
    print('O computador ganhou!!! \n\nJogador -> {} \nComputador -> {}'.format(v[jogador -1],v[computador -1]))
print('=-='*10)
