# Este programa faz a soma de todos os numeros ímpares que são múltiplos de 3 no intervalode 1 á 500
s = 0
cont = 0
for c in range(1,501,2):
    if(c%3==0):
        #print(c,end=' ')
        s += c
        cont += 1
print('Foram encontrados {} numeros dentro desta condição'.format(cont))
print('A soma é: {}'.format(s))