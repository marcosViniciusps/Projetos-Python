# Este programa é o desafio 51 implementado com o uso do laço while
# Este programa le o primeiro termo e a razão de uma PA e por fim exibe os 10 primeiros termos
p = int(input(' Primeiro termo da PA: '))
r = int(input(' Razão da PA: '))
i = 1
while i != 11:
    print('O {}° termo da PA é: {}'.format(i, p))
    p = p + r
    i += 1
print('Fim')
