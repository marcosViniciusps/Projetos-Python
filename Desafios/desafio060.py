# Este programa calcula o fatorial de um numero
n = int(input('Digite um numero: '))
f = 1
while n != 0:
    f = f * n
    n -= 1
print('Fatorial = {}'.format(f))
