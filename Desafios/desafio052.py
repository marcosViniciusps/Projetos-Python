# Este programa calcula se o numero lido é primo
n = int(input('Digite um numero: '))
total = 0
for c in range(2,n+1):
    if n % c == 0:
        print('\033[34m',end=' ')
        total += 1
    else:
        print('\033[31m',end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mO numero {} foi divisível {} vezes '.format(n,total))
if total == 1:
    print('E por isso ele é primo!')
else:
    print(' E por isso ele não é primo!')
