# Este programa le varios numeros e os coloca em uma lista
# Ao final é exibido a quantidade de elementos, a lista em ordem decrescente e se o numero 5 esta na lista
lista = []
i = ''
while True:
    lista.append(int(input('Digite algo: ')))
    i = str(input('Deseja continuar [S/N]? ').upper().strip())
    while i not in 'NS':
        i = str(input('Deseja continuar [S/N]? ').upper().strip())
    if i == 'N':
        break
print('=-='*20)
print(f'Lista = {lista}')
print(f'A lista posui {len(lista)} elementos.')
print(sorted(lista))
if 5 in lista:
    print('O numero 5 esta na lista!')
else:
    print('A lista não possue o numero 5')
print('=-='*20)
