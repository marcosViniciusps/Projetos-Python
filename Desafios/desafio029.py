# Este programa le a velocidade do carro fornecida pelo usuário e caso esteja acima de 80Km/h
# é exibida uma mensagem dizendo que foi multado e o valor da multa
v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    print('Acima da velocidade!!!')
    print(('Multa de {:.2f}R$'.format(7*(v-80))))
else:
    print('Tenha um bom dia. Dirija com segurança!')
