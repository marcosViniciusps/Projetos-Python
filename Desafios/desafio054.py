# Este programa le o ano de nascimento de sete pessoas e diz quantas são maiores e menores de maioridade(21)
# Uma pessoa é considerada maior de idade caso tenha mais de 21 anos
from datetime import date
ano = date.today().year
maioridade = 0
for c in range(1,8):
    n = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    if (ano - n)  > 21:
        maioridade += 1
print('São {} pessoas maiores e {} menores de idade'.format(maioridade,7 - maioridade))
