# Este programa calcula o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento
# Á vista em dinheiro/cheque: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartãp: 20% de juros no valor total
print('{:=^40}'.format(' LOJAS AMERICANAS '))
p = float(input('Digite o preço das compras: '))
print('''Digite o numero que corresponde a forma de pagamento: )
        [1]- Á vista em dinheiro/cheque: 10% de desconto)
        [2]- Á vista no cartão: 5% de desconto)
        [3]- Até 2x no cortão: preço normal)
        [4]- Com 3x ou mais no cartão: 20% de juros''')
f = int(input('Qual é a opção? '))
if f == 1:
    print('O preço final é: {}'.format(p-p*0.1))
elif f == 2:
    print('O preço final é: {}'.format(p-p*0.05))
elif f == 3:
    print('O preço final é: {}'.format(p))
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(p/2))
elif f == 4:
    parcela = int(input('Será dividido em quantas parcelas?'))
    print('O preço final é: {}'.format(p+p*0.2))
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(parcela,((p+p*0.2)/parcela)))
else:
    print('Opção não disponível. Tente novamente.')
