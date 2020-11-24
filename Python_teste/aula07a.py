#Este programa testa os operadores e também algumas finções do print
#nome = input('Digite o seu nome: ')
#print('Bem vindo {:*^20}'.format(nome))
n1 = int(input('Digite o  primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
md = n1 % n2
e = n1 ** n2
print(' A soma é :{} \n A multiplicação: {}\n A divisão: {}\n '. format(s,m,d),end='')
print('Adivisão inteira:{}\n O modulo da divisão: {}\n A exponenciação: {}'.format(di,md,e))
