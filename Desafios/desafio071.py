# Este programa simula um caixa eletrônico
# É perguntado ao usuário qual o valora ser sacado e o programa informa quantas celular de cada valor serão entreges
# As células possíveis são 50, 20, 10 e 1
cinquenta = vinte = dez = um =0
print('=='*15)
print('\t\t\tBANCO')
print('=='*15)
while True:
    valor = int(input('Qual valor voçê deseja sacar? '))
    cinquenta = int(valor / 50)
    valor -= cinquenta * 50
    vinte = int(valor / 20)
    valor -= vinte * 20
    dez = int(valor / 10)
    valor -= dez *10
    um = valor
    print(f'Total de {cinquenta} nota(s) de Cinquenta')
    print(f'Total de {vinte} nota(s) de Vinte')
    print(f'Total de {dez} nota(s) de Dez')
    print(f'Total de {um} nota(s) de Um')
    print('==' * 15)
