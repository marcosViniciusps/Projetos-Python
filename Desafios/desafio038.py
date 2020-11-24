# Este programa le dois numeros inteiros e os compara mostrando na tela uma mensagem:
# 'O primeiro valor é maior', ' O segundo valor é maior', 'Os valoores são iguais'
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro valor é maior! ')
elif n2 > n1:
    print('O segundo valor é maior! ')
else:
    print('Os valores são iguais! ')
