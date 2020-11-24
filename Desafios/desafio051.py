# Este programa le o primeiro termo e a razão de uma PA e por fim exibe os 10 primeiros termos
p = int(input(' Primeiro termo da PA: '))
r = int(input(' Razão da PA: '))
for c in range(1,11):
    print('O {}° termo da PA é: {}'.format(c, p))
    p = p + r
print('Fim')
