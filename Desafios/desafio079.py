# Este programa permita que o usuário digite varios valores numericos cadastrando-os em uma lista
# Em seguida, são exibidos os valores em ordem crescente
# Não podem ser adicionados valores repetidos
num = 0
lista = []
f = ' '
while True:
    num = float(input('Digite um numero: '))
    if num not in lista:
        lista.append(num)
        print('Numero adicionado com sucesso!')
    else:
        print('Numero duplicado!')
    f = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while f not in 'SN':
        f = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if 'N' in f:
        break
print(lista)
print(sorted(lista))
