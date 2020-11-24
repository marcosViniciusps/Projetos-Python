# Este é um programa de teste da estrutura condicional do If e If-else
nome = str(input('Qual é o seu nome? ')).strip().lower()
if nome == 'marcos':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}'.format(nome.capitalize()))
