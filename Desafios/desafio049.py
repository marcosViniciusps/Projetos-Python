# Este programa exibe a tabuada do numero fornecido pelo usuário
n = int(input('Digite um numero: '))
print('/'*27)
for c in range(1,10):
    print('/// \t{} x {} = {}   \t///'.format(n,c,n*c))
print('/'*27)
