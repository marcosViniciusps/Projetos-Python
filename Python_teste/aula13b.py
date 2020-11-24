# Este é um programa para teste do laço For
s = 0
c = int(input(' Quantos números voçê deseja somar: '))
for c in range(0,c):
    n = int(input('Digite digite o {}° numero a ser somado: '.format(c+1)))
    s += n
print('A soma dos valores é: {}'.format(s))
print('Fim')
