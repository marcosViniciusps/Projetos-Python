# Este programa calcula o salário do funcionário após o aumento
# Caso ele ganhe mais que 1250,00R$ seu salário será aumentado em 10%
# Nos demais casos será aumentado em 15%
s = float(input('Digite seu salário: '))
print('Seu novo salário será de: {}',s+s*0.15 if s < 1250 else s+s*0.1)

# Outra forma mais detalhada:
'''
if s > 1250:
    print('Seu novo salário será de: {}'.format(s+s*0.1))
else:
    print('Seu novo salário será de: {}'.format(s+0.15*s))
'''