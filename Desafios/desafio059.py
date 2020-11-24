# Este programa pega dois numeros do usuário, exibe opções das operações que podem ser feitas sobre eles
# e em seguida realiza a operação requerida pelo usuário
i = 0
while i != 5:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    i = 0
    while i != 4 and i != 5:
        print('[1] - Somar')
        print('[2] - Multiplicar')
        print('[3] - Maior')
        print('[4] - Novos numeros')
        print('[5] - Sair do programa')
        i = int(input('O que voçê deseja fazer? '))
        if i == 1:
            print('A soma é: {}'.format(n1 + n2))
        if i == 2:
            print('A multiplicação é: {}'.format(n1 * n2))
        if i == 3:
            if n1 > n2:
                print('O maior numero é: {}'.format(n1))
            else:
                print('O maior numero é: {}'.format(n2))
print('FIM')
