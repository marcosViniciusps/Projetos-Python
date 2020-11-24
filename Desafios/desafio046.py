# Este programa realiza uma contagem regressiva de 10 segundos para fogos de artifício com um intervalo de 1 segundo
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('BUM! BUM! POW!')