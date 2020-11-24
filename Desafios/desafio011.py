# Este programa pede a largura e a altura de uma parede
# E calcula sua área e a quantidade de tinta necessária para pintá-la
# Considerando que cada litro de tinta pinta 2m2
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = largura * altura
print('A parede possui {:.2f} metros quadrados de área'.format(area))
print('Serão necessários {:.2f} litros de tinta'.format(area/2))
