# Este programa possui uma tupla com nomes de produtos e seus preços em sequência
# Os nomes e preços são exibidos de forma organizada
tupla = ('pao',5.00,'acucar',10,'batata',1.50,'leite',3.58)
print('-'*40)
print('LISTAGEM DE PREÇOS')
print('-'*20)
for pos in range(0,len(tupla)):
    if pos % 2 ==0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R${tupla[pos]:>7.2f}')
print('-'*40)
