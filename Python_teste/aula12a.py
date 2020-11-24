# Este programa realiza testes de condições aninhadas
nome = str(input('Qual é o seu nome? ')).lower()
if nome == 'marcos':
    print('Que nome bonito! ')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('O seu nome é bem popular no Brasil! ')
elif nome in 'ana claudia jessica juliana':
    print('Este é um nome feminino!')
else:
    print('O seu nome é bem normal!')
print('Tenha um bom dia {}!'.format(nome))

