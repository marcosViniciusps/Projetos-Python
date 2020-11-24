# Este programa le um numero de 0 á 9999 e mostra seus numeros separados
# A restrição é que o numro inserido pelo usuário deve ser de 4 digitos quando tratado coomo string

# Tratando o problema com strings:

'''
num = input('Digite um numero: ')
print('Unidade: {}'.format(num[0]))
print('Dezena: {}'.format(num[1]))
print('Centena: {}'.format(num[2]))
print('Milhar: {}'.format(num[3]))
'''


# Tratando o problema com numeros:
num = int(input('Digite um numero: '))
milhar = int(num/1000)
print('Milhar = {}'.format(milhar))
centena = (int(num/100))%10
print('Centena = {}'.format(centena))
dezena = (int(num/10))%10
print('Dezena = {}'.format(dezena))
unidade = num % 10
print('Unidade = {}'.format(unidade))
