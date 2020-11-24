# Este programa le seis numeros fornecidos pelo usuário e soma apenas os pares
s = 0
cont = 0
print(' Digite seis numeros: \n')
for c in range(1,7):
    n = int(input('{}° numero: '.format(c)))
    if(n%2 == 0):
        s +=n
        cont += 1
print('Foram informados {} numeros pares e a soma foi: {}'.format(cont,s))
