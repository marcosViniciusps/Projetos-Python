# Este programa pergunta o sexo do usuário e só aceita M ou F como resposta
s = ''
while s != 'M' and s != 'F':
    s = str(input('Qual o sexo da pessoa? [M/F] ')).upper()
print('FIM')