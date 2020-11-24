# Este programa lê varios numeros do teclado e ao final da execução é exibido a média, o maior e o menor valor
# O usuário deve informar quando deseja parar de fornecer valores
s = 'S'
n = 0
media = 0
maior = 0
menor = 0
flag = 0
while s == 'S':
    n = float(input('Digite um numero: '))
    if flag == 0:
        menor = n
        maior = n
        media = n
        flag = 1
    else:
        media = (media + n)/2
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    s = str(input('Deseja digitar mais um numero? [S/N]')).upper()
print('A media dos numeros digitados é: {}'.format(media))
print('O maior valor digitado é: {}'.format(maior))
print('O menor valor digitado é {}'.format(menor))
