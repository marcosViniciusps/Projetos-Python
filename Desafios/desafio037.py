# Este programa le um numero inteiro e pergunta ao usuário qual a base de conversão desejada
# 1 para Binário
# 2 para Octal
# 3 para hexadecimal
n = int(input('Digite um numero inteiro para realizar uma conversão de bases: '))
print('Escolha uma das bases para conversão:'
      '[1] para converter para Binário '
      '[2] para para Octal'
      '[3] para para Hexadeximal: ')
num = int(input())
if num == 1:
    print('O numero {} convertido para binário é:{}'.format(n,bin(n)[2:]))
elif num == 2:
    print('O numero {} convertido para octal é: {}'.format(n,oct(n)[2:]))
elif num  == 3:
    print('O numero {} convertido para hexadecimal é:{}'.format(n,hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')
