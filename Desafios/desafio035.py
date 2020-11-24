# Este programa le o comprimento de tres retas e retorna se elas podem formar um triângulo
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digit e o valor do terceiro lado: '))
if l1 + l2 > l3 and l1 + l3 > l2:
    print('Os comprimentos digitados podem formar um triângulo! ')
else:
    print('Os comprimentos digitados não podem formar um triângulo! ')
