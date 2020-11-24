# Este programa le o comprimento dos tres lado de um triângulo e retorna se estes comprimentos podem formar um triângulo
# Além disso ele retorna se o trângulo é equilátero, Isóceles ou escaleno
l1 = float(input('Digite o valor do primeiro lado do triângulo: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print('Os comprimentos informados não podem formar um triângulo!')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO ')
else:
    print('ISÓCELES')
