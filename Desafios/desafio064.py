# Este programa le varios numeros inteiros e só para quando o usuário digita 999
# Em seguida é exibido a quantidade de numeros digitados e a soma total
n =0
cont = 0
soma = 0
print('Para finalizar, digite 999')
while n != 999:
    if n != 999:
        n = int(input('Digite um numero: '))
        cont += 1
        soma += n
print('Foram digitados {} numeros'.format(cont))
print('A soma dos numeros digitados é: {}'.format(soma))
