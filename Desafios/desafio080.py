# Este programa le 5 valores do usuário e os adiciona em uma lista ja na ordem crescente 
# Observação: Não deve ser utilizada a função 'sort'
lista = []
num = 0
cont = 0
for cont in range(0,5):
    num = int(input('Digite um numero: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Adicionado na {cont}° posição')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'Adicionado na {pos}° posição')
                break
            pos += 1
print('=-='*20)
print(lista)
