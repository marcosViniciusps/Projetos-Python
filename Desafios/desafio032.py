# Este programa lê um numero qualquer e retorna se ele é bisexto
from datetime import date
ano = int(input('Que ano voçê quer analisar? \nColoque 0 para analizar o ano da sua máquina: '))

if ano == 0:
    ano = date.today().year
if ano%4 == 0 and  ano%100 != 0 or ano%400 == 0:
    print(' O ano de {} é bisexto! '.format(ano))
else:
    print('Este ano não é bisexto! '.format(ano))
