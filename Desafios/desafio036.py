# Este programa le o valor da casa, o salário do comprador, tempo desejado para pagar a casa e retorna se ele pode comprar
# Em seguida, é calculado o valor da mensalidade
# A compra será negada caso a mensalidade ultrapasse 30% do salário
v = float(input('Digite o valor da casa: '))
s = float(input('Digite o seu saário: '))
t = 12*int(input('Digite em quantos anos deseja pagar a casa: '))
mensalidade = v/t
if mensalidade > 0.3*s:
    print('O valor mensal R${:.2f} excede seu orçamento!!!\n\tCompra negada!!!'.format(mensalidade))
else:
    print('Compra aprovada!!!\nSua mensalidade será de: {:.2f}'.format(mensalidade))
