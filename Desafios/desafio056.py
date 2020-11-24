#Este programa le o nome, idade e sexo de quatro pessoas e retorna:
# A média de idade do grupo
# O  nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
media_idade = 0
hmv = -1     # Homem mais velho: é -1 para não corresponder a um numero do vetor
mm = 0
nomes = ['','','','']
idades = [0,0,0,0]
sexos = ['','','','']

for c in range(0,4):
    print('-'*10,' INSIRA AS INFORMAÇÕES DA {}° PESSOA '.format(c + 1),'-'*10)
    nomes[c] = str(input('NOME: ')).strip()
    idades[c] = int(input('IDADE: '))
    sexos[c] = str(input('SEXO [M/F]: ')).strip().upper()
    media_idade += idades[c]
    if sexos[c] == 'M':
        if hmv == -1:   # Caso seja a primeira vez, hmv receberá o indice do primeiro homem
            hmv = c
        else:   # Hmv receberá o indice de c caso a idade do homem atual seja maior que a anterior
            if idades[hmv] < idades[c]:
                hmv = c
    else:
        if idades[c] < 20:
            mm +=1

media_idade = media_idade/4
print('\n\nA media de idade do grupo é: {}'.format(media_idade))
if mm != 0:
    print('Existe(m) {} mulher(es) com menos de 20 anos no grupo.'.format(mm))
else:
    print('O grupo não possui mulheres com menos de 20 anos')
if hmv == -1:
    print('Não existe homem neste grupo.')
else:
    print('O Homem mais velho do grupo é: {}'.format(nomes[hmv]))
