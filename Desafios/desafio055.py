# Este programa le o peso de cinco pessoas e exibe o maior e o menor
maior = 0
menor = 0
peso = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa mais pesada tem {:.2f} kilos'.format(maior))
print('A pessoa mais leve tem {:.2f} kilos'.format(menor))