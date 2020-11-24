# Este programa lê tres numeros e retorna o maior e o menor deles
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))

if n1 >= n2 and n1 >= n3:
    print(' O maior numero é: ',n1)
    if n2 >= n3:
        print(' O menor numero é: ',n3)
    else:
        print(' O menor numero é: ',n2)

if n2 >= n1 and n2 >= n3:
    print(' O maior numero é: ',n2)
    if n1 >= n3:
        print(' O menor numero é: ',n3)
    else:
        print(' O menor numero é: ',n1)

if n3 >= n1 and n3 >= n2:
    print(' O maior numero é: ',n3)
    if n1 >= n2:
        print(' O menor numero é: ',n2)
    else:
        print(' O menor numero é: ',n1)
