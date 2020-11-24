# Este programa é o desafio 61 melhorado
# Este programa le o primeiro termo e a razão de uma PA e por fim exibe os 10 primeiros termos
# Em seguida é perguntado ao usuário se ele deseja ver o calculo de mais termos da PA
p = int(input(' Primeiro termo da PA: '))
r = int(input(' Razão da PA: '))
i = 11
cont = 1
while cont < i:
    print('O {}° termo da PA é: {}'.format(cont, p))
    p = p + r
    cont +=1
    if cont == i:
        print('Deseja exibir mais termos da PA?')
        i += int(input('Digite o numero desejado ou [0] para cancelar: '))
