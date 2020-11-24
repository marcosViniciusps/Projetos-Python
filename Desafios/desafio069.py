# Este programa le o sexo e idade de várias pessoas enquanto o usuário desejar
# Ao final do programa, é exibido:
# Quantas pessoas tem mais de 18, quantos homens foram cadastrados, quantas mulheres com menos de 20
cont = homens = mulheres = maiores = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    cont += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheres += 1
    if idade >= 18:
        maiores += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Existem {homens} homen(s) neste grupo ')
print(f'Existem {maiores} pessoa(s) com mais de 18 anos e {mulheres} mulhere(s) com menos de 20 anos')

