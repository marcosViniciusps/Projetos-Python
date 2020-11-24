# Continuação de tuplas
a = (2,5,4)
b = (5,8,1,2)
c = a + b # Realiza a junção das tuplas
print(a)
print(b)
print(c)
c = b + a # A ordem da soma importa
print(c)
print(c.count(5))# Conta quantos '5' tem na tupla c
print(c.index(4))# Mostra a posição do numero 4 na tupla contando com a posição 0
print(c.index(2))# Mostra a posição do primeiro 2 na tupla
print(c.index(5,1))# Mostra a posição do próximo 5 na tupla, começando da posição 1
