# Este programa le o ano de nascimento de um jovem e de acordo com sua idade e a data do sistem, retorna:
# Se ele deve esperar para se alistar, se agora é a hora de se alistar,, se ele esta atrasado para se alistar
# O programa também deve retornar quanto tempo falta para ele se alistar ou o tempo de ele está atrasado
from datetime import date
data_atual = date.today()
print('A data atual é: {}'.format(data_atual))
ano = int(input('Digite o ano de seu nascimanto: '))
print(data_atual.year - ano)
if (data_atual.year - ano) > 18:
    print('Seu alistamento está atrasado {} ano(s)!'.format(data_atual.year - ano -18))
elif (data_atual.year - ano) == 18:
    print('Voçê deve se alistar ainda este ano!')
else:
    print('Voçê deve se alistar daqui a {} ano(s)!'.format(ano + 18 - data_atual.year))
