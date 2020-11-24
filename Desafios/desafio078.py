# Este programa le 5 valores e os armazena em uma lista, em seguida:
# Exibe o maior, o menor e suas posições
lista = []
maior = 0
menor = 0
p_naior = []
P_menor = []
for cont in range(0,5):
    lista.append(float(input('Digite um numero: ')))
    if cont == 0:
        menor = lista[cont]
        maior = lista[cont]
    elif menor > lista[cont]:
        menor = lista[cont]
    elif maior < lista[cont]:
        maior = lista[cont]
print(f'O maior valor da lista foi: {maior} que esta nas posições: ',end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}... ',end='')
print()
print(f'O menor valor da lista foi: {menor} que esta nas posições: ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ',end='')