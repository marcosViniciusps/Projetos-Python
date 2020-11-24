# Este programa retorna se o nome de uma pessoa posssui 'Silva'
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome possui Silva? {}'.format('SILVA' in nome.upper())) # Retorna True ou False
