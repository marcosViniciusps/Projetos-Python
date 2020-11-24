# Este programa le o nome completo de uma pessoa e retorna:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras no total, sem considerar os espaços
# Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip() # .strip elimina espaços antes e depois mas não no meiio da frase
print('Seu nome em maiúsculo: {}'.format(nome.upper()))

print(' Seu nome em minúsculo: {}'.format(nome.lower()))

print(' Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))

#print(' Seu nome sem espaços contém {} letras.'.format(len(nome.replace(" ", ""))))

nome_dividido = nome.split()
print( 'Seu primeiro nome é: {} e ele tem {} letras.'.format(nome_dividido[0],len(nome_dividido[0])))

# Outra forma:
#print( 'Seu primeiro nome é: {} e ele tem {} letras.'.format(nome_dividido[0],nome.find(' ')))
