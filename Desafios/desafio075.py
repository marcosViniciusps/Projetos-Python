# Este programa le quatro valores do teclado e armazena em uma tupla, em seguida é exibido:
# Quantas vezes apareceu o numero 9, em que posição tem o primeiro 3, quais foram os numeros pares
posicao = 0
print('Digite quatro valores: ')
tupla = (input('1°- '),input('2°- '),input('3°- '),input('4°- '))
print('=-='*20)
print(f'Tupla completa: {tupla}')
print('=-='*20)
print('O numero 9 apareceu {} vezes nesta tupla.'.format(tupla.count(9)))
print('=-='*20)
if 3 in tupla:
    print(f'O numero 3 apareceu na {tupla.index("3")}ª posição')
else:
    print('O numero 3 não existe nasta tupla.')
print('=-='*20)
print('Numeros pares: ',end=' ')
for c in tupla:
    if int(c) % 2 == 0:
        print(c,end=' ')
print('\n')
print('=-=' * 20)
