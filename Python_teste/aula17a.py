# Esta programa é um teste das funções da lista
lista = [2,5,9,1]
print(lista)
lista.append(7) # Adiciona um elemento na ultima posição da lista
lista.sort(reverse=True) # Osdena os elementos da lista na oedem inversa
print(lista)
lista .insert(3,2) # Insere o numero 2 na posição 3
print(lista)
lista.remove(2) # Remove apenas o primeiro numero 2 da lista
if 4 in lista: # Condição de teste antes de remover um elemento
    lista.remove(4)
else:
    print('O unumero quatro não esta nesta lista ')
print(lista)
print(f'Esta lista tem {len(lista)} elementos ')
