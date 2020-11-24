# Continuação de lista
a = [2,5,7,3]
'''
b = a # Neste caso, foi feita uma ligação de b e a 
'''
# Para que b receba os valores de a copiados, sem fazer uma ligação entre a e b:
b = a[:]
b[2] = 9
print(f'Lista a: {a}')
print(f'Lista b: {b}')