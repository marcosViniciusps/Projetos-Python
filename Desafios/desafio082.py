# Este programa le varios numeros e adicina em uma lista,
# Em seguida separa em duas lista diferemtes os numeros pares dos ímpares
lista = []
lista_par = []
lista_impar = []
i = ''
num = 0
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    i =  str(input('Deseja continuar [S/N]?')).strip().upper()
    while i not in 'SN':
        i = str(input('Deseja continuar [S/N]?').strip().upper())
    if i == 'N':
        break
for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    else:
        lista_impar.append(c)
print('=-='*20)
print(f'Lista digitada: {lista}')
print(f'Pares: {lista_par}')
print(f'Ímpares: {lista_impar}')
