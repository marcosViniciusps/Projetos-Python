# Este é um programa testes para a função while
print('-'*10,'Calculadora de media de numeros positivos','-'*10)
print('Digite -1 para sair')
n = 0
media = 0
while n != -1:
    n = float(input('Digite um valor: '))
    if media == 0:
        media = n
    if(n>0):
        media = (media+n)/2
print('A media dos numeros digitados é: {:.2f}'.format(media))
