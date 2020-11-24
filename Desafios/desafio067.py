# Este programa exibe a tabuada de cada numero digitado pelo usuário e para quando o numero for negativo

while True:
    print('--'*30)
    n = int(input('De qual numero voçê deseja ver a tabuada? \n '))
    print('-'*30)
    if n < 0:
        break
    print(f'Tabuada de {n}:')
    for c in range(1,10):
        print(f' {n} x {c} = {n*c}')
