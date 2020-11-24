# Este programa exibe os n numeros da sequência de Fibonacci, sendo n fornecido pelo usuário
n = int(input('Quantos numeros da sequência de Fibonacci devem ser exibidos? '))
n1 = 0
n2 = 0
n3 = 1
cont = 1
while cont <= n:
    if cont == 1:
        print('O 1° termo da série é 0')
    else:
        print('O {}° termo da série é: {}'.format(cont,n3))
        n1 = n2
        n2 = n3
        n3 = n2 + n1
    cont += 1
