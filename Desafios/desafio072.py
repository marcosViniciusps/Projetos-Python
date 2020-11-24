# Este programa tem uma tupla preenchida por uma contagem em extenso de 0 á 20
# O usuário deve digitar um numero e em seguida ele deve ser exibido em extenso
num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','quatorze','quize','dezessies','dezessete','dezoito','dezenove','vinte')
while True:
    while True:
        n = int(input('Digite um numero: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente: ',end='')
    print(f'Voçê digitou o numero: {num[n]}')
