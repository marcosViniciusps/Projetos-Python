# Este programa calcula o preço do aluguem de um veículo com base na quantidade de dias alugados e km rodados
# O carro custa 60R$ por dia a 0,15R$ por Km rodado
dias = int(input('Por quantos dias voçê alugou?'))
km = float(input('Quantos kilometros foram rodados?'))
print('O total a pagar é: {:.2f}'.format(60*dias+0.15*km))
