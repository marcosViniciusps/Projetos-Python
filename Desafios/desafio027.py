# Este programa çe o nome completo e retorna apenas  o primeiro e último nome
n = input('Digite seu nome: ').strip()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
#  O -1 é necessário pois a função len retorna o tamanho da string despresando o zero
