# Este programa le o peso e a altura de uma pessoa, calcula o IMC e retorna informações conforme abaixo:
#Menor que 18.5: abaixo do peso, entre 18 e 25: peso ideal, de 25 até 30: sobrepeso
#       De 30 á 40: obesidade, maior que 40: obesidade mórbida
altura = float(input('Digite sua altura(m): '))
peso = float(input('Digite seu peso(Kg): '))
imc = peso / (altura **2 )
print('Seu IMC é de: {:.2f}Kg/m2'.format(imc))
if imc < 18.5:
    print('Voçê está abaixo do peso! ')
elif imc <25:
    print('Voçê está no peso ideal! ')
elif imc < 30:
    print('Voçê está com sobrepeso!')
elif imc < 40:
    print('Voçê está com obesidade!')
else:
    print('Voçê está com obesidade mórbida!')