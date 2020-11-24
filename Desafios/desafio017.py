# Este programa le o valor do cateto adjacente e do cateto oposto e em seguida exibe a hiótenusa

#from math import sqrt
#hi = sqrt(pow(ca,2)+pow(co,2))

from math import hypot
ca = float(input('Dgigite o valor do cateto adjacente: '))
co = float(input('Digite o valor de cateto oposto: '))
print('A hipotenusa vale: {:.2f}'.format(hypot(ca,co)))
