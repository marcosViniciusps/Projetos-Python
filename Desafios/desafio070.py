# Este programa le o nome e o preço de um produto e finaliza só com a indicação do usuário
# No final é exibido:
# O total gasto na compra,quantos produtos custão mais de 1000, o nome do produto mais barato
nome_mais_barato = ''
menor_preco = -1 # É inicializado em -1 para não haver problema na primeira comparação    if preco < menor_preco:
total = 0
mais_de_mil = 0
continuar = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto R$: '))
    total += preco
    if preco > 1000:
        mais_de_mil += 1
    if menor_preco == -1 or preco < menor_preco:
        menor_preco = preco
        nome_mais_barato = nome
    continuar = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra foi: {total:.2f}')
print(f'{mais_de_mil} produtos custam mais de R$ 1000,00 reais')
print(f'O {nome_mais_barato} custa {menor_preco} e é o produto mais barato da lista informada.')
print('{:-^40}'.format('FIM DO PROGRAMA'))
