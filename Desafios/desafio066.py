# Este programa le varios numeros inteiros e para quando o usuário digita 999
# Em seguida é exibido a quantidade de numeros digitados e a sua soma desconsiderando o flag
cont = 0
n = 0
soma = 0
while True:
    n = int (input('Digite um numero: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} numeros e a soma deles é: {soma}')