# Este programa le o ano de nascimento de um nadador e o classifica de acordo com:
# Até 9 ano: Mirin, até 14: infantil, até 19:junior, até 20: senior e acima: master
from datetime import date
nascimento = int(input('Digite o ano de seu nascimento: '))
#print(date.today().year)
idade = date.today().year - nascimento
print(idade)
if idade <= 9:
    print('Mirin')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')
