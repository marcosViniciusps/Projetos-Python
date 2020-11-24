# Este programa lê o nome de uma cidade e retorna se ela começa ou não com o nome 'Santo'
cidade = str(input('Digite o nome da cidade: ')).strip()
cidade_dividida = cidade.split()
print('santo' in cidade_dividida[0].lower()) # Retorna True ou False
